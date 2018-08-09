# -*- coding: utf-8 -*-
"""
Created on 2018/8/9 11:38

@author: vincent

题目描述
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""
# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0
        n = len(rotateArray)
        if n == 1:
            return rotateArray[0]
        low, high = 0, n-1
        while low < high:
            mid = low + (high-low)//2
            if rotateArray[mid] > rotateArray[mid+1]:
                return rotateArray[mid+1]
            if rotateArray[mid] > rotateArray[0]:
                low += 1
            else:
                high -= 1
        return rotateArray[0]