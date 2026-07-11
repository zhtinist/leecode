"""
LeetCode #1743 - Restore the Array From Adjacent Pairs
中文题名：从相邻元素对还原数组
https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/

There is an integer array `nums` that consists of `n` unique elements,
but you have forgotten it. However, you do remember every pair of adjacent elements in
`nums`.

You are given a 2D integer array `adjacentPairs` of size `n -
1` where each `adjacentPairs[i] = [ui, vi]`
indicates that the elements `ui` and
`vi` are adjacent in `nums`.

It is guaranteed that every adjacent pair of elements `nums[i]` and `nums[i+1]`
will exist in `adjacentPairs`, either as `[nums[i],
nums[i+1]]` or `[nums[i+1], nums[i]]`. The pairs can appear
in any order.

Return the original array `nums`. If there are multiple
solutions, return any of them.

Example 1:

Input: adjacentPairs = [[2,1],[3,4],[3,2]]
Output: [1,2,3,4]
Explanation: This array has all its adjacent pairs in adjacentPairs.
Notice that adjacentPairs[i] may not be in left-to-right order.

Example 2:

Input: adjacentPairs = [[4,-2],[1,4],[-3,1]]
Output: [-2,4,1,-3]
Explanation: There can be negative numbers.
Another solution is [-3,1,4,-2], which would also be accepted.

Example 3:

Input: adjacentPairs = [[100000,-100000]]
Output: [100000,-100000]

Constraints:

`nums.length == n`

`adjacentPairs.length == n - 1`

`adjacentPairs[i].length == 2`

`2 <= n <= 105`

`-105 <= nums[i], ui, vi <=
105`

There exists some `nums` that has `adjacentPairs` as its
pairs.

【中文翻译】
给定一个由 n 个不同元素组成的数组 nums，以及其 n-1 个相邻元素对 adjacentPairs[i] = [u, v]（表示 u 和 v 在原始数组中相邻）。
请还原原始数组并以任意顺序返回。

示例 1：
输入: adjacentPairs = [[2,1],[3,4],[3,2]]
输出: [1,2,3,4]
解释: 原数组为 [1,2,3,4] 或 [4,3,2,1]。相邻对: [2,1],[3,4],[3,2] 全都匹配。
"""

from typing import List, Optional
from collections import defaultdict


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)

        # 起点是度为1的节点（端点）
        start = next(node for node in graph if len(graph[node]) == 1)

        n = len(adjacentPairs) + 1
        result = [start]
        prev = start
        cur = graph[start][0]

        for _ in range(n - 1):
            result.append(cur)
            # 找到下一个未访问的邻居
            nxt = next(nei for nei in graph[cur] if nei != prev)
            prev, cur = cur, nxt

        return result
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 构建邻接图：每个数字连接到它的相邻数字。
# 原数组的端点（第一个和最后一个元素）在图中度数为 1（只有一个邻居）。
# 从任意一个度数为1的节点开始，沿着唯一路径遍历即可还原整个数组。
#
# 时间复杂度: O(N) — 构建图 + 一次遍历
# 空间复杂度: O(N) — 邻接字典
#
# 关键点:
# - 数组两端点度数=1，中间点度数=2
# - 从端点开始，沿着唯一方向走 N 步
# - 用 next(nei for nei in graph[cur] if nei != prev) 找到未访问邻居
