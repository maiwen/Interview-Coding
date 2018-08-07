# -*- coding: utf-8 -*-
"""
Created on 2018/8/6 21:13

@author: vincent
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""
# -*- coding:utf-8 -*-
from functools import wraps
class Solution:
    def memo(func):
        cache = {}

        @wraps(func)
        def wrap(*args):
            if args not in cache:
                cache[args] = func(*args)
            return cache[args]
        return wrap

    @memo
    def rectCover(self, number):
        # write code here
        if number < 3:
            return number
        return self.rectCover(number-1)+self.rectCover(number-2)