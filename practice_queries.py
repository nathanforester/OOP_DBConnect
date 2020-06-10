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

query_result = cursor.execute('SELECT * FROM Orders')
print(len(query_result.fetchall()))
query_result_b = cursor.execute("SELECT o.ShipCity FROM Orders o WHERE o.ShipCity = 'Rio de Janeiro'")
print(len(query_result_b.fetchall()))
query_result_c = cursor.execute("SELECT * FROM Orders WHERE ShipCity = 'Rio de Janeiro' OR ShipCity ='Reims'")
print(query_result_c.fetchall())
query_result_d = cursor.execute("SELECT * FROM Customers WHERE CompanyName LIKE '%z%' OR CompanyName LIKE '%Z%'")
print(query_result_d.fetchall())
query_result_e = cursor.execute()
print(query_result_e.fetchall())

# create a function to call
# while True:
#     row = query_result_b.fetchone()
#     if row is None:
#         break
#     print(row ) # this changes according to your query parameters
#
# while True:
#     row = query_result_b.fetchone()
#     if row is None:
#         break
#     print(row)

while True:
    row = query_result_b.fetchone()
    if row is None:
        break
    print('Number of orders to Rio: ')


# need to change this string to call the correct table

