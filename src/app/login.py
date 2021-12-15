from connection import Connection
import window

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


def register_user(name: str, surname: str, date: str):
    query = "INSERT INTO user_info (name, surname, birthday) VALUES (%s, %s, TO_DATE(%s, 'DD/MM/YYYY'))"

    Connection().exec_and_commit(query, name, surname, date)
    print("Person added")


def prompt_info():
    window.WindowHandler().login_window()
    print("Precisa fazer login!")
    Gtk.main()
        
    

def login():
    query = "SELECT * FROM user_info"
    connection = Connection()
    user = connection.exec(query)

    if user is None:
        prompt_info()