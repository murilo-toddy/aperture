from typing import Any
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

    
    def __invalid_entry(self, update) -> None:
        print("Invalid input")
        if update:
            window.UpdateErrorWindow().show()
        else:    
            window.LoginErrorWindow().show()

    
    def on_exit_button_clicked(self, button) -> None:
        Gtk.main_quit()


    def on_error_login_button_clicked(self, button) -> None:
        window.LoginErrorWindow().hide()
        window.LoginWindow().show()


    def __get_user_data(self, update=False) -> Any:
        if self.__debug:
            print("Login button clicked")

        if update:
            name, surname, date = window.UpdateWindow().get_info()
        else:
            name, surname, date = window.LoginWindow().get_info()

        if self.__debug:
            print("\n-- Personal Info --")
            print(f"Nome: {name}")
            print(f"Sobrenome: {surname}")
            print(f"Nascimento: {date}")
            print()

        # Validação dos dados de entrada
        valid_input = (Regexes.date.match(date) and name != "" and surname != "")
        if not valid_input:
            self.__invalid_entry(update)
            raise ValueError()

        return name, surname, date

    """Collect user data"""
    def on_login_button_clicked(self, button) -> None:
        try: 
            name, surname, date = self.__get_user_data()
            print(name, surname, date)
            login.register_user(name, surname, date)
        except: 
            return
            
    def on_update_button_clicked(self, button) -> None:
        try:
            name, surname, date = self.__get_user_data(update=True)
            login.update_user(name, surname, date)
            window.HomeWindow().show()
        except:
            return


    def on_login_window_remove(self, *args) -> None:
        if self.__debug:
            print("Login Window closed")


    def on_todo_button_clicked(self, button) -> None:
        print("Todo button clicked")

    
    def on_acomp_button_clicked(self, button) -> None:
        print("Acomp button clicked")

    
    """Calendar Events"""
    def on_calendar_button_clicked(self, button) -> None:
        print("Calendar button clicked")


    """Update Info Events"""
    def on_updateinfo_button_clicked(self, button) -> None:
        if self.__debug:
            print("Update info button clicked")
        
        window.HomeWindow().hide()
        window.UpdateWindow().show()

    
    def on_updateinfo_window_remove(self, *args) -> None:
        window.HomeWindow().show()


    """Critical Error Events"""
    def on_criticalerror_button_clicked(self, button) -> None:
        window.CriticalErrorWindow().hide()

    def on_criticalerror_window_remove(self, *args) -> None:
        Gtk.main_quit()