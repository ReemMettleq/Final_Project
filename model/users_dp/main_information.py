class MainInformation:
    def __int__(self, id: int, full_name: str, age: int, id_no: str):
        self.__id = id
        self.__full_name = full_name
        self.__age = age
        self.__id_no = id_no

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_full_name(self, full_name):
        self.__full_name = full_name

    def get_full_name(self):
        return self.__full_name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_id_no(self, id_no):
        self.__id_no = id_no

    def get_id_no(self):
        return self.__id_no

    def get_information(self):
        return ("Id: ", self.__id, ", full name: ", self.__full_name, ", age: ", self.__age,
                ", id number: ", self.__id_no)
