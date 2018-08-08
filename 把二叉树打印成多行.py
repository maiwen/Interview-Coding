# -*- coding: utf-8 -*-
"""
Created on 2018/8/8 10:42

@author: vincent

题目描述
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
"""
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        result, queue = [], []
        queue.append(pRoot)
        while queue:
            layer = []
            for i in range(len(queue)):
                node = queue.pop(0)
                layer.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(layer)
        return result