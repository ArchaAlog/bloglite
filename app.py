from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    array=["archa","jodha","alog"]
    return render_template('index.html',array=array)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)
