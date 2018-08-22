# -*- coding: utf-8 -*-
"""
Created on 2018/8/6 18:19

@author: vincent
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
"""
# -*- coding:utf-8 -*-
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
    def jumpFloor(self, number):
        # write code here
        if number < 3:
            return number
        return self.jumpFloor(number-1)+self.jumpFloor(number-2)