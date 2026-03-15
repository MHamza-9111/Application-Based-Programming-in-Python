# Modules
import mysql.connector as msc
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *

# Connection
connection = msc.connect(
    user="root", password="root", host="localhost", database="hamza_db"
)
# Cursor
cursor = connection.cursor()


# Window Center Function
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")


# Window
root = tk.Tk()
root.title("Inventory Login")
center_window(root, 400, 250)
root.config(bg="orange")


# Login Function
def login():
    username = user_entry.get()
    password = pass_entry.get()

    query = "SELECT * FROM users WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))

    result = cursor.fetchone()

    if result:
        root.destroy()
        new()

    else:
        messagebox.showinfo("Wrong Credentials", "Invalid username or password!")


# Add Function
def Add():
    P_Id = f1.get()
    P_Name = f2.get()
    P_Qty = int(f3.get())
    P_Price = int(f4.get())
    total = P_Qty * P_Price

    connection = msc.connect(
        user="root", password="root", host="localhost", database="hamza_db"
    )
    cursor = connection.cursor()

    try:
        query = "INSERT INTO Products (id,name,quantity,price,total) VALUES (%s,%s,%s,%s,%s)"
        val = (P_Id, P_Name, P_Qty, P_Price, total)
        cursor.execute(query, val)
        connection.commit()
        lastid = cursor.lastrowid
        messagebox.showinfo("Info", f"Product {P_Name} has been Added!")
        f1.delete(0, END)
        f2.delete(0, END)
        f3.delete(0, END)
        f4.delete(0, END)
        f1.focus_set()
    except Exception as e:
        messagebox.showerror("Error", str(e))
        connection.rollback()
    finally:
        connection.close()


# Delete Function
def Delete():
    P_Id = f1.get()

    connection = msc.connect(
        user="root", password="root", host="localhost", database="hamza_db"
    )
    cursor = connection.cursor()

    try:
        query = "DELETE FROM Products WHERE id = %s"
        val = (P_Id,)
        cursor.execute(query, val)
        connection.commit()
        lastid = cursor.lastrowid
        messagebox.showinfo("Info", f"Product {P_Id} has been Deleted!")
        f1.delete(0, END)
        f2.delete(0, END)
        f3.delete(0, END)
        f4.delete(0, END)
        f1.focus_set()
    except Exception as e:
        messagebox.showerror("Error", str(e))
        connection.rollback()
    finally:
        connection.close()


# Update Function
def Update():
    P_Id = f1.get()
    P_Name = f2.get()
    P_Qty = int(f3.get())
    P_Price = int(f4.get())
    total = P_Qty * P_Price

    connection = msc.connect(
        user="root", password="root", host="localhost", database="hamza_db"
    )
    cursor = connection.cursor()

    try:
        query = "UPDATE Products SET name = %s, quantity = %s, price = %s, total = %s WHERE id = %s"
        val = (P_Name, P_Qty, P_Price, total, P_Id)
        cursor.execute(query, val)
        connection.commit()
        lastid = cursor.lastrowid
        messagebox.showinfo("Info", f"Product {P_Name} has been Updated!")
        f1.delete(0, END)
        f2.delete(0, END)
        f3.delete(0, END)
        f4.delete(0, END)
        f1.focus_set()
    except Exception as e:
        messagebox.showerror("Error", str(e))
        connection.rollback()
    finally:
        connection.close()


# Read Function
def Read():
    P_Name = f2.get()

    connection = msc.connect(
        user="root", password="root", host="localhost", database="hamza_db"
    )
    cursor = connection.cursor()

    try:
        query = "SELECT id, name, quantity, price FROM Products WHERE name = %s"
        val = (P_Name,)
        cursor.execute(query, val)
        items = cursor.fetchone()

        if items:
            f1.delete(0, END)
            f1.insert(0, items[0])

            f2.delete(0, END)
            f2.insert(0, items[1])

            f3.delete(0, END)
            f3.insert(0, items[2])

            f4.delete(0, END)
            f4.insert(0, items[3])
        else:
            messagebox.showinfo("Not Found", "Product not found")
            connection.rollback()
    finally:
        connection.close()


# Show Function
def Show():
    connection = msc.connect(
        host="localhost", user="root", password="root", database="hamza_db"
    )

    cursor = connection.cursor()

    children = listdisplay.get_children()
    for child in children:
        listdisplay.delete(child)

    cursor.execute("SELECT id, name, quantity, price, total FROM Products")
    records = cursor.fetchall()

    for i, (id, name, quantity, price, total) in enumerate(records, start=1):
        listdisplay.insert("", "end", values=(id, name, quantity, price, total))

    connection.close()


