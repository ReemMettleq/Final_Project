class MainInformation:
    def __int__(self, id, full_name, age, id_no, user_name, employment_type, password):
        self.__id = id
        self.__full_name = full_name
        self.__age = age
        self.__id_no = id_no
        self.__user_name = user_name
        self.__password = password
        self.__employment_type = employment_type

    def get_id(self):
        return self.__id

    def get_user_name(self):
        return self.__user_name

    def get_password(self):
        return self.__password
