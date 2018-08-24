# -*- coding: utf-8 -*-
"""
Created on 2018/8/14 17:56

@author: vincent
题目描述
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
"""


# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        visited = [[0] * cols for i in range(rows)]
        return self.search(threshold, rows, cols, 0, 0, visited)

    def search(self, threshold, rows, cols, row, col, visited):
        count = 0
        if self.check(threshold, rows, cols, row, col, visited):
            visited[row][col] = True
            count = 1 + self.search(threshold, rows, cols, row - 1, col, visited) + \
                    self.search(threshold, rows, cols,row, col - 1,visited) + \
                    self.search(threshold, rows, cols, row + 1, col, visited) + \
                    self.search(threshold, rows, cols, row, col + 1,visited)
        return count

    def check(self, threshold, rows, cols, row, col, visited):
        if row < 0 or row >= rows or col < 0 or col >= cols or (
                self.getdigitsum(row) + self.getdigitsum(col)) > threshold or visited[row][col]:
            return False
        else:
            return True

    def getdigitsum(self, num):
        sum = 0
        while num > 0:
            sum += num % 10
            num /= 10
        return sum