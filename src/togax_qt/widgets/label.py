from travertino.size import at_least
from travertino.constants import LEFT, CENTER, RIGHT

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel
from .base import Widget


class Label(Widget):
    def create(self):
        self.native = QLabel()

    def set_text_align(self, value):
        alignment = {
            LEFT: Qt.AlignmentFlag.AlignLeft,
            CENTER: Qt.AlignmentFlag.AlignCenter,
            RIGHT: Qt.AlignmentFlag.AlignRight,
        }.get(value, Qt.AlignLeft)
        self.native.setAlignment(alignment)

    def set_color(self, value):
        pass

    def set_font(self, font):
        pass

    def get_text(self):
        return self.native.text()

    def set_text(self, value):
        self.native.setText(value)
        self.refresh()

    def rehint(self):
        content_size = self.native.sizeHint()
        self.interface.intrinsic.width = at_least(content_size.width())
        self.interface.intrinsic.height = content_size.height()
