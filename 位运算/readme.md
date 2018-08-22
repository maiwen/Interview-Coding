
x ^ 0s = x      x & 0s = 0      x | 0s = x
x ^ 1s = ~x     x & 1s = x      x | 1s = 1s
x ^ x = 0       x & x = x       x | x = x

* n&(n-1) 去除 n 的位级表示中最低的那一位。
* n&(-n) 得到 n 的位级表示中最低的那一位。
不用额外变量交换两个整数:

a = a ^ b;
b = a ^ b;
a = a ^ b;
