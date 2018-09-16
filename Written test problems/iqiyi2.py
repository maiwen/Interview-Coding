# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 11:10:45 2018

@author: Administrator

局长的食物
时间限制：C/C++语言 1000MS；其他语言 3000MS
内存限制：C/C++语言 131072KB；其他语言 655360KB
题目描述：
局长有N种食物，每种食物有Ai份。

每天局长会吃一份食物，或者买一份食物（即每天只能进行吃或买其中的一种动作），这样过了M天

现在局长想知道M天后第p种食物的份数排名（从大到小，相同算并列，例如3 3 2，则排名为1 1 3）

N,M,P<=100,Ai<=1000

输入
第一行N M P

第二行N个数Ai

接下来M行，每行A i或者B i分别表示买一份食物i，吃一份食物i

输出
一个答案


样例输入
3 4 2
5 3 1
B 1
A 2
A 2
A 3
样例输出
1
"""


N, M, P = map(int,input().split())
A = list(map(int,input().split()))
for i in range(M):
    data = input().split()
    if not data:
        break
    if data[0] == 'A':
        A[int(data[1])-1] += 1
    else:
        A[int(data[1])-1] -= 1
key = A[P - 1]
ans = 1
for num in A:
    if num > key:
        ans += 1
print(ans)
