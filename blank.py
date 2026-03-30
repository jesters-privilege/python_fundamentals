### ME LEARNING ###

### WHILE LOOPS ###
while True:
        print('Who are you?')
        name = input('>')
        if name != 'Joe':
                continue
        print('Hello, Joe. What is the password? (It is a fish.)')
        password = input('>')
        if password == 'swordfish':
                break
        print('Access granted.')

### FOR LOOPS ###
total = 0
for num in range(101):
        total = total + num
print(total)

### SHORT PROGRAM - GUESS THE NUMBER ###
# This is a guess the number game
import random
secret_number = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guesses_taken in range (1,7):
        print('Take a guess.')
        guess = int(input('>'))

        if guess < secret_number:
                print('Your guess is too low.')
        elif guess > secret_number:
                print('Your guess is too high.')
        else:
                break   # This condition is the correct guess
        
if guess == secret_number:
        print('Good job! You got it in ' + str(guesses_taken) + 'guesses!')
else:
        print('Nope. The number was ' + str(secret_number))

### SHORT PROGRAM - ROCK PAPER SCISSORS ###
import random, sys

# These variables keep track of the number of wins, losses, and ties
wins = 0
losses = 0
ties = 0

while True: # The main game loop
        print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
        while True: # The player input loop
                print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
                player_move = input('>')
                if player_move == 'q':
                        sys.exit()  # Quit the program
                if player_move == 'r' or player_move =='p' or player_move =='s':
                        break   # Break out of player input loop
                print('Type one of r, p, s, or q.')

                # Display what the player chose
                if player_move == 'r':
                    print('ROCK versus...')
                elif player_move == 'p':
                    print('PAPER versus...')
                elif player_move == 's':
                    print('SCISSORS versus...')

        # Display what the computer chose:
        move_number = random.randint(1,3)
        if move_number == 1:
                computer_move = 'r'
                print('ROCK')
        elif move_number == 2:
                computer_move = 'p'
                print('PAPER')
        elif move_number == 3:
                computer_move = 's'
                print('SCISSORS')

        # Display and record the win/loss/tie:
        if player_move == computer_move:
                print('It is a tie!')
                ties = ties + 1
        elif player_move == 'r' and computer_move =='s':
                print('You win!')
                wins = wins + 1
        elif player_move == 'p' and computer_move == 'r':
                print('You win!')
                wins = wins + 1
        elif player_move == 's' and computer_move == 'p':
                print('You win!')
                wins = wins + 1
        elif player_move == 'r' and computer_move == 'p':
                print('You lose!')
                losses = losses + 1
        elif player_move == 'p' and computer_move == 's':
                print('You lose!')
                losses = losses + 1
        elif player_move == 's' and computer_move == 'r':
                    print('You lose!')
                    losses = losses + 1

### CREATING FUNCTIONS ###
def say_hello_to(name):
        # Prints three greetings to the name provided
        print('Good morning, ' + name)
        print('Good afternoon, ' + name)
        print('Good evening, ' + name)

say_hello_to('Alice')
say_hello_to('Bob')

import random

def get_answer(answer_number):
        # Returns a fortune answer based on what int answer_number is, 1 to 9
        if answer_number == 1:
                return 'It is certain'
        elif answer_number == 2:
                return 'It is decidely so'
        elif answer_number == 3:
                return 'Yes'
        elif answer_number == 4:
                return 'Reply hazy try again'
        elif answer_number == 5:
                return 'Ask again later'
        elif answer_number == 6:
                return 'Concentrate and ask again'
        elif answer_number == 7:
                return 'My reply is no'
        elif answer_number == 8:
                return 'Outlook not so good'
        elif answer_number == 9:
                return 'Very doubtful'
print('Ask a yes or no question:')
input('>')
r = random.randint(1,9)
fortune = get_answer(r)
print(fortune)

### DEBUGGING ###

### LOGGING LEVELS ###
# DEBUG - logging.debug(): the lowest level, small details. Important for messages when diagnosing problems.
# INFO - logging.info(): record information about general events in program or confirm it's working at various points.
# WARNING - logging.warning(): indicate a potential probelm that doesn't prevent the program from working but might do so in the future.
# ERROR - logging.error(): record an error that caused the program to fail to do something
# CRITICAL - logging.critical(): highest level; indicate a fatal error that has caused, or is about to cause, the program to stop running entirely

