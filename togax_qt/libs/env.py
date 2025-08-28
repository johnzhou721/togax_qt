from PySide6.QtGui import QGuiApplication
import os

IS_WAYLAND = "wayland" == QGuiApplication.platformName()
TESTING = "PYTEST_CURRENT_TEST" in os.environ
