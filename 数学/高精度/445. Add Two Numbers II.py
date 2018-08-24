# -*- coding: utf-8 -*-
"""
Created on 2018/7/16 18:08

@author: vincent
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

这道题是之前那道Add Two Numbers的拓展，我们可以看到这道题的最高位在链表首位置，
如果我们给链表翻转一下的话就跟之前的题目一样了，这里我们来看一些不修改链表顺序的方法。由于加法需要从最低位开始运算，
而最低位在链表末尾，链表只能从前往后遍历，没法取到前面的元素，那怎么办呢？我们可以利用栈来保存所有的元素，
然后利用栈的后进先出的特点就可以从后往前取数字了，我们首先遍历两个链表，将所有数字分别压入两个栈s1和s2中，
我们建立一个值为0的res节点，然后开始循环，如果栈不为空，则将栈顶数字加入sum中，然后将res节点值赋为sum%10，
然后新建一个进位节点head，赋值为sum/10，如果没有进位，那么就是0，然后我们head后面连上res，将res指向head，
这样循环退出后，我们只要看res的值是否为0，为0返回res->next，不为0则返回res即可，参见代码如下：

还有种方法是使用递归来实现的，我们知道递归其实也是用栈来保存每一个状态，那么也就可以实现从后往前取数字，
我们首先统计出两个链表长度，然后根据长度来调用递归函数，需要传一个参数差值，递归函数参数中的l1链表长度长于l2，
在递归函数中，我们建立一个节点res，如果差值不为0，节点值为l1的值，如果为0，那么就是l1和l2的和，
然后在根据差值分别调用递归函数求出节点post，然后要处理进位，如果post的值大于9，那么对10取余，
且res的值自增1，然后把pos连到res后面，返回res，最后回到原函数中，我们仍要处理进位情况
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1 = []
        stack2 = []
        ptr = l1
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        ptr = l2
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        result = []
        head = ListNode(-1)
        while stack1 or stack2:
            if not stack1:
                val = stack2.pop()
            elif not stack2:
                val = stack1.pop()
            else:
                val = stack1.pop() + stack2.pop()
            carry, val = divmod(carry + val, 10)
            head.val = val
            temp = head
            head = ListNode(-1)
            head.next = temp
        if carry: head.val = carry
        return head if head.val != -1 else head.next

    def addTwoNumbers1(self, l1, l2):
        if not l1 and not l2: return None
        if not l1 and l2: return l2
        if l1 and not l2: return l1

        def getlength(root):
            res = 0
            while root:
                res += 1
                root = root.next
            return res

        def addHelper(l1, l2, diff):
            if not l1 or not l2: return None, 0
            if diff > 0:
                result, carry = addHelper(l1.next, l2, diff - 1)
                sum = l1.val + carry
                node = ListNode(sum % 10)
            else:
                result, carry = addHelper(l1.next, l2.next, diff)
                sum = l1.val + l2.val + carry
                node = ListNode(sum % 10)
            node.next = result
            return node, int(sum / 10)

        n1, n2 = l1, l2

        dif = getlength(n1) - getlength(n2)

        if dif < 0:
            res, carry = addHelper(l2, l1, abs(dif))
        else:
            res, carry = addHelper(l1, l2, dif)

        if carry:
            newres = ListNode(carry)
            newres.next = res
            return newres
        return res