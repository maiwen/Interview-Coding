# -*- coding: utf-8 -*-
"""
Created on 2018/8/6 18:15

@author: vincent

一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""
from functools import wraps
class Solution:
    def memo(func):
        cache={}
        @wraps(func)
        def wrap(*args):
            if args not in cache:
                cache[args]=func(*args)
            return cache[args]
        return wrap
    @memo
    def jumpFloorII(self, number):
        # write code here
        result = 1
        if number < 3:
            return number
        for i in range(number):
            result += self.jumpFloorII(i)
        return result

class solution1:
    def jumpFloorII(self, number):
        return 2**(number - 1)

from functools import wraps
class Solution3:
    def memo(func):
        cache={}
        @wraps(func)
        def wrap(*args):
            if args not in cache:
                cache[args]=func(*args)
            return cache[args]
        return wrap
    @memo
    def jumpFloorII(self, number):
        # write code here
        if number < 3:
            return number
        return 2 * self.jumpFloorII(number - 1)