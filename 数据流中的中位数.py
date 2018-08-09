# -*- coding: utf-8 -*-
"""
Created on 2018/8/9 10:13

@author: vincent

如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，
那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
"""
# -*- coding:utf-8 -*-
import heapq

class Solution:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def Insert(self, num):
        # write code here
        if len(self.q1) <= 0:
            heapq.heappush(self.q1, -num)
        else:
            peek1 = -self.q1[0]
            if num <= peek1:
                heapq.heappush(self.q1, -num)
            else:
                heapq.heappush(self.q2, num)

            if len(self.q1) > len(self.q2) + 1:
                heapq.heappush(self.q2, -heapq.heappop(self.q1))
            elif len(self.q1) <= len(self.q2) - 1:
                heapq.heappush(self.q1, -heapq.heappop(self.q2))

    def GetMedian(self, ok):
        # write code here
        if len(self.q1) != len(self.q2):
            return -self.q1[0]
        else:
            return (-self.q1[0] + self.q2[0]) / 2.0


from heapq import *


class Solution:

    def __init__(self):
        self.before = []
        self.after = []

    def Insert(self, num):
        # write code here
        if len(self.before) == len(self.after):
            heappush(self.after, -heappushpop(self.before, -num))
        else:
            heappush(self.before, -heappushpop(self.after, num))

    def GetMedian(self, garbage):
        # write code here
        if not self.after:
            return None

        if len(self.after) == len(self.before):
            return (self.after[0] - self.before[0]) / float(2.0)
        else:
            return float(self.after[0])