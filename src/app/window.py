import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import events
# from events import EventsHandler

class WindowHandler:
    def __new__(cls, debug=False):
        if not hasattr(cls, "instance"):
            cls.instance = super(WindowHandler, cls).__new__(cls)
        return cls.instance
    
    
    def __init__(self, debug=False, file="src/interface/main.glade"):
        self.__debug = debug

        self.builder = Gtk.Builder()
        self.builder.add_from_file(file)

        self.builder.connect_signals(events.EventsHandler(True))
        
        if self.__debug:
            print("Established connection with Glade")
        

    def login_window(self):
        self.obj = self.builder.get_object
        print("Oppening login window")
        self.obj("login_window").show_all()
        print("Opened")


    def get_login_info(self):
        return self.obj("login_name").get_text(), self.obj("login_surname").get_text(), self.obj("login_birthday").get_text()

    
