class Borrowing:
    def __int__(self, id: int, date: str, client_id: int, book_id: int, status):
        self.__id = id
        self.__date = date
        self.__client_id = client_id
        self.__book_id = book_id
        self.__status = status

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_date(self, date):
        self.__date = date

    def get_date(self):
        return self.__date

    def set_client_id(self, client_id):
        self.__client_id = client_id

    def get_client_id(self):
        return self.__client_id

    def set_book_id(self, book_id):
        self.__book_id = book_id

    def get_book_id(self):
        return self.__book_id

    def set_status(self, status):
        self.__status = status

    def get_status(self):
        return self.__status

    def get_borrowing_information(self):
        return ("Id: ", self.__id, ", date: ", self.__date, ", client id: ", self.__client_id,
                ", book id: ", self.__book_id, ", status: ", self.__status)
