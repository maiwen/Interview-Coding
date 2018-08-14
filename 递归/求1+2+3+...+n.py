# -*- coding: utf-8 -*-
"""
Created on 2018/8/14 19:36

@author: vincent
题目描述
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
"""
# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        return n > 0 and n + self.Sum_Solution(n-1)