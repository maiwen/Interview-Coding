# -*- coding: utf-8 -*-
"""
Created on 2018/8/9 11:06

@author: vincent

题目描述
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，
那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
{[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
"""
# -*- coding:utf-8 -*-
from collections import *
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if not num or size < 1 or len(num) < size:
            return []
        if len(num) == size:
            return [max(num)]
        d = deque()
        result = []
        for i,n in enumerate(num):
            while d and n > num[d[-1]]:
                d.pop()
            d.append(i)
            if d[0] <= i-size:
                d.popleft()
            if i >= size - 1:
                result.append(num[d[0]])
        return result

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        result = []
        if not nums or n < k:
            return []
        for i in range(n):
            if i+k < n+1:
                result.append(max(nums[i:i+k]))
            else:
                break
        return result