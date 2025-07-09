import toga
from toga.style.pack import COLUMN, ROW
import threading

class HelloWorld(toga.App):
    def beepprint(self):
        print("Beep")
        self.beep()
    def startup(self):
        self.main_window = toga.MainWindow(title=self.formal_name)
        print("Startup")
        self.main_window.show()
        print("Should be shown")
        timer = threading.Timer(5.0, self.beepprint)
        timer.start()

HelloWorld("HelloWorld", "com.example.helloworld").main_loop()
