#!/usr/bin/env python3
number=23
guess=int(input('Enter number:'))
if guess==number:
    print('You WIN')
    print('Not priz')
elif guess<number:
    print('Number>guess')
else:
    print('number<guess')
print('End GAME')
