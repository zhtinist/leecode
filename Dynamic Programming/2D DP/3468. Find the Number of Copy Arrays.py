"""
LeetCode #3468 - Find the Number of Copy Arrays
可行数组的数目
https://leetcode.cn/problems/find-the-number-of-copy-arrays/

给你一个长度为 `n` 的数组 `original` 和一个长度为 `n x 2` 的二维数组 `bounds`，其中 `bounds[i] = [u_i, v_i]`。
你需要找到长度为 `n` 且满足以下条件的 可能的 数组 `copy` 的数量：
对于 `1 <= i <= n - 1` ，都有 `(copy[i] - copy[i - 1]) == (original[i] - original[i - 1])` 。
对于 `0 <= i <= n - 1` ，都有 `u_i <= copy[i] <= v_i`_ 。
返回满足这些条件的数组数目。

示例 1

输入：original = [1,2,3,4], bounds = [[1,2],[2,3],[3,4],[4,5]]
输出：2
解释：
可能的数组为：
`[1, 2, 3, 4]`
`[2, 3, 4, 5]`
示例 2

输入：original = [1,2,3,4], bounds = [[1,10],[2,9],[3,8],[4,7]]
输出：4
解释：
可能的数组为：
`[1, 2, 3, 4]`
`[2, 3, 4, 5]`
`[3, 4, 5, 6]`
`[4, 5, 6, 7]`
示例 3

输入：original = [1,2,1,2], bounds = [[1,1],[2,3],[3,3],[2,3]]
输出：0
解释：
没有可行的数组。

提示：
`2 <= n == original.length <= 10^5`
`1 <= original[i] <= 10^9`
`bounds.length == n`
`bounds[i].length == 2`
`1 <= bounds[i][0] <= bounds[i][1] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        n = len(original)
        # copy[i] = copy[0] + (original[i] - original[0])
        # For each i: u_i <= copy[0] + diff[i] <= v_i
        # => u_i - diff[i] <= copy[0] <= v_i - diff[i]
        lo = -10 ** 18
        hi = 10 ** 18
        base = original[0]
        for i in range(n):
            diff = original[i] - base
            lo = max(lo, bounds[i][0] - diff)
            hi = min(hi, bounds[i][1] - diff)
        if lo > hi:
            return 0
        return hi - lo + 1



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Math
#
# 解题思路:
# 1. 条件 copy[i] - copy[i-1] = original[i] - original[i-1] 意味着相邻差值固定
# 2. 令 diff[i] = original[i] - original[0]，则 copy[i] = copy[0] + diff[i]
# 3. 对每个位置 i：bounds[i][0] <= copy[0] + diff[i] <= bounds[i][1]
#    => bounds[i][0] - diff[i] <= copy[0] <= bounds[i][1] - diff[i]
# 4. 对所有约束取交集：lo = max(lower_bounds), hi = min(upper_bounds)
# 5. 若 lo <= hi，答案为 hi - lo + 1；否则为 0
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 整个 copy 数组由 copy[0] 唯一确定
# - 问题化简为求 copy[0] 的可行范围
