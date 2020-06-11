from new_oop_connection_oop import MSDBConnection

nwind = MSDBConnection()


class DBProductTable(MSDBConnection):


    def create_entry(self, productName, supplierID, categoryID, quantityPerUnit,
                               unitsInStock, unitsOnOrder, reorderLevel, discontinued):
        return self.sql_query(f"""INSERT INTO Products (ProductName, SupplierID, CategoryID, QuantityPerUnit,
                               UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued)
                               VALUES ('{productName}', {supplierID}, {categoryID}, '{quantityPerUnit}', 
                                {unitsInStock}, {unitsOnOrder}, {reorderLevel}, {discontinued})""").commit

    def get_by_id(self, id):
        return self.sql_query(f"SELECT * FROM Products WHERE ProductID = " + str(id)).fetchone()

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

    def update_db(self, column_1, val_1, column_2, condition):
        return self.sql_query(f"UPDATE Products SET {column_1} = '{val_1}' WHERE {column_2} = '{condition}'").commit


# results = DBProductTable(productName=None, supplierID=None, categoryID=None, quantityPerUnit=None,
#                          unitsInStock=None, unitsOnOrder=None,
#                          reorderLevel=None, discontinued=None).sql_query('SELECT * FROM Products').cursor()


# product_table = DBProductTable(productName=None, supplierID=None, categoryID=None, quantityPerUnit=None,
#                                unitsInStock=None, unitsOnOrder=None, reorderLevel=None, discontinued=None).cursor()

product_table = DBProductTable()

# print(product_table.get_by_id(1))
# print(product_table.get_all('Chai'))
# for data in product_table.get_all():
#     print(data)
# print(product_table.get_all('Chef'))
# print(product_table.create_entry('Chai', 1, 2, 'half doz', 4.0, 6, 7, 5))
# print(product_table.update_db('ProductName', 'Chai', 'QuantityPerUnit', '10 boxes x 20 bags'))


     # return self.sql_query(f"UPDATE Products SET ProductName = 'Chai Chai', SupplierID = 2 WHERE ProductID = 1").commit
# create update def
# carefully do the destroy by id
