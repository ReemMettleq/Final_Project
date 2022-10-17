from auth_controller.App_Auth import AppAuth
from model.books_dp.book import Book
from model.users_dp.client import Client
from model.users_dp.librarian import Librarian
from utils.Utils import Constants

app_auth = AppAuth()


def action_client(id: int):
    client = app_auth.search_for_client_by_id(id)
    print("What do you want to do: \n 1_Borrow book.\n 2_Show Your orders.\n 3-Return a book.")
    choice = input("Your choice(1/2/3): ")
    if choice == 1:
        print("Choose the book: ")
        app_auth.show_available_books()
        title = input()
        book = app_auth.search_for_book_by_title(title)
        order_id = app_auth.get_last_order_id()+1
        client.add_order(order_id, "Date()", id, book.get_id(), Constants.ACTIVE)
        book.set_status(Constants.INACTIVE)
        print("Borrowed book successfully")
    elif choice == 2:
        client.show_orders()

    elif choice == 3:
        order_id = input("Enter order id: ")
        order = app_auth.search_for_order_by_id(int(order_id))
        client.delete_order(order)

    else:
        return "Invalid Choice!"


def action_librarian(id: int):
    librarian = app_auth.search_for_librarian_by_id(id)
    print("What you want to do: \n1_Show books Info.\n2_Add book.\n3-Show Orders.\n4-Show Clients.")
    choice = input("Your choice(1/2/3): ")
    if choice == 1:
        librarian.showBooksInfo()
    elif choice == 2:
        book_id = app_auth.get_last_book_id() + 1
        title = input("Enter the title: ")
        description = input("Enter the description: ")
        author = input("Enter the author: ")
        book = Book(int(book_id), str(title), str(description), author, int(Constants.ACTIVE))
        librarian.add_book(book)
        print("Added Book Successfully")

    elif choice == 3:
        librarian.show_orders_info()
    elif choice == 4:
        librarian.show_clients_info()

    else:
        print("Invalid Choice!")


choice = int(input("1- Login \n2- Register as client"))


if choice == 1:
    fullName = input("Your Full Name: ")
    id = int(input("Your ID: "))
    for client in app_auth.clients_list:
        if client.get_id() == id and client.get_full_name() == fullName:
            action_client(id)
        else:
            for librarian in app_auth.librarians_list:
                if librarian.get_id() == id and librarian.get_full_name() == fullName:
                    action_librarian(id)
                else:
                    print("Invalid Name or Id!")

elif choice == 2:
    full_name = input("Your Full Name: ")
    age = input("Your age: ")
    id_no = input("Your ID no: ")
    phone_number = input("Your Phone Number: ")
    id = app_auth.get_last_client_id()+1
    client = Client(id, full_name, age, id_no, phone_number)
    app_auth.register_new_client(client)
    action_client(id)
else:
    print("Error!!")
