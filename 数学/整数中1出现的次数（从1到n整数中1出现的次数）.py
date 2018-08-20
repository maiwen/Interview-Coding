# -*- coding: utf-8 -*-
"""
Created on 2018/8/11 22:24

@author: vincent
题目描述
从1 到 n 中1出现的次数

主要思想是，把数拆成两部分，枚举各个位置，比如上面提到的133，枚举10位上有多少个1就是将其除以10和对10取模得到13和3左右两部分，
接着，要看十位上可以组成多少个1，因为十位数上是3，比1大，说明十位上为1的都满足，则一共可以有20个。01X和11X啊。

再比如，113，通用举十位上的例子，11和3，因为十位数上的为1，只能满足01X的数，剩下的有4个。 就是余数（右部分）+1的结果

代码中用(x+8) / 10 实现了大于等于2的判断，十分巧妙。
"""
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        ans, k = 0, 1
        while k <= n:
            x, r = n / k, n % k
            ans += (x + 8) / 10 * k + ((r + 1) if x % 10 == 1 else 0)
            k *= 10
        return ans