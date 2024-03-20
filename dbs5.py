import sqlite3

# Connecting to SQLite database
connection_obj = sqlite3.connect('geek.db')
cursor_obj = connection_obj.cursor()

# Check if the data already exists
query_check_existence = "SELECT COUNT(*) FROM Emp WHERE name = ?"
cursor_obj.execute(query_check_existence, ("novaij",))
result = cursor_obj.fetchone()[0]

if result > 0:
    # Execute UPDATE query if the data exists
    query_update = "UPDATE Emp SET age = ?, city = ? WHERE name = ?"
    cursor_obj.execute(query_update, (43, "junagadh", "novaij"))
    connection_obj.commit()
    print("Data updated successfully.")
else:
    print("Data does not exist in the database.")

# Execute SELECT query
query_select = "SELECT * FROM Emp WHERE name = ?"
cursor_obj.execute(query_select, ("novaij",))
row = cursor_obj.fetchone()

# Print the row
if row:
    print(row)
else:
    print("Data not found in the database.")

# Close the connection
connection_obj.close()
