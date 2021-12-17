from connection import Connection
import window
import home

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


def register_user(name: str, surname: str, date: str) -> None:
    query = "INSERT INTO user_info (name, surname, birthday) VALUES (%s, %s, TO_DATE(%s, 'DD/MM/YYYY'))"

    Connection().exec_and_commit(query, name, surname, date)
    print("Person added")
    window.WindowHandler().hide_login_window()
    home.home_screen()


def update_user(name: str, surname: str, date: str) -> None:
    try:
        query = "UPDATE user_info SET name = %s, surname = %s, birthday = TO_DATE(%s, 'DD/MM/YYYY')"
        print(name, surname, date)
        Connection().exec_and_commit(query, name, surname, date)
        print("Personal info updated")
        window.WindowHandler().hide_updateinfo_window()
        window.WindowHandler().load_default_config()

    except:
        window.WindowHandler().show_criticalerror_window()
    


def prompt_info() -> None:
    window.WindowHandler().show_login_window()
    print("No user found, prompting login")
        

def login() -> None:
    query = "SELECT * FROM user_info"
    connection = Connection()
    user = connection.exec(query, func=lambda cur: cur.fetchall())
    
    if not user:
        prompt_info()

    else:
        home.home_screen()
    
    Gtk.main()

