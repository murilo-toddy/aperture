import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from events import EventsHandler


class WindowHandler:
    def __new__(cls, debug=False):
        if not hasattr(cls, "instance"):
            cls.instance = super(WindowHandler, cls).__new__(cls)
        return cls.instance
    
    
    def __init__(self, debug=False):
        self.__debug = debug

        self.builder = Gtk.Builder()
        self.builder.add_from_file("src/interface/main.glade")

        self.builder.connect_signals(EventsHandler())
        self.obj = self.builder.get_object

        if self.__debug:
            print("Established connection with Glade")

    
    def login_window(self):
        print("Oppening login window")
        self.obj("login_window").show_all()
        Gtk.main()
        print("Opened")