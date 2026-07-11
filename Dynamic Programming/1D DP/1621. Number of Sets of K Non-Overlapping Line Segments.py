"""
LeetCode #1621 - Number of Sets of K Non-Overlapping Line Segments
中文题名：大小为 K 的不重叠线段的数目
https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/

Given `n` points on a 1-D plane, where the `ith`
point (from `0` to `n-1`) is at `x = i`, find the
number of ways we can draw exactly `k` non-overlapping
line segments such that each segment covers two or more points. The endpoints of each
segment must have integral coordinates. The `k` line
segments do not have to cover all `n` points, and they are
allowed to share endpoints.

Return the number of ways we can draw `k` non-overlapping
line segments. Since this number can be huge, return it modulo
`109 + 7`.

Example 1:

Input: n = 4, k = 2
Output: 5
Explanation:
The two line segments are shown in red and blue.
The image above shows the 5 different ways {(0,2),(2,3)}, {(0,1),(1,3)}, {(0,1),(2,3)}, {(1,2),(2,3)}, {(0,1),(1,2)}.

Example 2:

Input: n = 3, k = 1
Output: 3
Explanation: The 3 ways are {(0,1)}, {(0,2)}, {(1,2)}.

Example 3:

Input: n = 30, k = 7
Output: 796297179
Explanation: The total number of possible ways to draw 7 line segments is 3796297200. Taking this number modulo 109 + 7 gives us 796297179.

Example 4:

Input: n = 5, k = 3
Output: 7

Example 5:

Input: n = 3, k = 2
Output: 1

Constraints:

`2 <= n <= 1000`

`1 <= k <= n-1`

【中文翻译】
给定 n 个点（0 到 n-1）在一条直线上，以及整数 k。求选择 k 条不重叠线段的方案数。
线段由两个端点 (start, end) 定义，满足 0 <= start < end <= n-1。不同线段不能重叠（端点可以重合）。
由于答案可能很大，返回结果对 10^9+7 取模。

示例 1：
输入: n = 4, k = 2
输出: 5
解释: 可选方案为 [0,1]+[2,3], [0,1]+[1,3], [1,2]+[2,3], [0,2]+[2,3], [0,1]+[1,2]。
"""

from typing import List, Optional


class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        # 组合数学：C(n + k - 1, 2 * k)
        # 等价于在 n+k-1 个位置中选择 2k 个位置
        
        def nCr(n_val: int, r: int) -> int:
            if r > n_val:
                return 0
            r = min(r, n_val - r)
            num = 1
            den = 1
            for i in range(r):
                num = num * (n_val - i) % MOD
                den = den * (i + 1) % MOD
            # 费马小定理求逆元
            return num * pow(den, MOD - 2, MOD) % MOD

        return nCr(n + k - 1, 2 * k)
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 问题可转化为组合数学：在 n+k-1 个球中选择 2k 个位置放入隔板。
# 答案为 C(n+k-1, 2k)。使用费马小定理求乘法逆元计算组合数。
# 另一种解法是 DP：dp[i][j] 表示用 i 条线段覆盖前 j 个点的方案数。
#
# 时间复杂度: O(K) — 计算组合数需要 O(K) 的循环
# 空间复杂度: O(1)
#
# 关键点:
# - 组合数学推导：k 条线段的选择可转化为从 n+k-1 个位置选 2k 个端点
# - 费马小定理：a^(MOD-2) ≡ a^(-1) (mod MOD) 用于除法取模
# - 线段可以端点重合（不重叠意味着无内部交点）
