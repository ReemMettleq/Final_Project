from model.users_dp.main_information import MainInformation


class Clint(MainInformation):
    def __int__(self, id, full_name, age, id_no, phone_number, user_name, password):
        self.__phone_number = phone_number
        super(Clint, self).__int__(id=id, full_name=full_name, age=age, id_no=id_no,
                                   user_name=user_name, password=password)

    def get_phone_number(self):
        return self.__phone_number
