遍历树的数据结构中最常见的操作， 可以说大部分关于树的题目都是围绕遍历进行变体来解决的。 一般来说面试中遇到树的题目是用递归来解决的， 不过如果直接考察遍历， 那么一般递归的解法就过于简单了， 面试官一般还会问更多问题， 比如非递归实现， 或者空间复杂度分析以及能否优化等等。 树的遍历题目在LeetCode中有以下几个： 

Binary Tree Inorder Traversal
Binary Tree Preorder Traversal
Binary Tree Postorder Traversal
Binary Tree Level Order Traversal
Binary Tree Level Order Traversal II
Binary Tree Zigzag Level Order Traversal

树的遍历基本上分成两种类型， 下面分别介绍： 

第一种是以图的深度优先搜索为原型的遍历， 可以是中序， 先序和后序三种方式， 不过结点遍历的方式是相同的， 只是访问的时间点不同而已， 对应于Binary Tree Inorder Traversal， Binary Tree Preorder Traversal和Binary Tree Postorder Traversal这三道题目。 
在这种类型中， 递归的实现方式是非常简单的， 只需要递归左右结点， 直到结点为空作为结束条件就可以， 哪种序就取决于你访问结点的时间。 
不过一般这不能满足面试官的要求， 可能会接着问能不能用非递归实现一下， 这个说起来比较简单， 其实就是用一个栈手动模拟递归的过程， Binary Tree Inorder Traversal和Binary Tree Preorder Traversal比较简单， 用一个栈来保存前驱的分支结点（相当于图的深度搜索的栈）， 然后用一个结点来记录当前结点就可以了。 而Binary Tree Postorder Traversal则比较复杂一些， 保存栈和结点之后还得根据情况来判断当前应该走的方向（往左， 往右或者回溯）。 这里就不列举代码细节， 有兴趣的朋友可以看看具体题目的分析， 会更详细一些。 
有时候非递归还是不能满足面试官， 还会问一问， 上面的做法时间和空间复杂度是多少。 我们知道， 正常遍历时间复杂度是O(n), 而空间复杂度是则是递归栈（或者自己维护的栈）的大小， 也就是O(logn)。 好了， 他会问能不能够在常量空间内解决树的遍历问题呢？ 确实还真可以， 这里就要介绍Morris Traversal的方法。 Morris遍历方法用了线索二叉树，这个方法不需要为每个节点额外分配指针指向其前驱和后继结点，而是利用叶子节点中的右空指针指向中序遍历下的后继节点就可以了。 这样就节省了需要用栈来记录前驱或者后继结点的额外空间， 所以可以达到O（1）的空间复杂度。 不过这种方法有一个问题就是会暂时性的改动树的结构， 这在程序设计中并不是很好的习惯， 这些在面试中都可以和面试官讨论， 一般来说问到这里不会需要进行Morris遍历方法的代码实现了， 只需要知道这种方法和他的主要优劣势就可以了， 有兴趣知道实现的朋友可以看看具体题目的实现哈。 

另一种是以图的广度优先搜索为原型的， 在树中称为层序遍历， LeetCode中有三种自顶向下层序， 自底向上层序和锯齿层序遍历， 对应于Binary Tree Level Order Traversal， Binary Tree Level Order Traversal II和Binary Tree Zigzag Level Order Traversal。 
Binary Tree Level Order Traversal其实比较简单， 代码基本就是图的广度优先搜索， 思路就是维护一个队列存储上一层的结点， 逐层访问。 而Binary Tree Level Order Traversal II则要从最后一层倒序访问上来， 这个我没有想到太好的方法， 现在的实现就是把Binary Tree Level Order Traversal得到的层放入数据结构然后reverse过来， 确实没有太大的考核意义。 至于Binary Tree Zigzag Level Order Traversal因为每一层访问顺序有所改变， 而且是每次都反转顺序， 这让我们想到栈的数据结构， 所以这里不用队列对于上层结点进行， 而改用栈来保存， 就可以满足每层反转访问顺序的要求了。 

树的遍历是一个老生常谈的题目， 不过仔细研究还是有一些考点的， 对于考查对数据结构和算法的理解还是不错的， 所以简单的东西也得重视哈。