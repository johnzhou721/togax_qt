import asyncio
import pytest

from togax_qt.libs import QMainWindow


class WindowProbe:
    supports_closable = True
    supports_as_image = False  # not impld yet
    supports_focus = True
    supports_minimizable = False  # not impld yet
    supports_move_while_hidden = False
    supports_unminimize = False  # not impld yet
    supports_minimize = False  # not impld yet
    supports_placement = True

    def __init__(self, app, window):
        self.app = app
        self.window = window
        self.native = window._impl.native
        assert isinstance(self.native, QMainWindow) or hasattr(self.native, "close")

    async def wait_for_window(self, message, state=None):
        await self.redraw(message, delay=0.1)
        if state:
            timeout = 5
            polling_interval = 0.1
            exception = None
            loop = asyncio.get_running_loop()
            start_time = loop.time()
            while (loop.time() - start_time) < timeout:
                try:
                    assert self.instantaneous_state == state
                    assert self.window._impl._pending_state_transition is None
                    return
                except AssertionError as e:
                    exception = e
                    await asyncio.sleep(polling_interval)
            raise exception

    async def cleanup(self):
        self.window.close()
        await self.redraw("Closing window", delay=0.5)

    def close(self):
        if self.is_closable:
            self.native.close()

    @property
    def content_size(self):
        size = self.native.size()
        return size.width(), size.height()

    @property
    def is_resizable(self):
        return True  # currently not changing this

    @property
    def is_closable(self):
        return True  # currently not changing this

    @property
    def is_minimized(self):
        raise pytest.skip("window state no impl")

    def minimize(self):
        raise pytest.skip("window state no impl")

    def unminimize(self):
        raise pytest.skip("window state no impl")

    @property
    def instantaneous_state(self):
        raise pytest.skip("window state no impl")

    def has_toolbar(self):
        raise pytest.skip("toolbar no impl")

    def assert_is_toolbar_separator(self, index, section=False):
        raise pytest.skip("toolbar no impl")

    def assert_toolbar_item(self, index, label, tooltip, has_icon, enabled):
        raise pytest.skip("toolbar no impl")

    def press_toolbar_button(self, index):
        raise pytest.skip("toolbar no impl")
