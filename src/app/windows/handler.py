import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import utils
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

        self.__grade_relation = {
            "Português": "portuguese_grade",
            "Matemática": "math_grade",
            "História": "history_grade",
            "Geografia": "geography_grade",
            "Biologia": "biology_grade",
            "Física": "physics_grade",
            "Química": "chemistry_grade"
        }


    def get_text(self, field): return self.obj(field).get_text()
    def update_obj(self): self.obj = self.builder.get_object

    def show_window(self, window_name: str):
        if self.__debug: print(f"Opening {window_name}")
        self.update_obj()
        self.obj(window_name).show()

    def hide_window(self, window_name: str):
        if self.__debug: print(f"Hiding {window_name}")
        self.obj(window_name).close()
        

    # Home Window Handlers
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


    # Todo List Window Handlers
    def load_todo(self):
        if self.__debug:
            print("Loading tasks")

        self.tasks_tree_view = self.obj("todo_treeview")
        self.task_list_store = Gtk.ListStore(str)

        query = "SELECT * FROM tasks ORDER BY name ASC"
        tasks = Connection().exec(query, func=lambda cur: cur.fetchall())
        
        for task in tasks:
            self.task_list_store.append(list(task))

        renderer = Gtk.CellRendererText()
        col = Gtk.TreeViewColumn(title="Tasks", cell_renderer=renderer, text=0)
        self.tasks_tree_view.append_column(col)
        self.tasks_tree_view.set_model(self.task_list_store)


    def update_selected_task(self, user_data) -> None:
        selected = user_data.get_selected()[1]
        if selected:
            self.selected_task = selected


    def add_task(self) -> None:
        if self.__debug:
            print("Adding task")

        add_task = self.obj("add_task_entry").get_text().strip()
        if add_task != "":
            query = "INSERT INTO tasks (name) VALUES (%s)"
            try:
                self.obj("add_task_entry").set_text("")
                Connection().exec_and_commit(query, add_task)
                self.task_list_store.append([add_task])
            except:
                print("You cannot have duplicate task names") 


    def remove_task(self) -> None:
        query = "DELETE FROM tasks WHERE name = %s"
        try:
            task_name = self.task_list_store.get_value(self.selected_task, 0)
        except:
            print("No task selected")
            return

        try:
            Connection().exec_and_commit(query, task_name)
            self.task_list_store.remove(self.selected_task)
        except:
            print("Database error")


    # Grades Window Handler
    def load_grades(self) -> None:
        if self.__debug: print("Loading grades")
        query = "SELECT * FROM grade"
        grades = Connection().exec(query, func=lambda cur: cur.fetchall())
        for (subject, grade) in grades:
            entry = self.__grade_relation[subject]
            self.obj(entry).set_text(str(round(grade, 2)))

    def __update_grade(self, subject, grade) -> None:
        query = "UPDATE grade SET grade = %s WHERE subject = %s"
        Connection().exec_and_commit(query, grade, subject)


    def __saving_grades_error(self) -> None:
        SubjectsWindow.hide()
        GradesErrorWindow.show()

    def __saving_grades_success(self) -> None:
        SubjectsWindow.hide()
        GradesUpdatedWindow.show()

    def save_grades(self) -> None:
        if self.__debug: print("Saving grades")
        try:
            port_grade = float(self.obj("portuguese_grade").get_text())
            math_grade = float(self.obj("math_grade").get_text())
            hist_grade = float(self.obj("history_grade").get_text())
            geo_grade  = float(self.obj("geography_grade").get_text())
            bio_grade  = float(self.obj("biology_grade").get_text())
            phys_grade = float(self.obj("physics_grade").get_text())
            chem_grade = float(self.obj("chemistry_grade").get_text())
        except ValueError:
            if self.__debug: print("Invalid input")
            self.__saving_grades_error()
            return

        # Checks if grade is within desired range
        if port_grade > 10 or math_grade > 10 or hist_grade > 10 or geo_grade > 10 or \
            bio_grade > 10 or phys_grade > 10 or chem_grade > 10:
            if self.__debug: print("Invalid input")
            self.__saving_grades_error()
            return

        try:
            self.__update_grade("Português",  port_grade)
            self.__update_grade("Matemática", math_grade)
            self.__update_grade("História",   hist_grade)
            self.__update_grade("Geografia",  geo_grade )
            self.__update_grade("Biologia",   bio_grade )
            self.__update_grade("Física",     phys_grade)
            self.__update_grade("Química",    chem_grade)
        except:
            if self.__debug: print("Database error")
            self.__saving_grades_error()

        self.__saving_grades_success()


    # Affinity Window Handler
    def calc_affinity(self):
        if self.__debug: print("Calculating affinity")
        result = utils.calculate_affinity()
        for key, value in result.items():
            self.obj(key + "_pb").set_fraction(value / 10)
            self.obj(key + "_entry").set_text(str(round(value, 2)))


# Show and hide window in glade
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


class LoginErrorWindow():
    @staticmethod
    def show(): Window.show("error_login_dialog")

    @staticmethod
    def hide(): Window.hide("error_login_dialog")



class UpdateWindow():
    @staticmethod
    def get_info():
        name = WindowHandler().get_text("update_name")
        surname = WindowHandler().get_text("update_surname")
        date = WindowHandler().get_text("update_birthday")
        UpdateWindow.hide()
        return name, surname, date

    @staticmethod
    def show(): Window.show("updateinfo_window")

    @staticmethod
    def hide(): Window.hide("updateinfo_window")


class UpdateErrorWindow():
    @staticmethod
    def show(): Window.show("error_update_dialog")

    @staticmethod
    def hide(): Window.hide("error_update_dialog")



class HomeWindow():
    @staticmethod
    def show():
        Window.show("home_window")
        WindowHandler().load_default_config()

    @staticmethod
    def hide(): Window.hide("home_window")



class TodoWindow():
    @staticmethod
    def load(): WindowHandler().load_todo()

    @staticmethod
    def show(): 
        Window.show("todolist_window")
        TodoWindow.load()

    @staticmethod
    def hide(): Window.hide("todolist_window")



class MonitoringWindow:
    @staticmethod
    def show(): Window.show("monitoring_window")

    @staticmethod
    def hide(): Window.hide("monitoring_window")



class SubjectsWindow:
    @staticmethod
    def load(): WindowHandler().load_grades()

    @staticmethod
    def show():
        Window.show("subjects_window")
        SubjectsWindow.load()

    @staticmethod
    def hide(): Window.hide("subjects_window")


class GradesErrorWindow:
    @staticmethod
    def show(): Window.show("grades_invalidinput_error")

    @staticmethod
    def hide(): Window.hide("grades_invalidinput_error")


class GradesUpdatedWindow:
    @staticmethod
    def show(): Window.show("grades_updated_window")

    @staticmethod
    def hide(): Window.hide("grades_updated_window")




class AffinityWindow:
    @staticmethod
    def load(): WindowHandler().calc_affinity()

    @staticmethod
    def show(): 
        Window.show("affinity_window")
        AffinityWindow.load()

    @staticmethod
    def hide(): Window.hide("affinity_window")



class CriticalErrorWindow():
    @staticmethod
    def show(): Window.show("criticalerror_window")

    @staticmethod
    def hide(): Window.hide("criticalerror_window")