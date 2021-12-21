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
    query = "UPDATE user_info SET name = %s, surname = %s, birthday = TO_DATE(%s, 'DD/MM/YYYY')"
    Connection().exec_and_commit(query, name, surname, date)
    print("Personal info updated")
    w.UpdateWindow.hide()
    w.HomeWindow.show()


def calculate_affinity() -> dict:
    query = "SELECT * FROM grade"
    grades = Connection().exec(query, func=lambda cur: cur.fetchall())

    # Gets grades from query
    port_grade = grades[0][1]
    math_grade = grades[1][1]
    hist_grade = grades[2][1]
    geo_grade  = grades[3][1]
    bio_grade  = grades[4][1]
    phys_grade = grades[5][1]
    chem_grade = grades[6][1]
    
    hum_grade = (hist_grade + geo_grade) / 2
    sci_grade = (bio_grade + phys_grade + chem_grade) / 3

    # Calculates affinity using ENEM defined percentages
    return {
        "law": (2*port_grade   + 1*math_grade   + 3*hum_grade + 1*sci_grade)   / 7,
        "eng": (2*port_grade   + 3*math_grade   + 1*hum_grade + 3*sci_grade)   / 9,
        "adm": (3*port_grade   + 2.5*math_grade + 2*hum_grade + 0.5*sci_grade) / 8,
        "psy": (1.5*port_grade + 1*math_grade   + 3*hum_grade + 2*sci_grade)   / 7.5,
        "cc" : (2*port_grade   + 3*math_grade   + 1*hum_grade + 3*sci_grade)   / 9,
        "med": (2*port_grade   + 2.5*math_grade + 1*hum_grade + 3.5*sci_grade) / 9
    }



