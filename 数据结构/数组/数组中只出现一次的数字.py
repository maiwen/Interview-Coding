# -*- coding: utf-8 -*-
"""
Created on 2018/8/7 11:50

@author: vincent
题目描述
一个整型数组里除了两个数字之外，其他的数字都出现了偶数次。请写程序找出这两个只出现一次的数字。
"""
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        seen = set()
        for num in array:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)
        return list(seen)

class Solution1:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        diff = 0
        for num in array:
            diff ^= num
        pivot_bit = diff & -diff
        a, b = 0, 0
        for num in array:
            if num & pivot_bit:
                a ^= num
            else:
                b ^= num
        return [a,b]