这篇总结主要介绍树中比较常见的一类题型--树的构造。其实本质还是用递归的手法来实现，但是这类题目有一个特点，就是它是构建一棵树，而不是给定一棵树，然后进行遍历，所以实现起来思路上有点逆向，还是要练习一下。LeetCode中关于树的构造的题目有以下几道：

Convert Sorted Array to Binary Search Tree
Convert Sorted List to Binary Search Tree
Construct Binary Tree from Preorder and Inorder Traversal
Construct Binary Tree from Inorder and Postorder Traversal

先来看看最简单的Convert Sorted Array to Binary Search Tree，数组本身是有序的，那么我们知道每次只要取中点作为根，然后递归构建对应的左右子树就可以了，递归的写法跟常规稍有不同，就是要把根root先new出来，然后它的左节点接到递归左边部分的返回值，右节点接到递归右边部分的返回值，最后将root返回回去。这个模板在树的构造中非常有用，其他几道题也都是按照这个来实现。

接下来是Convert Sorted List to Binary Search Tree，这个跟Convert Sorted Array to Binary Search Tree比较近似，区别是元素存储的数据结构换成了链表，不过引入了一个重要的问题，就是链表的访问不是随机存取的，也就是不是O(1)的，如果每次去获取中点，然后进行左右递归的话，我们知道得到中点是O(n/2)=O(n)的，如此递推式是T(n) = 2T(n/2)+n/2，复杂度是O(nlogn)，并不是线性的，所以这里我们就得利用到树的中序遍历了，按照递归中序遍历的顺序对链表结点一个个进行访问，而我们要构造的二分查找树正是按照链表的顺序来的。如此就能按照链表的访问顺序来构造，不会因此而增加找中间结点的复杂度。

最后是Construct Binary Tree from Preorder and Inorder Traversal和Construct Binary Tree from Inorder and Postorder Traversal，这个方法还是跟上面的题目一样来构造，主要问题是如何将节点劈成左右两部分进行递归，Construct Binary Tree from Preorder and Inorder Traversal就是利用前序遍历跟一定在第一个，而中序遍历又可以根据根来把元素劈成两块，类似的Construct Binary Tree from Inorder and Postorder Traversal是根据后序遍历最后一个是根的特点，然后利用中序遍历劈块，原理是一样的，最后的实现大家可以参考一下代码。

这篇总结主要介绍了LeetCode中四个树的构造的题目，比较统一的思路就是在递归中创建根节点，然后找到将元素劈成左右子树的方法，递归得到左右根节点接上创建的根然后返回。方法还是比较具有模板型的，不熟悉的朋友可以练习一下哈。