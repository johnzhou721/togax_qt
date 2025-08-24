import pytest

from toga.images import Image as TogaImage

from .probe import BaseProbe


class ScreenProbe(BaseProbe):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self._impl = screen._impl
        self.native = screen._impl.native

    def get_screenshot(self, format=TogaImage):
        pytest.skip("Images aren't implemented yet'")
