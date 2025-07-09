import toga
from toga.style.pack import COLUMN, ROW

class HelloWorld(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title=self.formal_name)
        print("Startup")
        self.main_window.show()
        print("Should be shown")

HelloWorld("HelloWorld", "com.example.helloworld").main_loop()
