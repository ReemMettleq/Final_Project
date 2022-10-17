from auth_controller.App_Auth import AppAuth
from model.books_dp.book import Book
from model.users_dp.main_information import MainInformation


class Librarian(MainInformation):
    def __int__(self, id, full_name, age, id_no, employment_type=""):
        self.__employment_type = employment_type
        super(Librarian, self).__int__(id=id, full_name=full_name, age=age, id_no=id_no)

    def add_book(self, book: Book):
        AppAuth.books_list.append(book)

    def show_books_info(self):
        if len(AppAuth.books_list) != 0:
            for book in AppAuth.books_list:
                book.bookInfo()
        else:
            return "There is no book in the library!"

    def show_orders_info(self):
        if len(AppAuth.borrowing_list) != 0:
            for order in AppAuth.borrowing_list:
                order.orderInfo()
        else:
            return "There are no orders!"

    def show_clients_info(self):
        if len(AppAuth.clients_list) != 0:
            for client in AppAuth.clients_list:
                client.info()
        else:
            return "There are no clients!"

    def info(self):
        return super(Librarian, self), ", Employment Type: ", self.__employment_type

    def set_employment_type(self, employment_type):
        self.__employment_type = employment_type

    def get_employment_type(self):
        return self.__employment_type
