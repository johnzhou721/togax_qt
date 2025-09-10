from PySide6.QtWidgets import QApplication, QWidget, QPushButton
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Toggle Max/Normal", self)
        self.button.clicked.connect(self.toggle)
        self.show()

    def toggle(self):
        for _ in range(10):
            self.showMaximized()
            self.showNormal()


app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec())
