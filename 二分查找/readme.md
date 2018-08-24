针对已排序的数组
从中间值开始查找，
若中间值大于目标值，则 low = mid + 1
若中间值小于目标值，则 high = mid
循环直到 low = high

二分查找算法虽然简单，但面试中也比较常见，经常用来在有序的数列查找某个特定的位置。在LeetCode用到此算法的主要题目有：
Search Insert Position
Search for a Range
Sqrt(x)
Search a 2D Matrix
Search in Rotated Sorted Array
Search in Rotated Sorted Array II

这类题目基本可以分为如下四种题型：
1. Search Insert Position和Search for a Range是考察二分查找的基本用法。基本思路是每次取中间，如果等于目标即返回，否则根据大小关系切去一半，因此时间复杂度是O(logn)，空间复杂度O(1)。以Search Insert Position为例，其关键代码写法如下：
    int l = 0;
    int r = A.length-1;
    while(l<=r)
    {
        int mid = (l+r)/2;
        if(A[mid]==target)
            return mid;
        if(A[mid]<target)
            l = mid+1;
        else
            r = mid-1;
    }
    return l;
这样当循环停下来时，如果不是正好找到target，l指向的元素恰好大于target，r指向的元素恰好小于target，这里l和r可能越界，不过如果越界就说明大于（小于）target并且是最大（最小）。Search for a Range这道题能更好的解释这一点。其思路是先用二分查找找到其中一个target，然后再往左右找到target的边缘。我们主要看找边缘（往后找）的代码：
    int newL = m;
    int newR = A.length-1;
    while(newL<=newR)
    {
        int newM=(newL+newR)/2;
        if(A[newM]==target)
        {
            newL = newM+1;
        }
        else
        {
            newR = newM-1;
        }
    }
    res[1]=newR;
我们的目标是在后面找到target的右边界，因为左边界已经等于target，所以判断条件是相等则向右看，大于则向左看，根据上面说的，循环停下来时，l指向的元素应该恰好大于target，r指向的元素应该等于target，所以此时的r正是我们想要的。向前找边缘也同理。

2. Sqrt(x)是数值处理的题目，但同时也可以用二分查找的思想来解决。因为我们知道结果的范围，取定左界和右界，然后每次砍掉不满足条件的一半，直到左界和右界相遇。算法的时间复杂度是O(logx)，空间复杂度是O(1)。这里同样是考察二分查找的基本用法。代码如下：
public int sqrt(int x) {
    if(x<0) return -1;
    if(x==0) return 0;
    int l=1;
    int r=x/2+1;
    while(l<=r)
    {
        int m = (l+r)/2;
        if(m<=x/m && x/(m+1)<m+1)
            return m;
        if(x/m<m)
        {
            r = m-1;
        }
        else
        {
            l = m+1;
        }
    }
    return 0;
}
这里要注意，这里判断相等的条件不是简单的 m == x/m, 而是 m<=x/m && x/(m+1)<m+1, 这是因为输出是整型，sqrt(14)=3 但 3 != 14/3. 所以我们需要一个范围框住结果。另外根据二分查找算法的特性，如果不能正好m==x/m停下，那么r指向的数字将正好是结果取整的值。所以我们也可以这样写：
public int sqrt(int x) {
    if(x<0) return -1;
    if(x==0) return 0;
    int l=1;
    int r=x/2+1;
    while(l<=r)
    {
        int m = (l+r)/2;
        if(m==x/m )
            return m;
        if(x/m<m)
        {
            r = m-1;
        }
        else
        {
            l = m+1;
        }
    }
    return r;
}
3. Search a 2D Matrix是二分查找算法的多维应用，通过观察不难发现，输入的矩阵行内有序并且行间有序，所以查找只需要先按行查找，定位出在哪一行之后再进行列查找即可，两次二分查找，时间复杂度是O(logm+logn)，空间上只需两个辅助变量，因而是O(1)，这里不再赘述。

4. Search in Rotated Sorted Array和Search in Rotated Sorted Array II算是二分查找算法的一个变体。
在Search in Rotated Sorted Array中，乍一看感觉数组已经不是有序的了，也就无法用二分查找算法，但仔细分析一下会发现，
因为只rotate了一次，如果二分一下，总有一半是有序的，而且和另一半无区间重叠，我们只需要检查有序的一半的前后两个元素就可以确定target可能在哪一半。
具体来说，假设数组是A，每次左边缘为l，右边缘为r，还有中间位置是m。在每次迭代中，分三种情况：
（1）如果target==A[m]，那么m就是我们要的结果，直接返回；
（2）如果A[m]<A[r]，那么说明从m到r一定是有序的（没有受到rotate的影响），那么我们只需要判断target是不是在m到r之间，如果是则把左边缘移到m+1，
否则就target在另一半，即把右边缘移到m-1。
（3）如果A[m]>=A[r]，那么说明从l到m一定是有序的，同样只需要判断target是否在这个范围内，相应的移动边缘即可。
根据以上方法，每次我们都可以切掉一半的数据，所以算法的时间复杂度是O(logn)，空间复杂度是O(1)。
Search in Rotated Sorted Array II中array有重复元素，按照刚刚的思路，二分之后虽然一半是有序的，但我们会遇到中间和边缘相等的情况，
我们就丢失了哪边有序的信息，因为哪边都有可能是有序的结果。假设原数组是{1,2,3,3,3,3,3}，那么旋转之后有可能是{3,3,3,3,3,1,2}，
或者{3,1,2,3,3,3,3}，这样的我们判断左边缘和中心的时候都是3，如果我们要寻找1或者2，我们并不知道应该跳向哪一半。
解决的办法只能是对边缘移动一步，直到边缘和中间不在相等或者相遇，这就导致了会有不能切去一半的可能。
所以最坏情况（比如全部都是一个元素，或者只有一个元素不同于其他元素，而他就在最后一个）就会出现每次移动一步，总共是n步，算法的时间复杂度变成O(n)。

总体来说，二分查找算法理解起来并不算难，但在实际面试的过程中可能会出现各种变体，如何灵活的运用才是制胜的关键。我们要抓住“有序”的特点，一旦发现输入有“有序”的特点，我们就可以考虑是否可以运用二分查找算法来解决该问题。

