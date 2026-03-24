### SHORT PROGRAM - MAGIC 8 BALL 1ST ###
import random
def get_answer(answer_number):
        # Returns a fortune answer based on what int answer_number is 1 to 9
        if answer_number == 1:
                return 'It is certain'
        elif answer_number == 2:
                return 'It is decidedly so'
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
print(get_answer(random.randint(1,9)))

### SHORT PROGRAM - MAGIC 8 BALL W/ LIST ###
import random
messages = ['It is certain,'
        'It is decidedly so',
        'Yes definitely',
        'Reply hazy try again',
        'Ask again later',
        'Concentrate and ask again',
        'My reply is no ',
        'Outlook not so good',
        'Very doubtful']
print('Ask a yes or no question:')
input('>')
print(messages[random.randint(0, len(messages) - 1)])