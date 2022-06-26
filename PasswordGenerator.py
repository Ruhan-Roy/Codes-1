import random
import string

adjectives = ('sleepy', 'slow', 'fat', 'smelly', 'wet', 'red',
              'yellow', 'green', 'blue', 'orange',
              'white', 'purple', 'fluffy', 'proud', 'brave')
nouns = ('apple', 'dinosaur', 'ball',
         'goat', 'toaster', 'dragon', 'hammer', 'duck', 'panda',)

print('Welcome to Password Picker!')

while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)
    password = adjective + noun + str(number) + special_char
    print('Your new password is: %s' % password)

    response = input('Would you like a different Password? Type y or n:')
    if response == 'n':
        break