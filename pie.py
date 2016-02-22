from flask import Flask, render_template, request, redirect, url_for, session, escape

app = Flask(__name__)
users = {} #sorry for using globals

@app.route("/", methods=['post', 'get'])
def logIn():
    if request.method=='POST':
        username = request.form["username"]
        password = request.form["password"]
        if request.form["action"]=='signUp':
            if username not in users:
                userData = [password,[],[]]
                users[username] = userData
            else: return 'You have already signed up.'
        else:
            if username not in users: return 'user name not found.'
            if password != users[username][0]: return 'password not correct.'
        session['username'] = request.form["username"]
        return redirect(url_for('home',username = request.form["username"]));
    return render_template("log in.html");

@app.route('/logout/')
def logOut():
    session.pop('username', None)
    return 'You have logged out.'

@app.route('/user/<username>', methods=['post', 'get'])
def home(username):
    if 'username' not in session: return 'log in first!'
    if request.method=='POST':
        if "log out" in request.form:
            return redirect(url_for('logOut'))
        elif "del acc" in request.form:
            session.pop('username', None)
            del users[username]
            return 'Account deleted.'
        elif 'p' in request.form:
            msg = request.form["msg"]
            users[username][1].append(msg)
        elif 'search' in request.form:
            target = request.form["target"]
            if target not in users: return 'user not found.'
            if target in users[username][2]: return 'already following this person.'
            users[username][2].append(target)
        elif 'unfollow' in request.form:
            person = request.form["person"]
            if person not in users[username][2]: return 'not following this user.'
            users[username][2].remove(person)
            return 'unfollow sucessful.'
        elif 'posts' in request.form:
            lst = []
            lst += users[username][1]
            for otherUser in users[username][2]:
                lst += users[otherUser][1]
            return render_template("posts.html",seq = lst)
    return render_template("main.html",user = username);

app.secret_key = 'A0Zr98j/3yX R~XHH!jN]LWX/,?RT'
app.run("127.0.0.1", 13000, debug=True)
