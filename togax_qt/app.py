from .libs import Qt, QApplication, QGuiApplication, QAsyncioEventLoop, QObject, Signal, QTimer, QAsyncioTask
from PySide6.QtWidgets import QMainWindow
import asyncio

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

def gtk_task_factory(loop, coro, **kwargs):
    return QAsyncioTask(coro, loop=loop, **kwargs)

class App:
    # GTK apps exit when the last window is closed
    CLOSE_ON_LAST_WINDOW = True
    # GTK apps use default command line handling
    HANDLES_COMMAND_LINE = False

    def __init__(self, interface):
        self.interface = interface
        self.interface._impl = self
        
        self.native = QApplication()
        self.loop = QAsyncioEventLoop(self.native)
        self.loop.set_task_factory(gtk_task_factory)
        asyncio.set_event_loop(self.loop)
        
        # no idea what to name this...
        self.signalslistener = AppSignalsListener(self)

    ######################################################################
    # Commands and menus
    # Not impl'd yet
    ######################################################################

    def create_standard_commands(self):
        pass

    def _submenu(self, group, menubar):
        pass

    def create_menus(self):
        pass

    ######################################################################
    # App lifecycle
    ######################################################################

    # We can't call this under test conditions, because it would kill the test harness
    def exit(self):  # pragma: no cover
        self.native.quit()

    def main_loop(self):
        #self.native.exec()
        self.native.exec()

    # Not implemented yet
    def set_icon(self, icon):
    	self.interface.factory.not_implemented("App.set_icon()")

    # Not implemented yet
    def set_main_window(self, window):
        self.interface.factory.not_implemented("App.set_main_window()")

    ######################################################################
    # App resources
    ######################################################################

    # ScreenImpl not impl'd yet
    def get_screens(self):
        # return [ScreenImpl(native=monitor) for monitor in QGuiApplication.screens()]
        pass

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

    # not implemented
    def _close_about(self, dialog, *args, **kwargs):
        pass

    def show_about_dialog(self):
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
    # Not implemented
    ######################################################################

    def get_current_window(self):
        return self.native.activeWindow()

    def set_current_window(self, window):
        self.native.setActiveWindow(window)
