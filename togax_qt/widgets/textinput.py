from travertino.size import at_least
from travertino.constants import LEFT, CENTER, RIGHT

from ..libs import QEvent, QLineEdit, QObject, Qt
from .base import Widget
import warnings


class TextInputListener(QObject):
    def __init__(self, impl):
        super().__init__()
        self.impl = impl
        self.native = impl.native
        self.interface = impl.interface

        self.native.textChanged.connect(self.qt_on_change)
        self.native.returnPressed.connect(self.qt_on_confirm)
        self.native.installEventFilter(self)
        
    def qt_on_change(self):
        self.interface._value_changed()

    def qt_on_confirm(self):
        self.interface.on_confirm()

    def eventFilter(self, obj, event):
        if obj == self.native:
            if event.type() == QEvent.FocusIn:
                self.interface.on_gain_focus()
            elif event.type() == QEvent.FocusOut:
                self.interface.on_lose_focus()
        return False


class TextInput(Widget):
    def create(self):
        self.native = QLineEdit()
        self.listener = TextInputListener(self)

    def get_readonly(self):
        return self.native.isReadOnly()

    def set_readonly(self, value):
        self.native.setReadOnly(value)

    def get_placeholder(self):
        return self.native.placeholderText()

    def set_placeholder(self, value):
        self.native.setPlaceholderText(value)

    def set_text_align(self, value):
        alignment = {
            LEFT: Qt.AlignLeft,
            CENTER: Qt.AlignHCenter,
            RIGHT: Qt.AlignRight,
        }.get(value, Qt.AlignLeft)
        self.native.setAlignment(alignment)

    def get_value(self):
        return self.native.text()

    def set_value(self, value):
        self.native.setText(value)

    def rehint(self):
        size = self.native.sizeHint()
        self.interface.intrinsic.width = at_least(
            max(self.interface._MIN_WIDTH, size.width())
        )
        self.interface.intrinsic.height = size.height()

    def set_error(self, error_message):
        warnings.warn(
            "set_error stub not implemented", RuntimeWarning
        )

    def clear_error(self):
        warnings.warn(
            "clear_error stub not implemented", RuntimeWarning
        )

    def is_valid(self):
        return self.native.toolTip() == ""
