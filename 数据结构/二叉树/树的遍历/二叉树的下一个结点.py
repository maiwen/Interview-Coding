# -*- coding: utf-8 -*-
"""
Created on 2018/8/8 10:14

@author: vincent
题目描述
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
"""


# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return None
        target = pNode
        while pNode.next:
            pNode = pNode.next
        self.result = []
        self.inorder(pNode)
        return self.result[self.result.index(target) + 1] if self.result.index(target) != len(self.result) - 1 else None

    def inorder(self, root):
        if not root:
            return None
        self.inorder(root.left)
        self.result.append(root)
        self.inorder(root.right)