# -*- coding: utf-8 -*-
"""
Created on 2018/8/7 15:12

@author: vincent
题目描述
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
"""
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        l = self.TreeDepth(pRoot.left)
        r = self.TreeDepth(pRoot.right)
        return max(l,r)+1