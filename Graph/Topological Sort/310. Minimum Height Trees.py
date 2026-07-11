"""
LeetCode #310 - Minimum Height Trees
中文题名：最小高度树
https://leetcode.com/problems/minimum-height-trees/

For an undirected graph with tree characteristics, we can choose any node as the root. The
result graph is then a rooted tree. Among all possible rooted trees, those with minimum
height are called minimum height trees (MHTs). Given such a graph, write a function to find
all the MHTs and return a list of their root labels.

Format

The graph contains `n` nodes which are labeled from `0` to `n -
1`. You will be given the number `n` and a list of undirected `edges`
(each edge is a pair of labels).

You can assume that no duplicate edges will appear in `edges`. Since all edges are
undirected, `[0, 1]` is the same as `[1, 0]` and thus will not appear
together in `edges`.

Example 1 :

Input: `n = 4`, `edges = [[1, 0], [1, 2], [1, 3]]`

0
|
1
/ \
2   3

Output: `[1]`

Example 2 :

Input: `n = 6`, `edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]`

0  1  2
\ | /
3
|
4
|
5

Output: `[3, 4]`

Note:

According to the definition of tree on Wikipedia: &ldquo;a tree
is an undirected graph in which any two vertices are connected by exactly one
path. In other words, any connected graph without simple cycles is a tree.&rdquo;

The height of a rooted tree is the number of edges on the longest downward path between
the root and a leaf.

【中文翻译】
对于一个具有树特征的无向图，我们可以选择任意节点作为根。结果图将成为一个有根树。在所有可能的
有根树中，高度最小的树被称为最小高度树（MHT）。给定这样一个图，编写一个函数找到所有的最小
高度树并返回其根标签的列表。

格式

该图包含 n 个节点，标记从 0 到 n-1。给定数字 n 和一个无向边列表 edges（每条边是一对标签）。

你可以假设 edges 中不会出现重复的边。由于所有边都是无向的，[0, 1] 和 [1, 0] 是相同的，因此
不会同时在 edges 中出现。

示例 1：

输入：n = 4, edges = [[1, 0], [1, 2], [1, 3]]

   0
   |
   1
  / \
 2   3

输出：[1]

示例 2：

输入：n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

0  1  2
 \ | /
   3
   |
   4
   |
   5

输出：[3, 4]

注意：

根据维基百科上树的定义：「树是一个无向图，其中任意两个顶点之间只有一条路径相连。换句话说，
任何没有简单环路的连通图就是树。」

有根树的高度是根节点与叶子节点之间最长向下路径的边数。
"""

from typing import List, Optional


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        # 构建邻接表（使用 set 便于删除边）
        graph = [set() for _ in range(n)]
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        # 找出所有叶子节点（度为 1）
        leaves = [i for i in range(n) if len(graph[i]) == 1]
        remaining = n
        # 逐层剥离叶子，直到剩余节点数 <= 2
        while remaining > 2:
            remaining -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 拓扑排序（剥洋葱法 / 多源 BFS）。
# 最小高度树的根一定是树的最长路径（直径）的中点，最多有两个。
# 从所有叶子节点（度为 1 的节点）开始，逐层删除叶子节点及其关联边。
# 每删除一层叶子后，暴露出来的新度为 1 的节点成为下一层的叶子。
# 重复这个过程直到剩余节点数 <= 2，这些剩余节点就是答案。
# 直观理解：不断"剥去"树的外层，最终剩下最中心的一个或两个节点。
#
# 时间复杂度: O(n) - 每个节点和边最多被处理一次
# 空间复杂度: O(n) - 邻接表存储
#
# 关键点:
# - MHT 的根是树直径的中点，最多有两个
# - 类似拓扑排序，但处理的是无向图，从度为 1 的节点开始
# - 使用 set 存储邻接关系，删除边的操作 O(1)
# - 剩余节点数 > 2 时继续剥叶，<= 2 时停止即得答案
