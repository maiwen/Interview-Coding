# -*- coding: utf-8 -*-
"""
Created on 2018/7/16 18:40

@author: vincent
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.result = True
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def maxdepth(root):
            if not root:
                return 0
            l = maxdepth(root.left)
            r = maxdepth(root.right)
            if abs(l - r) > 1:
                self.result = False
            return max(l, r) + 1
        maxdepth(root)
        return self.result

class Solution1:
    def parse(self, node, depth):
        if node == None:
            return depth, True
        l_height, balancedl = self.parse(node.left, depth + 1)
        r_height, balancedr = self.parse(node.right, depth + 1)
        diff = abs(l_height - r_height)
        if diff > 1:
            return max(l_height, r_height), False
        return max(l_height, r_height), balancedl and balancedr

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        height, balanced = self.parse(root, 0)
        return balanced