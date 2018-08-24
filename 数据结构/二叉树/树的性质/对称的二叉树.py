# -*- coding: utf-8 -*-
"""
Created on 2018/8/8 10:25

@author: vincent

题目描述
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
"""
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        return self.isSymmetrical2(pRoot.left, pRoot.right)
    def isSymmetrical2(self, l, r):
        if l == None and r == None:
            return True
        if l == None or r == None:
            return False
        if l.val != r.val:
            return False
        return self.isSymmetrical2(l.left, r.right) and self.isSymmetrical2(l.right, r.left)