import logging
logging.basicConfig(level = logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Some minor code and debugging details.')
logging.info('An event happened.')
logging.warning('Something could go wrong.')
logging.error('An error has occurred.')
logging.critical('The program is unable to recover!')
logging.disable(logging.CRITICAL)
logging.critical('Critical error! Critical error!')
logging.error('Error! Error!')

### LISTS ###
spam = ['cat', 'bat', 'rat', 'elephant']
spam[0]
spam[1]
spam[2]
spam[3]
['cat', 'bat', 'rat', 'elephant'][3]
'Hello, ' + spam[0]
'The ' + spam[1] + ' ate the ' + spam[0] + '.'

spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
spam[0]
spam[0][1]
spam[1][4]

spam = ['cat', 'bat', 'rat', 'elephant']
spam[-1] # last index
spam[-3] # Third to last index
'The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.'

spam = ['cat', 'bat', 'rat', 'elephant']
spam[0:4]
spam[1:3]
spam[0:-1]
spam[:2]
spam[1:]
spam[:]

spam = ['cat', 'dog', 'moose']
len(spam)

spam = ['cat', 'bat', 'rat', 'elephant']
spam[1] = 'aardvark'
spam
spam[2] = spam[1]
spam
spam[-1] = 12345
spam

[1,2,3] + ['A', 'B', 'C']
['X', 'Y', 'Z'] * 3
spam = [1,2,3]
spam = spam + ['A', 'B', 'C']
spam

spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
spam
del spam[2]
spam

### FOR LOOPS AND LISTS ###
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
       print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

### TUPLE UNPACKING ###
cat = ['fat', 'gray', 'loud']
size, color, disposition = cat

### LIST ITEM ENUMERATION ###
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
       print('Index' + str(index) + ' in supplies is: ' + item)

### RANDOM SELECTION AND ORDERING ###
import random
pets = ['Dog', 'Cat', 'Moose']
random.choice(pets)

people = ['Alice', 'Bob', 'Carol', 'David']
random.shuffle(people)
people

spam = 'Hello,'
spam += ' world!'
spam

bacon = ['Zophie']
bacon *= 3
bacon

### METHODS ###
spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('hello')
spam.index('heyas')
spam.index('howdy howdy howdy')

spam = ['cat', 'dog', 'bat']
spam.append('moose')
spam

spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
spam

spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
spam

spam = [2, 5, 3.14, 1, -7]
spam.sort()
spam
spam = ['Ants', 'Cats', 'Dogs', 'Badgers', 'Elephants']
spam.sort()
spam
spam.sort(reverse=True)
spam

### SHORT-CIRCUTING BOOLEAN OPERATORS ###
spam = []
if len(spam) > 0 and spam[0] == 'cat':
       print('A cat is the first item')
else:
       print('The first item is not a cat')

### SEQUENCE DATA TYPES ###
name = 'Zophie'
name[0]
name[-2]
name[0:4]
'Zo' in name
'z' in name
'p' not in name
for i in name:
       print('* * * ' + i + ' * * *')

### MUTABLE AND IMMUTABLE DATA TYPES ###
name = 'Zophie a cat'
new_name = name[0:7] + 'the' + name[8:12]
name
new_name

eggs = ['A', 'B', 'C']
del eggs[2]
del eggs[1]
del eggs[0]
eggs.append('x')
eggs.append('y')
eggs.append('z')
eggs

### TUPLE DATA TYPE ###
eggs = ('hello', 42, 0.5)
eggs[0]
eggs[1:3]
len(eggs)
eggs[1] = 99

type(('hello',))
type(('hello'))

### LIST AND TUPLE TYPE CONVERSION ###
tuple(['cat', 'dog', 5])
list(('cat', 'dog', 5))
list('hello')

### REFERENCES ###
spam = 42
eggs = spam
spam = 99
spam
eggs

spam = [0,1,2,3]
eggs = spam     # The reference, not the list, is being copied
eggs[1] = 'Hello!'      # This changes the list value
spam
eggs    # The eggs variable refers to the same list
# VARIABLES NEVER CONTAIN VALUES. THEY CONTAIN ONLY REFERENCES TO VALUES
# THE '=' ASSIGNMENT OPERATOR COPIES ONLY REFERENCES, NEVER VALUES

### COPY() AND DEEPCOPY() FUNCTIONS ###
import copy
spam = ['A', 'B', 'C']
cheese = copy.copy(spam)        # Cretes a duplicate copy of the list
cheese[1] = 42  # Changes cheese
spam    # Spam variable is unchanged
cheese  # Cheese variable is changed

