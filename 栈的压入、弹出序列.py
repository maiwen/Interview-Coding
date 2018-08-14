# -*- coding: utf-8 -*-
"""
Created on 2018/8/14 11:25

@author: vincent
题目描述
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，
序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
"""
# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if set(pushV) != set(popV):
            return False
        else:
            if len(pushV) < 2:
                return True
            index = pushV.index(popV.pop(0))
            left = pushV[:index]
            right = pushV[index+1:]
            for num in right:
                popV.pop(popV.index(num))
            if list(reversed(left)) == popV:
                return True
            else:
                return False

# -*- coding:utf-8 -*-
class Solution1:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack = []
        for num in pushV:
            stack.append(num)
            while stack and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        return len(popV) == 0