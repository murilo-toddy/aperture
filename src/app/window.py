import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import events
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

        

    # def get_text(self, field): return self.obj(field).get_text()

    def update_obj(self): self.obj = self.builder.get_object


    def show_window(self, window_name: str):
        self.obj = self.builder.get_object
        # if self.__debug:
            # print(f"Opening {window_name}")
        self.obj(window_name).show()

    def hide_window(self, window_name: str):
        # if self.__debug:
        print(f"Hiding {window_name}")
        self.obj(window_name).close()


    def load_default_config(self):
        query = "SELECT * FROM user_info"
        user = Connection().exec(query, func=lambda cur: cur.fetchall())
        personal_info = list(user[0])
        self.name = personal_info[0]
        self.surname = personal_info[1]
        self.birthday = personal_info[2]

        self.builder.get_object("home_personal_info").set_text(
            f"Seja bem vindo(a),\n{self.name} {self.surname}"
        )



class Window:
    def __new__(cls, debug: bool = False, window_name: str = None):
        if not hasattr(cls, "instance"): cls.instance = super(Window, cls).__new__(cls)
        return cls.instance

    def __init__(self, debug: bool = False, window_name: str = None):
        self.__debug = debug
        self.__window_name = window_name

    def show(self):
        self.window = WindowHandler().show_window(window_name = self.__window_name)

    def hide(self):
        WindowHandler().hide_window(window_name = self.__window_name)



class LoginWindow(Window):
    def __new__(cls, debug: bool = False, window_name: str = None):
        if not hasattr(cls, "instance"): cls.instance = super(Window, cls).__new__(cls)
        return cls.instance
        
    def __init__(self, debug=False, window_name: str = "login_window"):
        Window.__init__(self, debug, window_name)
        self.__window_name = window_name

    def get_info(self):        
        name = WindowHandler().obj("login_name").get_text()
        surname = WindowHandler().obj("login_surname").get_text()
        date = WindowHandler().obj("login_birthday").get_text()
        self.hide()
        return name, surname, date



class UpdateWindow(Window):
    def __new__(cls, debug: bool = False, window_name: str = "updateinfo_window"):
        if not hasattr(cls, "instance"):
            cls.instance = super(UpdateWindow, cls).__new__(cls)
        return cls.instance
    
    def __init__(self, debug=False, window_name: str = "updateinfo_window"):
        Window.__init__(self, debug, window_name)
        self.__window_name = window_name

    def get_info(self):
        name = WindowHandler().obj("update_name").get_text() 
        surname = WindowHandler().obj("update_surname").get_text() 
        date = WindowHandler().obj("update_birthday").get_text()
        self.hide()
        return name, surname, date



class HomeWindow(Window):
    def __new__(cls, debug: bool = False, window_name: str = "home_window"):
        if not hasattr(cls, "instance"): cls.instance = super(HomeWindow, cls).__new__(cls)
        return cls.instance
    
    def __init__(self, debug=False, window_name: str = "home_window"):
        Window.__init__(self, debug, window_name)
        self.__window_name = window_name

    def show(self):
        WindowHandler().load_default_config()
        WindowHandler().show_window(window_name = self.__window_name)



class LoginErrorWindow(Window):
    def __new__(cls, debug: bool = False, window_name: str = "error_login_dialog"):
        if not hasattr(cls, "instance"): cls.instance = super(LoginErrorWindow, cls).__new__(cls)
        return cls.instance
    
    def __init__(self, debug=False, window_name: str = "error_login_dialog"):
        Window.__init__(self, debug, window_name)
        self.__window_name = window_name


class UpdateErrorWindow(Window):
    def __new__(cls, debug: bool = False, window_name: str = "error_update_dialog"):
        if not hasattr(cls, "instance"): cls.instance = super(UpdateErrorWindow, cls).__new__(cls)
        return cls.instance
    
    def __init__(self, debug=False, window_name: str = "error_update_dialog"):
        Window.__init__(self, debug, window_name)
        self.__window_name = window_name



class CriticalErrorWindow(Window):
    def __new__(cls, debug: bool = False, window_name: str = "criticalerror_window"):
        if not hasattr(cls, "instance"): cls.instance = super(CriticalErrorWindow, cls).__new__(cls)
        return cls.instance
    
    def __init__(self, debug=False, window_name: str = "criticalerror_window"):
        Window.__init__(self, debug, window_name)
        self.__window_name = window_name
