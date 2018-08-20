# -*- coding: utf-8 -*-
"""
Created on 2018/8/14 16:09

@author: vincent
"""
# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        s=s.lstrip()
        if len(s)==0: return 0
        res=''
        digits=['1','2','3','4','5','6','7','8','9','0','.']
        signs=['+','-']
        sciences = ['E','e']
        science = False
        for i in range(len(s)):
            if i==0:
                if(s[i] in digits or s[i] in signs):
                    res=s[i]
                else:
                    return 0
            else:
                if s[i] in sciences:
                    science = True
                if science:
                    if s[i] == '.':
                        return 0
                if s[i] in digits or s[i] in sciences or (s[i] in signs and s[i-1] in sciences):
                    res=res+s[i]
                else:
                    return 0
        if res.count('.') > 1 or (res.count('e')+res.count('E')) > 1 or res[-1] in sciences:
            return 0
        if len(res)==1 and (res in signs or res in sciences or res[0] == '.'):
            return 0
        else:
            return 1