# New Window Function
def new():
    global f1
    global f2
    global f3
    global f4
    global listdisplay

    dash = tk.Tk()
    dash.title("Inventory Management System")
    center_window(dash, 650, 400)
    dash.config(bg="navy")

    # Heading Label
    tk.Label(
        dash,
        text="QE - Inventory MGMT System",
        fg="white",
        bg="navy",
        font=("Bebas Neue", 17, "bold"),
    ).place(x=275, y=25)

    tk.Label(
        dash,
        text="Enter Product details to ADD, UPDATE or DELETE items.",
        fg="white",
        bg="navy",
        font=("Bebas Neue", 10),
    ).place(x=275, y=55)

    tk.Label(
        dash,
        text="Enter Product ID to search and click READ.",
        fg="white",
        bg="navy",
        font=("Bebas Neue", 10),
    ).place(x=275, y=75)

    tk.Label(
        dash,
        text="Click SHOW to display all Products.",
        fg="white",
        bg="navy",
        font=("Bebas Neue", 10),
    ).place(x=275, y=95)

    tk.Label(
        dash,
        text="Product Entry",
        fg="white",
        bg="navy",
        font=("Bebas Neue", 17, "bold", "underline"),
    ).place(x=40, y=10)

    tk.Label(
        dash, text="ID", fg="white", bg="navy", font=("Bebas Neue", 13, "bold")
    ).place(x=10, y=60)

    tk.Label(
        dash, text="Name", fg="white", bg="navy", font=("Bebas Neue", 13, "bold")
    ).place(x=10, y=90)

    tk.Label(
        dash, text="Quantity", fg="white", bg="navy", font=("Bebas Neue", 13, "bold")
    ).place(x=10, y=120)

    tk.Label(
        dash, text="Price", fg="white", bg="navy", font=("Bebas Neue", 13, "bold")
    ).place(x=10, y=150)

    f1 = tk.Entry(dash)
    f1.place(x=100, y=62)

    f2 = tk.Entry(dash)
    f2.place(x=100, y=92)

    f3 = tk.Entry(dash)
    f3.place(x=100, y=122)

    f4 = tk.Entry(dash)
    f4.place(x=100, y=152)

    tk.Button(dash, text="ADD", width=8, command=Add).place(x=265, y=145)
    tk.Button(dash, text="DELETE", width=8, command=Delete).place(x=340, y=145)
    tk.Button(dash, text="UPDATE", width=8, command=Update).place(x=415, y=145)
    tk.Button(dash, text="READ", width=8, command=Read).place(x=490, y=145)
    tk.Button(dash, text="SHOW", width=8, command=Show).place(x=565, y=145)

    tree_frame = tk.Frame(dash, bg="navy")
    tree_frame.place(x=0, y=200, width=650, height=180)

    cols = ("ID", "NAME", "QUANTITY", "PRICE", "TOTAL")
    listdisplay = ttk.Treeview(tree_frame, columns=cols, show="headings")

    listdisplay.column("ID", width=50, anchor="center")
    listdisplay.column("NAME", width=200, anchor="w")
    listdisplay.column("QUANTITY", width=100, anchor="center")
    listdisplay.column("PRICE", width=100, anchor="center")
    listdisplay.column("TOTAL", width=100, anchor="center")

    for col in cols:
        listdisplay.heading(col, text=col)
        listdisplay.pack(fill="both", expand=True)
    tk.Label(
        dash,
        text="Developed by Mohammad Hamza Mughal",
        bg="navy",
        fg="white",
        font=("Arial", 10, "bold"),
    ).pack(side="bottom", fill="x")


# Frame
frame = tk.Frame(root, bg="white")
frame.place(x=80, y=80)

# Heading Label
tk.Label(
    root,
    text="QE - IMS",
    fg="black",
    bg="orange",
    font=("Bebas Neue", 17, "bold"),
).pack(pady=(18, 0))

tk.Label(root, text="Login to Continue", bg="orange", font=("Bebas Neue", 11)).pack()

# Username Label
tk.Label(frame, text="Username", fg="black", font=("Bebas Neue", 10, "bold")).grid(
    row=0, column=0, padx=10, pady=10, sticky="e"
)

# Username Text Field
user_entry = tk.Entry(frame)
user_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# Password Label
tk.Label(frame, text="Password", fg="black", font=("Bebas Neue", 10, "bold")).grid(
    row=1, column=0, padx=10, pady=10, sticky="e"
)

# Password Text Field
pass_entry = tk.Entry(frame, show="*")
pass_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Login Button
tk.Button(frame, text="Login", command=login).grid(
    row=2, column=0, columnspan=2, pady=10
)

root.mainloop()
connection.close()
