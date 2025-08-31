from travertino.size import at_least
from travertino.constants import LEFT, CENTER, RIGHT, JUSTIFY

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit
from .base import Widget


class TogaLineEdit(QLineEdit):
    def __init__(self, impl, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.impl = impl
        self.interface = impl.interface
        self.textChanged.connect(self.qt_on_change)
        self.returnPressed.connect(self.qt_on_confirm)

    def qt_on_change(self):
        self.interface._value_changed()

    def qt_on_confirm(self):
        self.interface.on_confirm()

    def focusInEvent(self, event):
        super().focusInEvent(event)
        self.interface.on_gain_focus()

    def focusOutEvent(self, event):
        super().focusOutEvent(event)
        self.interface.on_lose_focus()


class TextInput(Widget):
    def create(self):
        self.native = TogaLineEdit(self)

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
            LEFT: Qt.AlignLeft | Qt.AlignVCenter,
            CENTER: Qt.AlignHCenter | Qt.AlignVCenter,
            RIGHT: Qt.AlignRight | Qt.AlignVCenter,
            JUSTIFY: Qt.AlignJustify | Qt.AlignVCenter,
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
        self.interface.factory.not_implemented("validation of textinput")

    def clear_error(self):
        self.interface.factory.not_implemented("validation of textinput")

    def is_valid(self):
        return self.native.toolTip() == ""
