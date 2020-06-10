from new_oop_connection_oop import MSDBConnection


class DBProductTable(MSDBConnection):

    # def __init__(self):
    #     super().__init__()

    def get_by_id(self, id):
        self.sql_query('SELECT * FROM Product WHERE ProductID =' + str(id)).fetchone()

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


        # create update def

        # carefully do the destroy by id
 # results = DBProductTable().sql_query('SELECT * FROM Products')

product_table = DBProductTable()

# print(product_table.get_by_id(1))
# print(product_table.get_all())
print(product_table.get_all('Chef'))

