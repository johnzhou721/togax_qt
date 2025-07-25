


class Command:

    def __init__(self, interface):
        self.interface = interface
        self.native = []

    @classmethod
    def standard(self, app, id):
        return None

    def set_enabled(self, value):
        pass
