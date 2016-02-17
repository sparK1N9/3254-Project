from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/", methods=['post', 'get'])
def someFunc():
    if request.method=='POST':
        return render_template("main.html");
    return render_template("log in.html");

app.run("127.0.0.1", 13000, debug=True)
