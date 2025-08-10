from .libs import (
    Qt,
    QApplication,
    QGuiApplication,
    QEventLoop,
    QObject,
    Signal,
    QTimer,
)
import asyncio
from .screens import Screen as ScreenImpl
from toga.command import Command, Group
import toga
from .togax import NativeIcon
from .libs import QIcon


def operate_on_focus(method_name, interface):
    fw = QApplication.focusWidget()
    if not fw:
        return
    # call the method if it exists
    fn = getattr(fw, method_name, None)
    if callable(fn):
        fn()


class AppSignalsListener(QObject):
    appStarting = Signal()

    def __init__(self, impl):
        super().__init__()
        self.impl = impl
        self.interface = impl.interface
        self.appStarting.connect(self.on_app_starting)
        QTimer.singleShot(0, self.appStarting.emit)

    def on_app_starting(self):
        self.interface._startup()


appsingle = QApplication()


class App:
    # GTK apps exit when the last window is closed
    CLOSE_ON_LAST_WINDOW = True
    # GTK apps use default command line handling
    HANDLES_COMMAND_LINE = False

    def __init__(self, interface):
        self.interface = interface
        self.interface._impl = self

        self.native = appsingle
        self.loop = QEventLoop(self.native)
        asyncio.set_event_loop(self.loop)
        self.app_close_event = asyncio.Event()
        self.native.aboutToQuit.connect(self.app_close_event.set)

        # no idea what to name this...
        self.signalslistener = AppSignalsListener(self)

    ######################################################################
    # Commands and menus
    # Impl incomplete.  See GitHub thread.
    ######################################################################

    def create_standard_commands(self):
        # This is sorta weird.  On KDE, default bundled apps have these stuff
        # and they automatically enable / disable based on if this functionality
        # is available... there's not a satisfying way to implement that in Qt
        # though... see https://stackoverflow.com/questions/2047456, so we omit
        # the enabled detection for now.  Most people just use Ctrl + Z etc.
        # anyways...
        self.interface.commands.add(
            Command(
                lambda interface: operate_on_focus("undo", interface),
                "Undo",
                shortcut=toga.Key.MOD_1 + "z",
                group=Group.EDIT,
                order=10,
                icon=NativeIcon(QIcon.fromTheme("edit-undo")),
            ),
            Command(
                lambda interface: operate_on_focus("redo", interface),
                "Redo",
                shortcut=toga.Key.SHIFT + toga.Key.MOD_1 + "z",
                group=Group.EDIT,
                order=20,
                icon=NativeIcon(QIcon.fromTheme("edit-redo")),
            ),
            Command(
                lambda interface: operate_on_focus("cut", interface),
                "Cut",
                shortcut=toga.Key.MOD_1 + "x",
                group=Group.EDIT,
                section=10,
                order=10,
                icon=NativeIcon(QIcon.fromTheme("edit-cut")),
            ),
            Command(
                lambda interface: operate_on_focus("copy", interface),
                "Copy",
                shortcut=toga.Key.MOD_1 + "c",
                group=Group.EDIT,
                section=10,
                order=20,
                icon=NativeIcon(QIcon.fromTheme("edit-copy")),
            ),
            Command(
                lambda interface: operate_on_focus("paste", interface),
                "Paste",
                shortcut=toga.Key.MOD_1 + "v",
                group=Group.EDIT,
                section=10,
                order=30,
                icon=NativeIcon(QIcon.fromTheme("edit-paste")),
            ),
        )

    def create_menus(self):
        for window in self.interface.windows:
            if hasattr(window._impl, "create_menus"):
                window._impl.create_menus()

    ######################################################################
    # App lifecycle
    ######################################################################

    # We can't call this under test conditions, because it would kill the test harness
    def exit(self):  # pragma: no cover
        self.native.quit()

    def main_loop(self):
        self.loop.run_until_complete(self.app_close_event.wait())

    def set_icon(self, icon):
        for window in QApplication.topLevelWidgets():
            window.setWindowIcon(icon._impl.native)
        self.interface.commands[Command.ABOUT].icon = icon
        self.interface.commands[Command.PREFERENCES].icon = icon

    # Not implemented yet
    def set_main_window(self, window):
        self.interface.factory.not_implemented("App.set_main_window()")

    ######################################################################
    # App resources
    ######################################################################

    # ScreenImpl not impl'd yet
    def get_screens(self):
        screens = QGuiApplication.screens()
        primary = QGuiApplication.primaryScreen()
        screens = [primary] + [
            s for s in screens if s != primary
        ]  # Ensure first is primary

        return [ScreenImpl(native=monitor) for monitor in QGuiApplication.screens()]

    ######################################################################
    # App state
    ######################################################################

    def get_dark_mode_state(self):
        return QGuiApplication.styleHints().colorScheme() == Qt.ColorScheme.Dark

    ######################################################################
    # App capabilities
    ######################################################################

    def beep(self):
        QApplication.beep()

    # TODO: Add Icon, make tabs, version
    def show_about_dialog(self):
        print("NOT IMPLD: ABOUT DIALOG")
        pass

    ######################################################################
    # Cursor control
    ######################################################################

    def hide_cursor(self):
        self.interface.factory.not_implemented("App.hide_cursor()")

    def show_cursor(self):
        self.interface.factory.not_implemented("App.show_cursor()")

    ######################################################################
    # Window control
    ######################################################################

    def get_current_window(self):
        return self.native.activeWindow()

    def set_current_window(self, window):
        window._impl.native.activateWindow()
