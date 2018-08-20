# -*- coding: utf-8 -*-
"""
Created on 2018/8/14 21:22

@author: vincent
题目描述
输入一个链表，反转链表后，输出新链表的表头。
"""
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        pre = None
        while pHead:
            temp = pHead.next
            pHead.next = pre
            pre = pHead
            pHead = temp
        return pre