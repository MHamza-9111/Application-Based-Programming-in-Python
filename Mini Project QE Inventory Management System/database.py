# Modules
import mysql.connector as msc

# Connection
connection = msc.connect(
    user = "root",
    password = "root",
    host = "localhost"
)

# Create Database hamza_db
query = "CREATE DATABASE IF NOT EXISTS hamza_db"

# Cursor
cursor = connection.cursor()
cursor.execute(query)
connection.close()