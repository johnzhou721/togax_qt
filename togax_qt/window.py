from .libs import QApplication, QMainWindow


class Window:
    def __init__(self, interface, title, position, size):
        self.interface = interface
        self.interface._impl = self

        self.create()

        self.native.setWindowTitle(title)
        self.native.resize(size[0], size[1])
        self.native.move(position[0], position[1])
    
    def create(self):
        self.native = QMainWindow()

    def show(self):
        self.native.show()

    def set_title(self, title):
        self.native.setWindowTitle(title)

    def close(self):
        self.native.close()

    def set_size(self, size):
        self.native.resize(size[0], size[1])

    def set_position(self, position):
        self.native.move(position[0], position[1])


class MainWindow(Window):
    def __init__(self, interface, title, position, size):
        super().__init__(interface, title, position, size)

