# -*- coding: utf-8 -*-
"""
Created on 2018/8/14 20:12

@author: vincent
题目描述
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
"""


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return
        self.res = []
        self.midtraversal(pRootOfTree)
        for i, v in enumerate(self.res[:-1]):
            v.right = self.res[i + 1]
            self.res[i + 1].left = v
        return self.res[0]

    def midtraversal(self, root):
        if not root: return
        self.midtraversal(root.left)
        self.res.append(root)
        self.midtraversal(root.right)
