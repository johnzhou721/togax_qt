from .base import Widget
from ..libs import QWidget
from travertino.size import at_least


class Box(Widget):
    def create(self):
        self.native = QWidget()

    def rehint(self):
        self.interface.intrinsic.width = at_least(0)
        self.interface.intrinsic.height = at_least(0)
