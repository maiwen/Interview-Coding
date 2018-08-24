# -*- coding: utf-8 -*-
"""
Created on 2018/8/24 17:46

@author: vincent
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

"""


class Solution:
    def dfs(self, x, y, matrix):
        if x < 0 or x > len(matrix) - 1 or y < 0 or y > len(matrix[0]) - 1 or matrix[x][y] != 'O':
            return
        matrix[x][y] = '#'
        self.dfs(x - 1, y, matrix)
        self.dfs(x, y - 1, matrix)
        self.dfs(x + 1, y, matrix)
        self.dfs(x, y + 1, matrix)

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) > 0:
            m, n = 0, 0
            for n in range(len(board[0])):
                if board[m][n] == 'O':
                    self.dfs(m, n, board)
            for m in range(1, len(board)):
                if board[m][n] == 'O':
                    self.dfs(m, n, board)
            for n in range(len(board[0]) - 2, -1, -1):
                if board[m][n] == 'O':
                    self.dfs(m, n, board)
            for m in range(len(board) - 2, 0, -1):
                if board[m][n] == 'O':
                    self.dfs(m, n, board)
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == '#':
                        board[i][j] = 'O'
                    else:
                        board[i][j] = 'X'
