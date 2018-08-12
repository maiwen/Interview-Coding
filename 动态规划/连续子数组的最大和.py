# -*- coding: utf-8 -*-
"""
Created on 2018/8/11 21:15

@author: vincent
例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。给一个数组，返回它的最大连续子序列的和,子向量的长度至少是1
"""
# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return 0
        dp = [0]*len(array)
        dp[0] = array[0]
        for i in range(1, len(array)):
            if dp[i-1] > 0:
                dp[i] = dp[i-1] + array[i]
            else:
                dp[i] = array[i]
        return max(dp)