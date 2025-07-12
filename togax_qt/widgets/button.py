from travertino.size import at_least

from ..libs import QPushButton, QObject, Slot
from .base import Widget


# Let's not risk inheriting button from QObject...
class PushListener(QObject):
    def __init__(self, impl):
        self.impl = impl
        self.interface = impl.interface
        impl.native.clicked.connect(self.clicked)
    
    @Slot()
    def clicked(self):
        self.interface.on_press()


class Button(Widget):
    def create(self):
        self.native = QPushButton()
        
        self.pushlistener = PushListener(self)

        self._icon = None

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
    
