# while True:
#     try:
#         user_input = int(input("Enter any number to continue: "))
#     except ValueError:
#         print("input must be a number from 1-9: ")
#     else:
#         print("Thank you, entry successful!")

import sys
from db_products_oop import DBProductTable
from db_clients_oop import DBClientTable
from new_oop_connection_oop import MSDBConnection

new_entry = DBProductTable()
new_entry_2 = DBClientTable()
while True:
    user_input = input("Press any key to continue or press 'x' to exit: ")
    while user_input != 'x':
        user_input = input("Please enter a table to use (press p for products, c for clients or x to exit): ")
        while user_input != 'x':
            if user_input == 'p':
                user_input = input("Push s to search, a to add entry, u to update entry or x to exit: ")
                while user_input != 'x':
                    if user_input == 'a':

                        user_input = input('press any key to continue or x to quit: ')
                        while user_input != 'x':
                            try:
                                user_input_1 = input("Enter product name or press 'x' to abort: ")
                                while user_input_1 == 'x':
                                    sys.exit(-1)
                                user_input_2 = input("Enter quantity in descriptive terms (words): ")
                                user_input_3 = int(input('enter number: '))
                                user_input_4 = int(input('enter number: '))
                                user_input_5 = int(input('enter number: '))
                                user_input_6 = int(input('enter number: '))
                                user_input_7 = int(input('enter number: '))
                                user_input_8 = int(input('enter number: '))
                            except ValueError:
                                print('Incorrect value selected. Enter only number when prompted. Please start again')
                            else:
                                print(new_entry.create_entry(user_input_1, user_input_4, user_input_3, user_input_2,
                                                             user_input_5, user_input_6, user_input_7, user_input_8))
                    elif user_input == 's':
                        while user_input != 'x':
                            user_input_2 = input("push any key to continue search or x to exit: ")
                            while user_input_2 != 'x':
                                user_input_1 = int(input("Enter product ID to search by: "))
                                print(new_entry.get_by_id(user_input_1))
                                user_input_3 = input('push y to start another search: ')
                                if user_input_3 == 'y':
                                    break
                            while user_input_2 == 'x':
                                user_input = input("push x to exit: ")
                                if user_input == 'x':
                                    break
                    elif user_input == 'u':
                        user_input_1 = input('Enter a column to alter or press x to exit: ')
                        user_input_2 = input('Enter a value to add/alter: ')
                        user_input_3 = input('Enter column to add corresponding value:')
                        user_input_4 = input('Enter corresponding value of altered/added item: ')
                        print(new_entry.update_db(user_input_1, user_input_2, user_input_3, user_input_4))
                        while user_input_1 == 'x':
                            break
            elif user_input == 'c':
                user_input = input("Push s to search, a to add entry, u to update entry or x to exit: ")
                while user_input != 'x':
                    if user_input == 'a':
                        user_input_1 = input("Enter product name or press 'x' to abort")
                        user_input_2 = input()
                        user_input_3 = input()
                        user_input_4 = input()
                        user_input_5 = input()
                        user_input_6 = input()
                        user_input_7 = input()
                        user_input_8 = input()
                        user_input_9 = input()
                        user_input_10 = input()
                        user_input_11 = input()
                        print(new_entry_2.create_client(user_input_1, user_input_2, user_input_3, user_input_4,
                              user_input_5, user_input_6, user_input_7, user_input_8, user_input_9, user_input_10,
                              user_input_11))
                        while user_input_1 == 'x':
                            break
                    elif user_input == 's':
                        while user_input != 'x':
                            user_input_2 = input("push any key to continue search or x to exit: ")
                            while user_input_2 != 'x':
                                user_input_1 = input("Enter Customer ID to search by: ")
                                print(new_entry.get_by_id(user_input_1))
                                user_input_3 = input('push y to start another search: ')
                                if user_input_3 == 'y':
                                    break
                            while user_input_2 == 'x':
                                user_input = input("push x to exit: ")
                                if user_input == 'x':
                                    break
        if user_input == 'x':
            break
    if user_input == 'x':
        break



