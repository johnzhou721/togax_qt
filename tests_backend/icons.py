from pathlib import Path

import pytest
from PySide6.QtGui import QIcon

import togax_qt

from .probe import BaseProbe


class IconProbe(BaseProbe):
    alternate_resource = "resources/icons/orange"

    def __init__(self, app, icon):
        self.icon = icon
        self.app = app
        assert isinstance(self.icon._impl.native, QIcon)

    def assert_icon_content(self, path):
        if path == "resources/icons/green":
            assert (
                self.icon._impl.path == self.app.paths.app / "resources/icons/green.png"
            )
        elif path == "resources/icons/blue":
            assert (
                self.icon._impl.path == self.app.paths.app / "resources/icons/blue.png"
            )
        elif path == "resources/icons/orange":
            assert (
                self.icon._impl.path
                == self.app.paths.app / "resources/icons/orange.ico"
            )
        else:
            pytest.fail("Unknown icon resource")

    def assert_default_icon_content(self):
        assert (
            self.icon._impl.path
            == Path(togax_qt.__file__).parent / "resources/toga.png"
        )

    def assert_platform_icon_content(self):
        pytest.xfail("Qt does not use sized icons")

    def assert_app_icon_content(self):
        pytest.xfail("Android apps don't have app icons at runtime")
