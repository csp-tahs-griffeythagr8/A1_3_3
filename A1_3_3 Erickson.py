"""
A1_3_2 Erickson.py
Programmer:Wyatt Erickson
"""
import random
guess = 24

def hiLo_game(guess):
    rand_num = random.randint(1,100)
    if guess == rand_num:
        print('congrats you found the correct number')
    elif guess < rand_num:
        print('this is too low')
    else guess > rand_num:
        print('this is too high')

"""
Documentation:
1. Provide EOL comments of important items and describe their intended purpose using '#'

Spacing: 
1. Provide appropriate spacing between lines to increase readability. 

Coding:
1. Your code currently has an error: else guess > rand_num returns a syntax error. 
"""
