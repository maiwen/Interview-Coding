# -*- coding: utf-8 -*-
"""
Created on 2018/7/9 18:11

@author: vincent

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [ [0 for j in range(n)] for i in range(m)]
        dp[m-1][n-1]=grid[m-1][n-1]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i==m-1 and j == n-1:
                    dp[i][j] = grid[m-1][n-1]
                elif  i==m-1:
                     dp[i][j] = grid[i][j]+ dp[i][j+1]
                elif  j == n-1:
                     dp[i][j] = grid[i][j]+ dp[i+1][j]
                else:
                    dp[i][j] = grid[i][j]+ min(dp[i+1][j],dp[i][j+1])
        return dp[0][0]