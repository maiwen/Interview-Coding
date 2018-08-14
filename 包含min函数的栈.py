# -*- coding: utf-8 -*-
"""
Created on 2018/8/13 22:14

@author: vincent
题目描述
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
"""
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.mins = []
    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.mins or node < self.mins[-1]:
            self.mins.append(node)
        else:
            self.mins.append(self.mins[-1])
    def pop(self):
        # write code here
        self.stack.pop()
        self.mins.pop()
    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        # write code here
        return self.mins[-1]