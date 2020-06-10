### PYODBC AND OOP

- We are looking into the PYODBC package
- We are going to use the package to make a new OOP module that abstracts our interaction with the NW DB
- Then further abstracts the interaction with specific tables
- Where appropriate, we will use the CRUD design to build methods
- Need to add further abstraction that abstracts interaction with specific tables
## CRUD
- Create:
````    
def create_entry(self, productName, supplierID, categoryID, quantityPerUnit,
                               unitsInStock, unitsOnOrder, reorderLevel, discontinued):
        return self.sql_query(f"""INSERT INTO Products (ProductName, SupplierID, CategoryID, QuantityPerUnit,
                               UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued)
                               VALUES ('{productName}', {supplierID}, {categoryID}, '{quantityPerUnit}', 
                                {unitsInStock}, {unitsOnOrder}, {reorderLevel}, {discontinued})""").commit

product_table = DBProductTable()
print(product_table.create_entry('Chai', 1, 2, 'half doz', 4.0, 6, 7, 5))
````
- Read (READ 1: by ID, READ ALL: based on all results/params)
````
    def get_all(self, client_name=None):
        result_list = []
        if client_name is None:
            query_result = self.sql_query('SELECT * FROM Customers')
        else:
            query_result = self.sql_query(f"SELECT * FROM Customers WHERE ContactName LIKE '%{client_name}%'")
        while True:
            row = query_result.fetchone()
            if row is None:
                break
            result_list.append(row)
        return result_list

new_client = DBClientTable()
print(new_client.get_all())
````
- Update
````
    def update_db(self, column_1, val_1, column_2, condition):
        return self.sql_query(f"UPDATE Products SET {column_1} = '{val_1}' WHERE {column_2} = '{condition}'").commit

product_table = DBProductTable()
print(product_table.update_db('ProductName', 'Chai', 'QuantityPerUnit', '10 boxes x 20 bags'))
````
- Delete: not yet attempted due to data volatility

## Summary:
- OOP pyodb connect is a complex process but one which is manageable with practice
- you must ensure that you declare a cursor and assign the cursor to an sql_query object:
````
    def sql_query(self, sql_string):

        return self.cursor.execute(sql_string)
````
- This cursor is initiated in the OOP_db_connect file.
````
 def __init__(self, database='Northwind'):
        self.server = 'databases2.spartaglobal.academy'
        self.database = database
        self.username = 'SA'
        self.password = 'Passw0rd2018'
        self.con = self._establish_connection()
        self.cursor = self.con.cursor()
````
- Within the same class, a connection should be established:
````
 def _establish_connection(self):
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';'
                                    'DATABASE='+self.database+';''UID='+self.username+';PWD='+self.password)
        return connection
````
- You may test the connectivity of the database with a simple search execution:
````
nwind = MSDBConnection()
print(nwind.sql_query('SELECT * FROM products').fetchall())
````
although in a business or commercial setting, this is not advisable, as it will take considerable time to return results, which consequently results in loss of revenue
A more efficient and cost effective query to test connectivity would be:
````
results = nwind.sql_query('SELECT * FROM products')
while True:
    row = results.fetchone()

    if row is None:
        break
    print(row)
````
This query will fetch one row of result at a time until there are no more rows to return. The while loop will check for True or False conditions for this process to run effectively, pre-declaring the None and break statement indented within the if condition, then simply printing until the condition is false
- Subclasses represent other tables within the database and inherit from the new_OOP_connection.py file
````
from new_oop_connection_oop import MSDBConnection


class DBClientTable(MSDBConnection):
````
 Within these subclasses, the functions for CRUD, which have been explained previously in this documentation
 are implemented and can be tested before user input is entered via the runfile
 
 - Previous version of software available via git hub branches