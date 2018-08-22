# -*- coding: utf-8 -*-
"""
Created on 2018/8/13 21:35

@author: vincent
题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if not array:
            return False
        rows, cols = len(array), len(array[0])
        row, col = 0, cols - 1
        while row < rows and col >= 0:
            if array[row][col] == target:
                return True
            elif array[row][col] < target:
                row += 1
            else:
                col -= 1
        return False


"""
Search a 2D Matrix
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
                        h = m
                    else:
                        l = m+1
            else:
                continue
        return False
