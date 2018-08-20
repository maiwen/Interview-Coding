# -*- coding: utf-8 -*-
"""
Created on 2018/8/9 22:11

@author: vincent

题目描述
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
"""
# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1
        for char in s:
            if s.count(char) == 1:
                return s.index(char)
        return -1

class Solution1:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1
        d = {}
        for char in s:
            if char in d.keys():
                d[char] += 1
            else:
                d[char] = 1
        for i,char in enumerate(s):
            if d[char] == 1:
                return i
        return -1