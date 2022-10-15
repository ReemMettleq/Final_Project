class Book:
    def __int__(self, id, title, description, author, status):
        self.__id = id
        self.__title = title
        self.__description = description
        self.__author = author
        self.__status = status

    def get_id(self):
        return self.__id
