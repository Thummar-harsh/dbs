import sqlite3

# Connecting to SQLite database
connection_obj = sqlite3.connect('geek.db')
cursor_obj = connection_obj.cursor()

# Execute SELECT query
qurry_obj='''
SELECT * FROM Emp 
WHERE name="novaij"
'''
q2="INSERT INTO Emp (name, age, city) VALUES (?, ?, ?)"
q3 = "DELETE FROM Emp WHERE name = ?"

cursor_obj.execute(q2, ("novaij", 42, "junagadh"))
cursor_obj.execute(q3, ("John Doe",))
connection_obj.commit() 





cursor_obj.execute(qurry_obj)
row = cursor_obj.fetchone()
print(row[0])
# Check if the row exists
if row:
    print(row)
else:
    print("data not found in the database.")

# Close the connection
connection_obj.close()
