import sys
from pathlib import Path

import toga

from .libs import QPixmap, QIcon


class Icon:
    EXTENSIONS = [".png", ".jpeg", ".jpg", ".gif", ".bmp"]
    SIZES = [512, 256, 128, 72, 64, 32, 16]  # same as GTK for now.

    def __init__(self, interface, path):
        self.interface = interface
        self._native = {}

        if path is None:
            # Use the executable location to find the share folder; look for icons
            # matching the app bundle in that location.
            hicolor = Path(sys.executable).parent.parent / "share/icons/hicolor"
            path = {
                size: hicolor / f"{size}x{size}/apps/{toga.App.app.app_id}.png"
                for size in self.SIZES
                if (hicolor / f"{size}x{size}/apps/{toga.App.app.app_id}.png").is_file()
            }

        self.paths = path

        if not path:
            raise FileNotFoundError("No icon variants found")

        try:
            for size, path in self.paths.items():
                native = QPixmap(str(path)).scaled(size, size)
                self._native[size] = native
        except Exception as exc:
            raise ValueError(f"Unable to load icon from {path}") from exc

    def native(self, size):
        try:
            return QIcon(self._native[size])
        except KeyError:
            native = self._native[next(iter(self._native))].scaled(size, size)
            self._native[size] = native
            return QIcon(native)
