import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import events
from connection import Connection

class WindowHandler:
    def __new__(cls, debug=False):
        if not hasattr(cls, "instance"):
            cls.instance = super(WindowHandler, cls).__new__(cls)
        return cls.instance
    
    
    def __init__(self, debug=False, file="src/interface/main.glade"):
        self.__debug = debug

        self.builder = Gtk.Builder()
        self.builder.add_from_file(file)

        self.builder.connect_signals(events.EventsHandler())
        
        if self.__debug:
            print("Established connection with Glade")
        

    def load_default_config(self):
        query = "SELECT * FROM user_info"
        connection = Connection()
        user = connection.exec(query, func=lambda cur: cur.fetchall())
        personal_info = list(user[0])
        self.name = personal_info[0]
        self.surname = personal_info[1]
        self.birthday = personal_info[2]

        self.obj("home_personal_info").set_text(
            f"Seja bem vindo(a),\n{self.name} {self.surname}"
        )
        

    def show_login_window(self):
        self.obj = self.builder.get_object
        self.obj("login_window").show_all()
        if self.__debug:
            print("Oppening login window")


    def hide_login_window(self):
        print("Closing")
        self.builder.get_object("login_window").close()
        self.obj("login_window").close()


    def get_login_info(self):
        return self.obj("login_name").get_text(), self.obj("login_surname").get_text(), self.obj("login_birthday").get_text()


    def show_home_window(self):
        self.obj = self.builder.get_object
        self.obj("home_window").show_all()
        self.load_default_config()
        