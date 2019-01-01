import unittest
import riddles

class test_run(unittest.TestCase):
    """
    Test suit for Milestone 3
    """
    
    def test_dynamic_scoring(self):
        """
        Test to see if scoring works correctly
        """
        
        self.assertEqual(riddles.dynamic_scoring([]), 100) #If user gets 0 wrong - recieve 100 points
        self.assertEqual(riddles.dynamic_scoring([1]), 90) #If user gets 1 wrong - recieve 90 points
        self.assertEqual(riddles.dynamic_scoring([2,2]), 60) #If user gets 2 wrong - recieve 60 points
        self.assertEqual(riddles.dynamic_scoring([3,3,3]), 30) #If user gets 3 wrong - recieve 30 points
        self.assertEqual(riddles.dynamic_scoring([4,4,4,4]), 30) #If user gets 4 wrong - recieve 30 points
        self.assertEqual(riddles.dynamic_scoring([5,5,5,5,5]), 30) #If user gets 5 wrong - recieve 30 points
        self.assertEqual(riddles.dynamic_scoring([6,6,6,6,6,6]), 15) #If user gets 6 wrong - recieve 15 points
        self.assertEqual(riddles.dynamic_scoring([7,7,7,7,7,7,7]), 15) #If user gets 7 wrong - recieve 15 points
        self.assertEqual(riddles.dynamic_scoring([8,8,8,8,8,8,8,8]), 15) #If user gets 8 wrong - recieve 15 points
        self.assertEqual(riddles.dynamic_scoring([9,9,9,9,9,9,9,9,9]), 15) #If user gets 9 wrong - recieve 15 points
        self.assertEqual(riddles.dynamic_scoring([10,10,10,10,10,10,10,10,10,10]), 5) #If user gets 10 wrong - recieve 5 points
        self.assertEqual(riddles.dynamic_scoring([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]), 5) #If user gets over 10 wrong - recieve 100 points
        
    def test_riddle_placements(self):
        """
        Test to see if placements are correct
        """
        self.assertEqual(riddles.riddle_placement(0), "1st")
        self.assertNotEqual(riddles.riddle_placement(0), "2nd") # Check to see if incorrect passes test.
        self.assertEqual(riddles.riddle_placement(1), "2nd")
        self.assertEqual(riddles.riddle_placement(2), "3rd")
        self.assertEqual(riddles.riddle_placement(3), "4th")
        self.assertEqual(riddles.riddle_placement(4), "5th")
        self.assertEqual(riddles.riddle_placement(5), "6th")
        self.assertEqual(riddles.riddle_placement(6), "7th")
        self.assertEqual(riddles.riddle_placement(7), "8th")
        self.assertEqual(riddles.riddle_placement(8), "9th")
        self.assertEqual(riddles.riddle_placement(9), "10th")
        self.assertEqual(riddles.riddle_placement(10), "11th")
        self.assertEqual(riddles.riddle_placement(11), "12th")
        self.assertEqual(riddles.riddle_placement(12), "13th")
        self.assertEqual(riddles.riddle_placement(13), "14th")
        self.assertEqual(riddles.riddle_placement(14), "15th")
        
    def test_text_or_picture(self):
        """
        Test to see if function returns correct questions or answers depending on the users choice
        """
        
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
        picture_riddles = ["../static/images/rebus-1.jpg", "../../static/images/rebus-2.jpg","../../static/images/rebus-3.jpg","../../static/images/rebus-4.jpg","../../static/images/rebus-5.jpg","../../static/images/rebus-6.jpg","../../static/images/rebus-7.jpg","../../static/images/rebus-8.jpg","../../static/images/rebus-9.jpg","../../static/images/rebus-10.jpg","../../static/images/rebus-11.jpg","../../static/images/rebus-12.jpg","../../static/images/rebus-13.jpg","../../static/images/rebus-14.jpg","../../static/images/rebus-15.jpg"]
        picture_answers = ["Fork in the road", "An inside job", "Two steps forward, one step back", "Undercover cop", "Half baked", "Play on words", "Cornerstone", "One foot in the grave", "Double decker bus", "Forever and a day", "Man overboard", "Mother in law", "Breakfast", "Equally Important", " Seven seas"]
            
        for i in range(len(text_riddles)):
            self.assertEquals(riddles.text_or_picture("question", "Text", i), text_riddles[i])
            self.assertNotEqual(riddles.text_or_picture("question", "Text", 5), text_riddles[6])
            self.assertEquals(riddles.text_or_picture("answer", "Text", i), answers[i])
            self.assertEquals(riddles.text_or_picture("question", "Photo", i), picture_riddles[i])
            self.assertEquals(riddles.text_or_picture("answer", "Photo", i), picture_answers[i])
        