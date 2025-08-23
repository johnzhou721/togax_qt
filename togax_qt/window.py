from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QMenu
from toga.constants import WindowState
from toga.types import Position, Size
from toga.command import Separator
from .screens import Screen as ScreenImpl
from .container import Container


class Window:
    def __init__(self, interface, title, position, size):
        self.interface = interface
        self.interface._impl = self

        self.create()

        self.native.interface = interface
        self.native.impl = self
        self.native.closeEvent = self.my_close_event
        self.accept_close = False

        self._in_presentation_mode = False

        self.native.setWindowTitle(title)
        self.native.resize(size[0], size[1])
        if position is not None:
            self.native.move(position[0], position[1])

        self.native.resizeEvent = self.resizeEvent

    def my_close_event(self, event):
        if self.accept_close:
            event.accept()
        else:
            self.interface.on_close()
            event.ignore()

    def create(self):
        self.container = Container()
        self.native = self.container.native
        self.container.native.show()

    def show(self):
        self.native.showNormal()
        self.native.activateWindow()

    def close(self):
        self.accept_close = True
        self.native.close()

    def hide(self):
        self.native.hide()

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
        self.native.resize(size[0], size[1])

    def resizeEvent(self, event):
        if self.interface.content:
            self.interface.content.refresh()

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
        self.native = QMainWindow()
        self.container = Container()
        self.container.native.show()
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
