"""
LeetCode #1864 - Minimum Number of Swaps to Make the Binary String Alternating
构成交替字符串需要的最小交换次数
https://leetcode.cn/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/

给你一个二进制字符串 `s` ，现需要将其转化为一个 交替字符串 。请你计算并返回转化所需的 最小 字符交换次数，如果无法完成转化，返回 `-1` 。
交替字符串 是指：相邻字符之间不存在相等情况的字符串。例如，字符串 `"010"` 和 `"1010"` 属于交替字符串，但 `"0100"` 不是。
任意两个字符都可以进行交换，不必相邻 。

示例 1：
输入：s = "111000" 输出：1 解释：交换位置 1 和 4："111000" -> "101010" ，字符串变为交替字符串。
示例 2：
输入：s = "010" 输出：0 解释：字符串已经是交替字符串了，不需要交换。
示例 3：
输入：s = "1110" 输出：-1

提示：
`1 <= s.length <= 1000`
`s[i]` 的值为 `'0'` 或 `'1'`
"""

from typing import List, Optional


class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        # Count zeros and ones
        zeros = s.count('0')
        ones = n - zeros

        # If difference > 1, impossible to make alternating
        if abs(zeros - ones) > 1:
            return -1

        # Count mismatches for pattern starting with '0': "0101..."
        mismatch0 = 0
        for i, ch in enumerate(s):
            if i % 2 == 0:
                if ch != '0':
                    mismatch0 += 1
            else:
                if ch != '1':
                    mismatch0 += 1

        # Count mismatches for pattern starting with '1': "1010..."
        mismatch1 = 0
        for i, ch in enumerate(s):
            if i % 2 == 0:
                if ch != '1':
                    mismatch1 += 1
            else:
                if ch != '0':
                    mismatch1 += 1

        # Each swap fixes 2 mismatches
        # Choose the valid pattern based on counts
        if zeros == ones:
            return min(mismatch0, mismatch1) // 2
        elif zeros > ones:
            return mismatch0 // 2
        else:
            return mismatch1 // 2



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, String
#
# 解题思路:
# 交替字符串只有两种模式："0101..." 和 "1010..."。
# 1. 统计0和1的数量，如果差值>1则无法构成交替字符串，返回-1。
# 2. 计算与两种模式的不匹配位置数。
# 3. 每次交换可以修正两个不匹配的位置，所以操作次数 = 不匹配数 / 2。
# 4. 根据0和1的数量选择有效的模式。
#
# 时间复杂度: O(n) — 遍历字符串两次
# 空间复杂度: O(1) — 只使用常数变量
#
# 关键点:
# - 只有两种交替模式
# - 每次交换修正两个位置，所以交换次数 = 不匹配数 / 2
# - 如果0和1数量相等，两种模式都可能，取最小值
# - 如果0比1多，必须以0开头的模式（"0101..."）
