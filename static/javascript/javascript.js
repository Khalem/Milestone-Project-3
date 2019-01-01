// This function is to have random congratulations messages, so it doesn't become stale

function random_congrats_msgs(){
    var messages = ["Good job, but don't stop now, there's still more to go!", "Congratulations, but there are still more riddles to answer!",
                    "Not bad, see if you can get the next one!", "Think you can beat the highscore? Keep going and find out!",
                    "You're unstoppable! Keep on going!", "The sky's the limit for you, onwards!", "These are too easy for you..",
                    "Maybe the next riddle might be harder..", "You're getting good at this!", "You're on a roll don't stop!"
                    ]
    var random = Math.floor(Math.random()*messages.length);
    
    $("#congrats").text(messages[random])
}

// This function will make the color of the riddle placement the same as the image. This will only be called for when a user chooses the images, as it would disrupt the flow of just the text based riddles.
function new_color(){
    
    var x = $("#riddleNum");
    
    if(x.text() == "2nd"){
        x.removeClass("bg-purple");
        x.addClass("bg-green");
    }
    else if(x.text() == "3rd"){
        x.removeClass("bg-purple");
        x.addClass("bg-pink");
    }
    else if(x.text() == "4th"){
        x.removeClass("bg-purple");
        x.addClass("bg-light-pink");
    }

    else if(x.text() == "6th"){
        x.removeClass("bg-purple");
        x.addClass("green-6");
    }
    else if(x.text() == "8th"){
        x.removeClass("bg-purple");
        x.addClass("peach-8");
    }
    else if(x.text() == "9th"){
        x.removeClass("bg-purple");
        x.addClass("blue-9");
    }
    else if(x.text() == "10th"){
        x.removeClass("bg-purple");
        x.addClass("bg-green");
    }
    else if(x.text() == "12th"){
        x.removeClass("bg-purple");
        x.addClass("bg-pink");
    }
    else if(x.text() == "13th"){
        x.removeClass("bg-purple");
        x.addClass("peach-8");
    }
    else if(x.text() == "15th"){
        x.removeClass("bg-purple");
        x.addClass("peach-8");
    }
}

random_congrats_msgs();
