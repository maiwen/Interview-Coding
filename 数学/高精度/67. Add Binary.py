# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 20:03:47 2018

@author: Administrator

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

使用一个变量c同时解决本位结果和本位进位，c本身有4种可能的值：0，1，2，3，c％2就是本位结果，c/2就是本位进位；
当i，j都进行完时，如果c还等于1，那就意味着要多一个最高位，while循环同时也能处理这种情况。

python: Time Limit Exceeded
"""

class Solution {
    public String addBinary(String a, String b) {
    int i = a.length() - 1, j = b.length() - 1, carry = 0;
    StringBuilder str = new StringBuilder();
    while (carry == 1 || i >= 0 || j >= 0) {
        if (i >= 0 && a.charAt(i--) == '1') {
            carry++;
        }
        if (j >= 0 && b.charAt(j--) == '1') {
            carry++;
        }
        str.append(carry % 2);
        carry /= 2;
    }
    return str.reverse().toString();
}
}