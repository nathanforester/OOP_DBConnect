from new_oop_connection_oop import MSDBConnection


class DBClientTable(MSDBConnection):

    # def __init__(self):
    #     super().__init__()

    # def create_client(self, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode,
    #                   Country, Phone, Fax):
    #     return self.sql_query(f"""INSERT INTO Customers (CompanyName, ContactName, ContactTitle, Address,
    #                             City, Region, PostalCode, Country, Phone, Fax)
    #                             VALUES ('{CompanyName}', '{ContactName}', '{ContactTitle}', '{Address}'
    #                             '{City}', '{Region}', {PostalCode}, '{Country}', '{Phone}', '{Fax}')""").commit

    def create_entry(self, CustomerID, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode,
                     Country, Phone, Fax):
        return self.sql_query(
            f"""INSERT INTO Customers (CustomerID, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone, Fax)
    VALUES (f{CustomerID}, '{CompanyName}', {ContactName}, {ContactTitle},'{Address}', {City}, {Region}, {PostalCode}, {Country}, {Phone}, {Fax})""")

    def get_by_id(self, id):
        self.sql_query('SELECT * FROM Product WHERE CustomerID =' + str(id)).fetchone()

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
print(new_client.create_entry('test', 'test', 'test', 'test', 'test', 'test', '7', 'test', '1', 'test', 'test'))
