"""
LeetCode #2896 - Apply Operations to Make Two Strings Equal
执行操作使两个字符串相等
https://leetcode.cn/problems/apply-operations-to-make-two-strings-equal/

给你两个下标从 0 开始的二进制字符串 `s1` 和 `s2` ，两个字符串的长度都是 `n` ，再给你一个正整数 `x` 。
你可以对字符串 `s1` 执行以下操作 任意次 ：
选择两个下标 `i` 和 `j` ，将 `s1[i]` 和 `s1[j]` 都反转，操作的代价为 `x` 。
选择满足 `i < n - 1` 的下标 `i` ，反转 `s1[i]` 和 `s1[i + 1]` ，操作的代价为 `1` 。
请你返回使字符串 `s1` 和 `s2` 相等的 最小 操作代价之和，如果无法让二者相等，返回 `-1` 。
注意 ，反转字符的意思是将 `0` 变成 `1` ，或者 `1` 变成 `0` 。

示例 1：
输入：s1 = "1100011000", s2 = "0101001010", x = 2 输出：4 解释：我们可以执行以下操作： - 选择 i = 3 执行第二个操作。结果字符串是 s1 = "1101111000" 。 - 选择 i = 4 执行第二个操作。结果字符串是 s1 = "1101001000" 。 - 选择 i = 0 和 j = 8 ，执行第一个操作。结果字符串是 s1 = "0101001010" = s2 。 总代价是 1 + 1 + 2 = 4 。这是最小代价和。
示例 2：
输入：s1 = "10110", s2 = "00011", x = 4 输出：-1 解释：无法使两个字符串相等。

提示：
`n == s1.length == s2.length`
`1 <= n, x <= 500`
`s1` 和 `s2` 只包含字符 `'0'` 和 `'1'` 。
"""

from typing import List, Optional


class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        n = len(s1)
        diff = [i for i in range(n) if s1[i] != s2[i]]
        m = len(diff)
        if m % 2 != 0:
            return -1
        if m == 0:
            return 0

        # dp[l][r] for interval [l, r] (inclusive)
        from functools import lru_cache

        @lru_cache(None)
        def solve(l: int, r: int) -> int:
            length = r - l + 1
            if length == 2:
                return min(x, diff[r] - diff[l])
            # Option 1: pair ends
            best = min(x, diff[r] - diff[l]) + solve(l + 1, r - 1)
            # Option 2: split
            for k in range(l + 1, r, 2):
                best = min(best, solve(l, k) + solve(k + 1, r))
            return best

        return solve(0, m - 1)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: String, Dynamic Programming
#
# 解题思路:
# 首先找出 s1 和 s2 中不同的位置索引，若数量为奇数则无法完成返回-1。
# 操作1可以翻转任意两个位置（代价 x），操作2翻转相邻位置（代价 = 距离）。
# 使用区间DP：对于排序后的差异位置数组，每次可以选择配对两端点（代价 min(x, 距离) + 中间部分）或将区间拆分为两个子区间。
#
# 时间复杂度: O(m^3) 其中 m 为不同位置数量（<= n <= 500）
# 空间复杂度: O(m^2)
#
# 关键点:
# - 差异位置数为奇数直接返回 -1
# - 每次操作本质上是配对两个需要翻转的位置
# - 操作2翻转 i 和 j 的代价等于距离 |j-i|（通过多次相邻翻转实现）
# - 区间DP：要么配对端点，要么拆分区间
