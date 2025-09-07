from travertino.constants import LEFT, CENTER, RIGHT, JUSTIFY, TOP, BOTTOM
from PySide6.QtCore import Qt


def qt_text_align(valuex, valuey):
    return {
        LEFT: Qt.AlignLeft,
        CENTER: Qt.AlignHCenter,
        RIGHT: Qt.AlignRight,
        JUSTIFY: Qt.AlignJustify,
    }[valuex] | {
        TOP: Qt.AlignTop,
        CENTER: Qt.AlignVCenter,
        BOTTOM: Qt.AlignBottom,
    }[valuey]
