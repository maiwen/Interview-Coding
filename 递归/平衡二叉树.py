# -*- coding: utf-8 -*-
"""
Created on 2018/8/6 21:45

@author: vincent

输入一棵二叉树，判断该二叉树是否是平衡二叉树。
"""
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.result = True
    def IsBalanced_Solution(self, pRoot):
        # write code here
        def maxdepth(root):
            if not root:
                return 0
            l = maxdepth(root.left)
            r = maxdepth(root.right)
            if abs(l - r) > 1:
                self.result = False
            return max(l, r) + 1
        maxdepth(pRoot)
        return self.result