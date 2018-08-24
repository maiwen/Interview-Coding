# -*- coding: utf-8 -*-
"""
Created on 2018/8/8 11:38

@author: vincent
题目描述
请实现两个函数，分别用来序列化和反序列化二叉树
"""


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        def walkTree(root):
            if root:
                output.append(root.val)
                walkTree(root.left)
                walkTree(root.right)
            else:
                output.append(None)

        output = []
        walkTree(root)
        return output

    def Deserialize(self, s):
        # write code here
        def walkArray(vals):
            root = None
            val = next(vals)
            if val != None:
                root = TreeNode(val)
                root.left = walkArray(vals)
                root.right = walkArray(vals)
            return root

        return walkArray(iter(s))