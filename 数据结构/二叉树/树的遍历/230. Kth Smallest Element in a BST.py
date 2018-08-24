# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 15:02:36 2018

@author: Administrator

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
"""
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def __init__(self):
        self.cnt = 0
        self.val = 0
    
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.inorder(root,k)
        return self.val
    
    def inorder(self, node, k):
        if not node:
            return
        self.inorder(node.left,k)
        self.cnt += 1
        if self.cnt == k:
            self.val = node.val
            return
        self.inorder(node.right,k)
