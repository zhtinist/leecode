"""
LeetCode #2406 - Divide Intervals Into Minimum Number of Groups
将区间分为最少组数
https://leetcode.cn/problems/divide-intervals-into-minimum-number-of-groups/

给你一个二维整数数组 `intervals` ，其中 `intervals[i] = [left_i, right_i]` 表示 闭 区间 `[left_i, right_i]` 。
你需要将 `intervals` 划分为一个或者多个区间 组 ，每个区间 只 属于一个组，且同一个组中任意两个区间 不相交 。
请你返回 最少 需要划分成多少个组。
如果两个区间覆盖的范围有重叠（即至少有一个公共数字），那么我们称这两个区间是 相交 的。比方说区间 `[1, 5]` 和 `[5, 8]` 相交。

示例 1：
输入：intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]] 输出：3 解释：我们可以将区间划分为如下的区间组： - 第 1 组：[1, 5] ，[6, 8] 。 - 第 2 组：[2, 3] ，[5, 10] 。 - 第 3 组：[1, 10] 。 可以证明无法将区间划分为少于 3 个组。
示例 2：
输入：intervals = [[1,3],[5,6],[8,10],[11,13]] 输出：1 解释：所有区间互不相交，所以我们可以把它们全部放在一个组内。

提示：
`1 <= intervals.length <= 10^5`
`intervals[i].length == 2`
`1 <= left_i <= right_i <= 10^6`
"""

from typing import List, Optional


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])
        res = 0
        e_idx = 0
        for s in starts:
            if s > ends[e_idx]:
                e_idx += 1
            else:
                res += 1
        return res



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Two Pointers, Prefix Sum, Sorting, Heap (Priority Queue)
#
# 解题思路:
# 问题等价于求最大同时重叠的区间数（类似会议室II）。
# 分别提取所有开始时间和结束时间并排序。
# 使用两个指针：遍历每个开始时间，若当前开始时间大于当前最早结束时间，
# 则可复用该结束时间对应的组（该组已空闲）；否则需要新开一组。
# 最终需要的组数即为最大并发区间数。
#
# 时间复杂度: O(n log n)，主要由排序决定。
# 空间复杂度: O(n)，需要存储开始和结束时间的数组。
#
# 关键点:
# - 转化为最大并发区间问题（扫描线思想）。
# - 分别排序开始和结束时间，用双指针计算所需最大组数。
