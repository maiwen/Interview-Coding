# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 12:06:37 2018

@author: Administrator

Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result, stack = [], []
        stack.append(root)
        while stack:
            node = stack.pop()
            if not node:
                continue
            result.append(node.val)
            stack.append(node.left)
            stack.append(node.right)
        return result[::-1]
    
    def postorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def postorderTraversalHelper(root, ordering):
            if root is None:
                return
            if root.left:
                postorderTraversalHelper(root.left, ordering)
            if root.right:
                postorderTraversalHelper(root.right, ordering)
            ordering.append(root.val)

        ordering = []
        postorderTraversalHelper(root, ordering)
        return ordering
