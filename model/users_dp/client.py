from auth_controller.App_Auth import AppAuth
from model.books_dp.borrowing_order import Borrowing
from model.users_dp.main_information import MainInformation


class Client(MainInformation):
    def __int__(self, id, full_name, age, id_no, phone_number=""):
        super(Client, self).__int__(id=id, full_name=full_name, age=age, id_no=id_no)
        self.__phone_number = phone_number

    def add_order(self, order: Borrowing):
        AppAuth.borrowing_list.append(order)
        print("Add Order Successfully")

    def delete_order(self, order: Borrowing):
        for item in AppAuth.borrowing_list:
            if order.get_client_id() == self.get_id() and order.get_id() == item.get_id():
                AppAuth.borrowing_list.remove(order)
            else:
                print("This order is not exist!")

    def show_orders(self):
        for order in AppAuth.borrowing_list:
            if order.get_id() == self.get_id():
                order.orderInfo()
            else:
                print("There are no orders exist!")

    def info(self):
        return super(Client, self), ", Phone Number: " + self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_phone_number(self):
        return self.__phone_number
