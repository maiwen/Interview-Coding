# -*- coding: utf-8 -*-
"""
Created on 2018/7/4 18:24

@author: vincent

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # Utilize O(n) extra space
    def hasCycle(self, head):
        dic = {}
        while head:
            if head in dic:
                return True
            dic[head] = 0
            head = head.next
        return False

    # follow up: classic two poiters method
    def hasCycle1(self, head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                return True
        return False

    def hasCycle2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        seen = set()
        while head:
            if head in seen: return True
            seen.add(head)
            head = head.next
        return False
    def hasCycle3(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head
        while slow and fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            if fast == slow:
                break
        if fast and slow and fast == slow:
            return True
        return False