#!/usr/bin/env python3
x=50
def func():
    global x
    print('x=',x)
    x=2
    print('Replace x=',x)

func()
print('x=',x)
