# -*- coding: utf-8 -*-
"""
Created on 2018/7/11 9:43

@author: vincent
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0: return 0
        dp = [0] * n
        dp[0] = 1 if s[0] != '0' else 0
        for i in range(1,n):
            if s[i] == '0':
                if 10 <= int(s[i-1:i+1]) <= 26:
                    dp[i] = dp[i-2] if i >= 2 else 1
                else:
                    return 0
            else:
                dp[i] = dp[i-1]
                if 10 <= int(s[i-1:i+1]) <= 26:
                    dp[i] += dp[i-2] if i >= 2 else 1
        return dp[-1]