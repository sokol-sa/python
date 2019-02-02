#!/usr/bin/env python3
while True:
    s=input('Enter any')
    if s=="Exit":
        break
    if len(s)<3:
        print('Too low!')
        continue
    print('Very well!')
