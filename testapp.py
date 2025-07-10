import toga
from toga.style.pack import COLUMN, ROW
import threading
import random
import time
import asyncio

async def my_coroutine():
    try:
        print("Hello from coroutine!")
        await asyncio.sleep(1)
        print("Finished!")
    except Exception as e:
        print(e)

class HelloWorld(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.show()
        print(self.loop.is_running())
        self.loop.create_task(my_coroutine())

HelloWorld("HelloWorld", "com.example.helloworld").main_loop()
