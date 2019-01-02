import os
import json
import random
from flask import Flask, redirect, render_template, request
from difflib import SequenceMatcher

app = Flask(__name__)
app.secret_key = os.getenv("SECRET", "randomstring123")

text_riddles = ["What is black and white and red all over?", 
                "What do you call 2 witches that live together?", 
                "The more you take, the more you leave behind. What am I?", 
                "What has a head, a tail, is brown, and has no legs?",
                "Can you name three consecutive days without using the words Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?",
                "David's father has three sons : Snap, Crackle and _____ ?",
                "What room do ghosts avoid?",
                "When does Christmas come before Thanksgiving?",
                "What has many keys, but can't even open a single door?",
                "Mr. and Mrs. Mustard have six daughters and each daughter has one brother. How many people are in the Mustard family?",
                "What belongs to you, but other people use it more than you?",
                "Tall I am young, Short I am old, While with life I glow, Wind is my foe. What am I?",
                "Re-arrange the letters, 'O O U S W T D N E J R' to spell just one word.",
                "I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?",
                "Before Mount Everest was discovered, what was the highest mountain on Earth?"]
answers = ["A Newspaper", "Broommates", "Footsteps", "A Coin", "Yesterday, Today, and Tomorrow", "David", "The Living Room", "In The Dictionary", "A Piano", "9", "Your Name", "A Candle", "Just One Word", "Fire", "Mount Everest"]

# To get the pictures on the template, I will stored the img src value as a variable then call it in the template
picture_riddles = ["../../static/images/rebus-1.jpg", "../../static/images/rebus-2.jpg","../../static/images/rebus-3.jpg","../../static/images/rebus-4.jpg","../../static/images/rebus-5.jpg","../../static/images/rebus-6.jpg","../../static/images/rebus-7.jpg","../../static/images/rebus-8.jpg","../../static/images/rebus-9.jpg","../../static/images/rebus-10.jpg","../../static/images/rebus-11.jpg","../../static/images/rebus-12.jpg","../../static/images/rebus-13.jpg","../../static/images/rebus-14.jpg","../../static/images/rebus-15.jpg"]
picture_answers = ["Fork in the road", "An inside job", "Two steps forward, one step back", "Undercover cop", "Half baked", "Play on words", "Cornerstone", "One foot in the grave", "Double decker bus", "Forever and a day", "Man overboard", "Mother in law", "Breakfast", "Equally Important", " Seven seas"]
incorrect_answers = []
dict_score = {}
points = 0
skip = False

def update_scores():
    """
    This function will update scores as the user plays the game
    """
    
    with open('data/scores.json') as f:
        data = json.load(f)

    data.update(dict_score)

    with open('data/scores.json', 'w') as f:
        json.dump(data, f)
        
def get_high_scores():
    """
    Get highscores then sort them from highest to lowest
    """
    
    with open('data/scores.json') as f:
        data = json.load(f)
        
    new_tuple = tuple(data.items())
    sorted_tuple = sorted(new_tuple, key=lambda x: x[1], reverse=True)
    return sorted_tuple

def dynamic_scoring(incorrect):
    """
    This function will give unique scores depending on how many tries it took the user to get the correct answer. This will give the leaderboards some extra depth - need to add more scoring options.
    """
    if len(incorrect) == 0:
        return 100
    elif len(incorrect) == 1:
        return 90
    elif len(incorrect) == 2:
        return 60
    elif len(incorrect) >= 3 and len(incorrect) < 6:
        return 30
    elif len(incorrect) >= 6 and len(incorrect) < 10:
        return 15
    else:
        return 5


def riddle_placement(riddle_number):
    """
    This function will put the correct heading on the riddle that the user is on
    """
    riddle_number = riddle_number + 1
    if riddle_number == 1:
        return str(riddle_number) + "st"
    elif riddle_number == 2:
        return str(riddle_number) + "nd"
    elif riddle_number == 3:
        return str(riddle_number) + "rd"
    else: 
        return str(riddle_number) + "th"

def text_or_picture(question_answer, choice, riddle_number):
    """
    This function is to select the appropriate riddles/answers based on the users choice and riddle number
    """
    if question_answer == "question":
        if choice == "Text":
            return text_riddles[riddle_number]
        elif choice == "Photo":
            return picture_riddles[riddle_number]
    elif question_answer == "answer":
        if choice == "Text":
            return answers[riddle_number]
        elif choice == "Photo":
            return picture_answers[riddle_number]

def update_number(number):
    """
    This function will just increase the number, while converting it to unicode
    """
    return unicode(number + 1)

@app.route('/', methods=["GET", "POST"])
def index():
    highscores = get_high_scores()
    # Home page which allows users to type their usernames
    if request.method == "POST":
        # Appending username to dictionary
        """
            To avoid having duplicate usernames, I will add a seperator and a random number up to 1 million. This will be split in the template to only display the name.
        """
        username = request.form["username"] + "^" + str(random.randint(1, 1000000))
        dict_score[username] = 0
        return redirect(username)
    return render_template("index.html", highscores = highscores)
    
@app.route('/<username>', methods=["GET", "POST"])
def choice(username):
    highscores = get_high_scores()
    # User choose which type of riddle they want
    if request.method == "POST":
        return redirect(username + "/" + request.form["choice"] + "/0")
    return render_template("choice.html", username = username, highscores = highscores)

@app.route('/<username>/<choice>/<number>', methods=["GET", "POST"])
def riddles(username, choice, number):
    global skip
    global points
    user_number = int(number)
    # User answers riddles
    highscores = get_high_scores()
    """
    When user reaches the end of the quiz, user will have the option to start again
    """
    if user_number == 15:
        if request.method == "POST":
            if request.form["play-again"] == "yes":
                # I need to reset the points if the user chooses to play again, otherwise the next username they enter will start at the points they finished at
                global points
                points = 0
                return redirect("/")
                
        return render_template("finished.html", highscores = highscores, points = points)
    
    riddle_number = riddle_placement(user_number)
    riddle = text_or_picture("question",choice, user_number)
    
    if request.method == "POST":
        
        # If a user skips a riddle, they will be awarded 0 points and redirected to the next riddle
        if request.form["guess"] == "":
            skip = True
            return redirect(username + "/" + choice + "/" + update_number(user_number))
        
        # To allow for spelling mistakes, I will use a Sequence Matcher and if the likeness ratio is 70% or over, the user will be awarded
        m = SequenceMatcher(None, request.form["guess"].title(), text_or_picture("answer", choice, user_number))
        if m.ratio() >= 0.70:
            skip = False
            points = points + dynamic_scoring(incorrect_answers)
            dict_score[username] = points
            update_scores()
            # Clearing list for next question
            incorrect_answers[:] = []
            return redirect(username + "/" + choice + "/" + update_number(user_number))
            
        # Otherwise, will append incorrect answer to list to be printed on users screen
        else: 
            incorrect_answers.append(request.form["guess"])
                
    return render_template("quiz.html", riddle = riddle, incorrect_answers = incorrect_answers, highscores = highscores, riddle_number = riddle_number, skip = skip, user_number = user_number)

app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT' '5000')), debug=False)


    





