import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer

app = QApplication(sys.argv)

window = QMainWindow()
window.resize(300, 200)
window.move(250, 200)  # Move window to x=250, y=200
window.show()


def print_info():
    pos = window.pos()
    size = window.size()
    print(f"Window position: ({pos.x()}, {pos.y()})")
    print(f"Window size: {size.width()} x {size.height()}")


# Wait 1 second before printing
QTimer.singleShot(1000, print_info)

sys.exit(app.exec())
