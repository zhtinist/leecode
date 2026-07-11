"""
LeetCode #1722 - Minimize Hamming Distance After Swap Operations
中文题名：执行交换操作后的最小汉明距离
https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/

You are given two integer arrays, `source` and `target`, both
of length `n`. You are also given an array `allowedSwaps` where
each `allowedSwaps[i] = [ai, bi]` indicates that you
are allowed to swap the elements at index `ai` and index
`bi` (0-indexed) of array `source`.
Note that you can swap elements at a specific pair of indices multiple
times and in any order.

The Hamming distance of two arrays of the same length,
`source` and `target`, is the number of positions where the
elements are different. Formally, it is the number of indices `i` for
`0 <= i <= n-1` where `source[i] != target[i]` (0-indexed).

Return the minimum Hamming distance of
`source` and `target` after performing any
amount of swap operations on array `source`.

Example 1:

Input: source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]
Output: 1
Explanation: source can be transformed the following way:
- Swap indices 0 and 1: source = [2,1,3,4]
- Swap indices 2 and 3: source = [2,1,4,3]
The Hamming distance of source and target is 1 as they differ in 1 position: index 3.

Example 2:

Input: source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []
Output: 2
Explanation: There are no allowed swaps.
The Hamming distance of source and target is 2 as they differ in 2 positions: index 1 and index 2.

Example 3:

Input: source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]
Output: 0

Constraints:

`n == source.length == target.length`

`1 <= n <= 105`

`1 <= source[i], target[i] <= 105`

`0 <= allowedSwaps.length <= 105`

`allowedSwaps[i].length == 2`

`0 <= ai, bi <= n - 1`

`ai != bi`

【中文翻译】
给定源数组 source、目标数组 target 和允许交换的索引对数组 allowedSwaps。
allowedSwaps[i] = [a, b] 表示可以交换 source 中位置 a 和 b 的元素。
可以通过任意顺序的交换操作（每个交换对可以使用任意次）。
求经过交换后，source 和 target 的最小汉明距离（不同位置的个数）。

示例 1：
输入: source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]
输出: 1
解释: 交换0和1得到[2,1,3,4]，交换2和3得到[2,1,4,3]。与target[2,1,4,5]相比，仅索引3不同，距离为1。
"""

from typing import List, Optional
from collections import defaultdict, Counter


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        uf = UnionFind(n)
        for a, b in allowedSwaps:
            uf.union(a, b)

        # 按连通分量分组
        groups = defaultdict(list)
        for i in range(n):
            groups[uf.find(i)].append(i)

        ans = 0
        for indices in groups.values():
            # 统计该连通分量中 source 和 target 的频次
            src_count = Counter(source[i] for i in indices)
            tgt_count = Counter(target[i] for i in indices)
            # 匹配的数量 = sum(min(src_count[val], tgt_count[val]))
            matches = sum((src_count & tgt_count).values())
            ans += len(indices) - matches

        return ans
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 并查集。允许交换的索引形成连通图，同一个连通分量内的元素可以任意排列。
# 1. 用并查集合并所有可交换的索引
# 2. 对每个连通分量，统计 source 和 target 的元素频次
# 3. 对于每个值 val，可以匹配 min(count_source[val], count_target[val]) 个位置
# 4. 汉明距离 = 连通分量大小 - 匹配数
#
# 时间复杂度: O(N + E * α(N)) — 并查集操作 + 统计频次
# 空间复杂度: O(N) — 并查集和分组字典
#
# 关键点:
# - 同一个连通分量内元素可任意排列
# - Counter 的 & 操作返回元素的最小计数交集
# - 每个连通分量独立计算汉明距离
