#!/usr/bin/env python3
numder=23
running=True
while running:
    guess=int(input('Enter'))
    if guess==numder:
        print('You WIN')
        running=False
    elif guess<numder:
        print('Guess<Number')
    else:
        print('Guess>Number')
else: #можно и без этого блока
   print('GAME OVER')
print ('END')
