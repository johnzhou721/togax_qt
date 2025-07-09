import toga
from toga.style.pack import COLUMN, ROW
import threading
import random
import time
from PySide6 import QtAsyncio

def my_coroutine():
    try:
        print("Hello from coroutine!")
        print("Finished!")
    except Exception as e:
        print(e)

class HelloWorld(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.show()
        print(self.loop.is_running())
        self.loop.call_later(5, my_coroutine)

HelloWorld("HelloWorld", "com.example.helloworld").main_loop()
