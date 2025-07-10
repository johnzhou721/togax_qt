import toga
from toga.style.pack import COLUMN, ROW
from PySide6.QtGui import QGuiApplication
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

async def grab(self):
    await asyncio.sleep(1)
    with open('output.png', 'wb') as f:
        f.write(self.screens[0]._impl.get_image_data())

class HelloWorld(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title=self.formal_name)
        #self.main_window = toga.App.BACKGROUND
        self.main_window.show()
        print(self.loop.is_running())
        self.loop.create_task(my_coroutine())
        print(self.screens[0].size)
        print(self.screens[0].name)
        self.loop.create_task(grab(self))
        platform = QGuiApplication.platformName()
        print(platform)
        

HelloWorld("HelloWorld", "com.example.helloworld").main_loop()
