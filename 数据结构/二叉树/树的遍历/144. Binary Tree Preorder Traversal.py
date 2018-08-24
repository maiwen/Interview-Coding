# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 12:00:51 2018

@author: Administrator

Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
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
            stack.append(node.right)
            stack.append(node.left)
        return result
    
class Solution1(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list = []
        if(root is None):
            return []
        list.append(root.val)
        list.extend(self.preorderTraversal(root.left))
        list.extend(self.preorderTraversal(root.right))
        
        return list
