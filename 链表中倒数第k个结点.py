# -*- coding: utf-8 -*-
"""
Created on 2018/8/14 21:40

@author: vincent
题目描述
输入一个链表，输出该链表中倒数第k个结点。
"""
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        res = []
        while head:
            res.append(head)
            head = head.next
        if k>len(res) or k<1:
            return
        return res[-k]