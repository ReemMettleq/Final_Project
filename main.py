from auth_controller.App_Auth import AppAuth
from model.users_dp.librarian import Librarian
from utils.Utils import MethodsUtils

print("Welcome, please enter your information: ")
user_name = input("Username: ")
password = input("Password: ")

if MethodsUtils.check_value_is_empty(user_name, password):
    exit()

auth = AppAuth()
print(auth.login(user_name, password))
