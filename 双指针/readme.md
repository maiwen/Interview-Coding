# 一. 首尾指针
两个指针一般是在有序数组中使用，一个放首，一个放尾，同时向中间遍历，直到两个指针相交，完成遍历，时间复杂度也是O(n)。

用法

一般会有两个指针front,tail。分别指向开始和结束位置。
  front = 0;
  tail = A.length()-1

一般循环结束条件采用的是判断两指针是否相遇
  while(fron < tail)
  {
  ……
  }

对于in place交换的问题，循环结束条件一般就是其中一个指针遍历完成。
使用范围
一般双指针在有序数组中使用的特别多。（部分情况下，未排序数组也有应用） 一般用来解决下列问题（陆续补充中）：
1. 两数求和
一般这种问题是问，寻找两个数的和为一个特定的值（比如后面的N SUM问题），这时候，如果数组有序，我们采用两个指针，分别从前和后往中间遍历，
front移动和增大，tail移动和减小，通过特定的判断，可以求出特定的和。
时间复杂度为O(n),如果用双重循环则要O(n^2)。
2. in place交换
数组的in place(就地)交换一般得用双指针，不然数组中添加或删除一个元素，需要移动大量元素。

这时候，一般是一个指针遍历，一个指针去找可以用来交换的元素。

# 二. 快慢指针


１概念
双指针：快慢指针。
快指针在每一步走的步长要比慢指针一步走的步长要多。快指针通常的步速是慢指针的2倍。

在循环中的指针移动通常为：
faster = faster.next.next; slower = slower.next;

2 应用
2.1. 用来判断链表是否有环以及寻找环入口
Linked List Cycle
Linked List Cycle II
是否有环：快慢指针思想，注意循环条件：(fast != null) && (fast.next != null)

寻找环的入口：快慢指针相遇的时候，distance(fast指针) = 2 * distance(slow指针)，可以推导出，只要把fast重新指向头结点，两个指针以一样的速度走，相遇的时候，便是环的入口。

2.2.数组寻找范围
Summary Ranges
范围的寻找，用2个指针:start ，end来记录范围。注意循环条件和判断条件：(end + 1 < len) && (nums[end + 1] == nums[end] + 1)

2.3.链表或者数组中移除重复的元素
Remove Duplicates from Sorted List I
Remove Duplicates from Sorted List II
Sorted List I用两个指针一前一后指向链表。维护两个指针:

tail 一个指向当前不重复的最后一个元素，
pCur 一个进行依次扫描，遇到不重复的则更新第一个指针，继续扫描，否则就把前面指针指向当前元素的下一个（即把当前元素从链表中删除）。
Sorted List II 维护两个指针：

prev前驱指针指向上一个不重复的元素
pCur遍历指针
思路类似Sorted List I，细节更多。
寻找不重复的元素 while循环条件pCur.next != null && prev.next.val == pCur.next.val
Array数组中的解题思想一样：

index指向上当前不重复的最后一个元素
i遍历数组
2.4. 用来找中点或中位数
2.5. 倒数第n个
题目中含有：倒数第n个，那么设置快指针步长为n，然后快慢指针同时以同一速度走，用慢指针寻找倒数第n个

2.6. 拆分链表
Partition List
给定一个x的值，小于x都放在大于等于x的前面，并且不改变链表之间node原始的相对位置。example中 4->3->5都是大于等3的数，这保持了他们原来的相对位置。

使用链表最常用的双指针：

一个指向当前小于x的最后一个元素
一个进行往前扫描。如果元素大于x，那么继续前进，否则，要把元素移到前面，并更新第一个指针。
Reorder List
思路：
1.利用快慢两个指针将链表一分为二；
2.针对第二个子链表求倒序；
3.利用merge思想将两个子链表合并。

3 相关题目
Summary Ranges
Linked List Cycle
Linked List Cycle II
Remove Duplicates from Sorted List I
Remove Duplicates from Sorted List II
Remove Duplicates from Sorted Array I
Remove Duplicates from Sorted Array II
Partition List
Intersection of Two Linked Lists
Remove Nth Node From End of List
Reorder List
Delete Node in a Linked List
4 注意
通常需要特别留意链表长度的奇偶性
如果快指针步速为慢指针步速2倍，循环条件为：faster.next!=null && faster.next.next!=null
当自行设置快指针步长时， 要考虑步长值等于链表长度的特殊情况
查找倒数第n个时，如果要求删除链表元素时，不要忘记记录应被删除元素的前一个元素
对于链表的题目，常常都会用到Two Pointers的思想。链表注意构建dummy头结点。在Java中，由于没有free函数，所以在删除一个节点的时候，无法用node = null来删除一个节点，需要用前一个节点来指向删除节点的下一个prev.next = node.next这样来删除node节点。