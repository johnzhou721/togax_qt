from toga.screens import Screen as ScreenInterface
from toga.types import Position, Size

from .libs import QScreen, QByteArray, QBuffer, QIODevice


class Screen:
    _instances = {}

    def __new__(cls, native):
        if native in cls._instances:
            return cls._instances[native]
        else:
            instance = super().__new__(cls)
            instance.interface = ScreenInterface(_impl=instance)
            instance.native = native
            cls._instances[native] = instance
            return instance

    def get_name(self):
        return '|'.join([self.native.name(), self.native.model(), self.native.manufacturer(), self.native.serialNumber()])

    def get_origin(self) -> Position:
        return self.native.geometry().topLeft()

    def get_size(self) -> Size:
        geometry = self.native.geometry()
        return Size(geometry.width(), geometry.height())

    def get_image_data(self):
        grabbed = self.native.grabWindow(0)
        byte_array = QByteArray()
        buffer = QBuffer(byte_array)
        buffer.open(QIODevice.WriteOnly)
        grabbed.save(buffer, "PNG")
        return byte_array.data()
