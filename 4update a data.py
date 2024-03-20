import sqlite3

# Connecting to SQLite database
connection_obj = sqlite3.connect('geedk.db')
cursor_obj = connection_obj.cursor()

# Execute UPDATE query for the first row
query_update = "UPDATE Emp SET age = ?, city = ? WHERE id=1"
cursor_obj.execute(query_update, (42, "junagadh"))
connection_obj.commit()
print("Data updated successfully.")

# Close the connection
connection_obj.close()
