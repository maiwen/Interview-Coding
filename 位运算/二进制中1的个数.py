# -*- coding: utf-8 -*-
"""
Created on 2018/8/14 13:37

@author: vincent
题目描述
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
"""
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            count += 1
            n = (n - 1) & n
        return count

class Solution:
    def NumberOf1(self, n):
        # write code here
        count, flag = 0, 1
        if n < 0:
            n = n & 0xffffffff
        for i in range(len(bin(n))-2):
            if n & flag:
                count += 1
            flag <<= 1
        return count