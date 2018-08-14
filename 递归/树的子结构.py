# -*- coding: utf-8 -*-
"""
Created on 2018/8/14 21:58

@author: vincent
题目描述
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
"""
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot1 and pRoot2:
            return self.isSubtreeWithRoot(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)
        else:
            return False
    def isSubtreeWithRoot(self, s, t):
        if t == None:
            return True
        if s == None:
            return False
        if s.val != t.val:
            return False
        return self.isSubtreeWithRoot(s.left, t.left) and self.isSubtreeWithRoot(s.right, t.right)