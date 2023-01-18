from flask_table import Table, Col
from ..database import cursor
from dataclasses import dataclass

cursor, connection = cursor()


@dataclass
class User:
    user_id: int
    firstname: str
    lastname: str
    username: str
    password: str
    date: str


class UserTables(Table):
    user_id = Col('Id')
    firstname = Col('Firstname')
    lastname = Col('Lastname')
    username = Col('Username')
    password = Col("Password")
    date = Col('Last Login Date')


def Table():
    connection.commit()
    cursor.execute("SELECT * FROM userinfo")
    data = cursor.fetchall()
    connection.commit()
    data_list = [User(*user_info) for user_info in data]
    return UserTables(data_list)
