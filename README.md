# Connecting a database to python

### Libraries and packages
- Libraries internal
- Packages external



# This package abstracts our connection to the db
- pyodbc

## 
- Only use fetch one in a while True loop to get many data sets - using fetchall() will take longer to load and with a heavy data set, will cost £££/$$$
- you call the database in the cursor.execute() method call as a string