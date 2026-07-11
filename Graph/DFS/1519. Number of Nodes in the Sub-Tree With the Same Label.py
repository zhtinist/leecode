"""
LeetCode #1519 - Number of Nodes in the Sub-Tree With the Same Label
中文题名：子树中标签相同的节点数
https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/

Given a tree (i.e. a connected, undirected graph that has no cycles) consisting of
`n` nodes numbered from `0` to `n - 1` and exactly
`n - 1` `edges`. The root of the tree is the node
`0`, and each node of the tree has a label which is a
lower-case character given in the string `labels` (i.e. The node with the
number `i` has the label `labels[i]`).

The `edges` array is given on the form `edges[i] = [ai,
bi]`, which means there is an edge between nodes
`ai` and `bi` in the tree.

Return an array of size `n` where `ans[i]` is the
number of nodes in the subtree of the `ith` node
which have the same label as node `i`.

A subtree of a tree `T` is the tree consisting of a node in
`T` and all of its descendant nodes.

Example 1:

Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"
Output: [2,1,1,1,1,1,1]
Explanation: Node 0 has label 'a' and its sub-tree has node 2 with label 'a' as well, thus the answer is 2. Notice that any node is part of its sub-tree.
Node 1 has a label 'b'. The sub-tree of node 1 contains nodes 1,4 and 5, as nodes 4 and 5 have different labels than node 1, the answer is just 1 (the node itself).

Example 2:

Input: n = 4, edges = [[0,1],[1,2],[0,3]], labels = "bbbb"
Output: [4,2,1,1]
Explanation: The sub-tree of node 2 contains only node 2, so the answer is 1.
The sub-tree of node 3 contains only node 3, so the answer is 1.
The sub-tree of node 1 contains nodes 1 and 2, both have label 'b', thus the answer is 2.
The sub-tree of node 0 contains nodes 0, 1, 2 and 3, all with label 'b', thus the answer is 4.

Example 3:

Input: n = 5, edges = [[0,1],[0,2],[1,3],[0,4]], labels = "aabab"
Output: [3,2,1,1,1]

Example 4:

Input: n = 6, edges = [[0,1],[0,2],[1,3],[3,4],[4,5]], labels = "cbabaa"
Output: [1,2,1,1,2,1]

Example 5:

Input: n = 7, edges = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6]], labels = "aaabaaa"
Output: [6,5,4,1,3,2,1]

Constraints:

`1 <= n <= 10^5`

`edges.length == n - 1`

`edges[i].length == 2`

`0 <= ai, bi < n`

`ai != bi`

`labels.length == n`

`labels` is consisting of only of lower-case English letters.

【中文翻译】
给定一棵树（连通无环无向图），包含 n 个节点（编号 0 到 n-1）和恰好 n-1 条边。
根节点是 0，每个节点有一个小写字母标签（字符串 labels，节点 i 的标签为 labels[i]）。
返回一个大小为 n 的数组 ans，其中 ans[i] 是节点 i 的子树中与节点 i 标签相同的节点数。

示例 1：

输入：n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"
输出：[2,1,1,1,1,1,1]
解释：节点 0 标签为 'a'，其子树中有节点 2 也是 'a'，因此答案为 2。

示例 2：

输入：n = 4, edges = [[0,1],[1,2],[0,3]], labels = "bbbb"
输出：[4,2,1,1]

示例 3：

输入：n = 5, edges = [[0,1],[0,2],[1,3],[0,4]], labels = "aabab"
输出：[3,2,1,1,1]

示例 4：

输入：n = 6, edges = [[0,1],[0,2],[1,3],[3,4],[4,5]], labels = "cbabaa"
输出：[1,2,1,1,2,1]

示例 5：

输入：n = 7, edges = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6]], labels = "aaabaaa"
输出：[6,5,4,1,3,2,1]
"""

from typing import List, Optional
from collections import defaultdict


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        # Build adjacency list
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        answer = [0] * n

        def dfs(node: int, parent: int) -> List[int]:
            # Count of each label (a-z) in subtree rooted at node
            count = [0] * 26
            count[ord(labels[node]) - ord('a')] = 1
            for child in graph[node]:
                if child == parent:
                    continue
                child_count = dfs(child, node)
                for i in range(26):
                    count[i] += child_count[i]
            answer[node] = count[ord(labels[node]) - ord('a')]
            return count

        dfs(0, -1)
        return answer



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 构建邻接表（无向图），从根节点 0 开始 DFS 后序遍历。
# 每个节点返回一个大小为 26 的数组，记录子树中每个字母的出现次数。
# 合并子节点的计数数组，当前节点自身的标签计数 + 1。
# 答案数组 ans[node] = 当前节点标签在子树中的出现次数。
#
# 时间复杂度: O(N * 26) — 每个节点合并 26 个字母的计数
# 空间复杂度: O(N * 26) — 递归栈 + 计数数组
#
# 关键点:
# - 无向图需要传 parent 参数避免回到父节点
# - 后序遍历：先处理子节点，再汇总到当前节点
# - 每次返回大小为 26 的数组，合并开销为常数
