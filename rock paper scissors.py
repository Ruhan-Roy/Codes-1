#!/bin/python3

from random import randint

player = input('rock(r) , paper(p) , scissor(s)?')
print(player, 'vs', end=' ')

chosen = randint(1,3)
#print(chosen)

if chosen == 1:
    computer = 'r'
    
elif chosen == 2:
    computer = 'p'

else:
    computer = 's'

print(computer)

if player == computer:
  print('DRAW!')
  
elif player == 'r' and computer == 's':
  print('YOU WIN!')
elif player == 'r' and computer == 'p':
  print('YOU LOSE!')
elif player == 'p' and computer == 's':
  print('YOU LOSE!')
elif player == 'p' and computer == 'r':
  print('YOU WIN!')
elif player == 's' and computer == 'p':
  print('YOU WIN!')
elif player == 's' and computer == 'r':
  print('YOU LOSE!')