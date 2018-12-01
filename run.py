import os
import json
from tests import *
from flask import Flask, redirect, render_template, request

app = Flask(__name__)
text_riddles = ["What is red and white and red all over?", "What do you call 2 witches that live together?"]
answers = ["A Newspaper", "Broommates"]
incorrect_answers = []
dict_score = {}

#This function will update scores as the user plays the game
def update_scores():
    with open('data/scores.json') as f:
        data = json.load(f)

    data.update(dict_score)

    with open('data/scores.json', 'w') as f:
        json.dump(data, f)
        
#Get highscores then sort them from highest to lowest
def get_high_scores():
    with open('data/scores.json') as f:
        data = json.load(f)
        
    new_tuple = tuple(data.items())
    sorted_tuple = sorted(new_tuple, key=lambda x: x[1], reverse=True)
    return sorted_tuple
    
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
    highscores = get_high_scores()
    # Homne page which allows users to type their usernames
    if request.method == "POST":
        with open("data/usernames.txt", "a") as user_list:
            # Appending username to dictionary
            dict_score[request.form["username"]] = 0
            user_list.writelines(request.form["username"] + "\n")
        return redirect(request.form["username"])
    return render_template("index.html", highscores = highscores)
    
@app.route('/<username>', methods=["GET", "POST"])
def choice(username):
    # User choose which type of riddle they want
    if request.method == "POST":
        return redirect(username + "/" + request.form["choice"])
    return render_template("choice.html", username = username)

@app.route('/<username>/<choice>', methods=["GET", "POST"])
def riddles(username, choice):
    # User answers riddles
    if choice == "Text":
        textriddle = text_riddles[0]
        
        if request.method == "POST":
            # If guess is right, will redirect to the 2nd riddle
            if request.form["guess"] == answers[0]:
                # Clearing list for next question
                incorrect_answers[:] = []
                #If answer is right, user will recieve point
                dict_score[username] = 1
                return redirect(username + "/" + choice + "/1")
            # Otherwise, will append incorrect answer to list to be printed on users screen
            else: 
                incorrect_answers.append(request.form["guess"])
                
        return render_template("quiz.html", textriddle = textriddle, incorrect_answers = incorrect_answers)
"""
The following function will redirect according to which part of the riddle the user is on. 

(Will try to loop instead of having if statements further down the line)
"""
@app.route('/<username>/<choice>/<number>', methods=["GET", "POST"])
def get_riddles(username, choice, number):
    if number == "1":
        textriddle = text_riddles[1]
        
        if request.method == "POST":
            if request.form["guess"] == answers[1]:
                incorrect_answers[:] = []
                dict_score[username] = 2
                update_scores()
                return redirect(username + "/" + choice + "/2")
            else:
                incorrect_answers.append(request.form["guess"])
        
        return render_template("quiz.html", textriddle = textriddle, incorrect_answers = incorrect_answers)
    elif number == "2":
        textriddle = text_riddles[2]
        
        if request.method == "POST":
            if request.form["guess"] == answers[2]:
                incorrect_answers[:] = []
                return redirect(username + "/" + choice + "/3")
            else:
                incorrect_answers.append(request.form["guess"])
        
        return render_template("quiz.html", textriddle = textriddle, incorrect_answers = incorrect_answers)
    elif number == "3":
        textriddle = text_riddles[3]
        
        if request.method == "POST":
            if request.form["guess"] == answers[3]:
                incorrect_answers[:] = []
                return redirect(username + "/" + choice + "/4")
            else:
                incorrect_answers.append(request.form["guess"])
        
        return render_template("quiz.html", textriddle = textriddle, incorrect_answers = incorrect_answers)
    elif number == "4":
        textriddle = text_riddles[4]
        
        if request.method == "POST":
            if request.form["guess"] == answers[4]:
                incorrect_answers[:] = []
                return redirect(username + "/" + choice + "/5")
            else:
                incorrect_answers.append(request.form["guess"])
        
        return render_template("quiz.html", textriddle = textriddle, incorrect_answers = incorrect_answers)
    elif number == "5":
        textriddle = text_riddles[5]
        
        if request.method == "POST":
            if request.form["guess"] == answers[5]:
                incorrect_answers[:] = []
                return redirect(username + "/" + choice + "/6")
            else:
                incorrect_answers.append(request.form["guess"])
        
        return render_template("quiz.html", textriddle = textriddle, incorrect_answers = incorrect_answers)
    elif number == "6":
        textriddle = text_riddles[6]
        
        if request.method == "POST":
            if request.form["guess"] == answers[6]:
                incorrect_answers[:] = []
                return redirect(username + "/" + choice + "/7")
            else:
                incorrect_answers.append(request.form["guess"])
        
        return render_template("quiz.html", textriddle = textriddle, incorrect_answers = incorrect_answers)
    elif number == "7":
        textriddle = text_riddles[7]
        
        if request.method == "POST":
            if request.form["guess"] == answers[7]:
                incorrect_answers[:] = []
                return redirect(username + "/" + choice + "/8")
            else:
                incorrect_answers.append(request.form["guess"])
        
        return render_template("quiz.html", textriddle = textriddle, incorrect_answers = incorrect_answers)
    elif number == "8":
        textriddle = text_riddles[8]
        
        if request.method == "POST":
            if request.form["guess"] == answers[8]:
                incorrect_answers[:] = []
                return redirect(username + "/" + choice + "/9")
            else:
                incorrect_answers.append(request.form["guess"])
        
        return render_template("quiz.html", textriddle = textriddle, incorrect_answers = incorrect_answers)
    elif number == "9":
        textriddle = text_riddles[9]
        
        if request.method == "POST":
            if request.form["guess"] == answers[9]:
                incorrect_answers[:] = []
                return redirect(username + "/" + choice + "/10")
            else:
                incorrect_answers.append(request.form["guess"])
        
        return render_template("quiz.html", textriddle = textriddle, incorrect_answers = incorrect_answers)
    elif number == "10":
        textriddle = text_riddles[10]
        
        if request.method == "POST":
            if request.form["guess"] == answers[10]:
                incorrect_answers[:] = []
                return redirect(username + "/" + choice + "/11")
            else:
                incorrect_answers.append(request.form["guess"])
        
        return render_template("quiz.html", textriddle = textriddle, incorrect_answers = incorrect_answers)
    elif number == "11":
        textriddle = text_riddles[11]
        
        if request.method == "POST":
            if request.form["guess"] == answers[11]:
                incorrect_answers[:] = []
                return redirect(username + "/" + choice + "/12")
            else:
                incorrect_answers.append(request.form["guess"])
        
        return render_template("quiz.html", textriddle = textriddle, incorrect_answers = incorrect_answers)
    elif number == "12":
        textriddle = text_riddles[12]
        
        if request.method == "POST":
            if request.form["guess"] == answers[12]:
                incorrect_answers[:] = []
                return redirect(username + "/" + choice + "/13")
            else:
                incorrect_answers.append(request.form["guess"])
        
        return render_template("quiz.html", textriddle = textriddle, incorrect_answers = incorrect_answers)
    elif number == "13":
        textriddle = text_riddles[13]
        
        if request.method == "POST":
            if request.form["guess"] == answers[13]:
                incorrect_answers[:] = []
                return redirect(username + "/" + choice + "/14")
            else:
                incorrect_answers.append(request.form["guess"])
        
        return render_template("quiz.html", textriddle = textriddle, incorrect_answers = incorrect_answers)

        



app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)


    





