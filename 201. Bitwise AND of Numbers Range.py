"""
LeetCode #201 - Bitwise AND of Numbers Range
中文题名：数字范围按位与
https://leetcode.com/problems/bitwise-and-of-numbers-range/

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all
numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4

Example 2:

Input: [0,1]
Output: 0

【中文翻译】
给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字（含 m 和 n）的按位与结果。

示例 1：

输入：[5,7]
输出：4

示例 2：

输入：[0,1]
输出：0
"""

from typing import List, Optional


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0
        # Find the common prefix (bits where m and n differ will become 0)
        while m < n:
            m >>= 1
            n >>= 1
            shift += 1

        # Shift back the common prefix
        return m << shift


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 题目等价于求 [m, n] 范围内所有数字二进制表示的公共前缀。
# 从 m 到 n，低位比特一定会经历 0 和 1 的变化，所以 AND 结果中低位都会变成 0。
# 只有高位（m 和 n 相同的二进制前缀）会保留下来。
#
# 例如：m=5(101), n=7(111)
# m<n, m>>=1 → 2(10), n>>=1 → 3(11), shift=1
# m<n, m>>=1 → 1(1),  n>>=1 → 1(1),  shift=2
# 返回 1 << 2 = 4(100) — 公共前缀是 1
#
# 时间复杂度: O(log N) — 最多移位 32 次
# 空间复杂度: O(1)
#
# 关键点:
# - 核心洞察：结果是 m 和 n 的公共二进制前缀
# - Brian Kernighan 变体：不断将 n 最低位 1 清零直到 n <= m
# - 移位法更直观：不断右移直到 m == n
