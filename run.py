import os
from tests import *
from flask import Flask, redirect, render_template, request

app = Flask(__name__)
text_riddles = ["What is red and white and red all over?", "What do you call 2 witches that live together?"]
answers = ["A Newspaper", "Broommates"]
incorrect_answers = []

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

@app.route('/<username>/<choice>', methods=["GET", "POST"])
def riddles(username, choice):
    # User answers riddles
    if choice == "Text":
        textriddle = text_riddles[0]
        
        if request.method == "POST":
            if request.form["guess"] == answers[0]:
                return redirect("username/choice/1")
            else: 
                incorrect_answers.append(request.form["guess"])
                
        return render_template("quiz.html", textriddle = textriddle, incorrect_answers = incorrect_answers)

@app.route('/<username>/<choice>/<number>', methods=["GET", "POST"])
def get_riddles(username, choice, number):
    if number == "1":
        textriddle = text_riddles[1]
        return render_template("quiz.html", textriddle = textriddle)

        



app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)


    





