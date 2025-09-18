import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER


class ToggleIconApp(toga.App):
    def startup(self):
        # Main window
        self.main_window = toga.MainWindow(title="Toggle Button Icon")

        # Button with no icon initially
        self.button = toga.Button(
            "Click me!", on_press=self.toggle_icon, style=Pack(padding=20)
        )

        # Keep track of icon state
        self.icon_set = False

        # Container to center the button
        box = toga.Box(
            children=[self.button], style=Pack(direction=COLUMN, alignment=CENTER)
        )
        self.main_window.content = box
        self.main_window.show()

    def toggle_icon(self, widget):
        if not self.icon_set:
            self.button.icon = "star.jpg"  # set icon
            self.icon_set = True
        else:
            self.button.icon = None  # remove icon
            self.icon_set = False


def main():
    return ToggleIconApp("Toggle Icon App", "org.example.toggleicon")


if __name__ == "__main__":
    app = main()
    app.main_loop()
