# -*- coding: utf-8 -*-
"""
Created on 2018/9/5 17:41

@author: vincent
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from heapq import heappush, heappop, heapify


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = [(node.val, index, node) for index, node in enumerate(lists) if node]
        heapify(h)
        sorted_head = ListNode(-1)
        cur = sorted_head
        while h:
            (cur_min, index, node) = heappop(h)
            next_node = node.next
            if next_node:
                heappush(h, (next_node.val, index, next_node))
            node.next = None
            cur.next = node
            cur = cur.next
        return sorted_head.next


class Solution1:
    def mergeKLists(self, lists):
        from operator import attrgetter

        sorted_list = []
        for lst in lists:
            while lst is not None:
                sorted_list.append(lst)
                lst = lst.next
        sorted_list = sorted(sorted_list, key=attrgetter('val'))
        dummy = curr = ListNode(0)
        for node in sorted_list:
            curr.next = curr = node
        return dummy.next
