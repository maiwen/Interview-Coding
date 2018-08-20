# -*- coding: utf-8 -*-
"""
Created on 2018/8/6 21:29

@author: vincent
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。
输入描述:
输入一个字符串,包括数字字母符号,可以为空
输出描述:
如果是合法的数值表达则返回该数字，否则返回0
示例1
输入
复制
+2147483647
    1a33
输出
复制
2147483647
    0
"""
# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        s = s.lstrip()
        if not s:
            return 0
        result = ''
        digits = ['1','2','3','4','5','6','7','8','9','0']
        signs = ['+','-']
        for i in range(len(s)):
            if i == 0:
                if s[i] in digits or s[i] in signs:
                    result += s[i]
                else:
                    return 0
            else:
                if s[i] in digits:
                    result += s[i]
                else:
                    return 0
        if len(result) == 1 and result in signs:
            return 0
        result = int(result)
        return result