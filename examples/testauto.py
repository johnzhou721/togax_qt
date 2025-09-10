import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER
from toga.constants import WindowState


class StateChangeApp(toga.App):
    def startup(self):
        box = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER, padding=20))
        btn = toga.Button(
            "Maximize → Restore", on_press=self.toggle_state, style=Pack(padding=10)
        )
        box.add(btn)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = box
        self.main_window.show()

    async def toggle_state(self, widget):
        # Maximize, then immediately restore
        self.main_window.state = WindowState.MAXIMIZED
        self.main_window.state = WindowState.NORMAL


def main():
    return StateChangeApp("StateChanger", "org.example.statechanger")


if __name__ == "__main__":
    main().main_loop()
