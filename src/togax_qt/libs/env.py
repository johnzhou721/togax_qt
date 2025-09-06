from PySide6.QtGui import QGuiApplication


def get_is_wayland():
    return "wayland" == QGuiApplication.platformName()
