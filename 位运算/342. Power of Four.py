# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 22:34:23 2018

@author: Administrator

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?

这种数在二进制表示中有且只有一个奇数位为 1，例如 16（10000）。
"""

class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and list(bin(num)).count('1') == 1 and (num & 0b01010101010101010101010101010101) != 0