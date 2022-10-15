class Borrowing:
    def __int__(self, id, date, client_id, book_id, status):
        self.__id = id
        self.__date = date
        self.__client_id = client_id
        self.__book_id = book_id
        self.__status = status

    def get_id(self):
        return self.__id
