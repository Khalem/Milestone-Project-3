import os
from tests import *
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    # Homne page which allows users to type their usernames
    if request.method == "POST":
        with open("data/usernames.txt", "a") as user_list:
            user_list.writelines(request.form["username"] + "\n")
        return redirect(request.form["username"])
    return render_template("index.html")
    
@app.route('/<username>', methods=["GET", "POST"])
def choice(username):
    # User choose which type of riddle they want
    if request.method == "POST":
        return redirect("username/" + request.form["choice"])
    return render_template("choice.html", username = username)

@app.route('/<username>/<choice>')
def riddles(username, choice):
    # User answers riddles
    
    # if choice == "Text":
        
    # else:
    return render_template("quiz.html")
        



app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)


    





