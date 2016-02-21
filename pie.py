from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
users = {} #sorry for using globals

@app.route("/", methods=['post', 'get'])
def logIn():
    if request.method=='POST':
        username = request.form["username"]
        password = request.form["password"]
        if request.form["action"]=='signUp':
            if username not in users: users[username]=password
            else: return 'You have already signed up.'
        else:
            if username not in users: return 'user name not found.'
            if password != users[username]: return 'password not correct.'     
        return redirect(url_for('main',username = request.form["username"]));
    return render_template("log in.html");

@app.route('/logout/', methods=['post', 'get'])
def logOut():
    return 'You have logged out.'

@app.route('/user/<username>', methods=['post', 'get'])
def main(username):
    if request.method=='POST':
        if request.form["log out"]:
            return redirect('/logout/')
        if request.form["delete account"]:
            del users[username]
            return 'Account deleted.'
    return render_template("main.html",user = username);

app.run("127.0.0.1", 13000, debug=True)
