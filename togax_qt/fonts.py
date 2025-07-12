import warnings

from toga.fonts import _IMPL_CACHE, UnknownFontError


_CUSTOM_FONT_NAMES = {}


class Font:
    def __init__(self, interface):
        self.interface = interface
        self.native = None

    def load_predefined_system_font(self):
        warnings.warn(
            "load_predefined_system_font stub not implemented", RuntimeWarning
        )

    def load_user_registered_font(self):
        warnings.warn(
            "load_user_registered_font stub not implemented", RuntimeWarning
        )

    def load_arbitrary_system_font(self):
        warnings.warn(
            "Arbitrary system fonts not yet supported on iOS", RuntimeWarning
        )

    def _assign_native(self, font_name):
        self.native = None
        _IMPL_CACHE[self.interface] = self

