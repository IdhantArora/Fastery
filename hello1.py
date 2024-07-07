from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')

def index():
#     return render_template("LoginPage.html")
    a=22
    thing = "Bold"
    array = ["by","bruce","ruce","hi"]
    return render_template("user.html",a=a, thing=thing, array=array)

# def user():
#     a = 21
#     return render_template("user.html",a=a)