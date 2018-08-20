# -*- coding: utf-8 -*-
"""
Created on 2018/8/7 15:39

@author: vincent
题目描述
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
输出描述:
对应每个测试案例，输出两个数，小的先输出。
"""


# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if len(array) < 2:
            return []
        result = []
        for num in array:
            sub = tsum - num
            if sub in array:
                result.append([num, sub])
        if not result:
            return []
        min = float('inf')
        minre = []
        for re in result:
            if re[0] * re[1] < min:
                min = re[0] * re[1]
                minre = [re[0], re[1]]

        return [minre[0], minre[1]] if minre[0] < minre[1] else [minre[1], minre[0]]


# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here

        for num in array:
            if tsum - num in array:
                return [num, tsum - num]
        return []