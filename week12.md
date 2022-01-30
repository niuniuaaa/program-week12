# week12

## leetcode111、leetcode114、leetcode124、commonsequence、maxarray、stairway

### leetcode111

1.层次遍历：首先用pop函数定位root节点，再利用层序遍历原理遍历每一层，

2.用变量i记录当前层数，当遇到叶子结点时则返回当前层数。

### leetcode124

定义一个辅助函数返回两个值：
 1.只包含一个方向（左右）的最大路径
 2.包含两个方向（左和右）的最大路径
 由于至少包含一个节点，所以如果ls和rs都是0时，必须包含当前节点，total取局部最大值。但也是必须要包含节点的

### commonsequence

1.序列a共同拥有m个元素，序列b共同拥有n个元素，假设a[m-1]==b[n-1]，那么a[:m]和b[:n]的最长公共子序列长度就是a[:m-1]和b[:n-1]的最长公共子序列长度+1；假设a[m-1]!=b[n-1]，那么a[:m]和b[:n]的最长公共子序列长度就是MAX（a[:m-1]和b[:n]的最长公共子序列长度，a[:m]和b[:n-1]的最长公共子序列长度）。

2.![image-20220130102756277](C:\Users\26977\AppData\Roaming\Typora\typora-user-images\image-20220130102756277.png)

3.依据计算最优值得到的信息，构造最优解

### maxarray

A[low…high]的任意连续子数组A[i…j]所处的位置必然是以下三种情况之一：

（a）完全位于子数组A[low…mid]中，因此low≤i≤j≤mid

（b）完全位于子数组A[mid+1…high]中，因此mid≤i≤j≤high

（c）跨越了中点，因此low≤i≤mid≤j≤high

分别找它们中的最大子数组就好了

### stairway

上第I级台阶的方法总共有两大种，第一种是从第（i-1）级台阶上跨一级，第二种则是从第（I-2）级台阶上跨两级，除此并无他法，由于这个上楼方法从（i-1）和（i-2）级各只有一种方法，那么上第i级台阶的总的方法和数就是上前两级台阶的方法总和数
