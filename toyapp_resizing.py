import toga
from toga.style import Pack
from toga.style.pack import COLUMN


class ExampleApp(toga.App):
    def startup(self):
        # Inner box starts at 100x100
        self.inner_box = toga.Box(style=Pack(width=100, height=100))

        # Button
        button = toga.Button(
            "Set min size to 200x200", on_press=self.set_min_size, style=Pack(padding=5)
        )

        # Layout
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
        main_box.add(self.inner_box)
        self.inner_box.add(button)

        # Main window (100x100, non-resizable)
        self.main_window = toga.MainWindow(
            title=self.formal_name, size=(150, 150), resizable=False
        )
        self.main_window.content = main_box
        self.main_window.show()

    def set_min_size(self, widget):
        # Force minimum size by expanding the box
        self.inner_box.style.update(width=200, height=200)


def main():
    return ExampleApp("Fixed Size with Box", "org.example.fixedsizebox")


if __name__ == "__main__":
    main().main_loop()
