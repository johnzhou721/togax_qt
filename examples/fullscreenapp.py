import toga
from toga.style import Pack
from toga.style.pack import ROW


class FullscreenApp(toga.App):
    def startup(self):
        # Create the main window
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.full_screen = True  # Start in fullscreen mode

        # Create buttons
        self.presentation_button = toga.Button(
            "Presentation Mode",
            on_press=self.toggle_presentation_mode,
            style=Pack(padding=10),
        )

        self.exit_button = toga.Button(
            "Exit", on_press=self.exit_app, style=Pack(padding=10)
        )

        # Layout
        box = toga.Box(
            children=[self.presentation_button, self.exit_button],
            style=Pack(direction=ROW, alignment="center", padding=20, flex=1),
        )

        # Set content and show window
        self.main_window.content = box
        self.main_window.show()

    def toggle_presentation_mode(self, widget):
        """
        Toggle presentation mode: hide window decorations.
        """
        if not self.in_presentation_mode:
            self.app.enter_presentation_mode([self.main_window])
        else:
            self.app.exit_presentation_mode()

    def exit_app(self, widget):
        """
        Exit the application.
        """
        self.main_window.close()


def main():
    return FullscreenApp("Fullscreen App", "org.example.fullscreenapp")


if __name__ == "__main__":
    main().main_loop()
