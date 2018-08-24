# -*- coding: utf-8 -*-
"""
Created on 2018/7/22 16:22

@author: vincent

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.


"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left == 0 or right == 0:
            return left + right + 1
        return min(left,right) + 1

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if not root : return 0
        return self.dfs(root,0)

    def dfs(self,root,depth):
        if not root : return depth
        if not root.left and root.right: return self.dfs(root.right,depth+1)
        if root.left and not root.right: return self.dfs(root.left,depth+1)
        if not root.left and not root.right: return depth + 1
        L , R = self.dfs(root.left,depth+1),self.dfs(root.right,depth+1)
        return min(L,R)