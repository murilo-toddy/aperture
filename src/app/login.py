from connection import Connection
import window
import home

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


def register_user(name: str, surname: str, date: str):
    query = "INSERT INTO user_info (name, surname, birthday) VALUES (%s, %s, TO_DATE(%s, 'DD/MM/YYYY'))"

    Connection().exec_and_commit(query, name, surname, date)
    print("Person added")
    window.WindowHandler().hide_login_window()
    home.home_screen()


def prompt_info():
    window.WindowHandler().show_login_window()
    print("No user found, prompting login")
    Gtk.main()
        

def login():
    query = "SELECT * FROM user_info"
    connection = Connection()
    user = connection.exec(query, func=lambda cur: cur.fetchall())

    if not user:
        prompt_info()

    home.home_screen()
