from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def loginpage():
    return render_template("welcome.html")

@app.route("/admin/<aid>")
def fun_admin(aid):
    return f"Welcome to the Coders_Web\n \
            You are Logged in as Admin with id: {aid}"

@app.route("/guest/<gid>")
def fun_guest(gid):
    return f"Welcome to the Coders_Web\n \
            You are Logged in as Guest with id: {gid}"

@app.route("/student/<sid>")
def fun_student(sid):
    return f"Welcome to the Coders_Web\n \
            You are Logged in as Student with id: {sid}"

@app.route("/coders-web/<login>/<id>")
def fun_coders_web(login,id):
    if login == "admin":
        return redirect(url_for("fun_admin", aid=id))
    elif login == "guest":
        return redirect(url_for("fun_guest", gid=id))
    elif login == "student":
        return redirect(url_for("fun_student", sid=id))
    else: 
        return "Invalid Credentials"

if __name__ == "__main__":
    app.run(debug=True)