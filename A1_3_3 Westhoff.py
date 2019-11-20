"""
A1_3_3 Westhoff.py
Programmer: Reece Westhoff
"""

#Place Your Code Below
#I will read the repository ReadMe
#I will update document with my own code
import random
guess = 26
def hiLo_game(guess):
    rand_num = random.randint(1,100)
    if rand_num > guess:
        print ('Too low')
    if rand_num < guess:
        print ('Too high')
    if rand_num == guess:
        print ('Winner')

       
"""
Documentation:
1. Provide EOL comments of important items and describe their intended purpose using '#'
2. Take out any additional EOL comments that are no longer necessay. 

Spacing: 
1. Provide appropriate spacing between lines to increase readability. 

Coding:
1. Recommend using an if, elif, else decision tree - you risk errors and longer computation times with the current decision tree. 

"""
