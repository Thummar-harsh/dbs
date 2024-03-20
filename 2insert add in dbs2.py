import sqlite3

# Connecting to SQLite database
connection_obj = sqlite3.connect('geedk.db')
cursor_obj = connection_obj.cursor()

# Define data to be inserted
data = [
    ("John Doe", 30, "New York"),
    ("Jane Smith", 25, "Los Angeles"),
    ("Michael Johnson", 35, "Chicago")
]

# Insert data into the table
for entry in data:
    cursor_obj.execute("INSERT INTO Emp (name, age, city) VALUES (?, ?, ?)", entry)

# Commit changes to the database
connection_obj.commit()

# Close the connection
connection_obj.close()

print("Data inserted successfully.")
