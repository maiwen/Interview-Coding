# -*- coding: utf-8 -*-
"""
Created on 2018/8/8 11:45

@author: vincent
题目描述
给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。
"""


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def __init__(self):
        self.cnt = 0
        self.val = None

    def KthNode(self, pRoot, k):
        # write code here
        if k == 0:
            return None
        self.inorder(pRoot, k)
        return self.val

    def inorder(self, node, k):
        if not node:
            return
        self.inorder(node.left, k)
        self.cnt += 1
        if self.cnt == k:
            self.val = node
            return
        self.inorder(node.right, k)