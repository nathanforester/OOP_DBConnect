from new_oop_connection_oop import MSDBConnection


class DBProductTable(MSDBConnection):

    # def __init__(self):
    #     super().__init__()
    def create_entry(self, productName, supplierID, categoryID, quantityPerUnit,
                               unitsInStock, unitsOnOrder, reorderLevel, discontinued):
        return self.sql_query(f"""INSERT INTO Products (ProductName, SupplierID, CategoryID, QuantityPerUnit,
                               UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued)
                               VALUES ('{productName}', {supplierID}, {categoryID}, '{quantityPerUnit}', 
                                {unitsInStock}, {unitsOnOrder}, {reorderLevel}, {discontinued})""").commit


    def get_by_id(self, id):
        return self.sql_query('SELECT * FROM Products WHERE ProductID =' + str(id)).fetchone()

    def get_all(self, product_name=None):
        result_list = []
        if product_name is None:
            query_result = self.sql_query('SELECT * FROM Products')
        else:
            query_result = self.sql_query(f"SELECT * FROM Products WHERE ProductName LIKE '%{product_name}%'")
        while True:
            row = query_result.fetchone()
            if row is None:
                break
            result_list.append(row)
        return result_list

    def update_db(self, column_1, val_1, column_2, val_2, column_3, condition):
        return self.sql_query(f"UPDATE Products SET {column_1} = {val_1} {column_2} = {val_2} WHERE {column_3} = {condition}").commit
        # return self.sql_query(f"UPDATE Products SET ProductName = 'Chai Chai', SupplierID = 2 WHERE ProductID = 1").commit



        # create update def

        # carefully do the destroy by id
 # results = DBProductTable().sql_query('SELECT * FROM Products')

product_table = DBProductTable()

# print(product_table.get_by_id(1))
# print(product_table.get_all())
# print(product_table.get_all('Chef'))
print(product_table.create_entry('Chai', 2, 4, '4 by 4', 4, 3, 2, '0'))
# print(product_table.update_db('ProductName', 'Chai', 'SupplierID', 2, 'ProductID', 1))
