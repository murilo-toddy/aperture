import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from utils import Regexes
import windows.handler as w
import utils

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
            w.UpdateErrorWindow.show()
        else:    
            w.LoginErrorWindow.show()

    
    def on_exit_button_clicked(self, button) -> None:
        Gtk.main_quit()


    def on_error_login_button_clicked(self, button) -> None:
        w.LoginErrorWindow.hide()
        w.LoginWindow.show()


    def __get_user_data(self, update=False):
        if self.__debug:
            print("Login button clicked")

        if update:
            name, surname, date = w.UpdateWindow.get_info()
        else:
            name, surname, date = w.LoginWindow.get_info()

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
            utils.register_user(name, surname, date)
        except: 
            return
            
    def on_update_button_clicked(self, button) -> None:
        try:
            name, surname, date = self.__get_user_data(update=True)
            utils.update_user(name, surname, date)
        except:
            return


    def on_login_window_remove(self, *args) -> None:
        if self.__debug:
            print("Login Window closed")


    def on_todo_button_clicked(self, button) -> None:
        if self.__debug:
            print("Todo button clicked")

        w.HomeWindow.hide()
        w.TodoWindow.show()

    
    def on_acomp_button_clicked(self, button) -> None:
        print("Acomp button clicked")

    
    """Calendar Events"""
    def on_calendar_button_clicked(self, button) -> None:
        print("Calendar button clicked")


    """Update Info Events"""
    def on_updateinfo_button_clicked(self, button) -> None:
        if self.__debug:
            print("Update info button clicked")
        
        w.HomeWindow.hide()
        w.UpdateWindow.show()

    
    def on_updateinfo_window_remove(self, *args) -> None:
        w.UpdateWindow.hide()
        w.HomeWindow.show()


    """Critical Error Events"""
    def on_criticalerror_button_clicked(self, button) -> None:
        w.CriticalErrorWindow.hide()

    def on_criticalerror_window_remove(self, *args) -> None:
        Gtk.main_quit()


    """Todo List Events"""
    def on_todolist_window_remove(self, *args):
        w.HomeWindow.show()

    def on_addtask_button_clicked(self, button) -> None:
        w.WindowHandler().add_task()
        print("Add button clicked")

    def on_deletetask_button_clicked(self, button) -> None:
        print("Delete task button clicked")

    def on_todohome_button_clicked(self, button) -> None:
        if self.__debug:
            print("Home button clicked")
        w.TodoWindow.hide()

