# -*- coding: utf-8 -*-
"""
Created on 2018/8/6 20:11

@author: vincent
"""
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
    def Fibonacci(self, n):
        # write code here
        if n < 2:
            return n
        return self.Fibonacci(n - 1) + self.Fibonacci(n - 2)