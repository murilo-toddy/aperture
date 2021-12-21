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


    def update_selected_task(self, user_data):
        selected = user_data.get_selected()[1]
        if selected:
            self.selected_task = selected


    def add_task(self):
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


    def remove_task(self):
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


    # Monitoring Window Handler
    def load_subjects(self):
        print("Loading grades")
        # if self.__debug:
        #     print("Loading subjects")

        # self.tasks_tree_view = self.obj("todo_treeview")
        # self.task_list_store = Gtk.ListStore(str)

        # query = "SELECT * FROM subjects"
        # subjects = Connection().exec(query, func=lambda cur: cur.fetchall())
        
        # for subject in subjects:
        #     self.task_list_store.append(list(task))

        # renderer = Gtk.CellRendererText()
        # col = Gtk.TreeViewColumn(title="Tasks", cell_renderer=renderer, text=0)
        # self.tasks_tree_view.append_column(col)
        # self.tasks_tree_view.set_model(self.task_list_store)
        



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
        name = WindowHandler().get_text("update_name")
        surname = WindowHandler().get_text("update_surname")
        date = WindowHandler().get_text("update_birthday")
        UpdateWindow.hide()
        return name, surname, date

    @staticmethod
    def show(): Window.show("updateinfo_window")

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
    def load(): WindowHandler().load_subjects()

    @staticmethod
    def show():
        Window.show("subjects_window")
        SubjectsWindow.load()

    @staticmethod
    def hide(): Window.hide("subjects_window")


class AffinityWindow:
    @staticmethod
    def show(): Window.show("affinity_window")

    @staticmethod
    def hide(): Window.hide("affinity_window")



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