"""
This is a module that stores some random stuff
that Toga doesn't yet conceptualize, but is needed
by this unofficial backend.
"""

from toga import Command, Icon, Group


###########################################
# Add support for native icon wrapper.
###########################################

# hack hack hack... the icon thing is used
# nowhere else, and our backend directly
# accesses the native method when using
# commands... so we just do it like this.


class NativeIcon:
    def __init__(self, native):
        self._impl = NativeIconImpl(native)


class NativeIconImpl:
    def __init__(self, native):
        self._native = native

    def native(self, size):
        # Trust that native icons have the correct size.
        return self._native


# Make setter of command accept the hack.


def __icon(self, icon_or_name) -> None:
    # added second condition.
    if (
        isinstance(icon_or_name, Icon)
        or isinstance(icon_or_name, NativeIcon)
        or icon_or_name is None
    ):
        self._icon = icon_or_name
    else:
        self._icon = Icon(icon_or_name)


Command.icon = Command.icon.setter(__icon)


###########################################
# Add support for Settings group.
###########################################

Group.SETTINGS = Group("Settings", order=80)
