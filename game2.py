#!/usr/bin/python
# -*- coding: utf-8 -*-
import  random
ran_num = random.randint(0,99)
left = 0
right = 99
while True:
    print('当前范围是：',left,'---',right)
    test = int(input('再猜一下\n'))
    if test == ran_num:
        print('^-^')
        break
    if test > ran_num:
        right = test
    else:
        left = test