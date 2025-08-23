from toga import NotImplementedWarning

from .app import App
from .paths import Paths
from .icons import Icon
from .statusicons import MenuStatusIcon, SimpleStatusIcon, StatusIconSet
from .window import MainWindow, Window
from .command import Command
from .widgets.button import Button
from .widgets.box import Box
from .fonts import Font
from .container import Container
from .widgets.label import Label
from .widgets.textinput import TextInput
from . import dialogs

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
    "Font",
    "Container",
    "Box",
    "Label",
    "TextInput",
    "dialogs",
]


def not_implemented(feature):
    NotImplementedWarning.warn("Qt", feature)


def __getattr__(name):  # pragma: no cover
    raise NotImplementedError(f"Toga's Qt backend doesn't implement {name}")
