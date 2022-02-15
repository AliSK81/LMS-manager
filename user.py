import csv
import os
from pathlib import Path

__filename = "users.csv"
__header = "USERNAME,PASSWORD,NAME"


class User:
    def __init__(self, username="", password="", name=""):
        self.username = username
        self.password = password
        self.name = name if name != "" else username

    def __str__(self):
        return str(self.name)

    def __iter__(self):
        return iter(self.__dict__.values())


def load_users():
    data = [User()]

    file = Path(__filename)
    if not file.exists() or os.stat(__filename).st_size == 0:
        file.write_text(__header + '\n')

    else:
        with open("users.csv", 'r') as file:
            csvreader = csv.reader(file)
            next(csvreader)
            for row in csvreader:
                data.append(User(*row))

    return data


def save_user(user: User):
    if len(user.username) == 0:
        return

    users = load_users()
    users[0] = User(*__header.split(","))

    for i in range(len(users)):
        if user.username == users[i].username:
            users[i] = user
            break
    else:
        users.append(user)

    with open(__filename, 'w', newline="") as file:
        csvwriter = csv.writer(file)
        csvwriter.writerows(users)
