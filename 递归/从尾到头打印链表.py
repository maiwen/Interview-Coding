# -*- coding: utf-8 -*-
"""
Created on 2018/8/6 20:10

@author: vincent

输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
"""
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def __init__(self):
        self.result = []
    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode:
            self.printListFromTailToHead(listNode.next)
            self.result.append(listNode.val)
        return self.result