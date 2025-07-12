import toga
from toga.style import Pack
from toga.style.pack import CENTER

def button_handler(widget):
    print("Button clicked!")

def build(app):
    # Create a button and set its on_press handler
    button = toga.Button('Click Me', on_press=button_handler, style=Pack(padding=20))
    
    
    return button

def main():
    return toga.App('Simple Button App', 'org.example.simplebutton', startup=build)

if __name__ == '__main__':
    app = main()
    app.main_loop()

