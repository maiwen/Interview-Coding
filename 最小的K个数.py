# -*- coding: utf-8 -*-
"""
Created on 2018/8/11 21:24

@author: vincent
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
"""
# -*- coding:utf-8 -*-
import heapq
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if len(tinput) < k:
            return []
        array, result = [], []
        for num in tinput:
            heapq.heappush(array, num)
        for i in range(k):
            result.append(heapq.heappop(array))
        return result