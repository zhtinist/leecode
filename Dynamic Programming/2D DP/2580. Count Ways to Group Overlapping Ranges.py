"""
LeetCode #2580 - Count Ways to Group Overlapping Ranges
统计将重叠区间合并成组的方案数
https://leetcode.cn/problems/count-ways-to-group-overlapping-ranges/

给你一个二维整数数组 `ranges` ，其中 `ranges[i] = [start_i, end_i]` 表示 `start_i` 到 `end_i` 之间（包括二者）的所有整数都包含在第 `i` 个区间中。
你需要将 `ranges` 分成 两个 组（可以为空），满足：
每个区间只属于一个组。
两个有 交集 的区间必须在 同一个 组内。
如果两个区间有至少 一个 公共整数，那么这两个区间是 有交集 的。
比方说，区间 `[1, 3]` 和 `[2, 5]` 有交集，因为 `2` 和 `3` 在两个区间中都被包含。
请你返回将 `ranges` 划分成两个组的 总方案数 。由于答案可能很大，将它对 `10^9 + 7` 取余 后返回。

示例 1：
输入：ranges = [[6,10],[5,15]] 输出：2 解释： 两个区间有交集，所以它们必须在同一个组内。 所以有两种方案： - 将两个区间都放在第 1 个组中。 - 将两个区间都放在第 2 个组中。
示例 2：
输入：ranges = [[1,3],[10,20],[2,5],[4,8]] 输出：4 解释： 区间 [1,3] 和 [2,5] 有交集，所以它们必须在同一个组中。 同理，区间 [2,5] 和 [4,8] 也有交集，所以它们也必须在同一个组中。 所以总共有 4 种分组方案： - 所有区间都在第 1 组。 - 所有区间都在第 2 组。 - 区间 [1,3] ，[2,5] 和 [4,8] 在第 1 个组中，[10,20] 在第 2 个组中。 - 区间 [1,3] ，[2,5] 和 [4,8] 在第 2 个组中，[10,20] 在第 1 个组中。

提示：
`1 <= ranges.length <= 10^5`
`ranges[i].length == 2`
`0 <= start_i <= end_i <= 10^9`
"""

from typing import List, Optional


class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        ranges.sort(key=lambda x: x[0])
        groups = 0
        cur_end = -1
        for start, end in ranges:
            if start > cur_end:
                groups += 1
            cur_end = max(cur_end, end)
        return pow(2, groups, MOD)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Sorting
#
# 解题思路:
# 排序后合并重叠区间，得到互不重叠的连通分量数m。每个分量可以独立选择放入第1组或第2组，
# 有2种选择。m个分量总共有2^m种分法。使用快速幂计算2^m mod 1e9+7。
#
# 时间复杂度: O(N log N)
# 空间复杂度: O(1)
#
# 关键点:
# - 合并重叠区间得到独立分量
# - 每个分量2种选择，总数=2^m
# - pow(x, y, mod)内置快速幂取模
