"""
LeetCode #738 - Monotone Increasing Digits
中文题名：单调递增的数字
https://leetcode.com/problems/monotone-increasing-digits/

Given a non-negative integer `N`, find the largest number that is less than or
equal to `N` with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if each pair of
adjacent digits `x` and `y` satisfy `x <= y`.)

Example 1:

Input: N = 10
Output: 9

Example 2:

Input: N = 1234
Output: 1234

Example 3:

Input: N = 332
Output: 299

Note:
`N` is an integer in the range `[0, 10^9]`.

【中文翻译】
给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调非递减的。

（当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）

示例 1：

输入：N = 10
输出：9

示例 2：

输入：N = 1234
输出：1234

示例 3：

输入：N = 332
输出：299

注意：
N 是在 [0, 10^9] 范围内的整数。
"""

from typing import List, Optional


class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        s = list(str(n))
        marker = len(s)
        for i in range(len(s) - 1, 0, -1):
            if s[i - 1] > s[i]:
                marker = i
                s[i - 1] = str(int(s[i - 1]) - 1)
        for i in range(marker, len(s)):
            s[i] = "9"
        return int("".join(s))



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心算法，从右向左扫描数字字符串。
# 将 N 转换为字符串数组 s。从倒数第二位向左遍历：
# - 如果 s[i-1] > s[i]（出现递减），说明需要调整。
# - 将 s[i-1] 减 1，并标记 marker = i（从这个位置开始后面全部变成 9）。
# 遍历结束后，将 marker 及之后的所有位置都设为 '9'。
# 例如：N = 332 → s = ['3','3','2']
# i=2: s[1]='3' > s[2]='2', marker=2, s[1]='2' → s=['3','2','2']
# i=1: s[0]='3' > s[1]='2', marker=1, s[0]='2' → s=['2','2','2']
# 最后 marker=1 开始全变 9 → ['2','9','9'] → 299
#
# 时间复杂度: O(log N) - log N 是 N 的位数，最多 10 位（N <= 10^9）
# 空间复杂度: O(log N) - 存储数字字符串
#
# 关键点:
# - 从右向左扫描，找第一个递减的位置
# - 找到递减后，该位置减 1，后面全部变 9
# - 贪心思想：我们想得到最大的单调递增数，所以尽量保留高位
# - 注意要处理连续递减的情况（例如 332 → 299）
