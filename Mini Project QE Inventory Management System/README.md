# QE - Inventory Management System (IMS)

A simple **Inventory Management System** built with **Python Tkinter** for GUI and **MySQL** for database management. This project allows users to **add, read, update, delete, and display products** in a database.

---

## Features

* **User Login System**

  * Simple authentication using `username` and `password`.
  * Prevents unauthorized access.

* **Product Management**

  * **Add Products**: Input product ID, name, quantity, and price.
  * **Read Products**: Search products by name.
  * **Update Products**: Modify existing product details.
  * **Delete Products**: Remove products by ID.
  * **Show Products**: Display all products in a table.

* **GUI Features**

  * Centered windows for login and dashboard.
  * Interactive `Treeview` table for displaying product records.
  * Easy-to-use buttons for operations.

* **Database Interaction**

  * Connects to MySQL database `hamza_db`.
  * Uses `Products` table with fields:

    * `id`
    * `name`
    * `quantity`
    * `price`
    * `total` (automatically calculated)

---

## Requirements

* Python 3.x
* Tkinter (`tkinter` comes with Python by default)
* MySQL Server
* Python package: `mysql-connector-python`

Install MySQL connector if not installed:

```bash
pip install mysql-connector-python
```

---

## Database Setup

1. Create a database named `hamza_db`:

```sql
CREATE DATABASE hamza_db;
```

2. Create `users` table:

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL
);
```

3. Create `Products` table:

```sql
CREATE TABLE Products (
    id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100),
    quantity INT,
    price INT,
    total INT
);
```

4. Add a sample user to login:

```sql
INSERT INTO users (username, password) VALUES ('admin', 'admin123');
```

---

## How to Run

1. Ensure **MySQL server** is running.
2. Update MySQL connection details in the code if needed:

```python
connection = msc.connect(
    user="root",
    password="root",
    host="localhost",
    database="hamza_db"
)
```

3. Run the Python script:

```bash
python inventory_system.py
```

4. Login with your credentials and start managing products!
---

## Developer

**Mohammad Hamza Mughal**

* Built with ❤️ using Python and Tkinter
* Email: `mughalhamza2015@gmail.com`
* Linkedin: `mhamza9111`
