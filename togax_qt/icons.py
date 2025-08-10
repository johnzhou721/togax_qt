import sys
from pathlib import Path

import toga

from .libs import QIcon


class Icon:
    EXTENSIONS = [".png", ".jpeg", ".jpg", ".gif", ".bmp"]
    SIZES = None

    def __init__(self, interface, path):
        self.interface = interface

        if path is None:
            SIZES = [512, 256, 128, 72, 64, 32, 16]  # same as GTK for now.
            # Use the executable location to find the share folder; look for icons
            # matching the app bundle in that location.
            hicolor = Path(sys.executable).parent.parent / "share/icons/hicolor"
            sizes = {
                size: hicolor / f"{size}x{size}/apps/{toga.App.app.app_id}.png"
                for size in SIZES
                if (hicolor / f"{size}x{size}/apps/{toga.App.app.app_id}.png").is_file()
            }

            if not sizes:
                raise FileNotFoundError("No icon variants found")

            self.native = QIcon(str(sizes[max(sizes)]))
        else:
            self.native = QIcon(str(path))
