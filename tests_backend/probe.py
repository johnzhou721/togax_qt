import asyncio

import toga
from togax_qt.libs import QApplication


class BaseProbe:
    async def redraw(self, message=None, delay=0):
        for widget in QApplication.allWidgets():
            widget.repaint()  # repaint immediately

        # Wait a second... (pun intended)
        if toga.App.app.run_slow:
            delay = max(1, delay)

        if delay:
            print("Waiting for redraw" if message is None else message)
            await asyncio.sleep(delay)

    def assert_image_size(self, image_size, size, screen):
        assert image_size == size
