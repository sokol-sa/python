#!/usr/bin/env python3
def func_outer():
    x=2
    print('x=',x)

    def func_inner():
        nonlocal x
        x=50
    func_inner()
    print('x replace to',x)
func_outer()
