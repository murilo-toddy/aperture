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

    def on_error_update_button_clicked(self, button) -> None:
        w.UpdateErrorWindow.hide()
        w.UpdateWindow.show()


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

        # Validates input data
        valid_input = (Regexes.date.match(date) and name != "" and surname != "")
        if not valid_input:
            self.__invalid_entry(update)
            raise ValueError()

        return name, surname, date


    # Collect user data
    def on_login_button_clicked(self, button) -> None:
        try: 
            name, surname, date = self.__get_user_data()
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
        w.HomeWindow.hide()
        w.MonitoringWindow.show()


    # Update Info Events
    def on_updateinfo_button_clicked(self, button) -> None:
        if self.__debug:
            print("Update info button clicked")
        
        w.HomeWindow.hide()
        w.UpdateWindow.show()
    
    def on_updateinfo_window_remove(self, *args) -> None:
        if self.__debug: print("Update Window closed")
         # w.UpdateWindow.hide()
        # w.HomeWindow.show()


    # Critical Error Events
    def on_criticalerror_button_clicked(self, button) -> None:
        w.CriticalErrorWindow.hide()

    def on_criticalerror_window_remove(self, *args) -> None:
        Gtk.main_quit()


    # ToDo List Events
    def on_todolist_window_remove(self, *args):
        w.HomeWindow.show()

    def on_addtask_button_clicked(self, button) -> None:
        w.WindowHandler().add_task()
        if self.__debug:
            print("Add task button clicked")

    def on_deletetask_button_clicked(self, button) -> None:
        w.WindowHandler().remove_task()

    def on_todohome_button_clicked(self, button) -> None:
        if self.__debug:
            print("Home button clicked")
        w.TodoWindow.hide()

    def set_selected_todo_task(self, user_data) -> None:
        w.WindowHandler().update_selected_task(user_data)


    # Monitoring Events
    def on_monitoring_window_remove(self, *args) -> None:
        if self.__debug: print("Monitoring window closed")

    def on_monitorhome_button_clicked(self, button) -> None:
        if self.__debug:
            print("Home button clicked")
        w.MonitoringWindow.hide()
        w.HomeWindow.show()

    def on_subject_button_clicked(self, button) -> None:
        w.MonitoringWindow.hide()
        w.SubjectsWindow.show()

    def on_affinity_button_clicked(self, button) -> None:
        w.MonitoringWindow.hide()
        w.AffinityWindow.show()


    # Subjects Events
    def on_subjectback_button_pressed(self, button) -> None:
        if self.__debug:
            print("Back button pressed")
        w.SubjectsWindow.hide()
        w.MonitoringWindow.show()

    def on_subjects_window_remove(self, *args) -> None:
        if self.__debug: print("Subjects window closed")

    def on_savegrades_button_pressed(self, button) -> None:
        w.WindowHandler().save_grades()

    def on_inputerror_grade_button_clicked(self, button) -> None:
        w.GradesErrorWindow.hide()
        w.SubjectsWindow.show()

    def on_grades_invalidinput_error_close(self, *args) -> None:
        w.SubjectsWindow.show()

    def on_gradesupdated_button_clicked(self, button) -> None:
        w.GradesUpdatedWindow.hide()
        w.SubjectsWindow.show()

    def on_gradesupdated_close(self, *args) -> None:
        w.SubjectsWindow.show()


    # Affinity Events
    def on_affinityback_button_pressed(self, button) -> None:
        w.AffinityWindow.hide()

    def on_affinity_window_remove(self, *args) -> None:
        w.MonitoringWindow.show()

        

