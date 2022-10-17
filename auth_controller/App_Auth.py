from model.books_dp.book import Book
from model.books_dp.borrowing_order import Borrowing
from model.users_dp.client import Client
from model.users_dp.librarian import Librarian
from utils.Utils import Constants


class AppAuth:

    librarians_list: list[Librarian] = [
        Librarian(1, "Ahmed", 25, "9457", Constants.FULL),
        Librarian(2, "Mahmoud", 34, "4568", Constants.PART)
    ]
    clients_list: list[Client] = [
        Client(1, "Mohammed", 22, "4433", "0598753456"),
        Client(2, "Sami", 19, "1234", "0598766543"),
        Client(3, "Hani", 43, "4653", "0598765432")
    ]
    books_list = list[Book] = [
        Book(1, "Medical Terminology", "description...", "unknown", Constants.ACTIVE),
        Book(2, "Math", "description...", "unknown", Constants.ACTIVE),
        Book(3, "Programming", "description...", "unknown", Constants.INACTIVE)
    ]
    borrowing_list = list[Borrowing] = [
        Borrowing(1, "82/10/2022", 1, 1, Constants.ACTIVE),
        Borrowing(2, "1/12/2022", 2, 2, Constants.EXPIRED),
        Borrowing(3, "20/6/2022", 3, 3, Constants.ACTIVE)
    ]

    def get_last_client_id(self):
        return self.clients_list[len(self.clients_list) - 1].get_id()

    def get_last_book_id(self):
        return self.books_list[len(self.books_list) - 1].get_id()

    def get_last_order_id(self):
        return self.borrowing_list[len(self.borrowing_list) - 1].get_id()

    def register_new_client(self, client: Client):
        if not self.check_if_client_exist(client.get_full_name()):
            self.clients_list.append(client)
        else:
            print("Client already Exist!")

    def check_if_client_exist(self, full_name):
        for item in self.clients_list:
            if item.get_full_name() == full_name:
                return True
        return False

    def get_clients_list(self):
        return self.clients_list

    def search_for_client_by_id(self, id: int):
        if self.clients_list is None or len(self.clients_list) == 0:
            return None
        else:
            for item in self.clients_list:
                if item.get_id() == id:
                    return item

    def search_for_librarian_by_id(self, id: int):
        if self.librarians_list is None or len(self.librarians_list) == 0:
            return None
        else:
            for item in self.librarians_list:
                if item.get_id() == id:
                    return item

    def search_for_order_by_id(self, id: int):
        if self.borrowing_list is None or len(self.borrowing_list) == 0:
            return None
        else:
            for item in self.borrowing_list:
                if item.get_id() == id:
                    return item

    def search_for_book_by_title(self, title: str):
        if self.books_list is None or len(self.books_list) == 0:
            return None
        else:
            for item in self.books_list:
                if item.get_title() == title:
                    return item

    def show_available_books(self):
        for book in self.books_list:
            if book.get_status() == Constants.ACTIVE:
                print(book.get_title())
