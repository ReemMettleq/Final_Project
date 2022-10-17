class Book:
    def __int__(self, id: int, title: str, description: str, author, status: int):
        self.__id = id
        self.__title = title
        self.__description = description
        self.__author = author
        self.__status = status

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def set_description(self, description):
        self.__description = description

    def get_description(self):
        return self.__description

    def set_author(self, author):
        self.__author = author

    def get_author(self):
        return self.__author

    def set_status(self, status):
        self.__status = status

    def get_status(self):
        return self.__status

    def get_book_information(self):
        return ("Id: ", self.__id, ", title: ", self.__title, ", description: ", self.__description, ", author: ",
                self.__author, ", status: ", self.__status)
