# -*- coding: utf-8 -*-
"""
Created on 2018/8/13 21:34

@author: vincent

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        n = len(matrix[0])
        for row in matrix:
            l, h = 0, n-1
            if row[-1] >= target:
                if row[-1] == target:
                    return True
                while l < h:
                    m = l + (h-l)//2
                    if row[m] == target:
                        return True
                    elif row[m] > target:
                        h -= 1
                    else:
                        l += 1
            else:
                continue
        return False