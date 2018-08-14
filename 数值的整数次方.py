# -*- coding: utf-8 -*-
"""
Created on 2018/8/14 22:13

@author: vincent
题目描述
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
"""


# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        self.invalidInput = False
        if base == 0.0 and exponent < 0:
            self.invalidInput = True
            return 0.0
        absexponent = abs(exponent)
        result = self.powerUnsigned(base, absexponent)
        if exponent < 0:
            result = 1.0 / result
        return result

    def powerUnsigned(self, base, absexponent):
        if absexponent == 0:
            return 1
        if absexponent == 1:
            return base
        result = self.powerUnsigned(base, absexponent >> 1)
        result *= result
        if absexponent & 0x1 == 1:
            result *= base
        return result