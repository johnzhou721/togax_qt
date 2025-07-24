from travertino.size import at_least

from ..libs import QLabel, Qt
from .base import Widget


class Label(Widget):
    def create(self):
        self.native = QLabel()

    def set_text_align(self, value):
        alignment_map = {
            0: Qt.AlignmentFlag.AlignLeft,
            1: Qt.AlignmentFlag.AlignCenter,
            2: Qt.AlignmentFlag.AlignRight,
        }
        self.native.setAlignment(alignment_map.get(value, Qt.AlignmentFlag.AlignLeft))

    def set_color(self, value):
        pass

    def set_font(self, font):
        pass

    def get_text(self):
        return self.native.text()

    def set_text(self, value):
        self.native.setText(value)

    def rehint(self):
        content_size = self.native.sizeHint()
        self.interface.intrinsic.width = at_least(content_size.width())
        self.interface.intrinsic.height = content_size.height()

