from PySide6.QtGui import QGuiApplication

IS_WAYLAND = "wayland" == QGuiApplication.platformName()
