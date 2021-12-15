import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from utils import Regexes
import window
import login


class EventsHandler:
    def __new__(cls, debug=False):
        if not hasattr(cls, "instance"):
            cls.instance = super(EventsHandler, cls).__new__(cls)
        return cls.instance
    

    def __init__(self, debug=False):
        self.__debug = debug

    
    def __invalid_entry(self):
        print("Invalid input")


    def on_login_button_clicked(self, button):
        if self.__debug:
            print("Login button clicked")
        
        name, surname, date = window.WindowHandler().get_login_info()

        if self.__debug:
            print("\n-- Personal Info --")
            print(f"Nome: {name}")
            print(f"Sobrenome: {surname}")
            print(f"Nascimento: {date}")
            print()

        # Validação dos dados de entrada
        valid_input = (Regexes.date.match(date) and name != "" and surname != "")
        if not valid_input:
            self.__invalid_entry()
            return

        login.register_user(name, surname, date)


    def on_login_window_remove(self, *args):
        if self.__debug:
            print("App Closed")
        