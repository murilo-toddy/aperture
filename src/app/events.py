class EventsHandler:
    def __new__(cls, debug=False):
        if not hasattr(cls, "instance"):
            cls.instance = super(EventsHandler, cls).__new__(cls)
        return cls.instance
    
    
    def on_login_button_clicked(self, button):
        print("Login button clicked")