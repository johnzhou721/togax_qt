import sys

from toga import Command as StandardCommand, Group, Key


class Command:

    def __init__(self, interface):
        self.interface = interface
        self.native = []

    @classmethod
    def standard(self, app, id):
        return None

    def set_enabled(self, value):
        pass
