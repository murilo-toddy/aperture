from window import WindowHandler
from connection import Connection

def register_user():
    print("Precisa fazer login!")
    WindowHandler(True).login_window()


def login():
    query = "SELECT * FROM user_info"
    connection = Connection()
    user = connection.exec(query)

    if user is None:
        register_user()



if __name__ == "__main__":
    login()
    # Connection().disconnect()