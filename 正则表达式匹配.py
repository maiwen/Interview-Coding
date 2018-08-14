# -*- coding: utf-8 -*-
"""
Created on 2018/8/14 22:22

@author: vincent
题目描述
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
"""
# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        # write code here
        ###当模式中的第二个字符不是&quot;*&quot;时
        # 1、如果字符串第一个字符和模式中的第一个字符匹配(相等或匹配到&quot;.&quot;)，
        #    那么字符串和模式都后移一个字符，然后匹配剩余的
        # 2、如果字符串第一个字符和模拟中的第一个字符相不匹配，直接返回false
        ###而当模式中的第二个字符是&quot;*&quot;时
        # 如果字符串和第一个字符不匹配，则模式后移两个字符，继续匹配。
        # 如果字符串第一个字符跟模式第一个字符匹配(相等或匹配到&quot;.&quot;)，可以有3中匹配方式：
        # 1、模式后移2字符，相当于X*被忽略；
        # 2、字符串后移1字符，模式后移两字符；
        # 3、字符串后移1字符，模式不变，即继续匹配字符下一位，因为*可以匹配多位
        if len(s)==0 and len(pattern)==0:
            return True
        if len(s) !=0 and len(pattern) == 0:
            return False
        if len(pattern) > 1 and pattern[1] == '*':  # 当模式的第二个字符是‘*’时
            if len(s) > 0 and (pattern[0] == s[0] or pattern[0]== '.'):
                return self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern)
            else:
                return self.match(s, pattern[2:])
        if len(s) > 0 and (pattern[0] == s[0] or pattern[0]== '.'):
            return self.match(s[1:],pattern[1:])
        return False