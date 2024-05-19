import pymysql

# Establish a connection to the MySQL server
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
)

# Prepare a cursor object
cursorObject = connection.cursor()

# Create a database if it does not exist
cursorObject.execute("CREATE DATABASE IF NOT EXISTS dcrmproject")
print("Database checked/created successfully!")

# Switch to the new database
cursorObject.execute("USE dcrmproject")

# Here you can add more operations, for example, creating tables

# Close the cursor and connection
cursorObject.close()
connection.close()
