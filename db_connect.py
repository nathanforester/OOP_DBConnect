import pyodbc

server = 'databases2.spartaglobal.academy'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';'
                            'UID='+username+';PWD='+password)

print(connection)

cursor = connection.cursor()
print(cursor)

query_result = cursor.execute('SELECT * FROM products')
# # print(query_result.fetchone())
# # print(query_result.fetchone())
# # print(query_result.fetchall()) # less one entry in th cursor
# # fetchone/fetchall is on the cursor object
# # if you want to get back to the start, you have to run a new cursor again
# all_results_list = query_result.fetchone() #utputs all the rows into a list
# # cursor maintains state,
#
# for data in all_results_list:
#     print(data.ProductName, ', cost:', data.UnitPrice)

# do not use fetchall in real life. DO NOT!

# Search documentation or internet to use a for loop to get our all of the data using the .fetchone() method
# while True:
#     row = cursor.fetchone()
#     if row is None:
#         break
#     print(row)

#'behaves like a row, not at tuple'
# behaves like an iterable list, organised with index



# also behaves like an oop objects, where the parameters are the column names

print(cursor.fetchmany())
