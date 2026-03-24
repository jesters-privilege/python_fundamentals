### PRACTICE PROGRAM - DEBUGGING COIN TOSS ###
import random, logging

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    toss = random.randint(0, 1)  # 0 is tails, 1 is heads
    toss_str = 'heads' if toss == 1 else 'tails' # Convert toss int to str
    if toss_str == guess:
        print('You got it!')
    else:
        print('Nope! Guess again!')
        guess = input()
        if toss_str == guess:
            print('You got it!')
        else:
            print('Nope. You are reallheay bad at this game.')