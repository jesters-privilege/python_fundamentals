### IN AND NOT IN OPERATORS ###
'howdy' in ['hello', 'hi', 'howdy', 'heyas']
spam = ['hello', 'hi', 'howdy', 'heyas']
'cat' in spam
'howdy' not in spam
'cat' not in spam

my_pets = ['Zophie' , 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in my_pets:
       print('I do not have a pet named ' + name)
else:
       print(name + 'is my pet.')