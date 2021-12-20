from configparser import ConfigParser
from typing import Any
import psycopg2

class Connection:
    def __new__(cls, debug=False):
        if not hasattr(cls, "instance"):
            cls.instance = super(Connection, cls).__new__(cls)
        return cls.instance


    def __init__(self, debug=False):
        self.__debug = debug
        self.__connect()


    def __read_config(self, parsefile="database.ini", database="postgresql") -> dict:
        parser = ConfigParser()
        parser.read(parsefile)

        if not parser.has_section(database):
            raise Exception("Could not establish connection to database")

        return dict(parser.items(database))


    def __connect(self) -> None:
        if self.__debug:
            print("Connecting to database")

        self.connection = psycopg2.connect(**(self.__read_config()))
        self.cursor = self.connection.cursor()
        
        if self.__debug:
            print("Connection established")
            self.cursor.execute("SELECT version()")
            print(self.cursor.fetchone())


    def exec(self, command: str, *args, func: callable = None) -> Any:
        self.cursor.execute(command, args)
        return func(self.cursor) if func else None


    def commit(self) -> None:
        self.connection.commit()


    def exec_and_commit(self, command: str, *args, func: callable = None) -> Any:
        return_value = self.exec(command, *args, func=func)
        self.commit()
        return return_value


    def disconnect(self) -> None:
        if self.connection:
            self.connection.close()
            if self.__debug:
                print("Connection to database closed")
