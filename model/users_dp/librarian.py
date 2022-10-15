from model.users_dp.main_information import MainInformation


class Librarian(MainInformation):
    def __int__(self, id, full_name, age, id_no, employment_type, user_name, password):
        super(Librarian, self).__int__(id=id, full_name=full_name, age=age, id_no=id_no,
                                       user_name=user_name, password=password, employment_type=employment_type)
