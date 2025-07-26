"""
As someone who does not use KDE, this is just a huge mess.

Also how am I supposed to put all the icons??? Will they display
on macOS??? Anyone more familiar with KDE?
"""

import sys

from toga import Command as StandardCommand, Group, Key

# Is the order even correct??? Why doesn't GTK pre-provide
# menu bars???
# Will this monkeypatch even work? (hack hack hack)
Group.SETTINGS = Group("Settings", order=80)


class Command:
    """Command `native` property is a list of native widgets associated with the command.

    Native widgets is of type QAction (???)
    """

    def __init__(self, interface):
        self.interface = interface
        self.native = []

    # Referenced https://www.youtube.com/watch?v=KAZY79W5yOI for
    # the native locations.  Ran out of disk space to set up a
    # KDE machine, because I'm too afraid to delete my nonworking
    # ubuntu backup...
    @classmethod
    def standard(self, app, id):
        # ---- File menu ("abused" for app stuff) ----------
        if id == StandardCommand.PREFERENCES:
            # TODO: What is supposed to be the native location of this?
            return {
                "text": "Configure" + app.formal_name,
                "group": Group.SETTINGS,
                "section": sys.maxsize - 1,
            }
        elif id == StandardCommand.EXIT:
            # File > Quit??
            return {
                "text": "Quit",
                "shortcut": Key.MOD_1 + "q",
                "group": Group.FILE,
                "section": sys.maxsize,
            }

        # ---- File menu -----------------------------------
        elif id == StandardCommand.NEW:
            return {
                "text": "New",
                "shortcut": Key.MOD_1 + "n",
                "group": Group.FILE,
                "section": 0,
                "order": 0,
            }
        elif id == StandardCommand.OPEN:
            return {
                "text": "Open...",
                "shortcut": Key.MOD_1 + "o",
                "group": Group.FILE,
                "section": 0,
                "order": 10,
            }

        elif id == StandardCommand.SAVE:
            return {
                "text": "Save",
                "shortcut": Key.MOD_1 + "s",
                "group": Group.FILE,
                "section": 0,
                "order": 20,
            }
        elif id == StandardCommand.SAVE_AS:
            return {
                "text": "Save As...",
                "shortcut": Key.MOD_1 + "S",
                "group": Group.FILE,
                "section": 0,
                "order": 21,
            }
        elif id == StandardCommand.SAVE_ALL:
            return {
                "text": "Save All",
                "shortcut": Key.MOD_1 + Key.MOD_2 + "s",
                "group": Group.FILE,
                "section": 0,
                "order": 21,
            }
        # ---- Help menu -----------------------------------
        elif id == StandardCommand.VISIT_HOMEPAGE:
            return {
                "text": "Visit homepage",
                "enabled": app.home_page is not None,
                "group": Group.HELP,
            }
        elif id == StandardCommand.ABOUT:
            return {
                "text": f"About {app.formal_name}",
                "group": Group.HELP,
                "section": sys.maxsize,
            }

        raise ValueError(f"Unknown standard command {id!r}")

    def set_enabled(self, value):
        enabled = self.interface.enabled
        for widget in self.native:
            widget.setEnabled(enabled)
