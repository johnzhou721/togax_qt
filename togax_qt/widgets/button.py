from travertino.size import at_least

from ..libs import QPushButton
from .base import Widget


class Button(Widget):
    def create(self):
        self.native = QPushButton()

        self.native.clicked.connect(self.clicked)

        self._icon = None

    def clicked(self):
        self.interface.on_press()

    def get_text(self):
        return str(self.native.text())

    def set_text(self, text):
        self.native.setText(text)

    def get_icon(self):
        # Not impl'd yet
        return None

    def set_icon(self, icon):
        # Not impl'd yet
        pass

    def rehint(self):
        width = self.native.sizeHint().width()
        height = self.native.sizeHint().height()

        self.interface.intrinsic.width = at_least(width)
        self.interface.intrinsic.height = height  # height of a button is known
