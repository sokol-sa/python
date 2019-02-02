#!/usr/bin/env python3
def printMax(x, y):
    '''Print max from two number.

    Each may be INT.'''
    x=int(x)
    y=int(y)
    if x>y:
        print(x, 'max')
    else:
        print(y, 'max')
    
printMax (3, 5)
print (printMax.__doc__)
help(printMax)