import os

os.environ['TOGA_BACKEND'] = 'togax_qt'

import toga
from toga.style import Pack
from toga.style.pack import CENTER

def button_handler(widget):
    print("Button clicked!")

def button_handler2(widget):
    print("Button2 clicked!")

def build(app):
    # Create a button and set its on_press handler
    box = toga.Box()
    
    button = toga.Button('Click Me', on_press=button_handler, style=Pack(margin=100))
    
    box.add(button)
    
    return button

def main():
    return toga.App('Simple Button App', 'org.example.simplebutton', startup=build)

if __name__ == '__main__':
    app = main()
    app.main_loop()

