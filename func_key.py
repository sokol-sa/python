#!/usr/bin/env python3
def func(a, b=5, c=10):
    print('a=',a,'b=',b,'c=',c)
func(3,7)
func(25,c=24)
func(c=100, a=50)
