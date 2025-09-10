from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from PySide6.QtCore import Qt, QEvent, QTimer
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Toggle Max/Normal", self)
        self.button.clicked.connect(self.start_toggle)
        self.monitoring = False
        self.show()

    def start_toggle(self):
        if not self.monitoring:
            self.monitoring = True
            self.showMaximized()

    def changeEvent(self, event):
        if event.type() == QEvent.Type.WindowStateChange:
            if self.monitoring and self.windowState() & Qt.WindowState.WindowMaximized:
                QTimer.singleShot(0, self.normalshow)

    def normalshow(self):
        self.monitoring = False
        self.showNormal()


app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec())
