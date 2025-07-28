from .libs import QMainWindow, QMenu
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

        self.native.setWindowTitle(title)
        self.native.resize(size[0], size[1])
        if position is not None:
            self.native.move(position[0], position[1])

        self.native.resizeEvent = self.resizeEvent

    def create(self):
        self.container = Container()
        self.native = self.container.native

    def show(self):
        self.native.show()

    def close(self):
        self.native.close()

    def get_title(self):
        self.native.windowTitle()

    def set_title(self, title):
        self.native.setWindowTitle(title)

    def get_size(self):
        return Size(
            self.native.size().width,
            self.native.size().height,
        )

    def set_size(self, size):
        self.native.resize(size[0], size[1])

    def resizeEvent(self, event):
        if self.interface.content:
            self.interface.content.refresh()

    def get_current_screen(self):
        return ScreenImpl(self.native.screen())

    def get_position(self) -> Position:
        return Position(self.native.position().x(), self.native.position().y())

    def set_position(self, position):
        self.native.move(position[0], position[1])

    def set_app(self, app):
        # you don't set the app a window belongs to, all windows
        # instantiated belongs to your only QApplication
        pass

    def get_visible(self):
        return self.native.isVisible()

    # =============== STUBS FOR WINDOW STATES ================
    def get_window_state(self, in_progress_state=False):
        # Stub.
        return WindowState.NORMAL

    def set_window_state(self, state):
        pass

    # ============== STUB =============

    def get_image_data(self):
        pass

    def set_content(self, widget):
        self.container.content = widget


class MainWindow(Window):
    def create(self):
        self.native = QMainWindow()
        self.container = Container()
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
