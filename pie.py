from flask import Flask, render_template, request, redirect

app = Flask(__name__)
users = {} #sorry for using globals
loggedIn = 0

@app.route("/", methods=['post', 'get'])
def func():
    if request.method=='POST':
        username = request.form["username"]
        password = request.form["password"]
        if request.form["action"]=='signUp':
            if username not in users: users[username]=password
            else: return 'You have already signed up.'
        else:
            if username not in users: return 'user name not found.'
            if password != users[username]: return 'password not correct.'
        loggedIn = 1
        return redirect('/user/<username>')
    return render_template("log in.html");

@app.route('/logout/', methods=['post', 'get'])
def func2():
    loggedIn = 0
    return 'You have logged out.'

@app.route('/user/<username>/', methods=['post', 'get'])
def func3():
    return render_template("main.html",user = username, loggedIn = loggedIn);

app.run("127.0.0.1", 13000, debug=True)
