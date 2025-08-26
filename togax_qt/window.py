from PySide6.QtCore import Qt, QEvent
from PySide6.QtWidgets import QMainWindow, QMenu, QWidget, QVBoxLayout
from toga.constants import WindowState
from toga.types import Position, Size
from toga.command import Separator
from .screens import Screen as ScreenImpl
from .container import Container


def process_change(native, event):
    if event.type() == QEvent.WindowStateChange:
        old = event.oldState()
        new = native.windowState()
        if not old & Qt.WindowMinimized and new & Qt.WindowMinimized:
            native.interface.on_hide()
        elif old & Qt.WindowMinimized and not new & Qt.WindowMinimized:
            native.interface.on_show()


class TogaTLWidget(QWidget):
    def __init__(self, impl, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.interface = impl.interface

    def changeEvent(self, event):
        process_change(self, event)
        super().changeEvent(event)


class TogaMainWindow(QMainWindow):
    def __init__(self, impl, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.interface = impl.interface

    def changeEvent(self, event):
        process_change(self, event)
        super().changeEvent(event)


def wrap_container(widget, impl):
    wrapper = TogaTLWidget(impl)
    layout = QVBoxLayout(wrapper)
    layout.setContentsMargins(0, 0, 0, 0)
    layout.setSpacing(0)
    layout.addWidget(widget)
    return wrapper


class Window:
    def __init__(self, interface, title, position, size):
        self.interface = interface
        self.interface._impl = self
        self.container = Container(on_refresh=self.container_refreshed)
        self.container.native.show()

        self.create()

        self.native.interface = interface
        self.native.impl = self
        self.native.closeEvent = self.qt_close_event
        self.prog_close = False

        self._in_presentation_mode = False

        self.native.setWindowTitle(title)
        self.native.resize(size[0], size[1])
        if not self.interface.resizable:
            self.native.setFixedSize(size[0], size[1])
        if position is not None:
            self.native.move(position[0], position[1])

        self.native.resizeEvent = self.resizeEvent

    def qt_close_event(self, event):
        if not self.prog_close:
            event.ignore()
            if self.interface.closable:
                # Subtlety: If on_close approves the closing
                # this handler doesn't get called again
                self.interface.on_close()

    def create(self):
        self.native = wrap_container(self.container.native, self)

    def show(self):
        self.native.show()
        self.interface.on_show()

    def close(self):
        # OK, this is a bit of a stretch, since
        # this could've been a user-induced close
        # on_closed as well, however this flag
        # is only used for qt_close_event and you
        # can check out the subtlety there.
        self.prog_close = True
        self.native.close()

    def hide(self):
        self.native.hide()
        self.interface.on_hide()

    def get_title(self):
        return self.native.windowTitle()

    def set_title(self, title):
        self.native.setWindowTitle(title)

    def get_size(self):
        return Size(
            self.native.size().width(),
            self.native.size().height(),
        )

    def set_size(self, size):
        if not self.interface.resizable:
            self.native.setFixedSize(size[0], size[1])
        self.native.resize(size[0], size[1])

    def resizeEvent(self, event):
        if self.interface.content:
            self.interface.content.refresh()

    def _extra_height(self):
        return self.native.size().height() - self.container.native.size().height()

    def container_refreshed(self, container):
        min_width = self.interface.content.layout.min_width
        min_height = self.interface.content.layout.min_height
        size = self.container.native.size()
        # Calling self.set_size here to trigger logic about fixed size windows.
        if size.width() < min_width and size.height() < min_height:
            self.set_size((min_width, min_height + self._extra_height()))
        elif size.width() < min_width:
            self.set_size((min_width, size.height() + self._extra_height()))
        elif size.height() < min_height:
            self.set_size((size.width(), size.height() + self._extra_height()))
        self.container.native.setMinimumSize(min_width, min_height)

    def get_current_screen(self):
        return ScreenImpl(self.native.screen())

    def get_position(self) -> Position:
        return Position(self.native.pos().x(), self.native.pos().y())

    def set_position(self, position):
        self.native.move(position[0], position[1])

    def set_app(self, app):
        # All windows instantiated belongs to your only QApplication
        # but we need to set the icon
        self.native.setWindowIcon(app.interface.icon._impl.native)

    def get_visible(self):
        return self.native.isVisible()

    # =============== WINDOW STATES ================
    def get_window_state(self, in_progress_state=False):
        window_state = self.native.windowState()

        if window_state & Qt.WindowFullScreen:
            if self._in_presentation_mode:
                return WindowState.PRESENTATION
            else:
                return WindowState.FULLSCREEN
        elif window_state & Qt.WindowMaximized:
            return WindowState.MAXIMIZED
        elif window_state & Qt.WindowMinimized:
            return WindowState.MINIMIZED
        else:
            return WindowState.NORMAL

    def set_window_state(self, state):
        # Exit app presentation mode if another window is in it
        if any(
            window.state == WindowState.PRESENTATION and window != self.interface
            for window in self.interface.app.windows
        ):
            self.interface.app.exit_presentation_mode()

        current_state = self.get_window_state()
        if current_state == state:
            return

        elif current_state != WindowState.NORMAL:
            if current_state == WindowState.PRESENTATION:
                self.interface.screen = self._before_presentation_mode_screen
                del self._before_presentation_mode_screen
                self._in_presentation_mode = False
            self.native.showNormal()
            self.set_window_state(state)

        else:
            if state == WindowState.MAXIMIZED:
                self.native.showMaximized()

            elif state == WindowState.MINIMIZED:
                self.native.showMinimized()

            elif state == WindowState.FULLSCREEN:
                self.native.showFullScreen()

            elif state == WindowState.PRESENTATION:
                self._before_presentation_mode_screen = self.interface.screen
                self.native.showFullScreen()
                self._in_presentation_mode = True

    # ============== STUB =============

    def get_image_data(self):
        pass

    def set_content(self, widget):
        self.container.content = widget


class MainWindow(Window):
    def create(self):
        self.native = TogaMainWindow(self)
        self.native.setCentralWidget(self.container.native)

    def _submenu(self, group, group_cache):
        try:
            return group_cache[group]
        except KeyError:
            parent_menu = self._submenu(group.parent, group_cache)
            submenu = QMenu(group.text)
            parent_menu.addMenu(submenu)

        group_cache[group] = submenu
        return submenu

    def create_menus(self):
        menubar = self.native.menuBar()
        menubar.clear()

        group_cache = {None: menubar}
        submenu = None
        for cmd in self.interface.app.commands:
            submenu = self._submenu(cmd.group, group_cache)
            if isinstance(cmd, Separator):
                submenu.addSeparator()
            else:
                submenu.addAction(cmd._impl.create_menu_item())

    def create_toolbar(self):
        pass
