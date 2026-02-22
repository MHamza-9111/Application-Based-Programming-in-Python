# 🚀 Coders-Web Flask Application

A simple Flask web application demonstrating:

- Routing  
- Dynamic URL parameters  
- Redirects  
- Template rendering  
- Basic role-based login simulation (Admin, Guest, Student)

---

## 📂 Project Structure

```
HAMZA-ENV-WEBAPP/
│
├── app.py
├── templates/
│   └── welcome.html
└── env/   (virtual environment)
```

---

## 🐍 Technologies Used

- Python  
- Flask  
- HTML  
- Basic CSS (Internal Styling)

---

## ⚙️ Features

### 1️⃣ Homepage

**Route:** `/`

- Renders `welcome.html` using `render_template()`

---

### 2️⃣ Admin Route

**Route:** `/admin/<aid>`

Displays:

```
Welcome to the Coders_Web
You are Logged in as Admin with id: <aid>
```

---

### 3️⃣ Guest Route

**Route:** `/guest/<gid>`

Displays:

```
Welcome to the Coders_Web
You are Logged in as Guest with id: <gid>
```

---

### 4️⃣ Student Route

**Route:** `/student/<sid>`

Displays:

```
Welcome to the Coders_Web
You are Logged in as Student with id: <sid>
```

---

### 5️⃣ Dynamic Login Redirect System

**Route:** `/coders-web/<login>/<id>`

| Login Type | Redirects To |
|------------|-------------|
| admin      | `/admin/<id>` |
| guest      | `/guest/<id>` |
| student    | `/student/<id>` |
| other      | Invalid Credentials |

---

## 🌐 HTML Template (welcome.html)

- Center aligned text  
- Styled `<h1>` with border  
- Basic responsive meta viewport  

---

## ▶️ How To Run

### Step 1: Install Flask

```
pip install flask
```

### Step 2: Run the Application

```
python app.py
```

### Step 3: Open in Browser

```
http://127.0.0.1:5000/
```

---

## 🧠 Example URLs To Test

```
http://127.0.0.1:5000/coders-web/admin/101
http://127.0.0.1:5000/coders-web/guest/202
http://127.0.0.1:5000/coders-web/student/303
http://127.0.0.1:5000/coders-web/unknown/404
```

---

## 🎯 Learning Concepts Covered

- Flask Routing  
- URL Parameters  
- Redirecting with `url_for()`  
- Template Rendering  
- Basic Web Structure  
- Conditional Logic in Routes  

---

## 👨‍💻 Author

**Mohammad Hamza**
