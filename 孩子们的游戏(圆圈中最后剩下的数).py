# -*- coding: utf-8 -*-
"""
Created on 2018/8/14 15:29

@author: vincent
题目：0, 1, … , n-1 这 n 个数字排成一个圈圈，从数字 0 开始每次从圆圏里删除第 m 个数字。求出这个圈圈里剩下的最后一个数字。
"""
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n < 1 or m < 1:
            return -1
        last = 0
        for i in range(2, n+1):
            last = (last+m)%i
        return last

class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n < 1 or m < 1:
            return -1
        nums = list(range(n))
        cur = 0
        while len(nums) > 1:
            for i in range(1,m):
                cur += 1
                if cur == len(nums):
                    cur = 0
            nums.remove(nums[cur])
            if cur == len(nums):
                cur = 0
        return nums[0]