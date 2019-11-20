'''
1.3.3
Connor Mckinney
'''
import random
guess= 47
def hiLo_game(guess):
    rand_num = 788
    if guess == rand_num:
        print ("Congrats you got it right")
    elif guess > rand_num:
        print ("your number is too high")
    else:
        print ("your number is too low")
        
"""
Documentation:
1. Provide EOL comments of important items and describe their intended purpose using '#'
2. Take out any additional EOL comments that are no longer necessay. 

Spacing: 
1. Provide appropriate spacing between lines to increase readability. 

Coding:
1. Need to assign a random number from 1 - 100 to the rand_num variable. 

"""
