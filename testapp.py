import os

os.environ['TOGA_BACKEND'] = 'togax_qt'

import toga


def button_handler(widget):
    print("hello")


def build(app):
    box = toga.Box()

    label = toga.Label("Hello!")
    button = toga.Button("Hello world", on_press=button_handler)
    box.add(label)
    box.add(button)

    return box


def main():
    return toga.App("First App", "org.beeware.toga.examples.tutorial", startup=build)


if __name__ == "__main__":
    main().main_loop()
