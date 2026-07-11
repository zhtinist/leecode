"""
LeetCode #558 - Logical OR of Two Binary Grids Represented as Quad-Trees
中文题名：四叉树交集
https://leetcode.com/problems/logical-or-of-two-binary-grids-represented-as-quad-trees/

A quadtree is a tree data in which each internal node has exactly four children: `topLeft`,
`topRight`, `bottomLeft` and `bottomRight`. Quad trees are
often used to partition a two-dimensional space by recursively subdividing it into four
quadrants or regions.

We want to store True/False information in our quad tree. The quad tree is used to represent
a `N * N` boolean grid. For each node, it will be subdivided into four children
nodes until the values in the region it represents are all the same. Each
node has another two boolean attributes : `isLeaf` and `val`. `isLeaf`
is true if and only if the node is a leaf node. The `val` attribute for a leaf
node contains the value of the region it represents.

For example, below are two quad trees A and B:

A:
+-------+-------+   T: true
|       |       |   F: false
|   T   |   T   |
|       |       |
+-------+-------+
|       |       |
|   F   |   F   |
|       |       |
+-------+-------+
topLeft: T
topRight: T
bottomLeft: F
bottomRight: F

B:
+-------+---+---+
|       | F | F |
|   T   +---+---+
|       | T | T |
+-------+---+---+
|       |       |
|   T   |   F   |
|       |       |
+-------+-------+
topLeft: T
topRight:
topLeft: F
topRight: F
bottomLeft: T
bottomRight: T
bottomLeft: T
bottomRight: F

Your task is to implement a function that will take two quadtrees and return a quadtree that
represents the logical OR (or union) of the two trees.

A:                 B:                 C (A or B):
+-------+-------+  +-------+---+---+  +-------+-------+
|       |       |  |       | F | F |  |       |       |
|   T   |   T   |  |   T   +---+---+  |   T   |   T   |
|       |       |  |       | T | T |  |       |       |
+-------+-------+  +-------+---+---+  +-------+-------+
|       |       |  |       |       |  |       |       |
|   F   |   F   |  |   T   |   F   |  |   T   |   F   |
|       |       |  |       |       |  |       |       |
+-------+-------+  +-------+-------+  +-------+-------+

Note:

Both `A` and `B` represent grids of size `N * N`.

`N` is guaranteed to be a power of 2.

If you want to know more about the quad tree, you can refer to its wiki.

The logic OR operation is defined as this: "A or B" is true if `A is
true`, or if `B is true`, or if `both A and B are true`.

【中文翻译】
四叉树是一种树数据结构，其中每个内部节点恰好有四个子节点：topLeft、topRight、bottomLeft
和 bottomRight。四叉树常用于通过递归地将空间划分为四个象限或区域来划分二维空间。

我们想在四叉树中存储 True/False 信息。四叉树用于表示一个 N×N 的布尔网格。对于每个节点，
它会被细分为四个子节点，直到其所代表区域内的值全部相同。每个节点还有两个布尔属性：isLeaf
和 val。当且仅当节点是叶子节点时 isLeaf 为 true。叶子节点的 val 属性包含其所代表区域的值。

你的任务是实现一个函数，接受两个四叉树并返回一个表示两棵树逻辑 OR（或并集）的四叉树。

注意：
    A 和 B 都表示大小为 N×N 的网格。
    N 保证是 2 的幂。
    逻辑 OR 操作定义为："A or B" 为 true，如果 A 为 true，或 B 为 true，或 A 和 B 都为 true。
"""

from typing import List, Optional


# Definition for a QuadTree node.
class Node:
    def __init__(self, val: bool, isLeaf: bool, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        # 如果 quadTree1 是叶子且值为 True，OR 结果就是 True 的叶子
        if quadTree1.isLeaf:
            return quadTree1 if quadTree1.val else quadTree2

        # 如果 quadTree2 是叶子且值为 True，OR 结果就是 True 的叶子
        if quadTree2.isLeaf:
            return quadTree2 if quadTree2.val else quadTree1

        # 两者都不是叶子：递归合并四个象限
        tl = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        tr = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bl = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        br = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)

        # 如果四个子节点都是叶子且值相同，则合并为单个叶子节点
        if (tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and
                tl.val == tr.val == bl.val == br.val):
            return Node(val=tl.val, isLeaf=True)

        return Node(val=True, isLeaf=False, topLeft=tl, topRight=tr,
                    bottomLeft=bl, bottomRight=br)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 递归合并两棵四叉树。终止条件：若一棵树是值为 True 的叶子，直接返回该叶子（OR 结果为 True）；
# 若一棵树是值为 False 的叶子，返回另一棵树（相当于 OR 中忽略 False）。
# 递归处理四个子象限后，检查是否可以压缩：若四个子节点都是叶子且值全相同，则合并为一个叶子节点。
#
# 时间复杂度: O(N^2) — 其中 N 是网格边长，最坏情况需遍历所有格子
# 空间复杂度: O(log N) — 递归栈深度等于四叉树的高度
#
# 关键点:
# - 正确处理叶子节点的提前返回（True 叶子短路、False 叶子忽略）
# - 递归后检查四个子节点是否可以合并（压缩优化）
# - 四叉树的 OR 操作在逻辑上等价于逐格 OR
