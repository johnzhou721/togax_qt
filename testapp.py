import os

os.environ["TOGA_BACKEND"] = "togax_qt"

import toga
from toga.style.pack import COLUMN, LEFT, RIGHT, ROW, Pack


class MyApp(toga.App):
    def startup(self):
        self.icon = toga.Icon("icon.png")
        c_box = toga.Box()
        f_box = toga.Box()
        box = toga.Box()

        c_input = toga.TextInput(readonly=True)
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
                print("hello!1")
                print(self.current_window)

            wind = toga.Window(title="Toga", position=(800, 200), size=(300, 250))
            but = toga.Button("Hello!", on_press=handler)
            wind.content = but
            wind.show()

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
        self.main_window.content = box
        self.main_window.show()

    def preferences(self):
        print("Preferences!")
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
