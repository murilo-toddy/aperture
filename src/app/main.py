from connection import Connection
import windows.handler as w

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
        

def login(debug=False) -> None:
    query = "SELECT * FROM user_info"
    connection = Connection(debug=debug)
    user = connection.exec(query, func=lambda cur: cur.fetchall())

    if not user:
        if debug:
            print("No user found, prompting login")
        w.LoginWindow.show()
    else:
        w.HomeWindow.show()
    
    Gtk.main()


if __name__ == "__main__":
    login()

