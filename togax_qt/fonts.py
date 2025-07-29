_CUSTOM_FONT_NAMES = {}


## Note -- have to pass b/c in tests warning seem to be errors


class Font:
    def __init__(self, interface):
        # warnings.warn("Unsupported", RuntimeWarning)
        pass

    def load_predefined_system_font(self):
        # warnings.warn(
        #    "load_predefined_system_font stub not implemented", RuntimeWarning
        # )
        pass

    def load_user_registered_font(self):
        # warnings.warn("load_user_registered_font stub not implemented", RuntimeWarning)
        pass

    def load_arbitrary_system_font(self):
        # warnings.warn("Arbitrary system fonts not yet supported on iOS", RuntimeWarning)
        pass
