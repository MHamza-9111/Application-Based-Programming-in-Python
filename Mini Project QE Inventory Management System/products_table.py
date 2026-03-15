# Modules
import mysql.connector as msc

# Connection
connection = msc.connect(
    user = "root",
    password = "root",
    host = "localhost",
    database = "hamza_db"
)

# Create Table products
query = """
    CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name CHAR(100),
    quantity INT,
    price INT
)
    """

# Cursor
cursor = connection.cursor()
cursor.execute(query)
connection.close()


print("Table Created Successfully!")