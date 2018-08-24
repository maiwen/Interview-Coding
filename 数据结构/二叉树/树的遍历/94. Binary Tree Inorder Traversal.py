# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 12:04:49 2018

@author: Administrator

Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result, stack = [], []
        if not root:
            return result
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            result.append(node.val)
            cur = node.right
        return result
    
    def inorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inorderhelper(root,order):
            if root is None:
                return 
            if root.left:
                inorderhelper(root.left,order)
            order.append(root.val)
            if root.right:
                inorderhelper(root.right,order)
        
        order=[]
        inorderhelper(root,order)
        return order

