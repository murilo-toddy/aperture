import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import windows.events as events
from connection import Connection

class WindowHandler:
    def __new__(cls, debug=False):
        if not hasattr(cls, "instance"): cls.instance = super(WindowHandler, cls).__new__(cls)
        return cls.instance
    
    def __init__(self, debug=False, file="src/interface/main.glade"):
        self.__debug = debug

        self.builder = Gtk.Builder()
        self.builder.add_from_file(file)

        self.builder.connect_signals(events.EventsHandler())
        
        if self.__debug:
            print("Established connection with Glade")


    def get_text(self, field): return self.obj(field).get_text()
    def update_obj(self): self.obj = self.builder.get_object


    def show_window(self, window_name: str):
        if self.__debug:
            print(f"Opening {window_name}")
        self.update_obj()
        self.obj(window_name).show()

    def hide_window(self, window_name: str):
        if self.__debug:
            print(f"Hiding {window_name}")
        self.obj(window_name).close()
        

    def load_default_config(self):
        query = "SELECT * FROM user_info"
        user = Connection().exec(query, func=lambda cur: cur.fetchall())
        personal_info = list(user[0])
        self.name = personal_info[0]
        self.surname = personal_info[1]
        self.birthday = personal_info[2]

        self.obj("home_personal_info").set_text(
            f"Seja bem vindo(a),\n{self.name} {self.surname}"
        )



class Window:
    @staticmethod
    def show(window_name): WindowHandler().show_window(window_name=window_name)

    @staticmethod
    def hide(window_name): WindowHandler().hide_window(window_name=window_name)


class LoginWindow():
    @staticmethod
    def get_info():
        name = WindowHandler().get_text("login_name")
        surname = WindowHandler().get_text("login_surname")
        date = WindowHandler().get_text("login_birthday")
        LoginWindow.hide()
        return name, surname, date

    @staticmethod
    def show(): Window.show("login_window")

    @staticmethod
    def hide(): Window.hide("login_window")


class UpdateWindow():
    @staticmethod
    def get_info():
        name = WindowHandler().obj("update_name").get_text() 
        surname = WindowHandler().obj("update_surname").get_text() 
        date = WindowHandler().obj("update_birthday").get_text()
        UpdateWindow.hide()
        return name, surname, date

    @staticmethod
    def show(): Window.show("updateinfo_widow")

    @staticmethod
    def hide(): Window.hide("updateinfo_window")


class HomeWindow():
    @staticmethod
    def show():
        Window.show("home_window")
        WindowHandler().load_default_config()

    @staticmethod
    def hide(): Window.hide("home_window")


class LoginErrorWindow():
    @staticmethod
    def show(): Window.show("error_login_dialog")

    @staticmethod
    def hide(): Window.hide("error_login_dialog")


class UpdateErrorWindow():
    @staticmethod
    def show(): Window.show("error_update_dialog")

    @staticmethod
    def hide(): Window.hide("error_update_dialog")


class CriticalErrorWindow():
    @staticmethod
    def show(): Window.show("criticalerror_window")

    @staticmethod
    def hide(): Window.hide("criticalerror_window")