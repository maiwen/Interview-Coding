# -*- coding: utf-8 -*-
"""
Created on 2018/9/6 13:59

@author: vincent

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(cur, left_limit, right_limit):
            if not cur:
                return True
            if left_limit < cur.val and cur.val < right_limit:
                return check(cur.left, left_limit, cur.val) and check(cur.right, cur.val, right_limit)
            return False
        return check(root, -1*float("inf"), float("inf"))