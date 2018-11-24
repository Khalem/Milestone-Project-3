import os
from tests import *
from flask import Flask, redirect, render_template, request

app = Flask(__name__)
text_riddles = ["What is red and white and red all over?", "HELLO"]
answers = ["A Newspaper", "HI"]

def riddle_placement(iteration=0):
    #Create function to get the correct placement for which riddle the user is on
    if iteration == 1:
        return "st"
    elif iteration == 2 or iteration == 3:
        return "rd"
    else: 
        return "th"

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
    if choice == "Text":
        return render_template("quiz.html", txtriddles = text_riddles)

        



app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)


    





