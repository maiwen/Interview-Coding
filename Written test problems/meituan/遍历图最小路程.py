# -*- coding: utf-8 -*-
"""
Created on 2018/9/7 13:41

@author: vincent

说给了一张包含个N个点N-1条边的无向连通图，节点从1到N编号，每条边长度均为1，设你从1号节点出发并打算遍历所有节点，那么总路程至少是多少？

输入：第一行包含一个整数N,接下来N-1行，每行包括两个整数x，y表示x与y之间有一条边
输出：总路程最小和

样例：
4
1 2
1 3
3 4

输出：4

"""
import sys
from collections import defaultdict


def get_max_depth(temp_dict):
    """得到最大深度：此时计算的深度为边的个数，


    Args:
        temp_dict (dict): 保存有节点单向连边的字典

    Returns:
        int: 最大深度
    """

    res = []
    length = 0
    for item in temp_dict[1]:
        get_depth(item, temp_dict, length, res)

    return max(res)


def get_depth(item, temp_dict, length, res):
    """取得从节点1每一个子树出发的最大深度

    Args:
        item (int): 当前节点
        temp_dict (dict): 保存有连接情况的节点
        length (int): 当前长度
        res (list): 保存有最大深度的数组
    """

    length += 1
    if not temp_dict[item]:
        res.append(length)
        return
    for item in temp_dict[item]:
        get_depth(item, temp_dict, length, res)


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())

    temp_dict = defaultdict(list)

    for i in range(n - 1):
        n1, n2 = map(int, sys.stdin.readline().strip().split())
        if n2 < n1:
            n1, n2 = n2, n1
        temp_dict[n1].append(n2)

    print(2 * (n - 1) - get_max_depth(temp_dict))

def main():
    n = int(input())
    temp = []
    for i in range(n - 1):
        line = input().split()
        line = list(map(int, line))
        temp.append(line)

    node_list = [0] * (n + 1)
    for item in temp:
        l, r = item[0], item[1]
        node_list[r] = node_list[l] + 1

    print(2 * n - 2 - max(node_list))