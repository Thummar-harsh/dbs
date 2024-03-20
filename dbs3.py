import sqlite3

# Connecting to SQLite database
connection_obj = sqlite3.connect('geek.db')
cursor_obj = connection_obj.cursor()

# Execute SELECT query
cursor_obj.execute("SELECT * FROM Emp")

# Fetch all rows
rows = cursor_obj.fetchall()

# Print the fetched rows
for row in rows:
    print(row)

# Close the connection
connection_obj.close()
