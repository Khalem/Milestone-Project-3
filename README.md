# Milestone Project 3

For my third milestone project, I was required to make a "riddle-me-this" website that would consist of HTML, CSS, JavaScript and Python.
My objective for this project was to ensure everything was fully functional while being visually pleasing at the same time.

My project has the user guess 15 riddles. The user has the option to choose photo or text riddles. With a fixed leaderboard sidebar, the users
playing will be able to see when they beat a new score, along with some positive feedback, gives some extra encouragement to continue playing.

## UX

For the design of this website, I wanted to keep it as clean as possible, keeping the focus on the riddles and leaderboards. The websit was made
for people who enjoy guessing riddles, so it is best to make the user feel rewarded when they get a riddle correct. I did this by having messages
pop up when the user gets an answer right, and by also having the leaderboard on display at all times on devices (except mobile). To not disrupt
the flow of the website, I re-created the rebus puzzles so the font and color scheme would match the rest of the website.

#### User Stories:
- **As a user, I can:**  Enter my username for it to be saved. 
- **As a user, I can:**  See leaderboards being updated if a new score is beaten when page is refreshed.
- **As a user, I can:**  Select what type of riddles I would like to answer.
- **As a user, I can:**  Skip the riddle if it is to hard to continue playing.
- **As a user, I can:**  Have the option to play again once I have completed it, to try out a different type of riddle.
- **As a user, I can:**  Click on a button to see how to game is scored/played.
- **As a user, I can:** Answer a riddle and if the answer is incorrect, see it posted on the page.

I have left both a .pdf and .xd files in the cloud9 workspace.

## Features

#### Existing Features
- **Sidebar / Nav:** This is where the leaderboard is displayed. Users on mobile have to click a button to view it, while on larger screens leaderboards will be displayed by default.
- **Form:** This allows users to type and submit their username and answers.
- **Modals:** There are two modals in this page, one for when a user gets an answer correct, another for when the user is looking for a little help.
- **Riddles:** Depending on what the user chose, there will be either a text or photo riddle displayed.
- **Skip Button:** If a question is too difficult, the user will have the option to skip.
- **Play Again Button:** User has the option to play again when he/she has reached the end.

## Technologies Used

[Bootstrap 3.3.7](https://getbootstrap.com/docs/3.3/getting-started/) - Used for structure, modal and dropdown.

[Fontawesome](https://fontawesome.com/) - Used for icons.

[jQuery](https://code.jquery.com/) - Used for modal and JavaScript code.

[Flask](http://flask.pocoo.org/) - Used for routing.

## Testing

For testing I tested the website with automated tests and by manual tests. 

#### Automated Tests:
For my automated tests, I tested 3 different functions inside my main python code.
1. **Dynamic Scoring:** I tested to see if my scoring system worked as intended.
2. **Test Riddle Placements:** I tested to ensure my function with would display what riddle the user was functional.
3. **Text or Picture:** This test was to make sure that the function reliable for selecting the correct riddle and answer worked as intednded.

You can view the tests in the test_riddles.py file. All tests were used with unittest. To test you must first
comment out the app.run in the riddles.py file.

#### Manual Tests
For my manual tests, I tested all features to find any bugs.

- Text Area: On all pages I attempted to submit an empty field - unable to.
- Leaderboards: I had the website open on two browsers. I then answered questions correctly until I would break a highscore. I refreshed the page on the second browser to see if it would update. - It did.
- General Redirects: I clicked on every possible button that would redirect, it all works as inteded.
- Answering incorrect: Answering incorrectly will display your incorrect answer and will not advance you to the next question. Answering correctly with a spelling mistake will still advance you to the next quesiton.

#### Responsiveness
I tested the responsiveness of this website with chrome developer tools and with [Responsinator](https://www.responsinator.com/). I saw no issue with any device. But just to be safe, I tested it 
with my own mobile and I am very pleased with the results. The website works on all browsers also.

## Deployment

I deployed the website onto Heroku. You can view the website [here!](https://khalem-milestone-project-3.herokuapp.com/)

There is also a git repository which you can view [here.](https://github.com/Khalem/Milestone-Project-3)

To run this code locally, I use Visual Studio 2017.

## Credits

#### Content
 - The text riddles were from [here!](https://www.riddles.com/best-riddles)

#### Media
- While I created the images myself, the actual rebus puzzle came from [here!](https://www.news.com.au/technology/online/social/can-you-solve-these-word-riddles-take-the-quiz-to-see-how-many-catchphrasestyle-clues-you-can-get/news-story/962d532d4d7b0a131e74d7f9cc7fb138)


