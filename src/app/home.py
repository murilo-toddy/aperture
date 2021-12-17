import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import window

def home_screen():
    window.WindowHandler().show_home_window()
    