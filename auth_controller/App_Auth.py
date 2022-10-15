from model.users_dp.librarian import Librarian
from utils.Utils import Constants


class AppAuth:

    librarians_list: list[Librarian] = [Librarian()]

    def login(self, username: str, password: str) -> bool:
        for item in self.librarians_list:
            if username == item.get_user_name() and password == item.get_password():
                return True
        return False

    def register_new_user(self, user: Librarian):
        if not self.check_user_exist(user.get_user_name()):
            self.librarians_list.append(user)
        else:
            print("User already exist!")

    def check_user_exist(self, username: str):
        for item in self.librarians_list:
            if item.get_user_name() == username:
                return True
        return False
