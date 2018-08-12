# -*- coding: utf-8 -*-
"""
Created on 2018/8/9 21:51

@author: vincent
题目描述
输入两个链表，找出它们的第一个公共结点。
"""


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        na, nb = pHead1, pHead2
        while na != nb:
            na = na.next if na else pHead2
            nb = nb.next if nb else pHead1
        return na
