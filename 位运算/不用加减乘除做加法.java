# -*- coding: utf-8 -*-
"""
Created on 2018/8/14 19:32

@author: vincent
题目描述
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
"""
public class Solution {
    public int Add(int num1,int num2) {
        return num2 == 0 ? num1 : Add((num1 ^ num2), (num1 & num2) << 1);
    }
}