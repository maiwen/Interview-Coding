# -*- coding: utf-8 -*-
"""
Created on 2018/9/6 14:05

@author: vincent

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1 for i in range(n+1)]
        for i in range(2,n+1):
            dp[i] = sum([dp[j-1] * dp[i-j] for j in range(1,i+1)])
        return dp[-1]