from flask import Flask, render_template, request, redirect

app = Flask(__name__)
users = {} #sorry for using a global

@app.route("/", methods=['post', 'get'])
def func():
    if request.method=='POST':
        username = request.form["username"]
        password = request.form["password"]
        if request.form["action"]=='signUp':
            users[username]=password
        else:
            if username not in users: return 'user name not found.'
            if password != users[username]: return 'password not correct.'
        return render_template("main.html",username = request.form["username"]);
    return render_template("log in.html");

app.run("127.0.0.1", 13000, debug=True)
