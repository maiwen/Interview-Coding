# -*- coding: utf-8 -*-
"""
Created on 2018/8/8 21:22

@author: vincent

用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

链接：https://www.nowcoder.com/questionTerminal/54275ddae22f475981afa2244dd448c6?commentTags=Python
来源：牛客网

python中，以列表定义两个栈，append()则为在尾部加上一个值，pop()则为在尾部删除一个值，相当于栈的后进先出了。需要完成队列的先进先出。两个栈为stackA和stackB，对于队列的实现来说，stackA负责装入数据，stackB负责弹出数据。
两个方法，push()和pop()。
push()直接在stackA末尾加值就好了。
pop()分为三种情况：
1、若stackB不为空，则直接stackB.pop()完事
2、若stackB为空，stackA也为空，就意味着队列没数据了，返回空
3、若stackB为空，stackA不为空，这里是重点，stackB逐个添加stackA逐个弹出的数据，这时改变了数据的顺序。

class Solution:
    def __init__(self):
        self.stackA = []
        self.stackB = []
    def push(self, node):
        self.stackA.append(node)
    def pop(self):
        if self.stackB:
            return self.stackB.pop()
        elif self.stackA == []:
            return None
        else:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()
"""
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.queue = []
    def push(self, node):
        # write code here
        self.queue.append(node)
    def pop(self):
        # return xx
        return self.queue.pop(0)