"""Lockbyte"""

import time
import pickle
import hashlib


class Lockbyte:
    """Lockbyte"""

    def __init__(self):
        self.settings = self.load_settings()
        self.password: dict[str, list[str]] = {}
        self.created = time.ctime(time.time())

    def load_settings(self):
        """load_settings"""

        with open(".settings", "rb") as f:
            try:
                return pickle.load(f)
            except EOFError:
                pass

    def load(self):
        """add"""

        with open(".passwords", "rb") as f:
            try:
                return pickle.load(f)
            except EOFError:
                pass

    def dump(self, passwords):
        """add"""

        with open(".passwords", "wb") as f:
            pickle.dump(passwords, f)

    def add(self, name, details: list[str]):
        """add"""

        password = self.load()

        if name not in password:
            password[name] = details

        self.dump(password)
        self.password = password

    def remove(self, name):
        """remove"""

        password = self.load()

        if name in password:
            del password[name]

        self.dump(password)
        self.password = password

    def get(self, name):
        """get"""

        if name in self.load():
            return self.load()[name]
        return None

    def update(self, name, details: list[str]):
        """update"""

        password = self.load()

        if name in password:
            password[name] = details

        self.dump(password)
        self.password = password

    def get_csv(self):
        """get_csv"""

        password = self.load()

        csv = "Name,Username,Password,URL\n"
        for name, details in password.items():
            csv += f"{name},{details[0]},{details[1]},{details[2]}\n"

        with open("lockbyte.csv", "w", encoding="utf-8") as f:
            f.write(csv)

        return csv

    def from_csv(self, csv):
        """from_csv"""

        password = {}
        lines = csv.split("\n")

        for line in lines[1:]:
            if not line:
                continue
            name, username, password, url = line.split(",")
            password[name] = [username, password, url]

        self.dump(password)
        self.password = password

    def hash_password(self, password):
        """hash_password"""

        return hashlib.sha256(password.encode()).hexdigest()
