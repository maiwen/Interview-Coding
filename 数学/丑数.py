# -*- coding: utf-8 -*-
"""
Created on 2018/8/9 15:42

@author: vincent
题目描述
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
"""
# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0:
            return 0
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while index > 1:
            u2, u3, u5 = ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5
            minu = min([u2, u3, u5])
            if minu == u2:
                i2 += 1
            if minu == u3:
                i3 += 1
            if minu == u5:
                i5 += 1
            ugly.append(minu)
            index -= 1
        return ugly[-1]

    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False

        for n in [2, 3, 5]:
            while (num % n == 0):
                num /= n

        return num == 1