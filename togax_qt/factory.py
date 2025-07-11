from toga import NotImplementedWarning

from .app import App
from .paths import Paths
from .icons import Icon
from .statusicons import MenuStatusIcon, SimpleStatusIcon, StatusIconSet
from .window import MainWindow, Window
from .command import Command
from .widgets.button import Button


__all__ = [
    "not_implemented",
    "App",
    "Paths",
    "Icon",
    "MenuStatusIcon",
    "SimpleStatusIcon",
    "StatusIconSet",
    "Window",
    "MainWindow",
    "Command",
    "Button",
]

def not_implemented(feature):
    NotImplementedWarning.warn("GTK", feature)

def __getattr__(name):  # pragma: no cover
    raise NotImplementedError(f"Toga's Qt backend doesn't implement {name}")
