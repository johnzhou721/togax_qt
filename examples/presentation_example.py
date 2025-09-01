import toga
from toga.style import Pack
import asyncio


class PresentationApp(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = toga.Label(
            "Entering presentation mode...\nWill exit in 3 seconds",
            style=Pack(padding=20),
        )
        self.main_window.show()

        # Enter presentation mode
        self.enter_presentation_mode([self.main_window])

        # Schedule exit after 3 seconds
        asyncio.get_event_loop().call_later(3, self.exit_presentation)

    def exit_presentation(self):
        # Exit presentation mode and close the window
        self.exit_presentation_mode()
        self.main_window.close()


def main():
    return PresentationApp("Presentation Mode Example", "test.beeware.presentation")


if __name__ == "__main__":
    main().main_loop()
