# -*- coding: utf-8 -*-
"""
Created on 2018/8/8 20:56

@author: vincent
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。

"""
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        seen = set()
        while pHead:
            if pHead in seen:
                return pHead
            seen.add(pHead)
            pHead = pHead.next
        return None