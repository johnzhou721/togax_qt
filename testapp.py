import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER

def build(app):
    main_window = toga.Window(title="Single Window App")
    main_window.show()
    return main_window

def main():
    return toga.App('Single Window App', 'org.example.singlewindow', startup=build)

if __name__ == '__main__':
    app = main()
    app.main_loop()

