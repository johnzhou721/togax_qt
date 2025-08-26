import os
import asyncio

from toga.keys import Key

os.environ["TOGA_BACKEND"] = "togax_qt"

import toga
from toga.style.pack import COLUMN, LEFT, RIGHT, ROW, Pack


async def my_task(self):
    print("Task started")
    await asyncio.sleep(2)
    print("Task finished")
    print("===", self.main_window._impl.get_window_state())
    # self.main_window.hide()
    # self.main_window.show()
    # print(self.current_window)
    # await asyncio.sleep(0.5)
    # print(self.current_window)
    # print(self.current_window.title)


class MyApp(toga.App):
    def startup(self):
        self.icon = toga.Icon("star.jpg")
        c_box = toga.Box()
        f_box = toga.Box()
        box = toga.Box()

        self.c_input = toga.TextInput(readonly=False)
        c_input = self.c_input
        f_input = toga.TextInput()

        c_label = toga.Label("Celsius", style=Pack(text_align=LEFT))
        f_label = toga.Label("Fahrenheit", style=Pack(text_align=LEFT))
        join_label = toga.Label("is equivalent to", style=Pack(text_align=RIGHT))

        def calculate(widget):
            try:
                c_input.value = (float(f_input.value) - 32.0) * 5.0 / 9.0
            except ValueError:
                c_input.value = "???"

        button = toga.Button("Calculate", on_press=calculate)

        def showwindow(widget):
            def handler(widget):
                self.current_window.close()

            wind = toga.MainWindow(
                title="Toga",
                position=(800, 200),
                size=(300, 250),
                resizable=False,
                closable=False,
            )
            but = toga.Button("Hello!", on_press=handler)
            wind.content = but
            wind.show()

        def changeicon(widget):
            self.icon = toga.Icon("icon1.png")

        def minmizewindow(widget):
            print("Minimize", self.main_window)
            self.main_window.state = toga.constants.WindowState.MINIMIZED
            print("===", self.main_window._impl.get_window_state())

        button2 = toga.Button("Change Icon", on_press=changeicon)
        button3 = toga.Button("Minimize", on_press=minmizewindow)
        button4 = toga.Button("READONLY Textfield", on_press=self.disable)
        button5 = toga.Button("DISABLE Textfield", on_press=self.disable1)
        button6 = toga.Button("print ACTIVE WINDOW", on_press=self.activewindowprint)

        show = toga.Button("Show Window", on_press=showwindow)

        f_box.add(f_input)
        f_box.add(f_label)

        c_box.add(join_label)
        c_box.add(c_input)
        c_box.add(c_label)

        box.add(f_box)
        box.add(c_box)
        box.add(button)
        box.add(show)
        box.add(button2)
        box.add(button3)
        box.add(button4)
        box.add(button5)
        box.add(button6)

        box.style.update(direction=COLUMN, margin=10, gap=10)
        f_box.style.update(direction=ROW, gap=10)
        c_box.style.update(direction=ROW, gap=10)

        c_input.style.update(flex=1)
        f_input.style.update(flex=1, margin_left=210)
        c_label.style.update(width=100)
        f_label.style.update(width=100)
        join_label.style.update(width=200)

        button.style.update(margin_top=5)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.title = "Title"
        self.main_window.content = box
        self.main_window.show()
        self.main_window.state = toga.constants.WindowState.MINIMIZED
        asyncio.create_task(my_task(self))

        backtab_command = toga.Command(
            self.on_backtab,
            "BackTab",
            shortcut=Key.SHIFT + Key.TAB,  # Shift + Tab
        )
        self.commands.add(backtab_command)
        print(self.main_window.title)

    async def on_backtab(self, widget):
        print("backtab")
        await self.current_window.dialog(
            toga.InfoDialog("Hello", "This is an information dialog!")
        )

    def preferences(self):
        print("Preferences!")
        print(self.current_window)

    def disable(self, widget):
        self.c_input.readonly = True

    def disable1(self, widget):
        self.c_input.enabled = False

    def activewindowprint(self, widget):
        print(self.current_window)


def main():
    app = MyApp(
        "Temperature Converter",
        "org.beeware.toga.examples.tutorial",
        home_page="https://github.com/johnzhou721",
    )
    cmd = toga.Command.standard(app, toga.Command.PREFERENCES)
    app.commands.add(cmd)
    return app


if __name__ == "__main__":
    main().main_loop()
