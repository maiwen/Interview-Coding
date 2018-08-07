# -*- coding: utf-8 -*-
"""
Created on 2018/8/7 16:14

@author: vincent

题目描述
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
"""


# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def __init__(self):
        self.result = []

    def printMatrix(self, matrix):
        # write code here
        if not matrix:
            return []
        rows = len(matrix)
        cols = len(matrix[0])
        start = 0
        while rows > start * 2 and cols > start * 2:
            self.printMatrixInCircle(matrix, cols, rows, start)
            start += 1
        return self.result

    def printMatrixInCircle(self, matrix, cols, rows, start):
        endx = cols - 1 - start
        endy = rows - 1 - start

        for i in range(start, endx + 1):
            self.result.append(matrix[start][i])

        if start < endy:
            for i in range(start + 1, endy + 1):
                self.result.append(matrix[i][endx])

        if start < endx and start < endy:
            for i in range(endx - 1, start - 1, -1):
                self.result.append(matrix[endy][i])

        if start < endx and start < endy - 1:
            for i in range(endy - 1, start, -1):
                self.result.append(matrix[i][start])
