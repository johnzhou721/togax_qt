import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from faker import Faker

fake = Faker()


def greeting(name):
    return f"Hello, {name}!"


class HelloApp(toga.App):
    def startup(self):
        # Main window
        self.main_window = toga.MainWindow(title=self.formal_name)

        # Input field for the user's name
        self.name_input = toga.TextInput(placeholder="Enter your name")

        # Button to trigger the async say_hello function
        hello_button = toga.Button("Say Hello", on_press=self.say_hello)

        # Layout container
        box = toga.Box(
            children=[self.name_input, hello_button],
            style=Pack(direction=COLUMN, padding=10),
        )

        self.main_window.content = box
        self.main_window.show()

    async def say_hello(self, widget):
        # Async dialog showing greeting and fake data
        await self.main_window.dialog(
            toga.InfoDialog(
                title=greeting(self.name_input.value),
                message=f"A message from {fake.name()}: {fake.text()}",
            )
        )


def main():
    return HelloApp("Hello Toga App", "com.johnzhou.example")


if __name__ == "__main__":
    app = main()
    app.main_loop()
