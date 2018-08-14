# -*- coding: utf-8 -*-
"""
Created on 2018/8/13 21:00

@author: vincent
题目描述
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法
"""
# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        n = len(A)
        B = [1] * n

        left = [1] * n
        left[0] = A[0]
        right = [1] * n
        right[n-1] = A[-1]

        for i in range(1, n):
            left[i] = left[i-1]*A[i]
        for i in range(n-2, -1, -1):
            right[i] = right[i+1]*A[i]

        B[0] = right[1]
        B[n-1] = left[n-2]
        for i in range(1,n-1):
            B[i] = left[i-1]*right[i+1]

        return B

class Solution1:
    def multiply(self, A):
        # write code here
        head = [1]
        tail = [1]
        for i in range(len(A) - 1):
            head.append(A[i]*head[i])
            tail.append(A[-i-1]*tail[i])
        B = []
        for j in range(len(head)):
            B.append(head[j] * tail[-j-1])
        return B