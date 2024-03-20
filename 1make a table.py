import sqlite3


# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('geedk.db')

# cursor object
cursor_obj = connection_obj.cursor()

# Drop the GEEK table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS GEEK")

# Creating table
table = """ CREATE TABLE Emp (
            id INTEGER PRIMARY KEY,
			name,
			age,
			city
		); """

cursor_obj.execute(table)

print("Table is Ready")

 
# display all data from FOOD1 table



# Close the connection
connection_obj.close()



