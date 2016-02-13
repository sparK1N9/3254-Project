from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def someFunc():
    return render_template("main.html");

app.run("127.0.0.1", 13000, debug=True)
