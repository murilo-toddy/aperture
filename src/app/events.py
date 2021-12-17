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
        window.WindowHandler().show_error_window()

    
    def on_exit_button_clicked(self, button):
        Gtk.main_quit()


    def on_error_button_clicked(self, button):
        window.WindowHandler().hide_error_window()


    def __get_user_data(self, update=False):
        if self.__debug:
            print("Login button clicked")
        
        if update:
            name, surname, date = window.WindowHandler().get_update_info()
        else:
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
            raise ValueError()

        return name, surname, date


    def on_login_button_clicked(self, button):
        try: 
            name, surname, date = self.__get_user_data()
            login.register_user(name, surname, date)
        except: 
            return
            


    def on_login_window_remove(self, *args):
        if self.__debug:
            print("Login Window closed")


    def on_todo_button_clicked(self, button):
        print("Todo button clicked")

    
    def on_acomp_button_clicked(self, button):
        print("Acomp button clicked")

    
    """Calendar Events"""
    def on_calendar_button_clicked(self, button):
        print("Calendar button clicked")


    """Update Info Events"""
    def on_updateinfo_button_clicked(self, button):
        if self.__debug:
            print("Update info button clicked")
        
        window.WindowHandler().hide_home_window()
        window.WindowHandler().show_updateinfo_window()
        
    
    def on_update_button_clicked(self, button):
        try:
            name, surname, date = self.__get_user_data(update=True)
            login.update_user(name, surname, date)
            window.WindowHandler().load_default_config()
        except:
            return

    
    def on_updateinfo_window_remove(self, *args):
        window.WindowHandler().show_home_window()




    """Critical Error Events"""
    def on_criticalerror_button_clicked(self, button):
        window.WindowHandler().hide_criticalerror_window()

    def on_criticalerror_window_remove(self, *args):
        Gtk.main_quit()