# -*- coding: utf-8 -*-
"""
Created on 2018/8/13 21:56

@author: vincent
题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""
# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        if len(array) < 2:
            return array
        odd, even = [], []
        for num in array:
            if num%2 == 0:
                even.append(num)
            else:
                odd.append(num)
        return odd+even