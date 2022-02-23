import csv
import os
from pathlib import Path


class User:
    __filename = "users.csv"
    __header = "USERNAME,PASSWORD,NAME"

    def __init__(self, username="", password="", name=""):
        self.username = username
        self.password = password
        self.name = name if name != "" else username

    def __str__(self):
        return str(self.name)

    def __iter__(self):
        return iter(self.__dict__.values())

    def save_user(self):
        if len(self.username) == 0:
            return

        users = User.load_users()
        users[0] = User(*User.__header.split(","))

        for i in range(len(users)):
            if self.username == users[i].username:
                users[i] = self
                break
        else:
            users.append(self)

        with open(User.__filename, 'w', newline="") as file:
            csvwriter = csv.writer(file)
            csvwriter.writerows(users)

    @staticmethod
    def load_users():
        data = [User()]

        file = Path(User.__filename)
        if not file.exists() or os.stat(User.__filename).st_size == 0:
            file.write_text(User.__header + '\n')

        else:
            with open("users.csv", 'r') as file:
                csvreader = csv.reader(file)
                next(csvreader)
                for row in csvreader:
                    data.append(User(*row))

        return data
