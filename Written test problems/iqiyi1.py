# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 11:34:08 2018

@author: Administrator

幸运ID
时间限制：C/C++语言 1000MS；其他语言 3000MS
内存限制：C/C++语言 131072KB；其他语言 655360KB
题目描述：
小C有一张票，这张票的ID是长度为6的字符串，每个字符都是数字，他想让这个ID变成他的辛运ID，所以他就开始更改ID，每一次操作，他可以选择任意一个数字并且替换它。

如果这个ID的前三位数字之和等于后三位数字之和，那么这个ID就是辛运的。你帮小C求一下，最少需要操作几次，能使ID变成辛运ID

输入
输入只有一行，是一个长度为6的字符串。

输出
输出这个最小操作次数


样例输入
000000
样例输出
0

输入样例2
000018

输出样例2
1

样例解释：将前三位任意一个改为9即可满足条件，操作数为1
"""
s = input()
data = []
for num in s:
    data.append(int(num))
s, l, e = 0, 0, sum(data[:3]) - sum(data[3:])
temp = e
if e == 0:
    print(0)
else:
    if e > 0:
        large = sorted(data[:3])
        small = sorted(data[3:])
    else:
        large = sorted(data[3:])
        small = sorted(data[:3])
    for n in large[::-1]:
        if e <= n:
            l += 1
            break
        else:
            e -= n
    e = temp
    for n in small:
        if n + e <= 9:
            s += 1
            break
        else:
            e = 9 - n
    print(min(s,l))
    
    









