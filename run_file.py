from db_products_oop import DBProductTable
from new_oop_connection_oop import MSDBConnection

new_entry = DBProductTable()

while True:
    user_input = input("Press any key to continue or press 'x' to exit: ")
    while user_input != 'x':
        user_input_1 = input("Enter product name or press 'x' to abort")
        user_input_2 = int(input())
        user_input_3 = int(input())
        user_input_4 = input()
        user_input_5 = int(input())
        user_input_6 = int(input())
        user_input_7 = int(input())
        user_input_8 = int(input())
        print(new_entry.create_entry(user_input_1, user_input_2, user_input_3, user_input_4, user_input_5, user_input_6,
                                     user_input_7, user_input_8))
        while user_input_1 == 'x':
            break
    if user_input == 'x':
        break

