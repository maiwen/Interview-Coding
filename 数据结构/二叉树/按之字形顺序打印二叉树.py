# -*- coding: utf-8 -*-
"""
Created on 2018/8/8 10:51

@author: vincent
题目描述
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
"""
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        result, queue = [], []
        queue.append(pRoot)
        s = 0
        while queue:
            layer = []
            for i in range(len(queue)):
                node = queue.pop(0)
                layer.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if s%2 ==0:
                result.append(layer)
            else:
                result.append(layer[::-1])
            s += 1
        return result