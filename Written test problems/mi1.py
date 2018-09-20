# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 18:59:51 2018

@author: Administrator

小米大礼包
时间限制：C/C++语言 1000MS；其他语言 3000MS
内存限制：C/C++语言 65536KB；其他语言 589824KB
题目描述：
小米之家是成人糖果店。里面有很多便宜，好用，好玩的产品。中秋节快到了，小米之家想给米粉们准备一些固定金额大礼包。
对于给定的一个金额，需要判断能不能用不同种产品（一种产品在礼包最多出现一次）组合出来这个金额。聪明的你来帮帮米家的小伙伴吧。

输入
输入 N （N 是正整数， N  <= 200）

输入 N 个价格p（正整数, p <= 10000）用单空格分割

输入金额 M（M是正整数，M <= 100000 ）

输出
能组合出来输出 1

否则输出 0


样例输入
6
99 199 1999 10000 39 1499
10238
样例输出
1

"""
#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re

#请完成下面这个函数，实现题目要求的功能
#当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^ 
#******************************开始写代码******************************


def miHomeGiftBag(p, M):
    p.sort()
    result = []
    def helper(start, path, xtarget):
        if xtarget == 0:
            result.append(path)
            return
        
        for i in range(start, len(p)):
            if i > start and p[i] == p[i-1]:
                continue
            if p[i] > xtarget:
                break
            helper(i+1, path+[p[i]], xtarget-p[i])
    helper(0, [], M)
    return 1 if result else 0
    


#******************************结束写代码******************************


_p_cnt = 0
_p_cnt = int(input())
_p_i=0
_p = []
_p = list(map(int,input().split()))

_M = int(input())

  
res=miHomeGiftBag(_p, _M)

print(str(int(res)) + "\n")
