# Modules
import mysql.connector as msc

# Connection
connection = msc.connect(
    user = "root",
    password = "root",
    host = "localhost",
    database = "hamza_db"
)

# Create Table users
query = """
    CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username CHAR(50),
    password CHAR(50)
)
    """

# Cursor
cursor = connection.cursor()
cursor.execute(query)
connection.close()

print("Table Created Successfully!")


# Insert Into Table users
query = "INSERT INTO users (username,password) VALUES (%s,%s)"
values = ("admin","admin")

# Cursor
cursor = connection.cursor()
cursor.execute(query,values)
connection.commit()
connection.close()

print("Data Inserted Successfully!")