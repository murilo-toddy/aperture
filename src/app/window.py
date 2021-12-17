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

        self.__login_window_name = "login_window"
        self.__home_window_name = "home_window"
        self.__error_window_name = "error_dialog"
        self.__home_window_name = "home_window"
        self.__updateinfo_window_name = "updateinfo_window"
        self.__criticalerror_window_name = "criticalerror_window"


    def __update_obj(self): self.obj = self.builder.get_object


    def __show_window(self, window_name: str):
        self.__update_obj()
        if self.__debug:
            print(f"Opening {window_name}")
        
        self.obj(window_name).show_all()


    def __hide_window(self, window_name: str):
        if self.__debug:
            print(f"Hiding {window_name}")
        self.obj(window_name).close()


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
        

    """Login Window"""
    def show_login_window(self):
        self.__show_window(self.__login_window_name)

    def hide_login_window(self):
        self.__hide_window(self.__login_window_name)

    def get_login_info(self):
        return self.obj("login_name").get_text(), self.obj("login_surname").get_text(), self.obj("login_birthday").get_text()

    def get_update_info(self):
        return self.obj("update_name").get_text(), self.obj("update_surname").get_text(), self.obj("update_birthday").get_text()


    """Error Window"""
    def show_error_window(self):
        self.__show_window(self.__error_window_name)

    def hide_error_window(self):
        self.__hide_window(self.__error_window_name)

    
    """Critical Error Window"""
    def show_criticalerror_window(self):
        self.__show_window(self.__criticalerror_window_name)

    def hide_criticalerror_window(self):
        self.__hide_window(self.__criticalerror_window_name)


    """Home Window"""
    def show_home_window(self):
        self.__show_window(self.__home_window_name)
        self.load_default_config()

    def hide_home_window(self):
        self.__hide_window(self.__home_window_name)


    """Update Info Window"""
    def show_updateinfo_window(self):
        self.__show_window(self.__updateinfo_window_name)

    def hide_updateinfo_window(self):
        self.__hide_window(self.__updateinfo_window_name)
        