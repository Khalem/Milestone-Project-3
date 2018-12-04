import os
import json
from tests import *
from flask import Flask, redirect, render_template, request

app = Flask(__name__)
text_riddles = ["What is red and white and red all over?", "What do you call 2 witches that live together?", "What is my name?"]
answers = ["A Newspaper", "Broommates", "Khalem"]
incorrect_answers = []
dict_score = {}
points = 0

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
"""
This function will give unique scores depending on how many tries it took the user to get the correct answer. This will give the leaderboards some extra depth
"""
def dynamic_scoring(incorrect, points):
    if len(incorrect) == 0:
        points = points + 10
        return points
    elif len(incorrect) == 1:
        points = points + 7
        return points
    elif len(incorrect) > 1 and len(incorrect) < 4:
        points = points + 4
        return points
    else:
        points = points + 1
        return points

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
    highscores = get_high_scores()
    # User choose which type of riddle they want
    if request.method == "POST":
        return redirect(username + "/" + request.form["choice"])
    return render_template("choice.html", username = username, highscores = highscores)

@app.route('/<username>/<choice>', methods=["GET", "POST"])
def riddles(username, choice):
    # User answers riddles
    highscores = get_high_scores()
    if choice == "Text":
        textriddle = text_riddles[0]
        
        if request.method == "POST":
            # If guess is right, will redirect to the 2nd riddle
            if request.form["guess"] == answers[0]:
                
                # If answer is right, user will recieve points
                dict_score[username] = dynamic_scoring(incorrect_answers, points)
                update_scores()
                # Clearing list for next question
                incorrect_answers[:] = []
                
                return redirect(username + "/" + choice + "/1")
            # Otherwise, will append incorrect answer to list to be printed on users screen
            else: 
                incorrect_answers.append(request.form["guess"])
                
        return render_template("quiz.html", textriddle = textriddle, incorrect_answers = incorrect_answers, highscores = highscores)

"""
This function will just increase the number, while converting it to unicode
"""
def update_number(number):
    return unicode(number + 1)

""" 
I increase the variable number up by one each time the user gets a question right, redirecting them back
to this function with a new variable
"""
@app.route('/<username>/<choice>/<number>', methods=["GET", "POST"])
def get_riddles(username, choice, number):
    highscores = get_high_scores()
    user_number = int(number)
    textriddle = text_riddles[user_number]
        
    if request.method == "POST":
        if request.form["guess"] == answers[user_number]:
            dict_score[username] = dynamic_scoring(incorrect_answers, points)
            incorrect_answers[:] = []
            update_scores()
            return redirect(username + "/" + choice + "/" + update_number(user_number))
        else:
            incorrect_answers.append(request.form["guess"])        
        
    return render_template("quiz.html", textriddle = textriddle, incorrect_answers = incorrect_answers, highscores = highscores)


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)


    





