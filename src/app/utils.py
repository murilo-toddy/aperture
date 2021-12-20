import re
import windows.handler as w
from connection import Connection


class Regexes:
    date = re.compile(r"^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$")


def validate_input(string: str, regex: re.Pattern) -> None:
    if not regex.match(string):
        raise ValueError("Invalid input")


def register_user(name: str, surname: str, date: str) -> None:
    query = "INSERT INTO user_info (name, surname, birthday) VALUES (%s, %s, TO_DATE(%s, 'DD/MM/YYYY'))"
    Connection().exec_and_commit(query, name, surname, date)
    print("Person added")
    w.LoginWindow.hide()
    w.HomeWindow.show()


def update_user(name: str, surname: str, date: str) -> None:
    try:
        query = "UPDATE user_info SET name = %s, surname = %s, birthday = TO_DATE(%s, 'DD/MM/YYYY')"
        Connection().exec_and_commit(query, name, surname, date)
        print("Personal info updated")
        w.UpdateWindow.hide()
        w.WindowHandler().load_default_config()
    except:
        w.CriticalErrorWindow.show()