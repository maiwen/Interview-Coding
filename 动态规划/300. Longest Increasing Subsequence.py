# -*- coding: utf-8 -*-
"""
Created on 2018/7/11 10:14

@author: vincent

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""
from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return n
        dp = [1] * n
        for i in range(1,n):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)

    def lengthOfLIS1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # tails[i] stores min tail with LIS of length i+1
        # tails is an increasing array
        # a new x falls between tails[i-1] and tails[i] means tails[i] <- x
        size = 0
        tails = [0] * len(nums)
        for x in nums:
            pos = bisect_left(tails, x, 0, size)
            if pos == size:
                size += 1
            tails[pos] = x
        return size