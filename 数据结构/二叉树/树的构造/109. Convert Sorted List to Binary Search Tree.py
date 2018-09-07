# -*- coding: utf-8 -*-
"""
Created on 2018/9/6 13:19

@author: vincent

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        x = {'header': head}

        def sortedListToBSTHelper(start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            left = sortedListToBSTHelper(start, mid - 1)
            node = TreeNode(x['header'].val)
            node.left = left

            x['header'] = x['header'].next
            right = sortedListToBSTHelper(mid + 1, end)
            node.right = right
            return node

        runner = head
        size = 0
        while runner:
            runner = runner.next
            size += 1
        end = size
        start = 0
        return sortedListToBSTHelper(start, end - 1)