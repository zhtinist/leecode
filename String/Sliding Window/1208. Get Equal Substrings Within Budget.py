"""
LeetCode #1208 - Get Equal Substrings Within Budget
中文题名：尽可能使字符串相等
https://leetcode.com/problems/get-equal-substrings-within-budget/

You are given two strings `s` and `t` of the same length. You want to
change `s` to `t`. Changing the `i`-th character of
`s` to `i`-th character of `t` costs `|s[i] -
t[i]|` that is, the absolute difference between the ASCII values of the
characters.

You are also given an integer `maxCost`.

Return the maximum length of a substring of `s` that can be changed to be the same
as the corresponding substring of `t`with a cost less than or equal to `maxCost`.

If there is no substring from `s` that can be changed to its corresponding
substring from `t`, return `0`.

Example 1:

Input: s = "abcd", t = "bcdf", maxCost = 3
Output: 3
Explanation: "abc" of s can change to "bcd". That costs 3, so the maximum length is 3.

Example 2:

Input: s = "abcd", t = "cdef", maxCost = 3
Output: 1
Explanation: Each character in s costs 2 to change to charactor in `t, so the maximum length is 1.`

Example 3:

Input: s = "abcd", t = "acde", maxCost = 0
Output: 1
Explanation: You can't make any change, so the maximum length is 1.

Constraints:

`1 <= s.length, t.length <= 10^5`

`0 <= maxCost <= 10^6`

`s` and `t` only contain lower case English letters.

【中文翻译】
给你两个长度相同的字符串 s 和 t。将 s 中的第 i 个字符变到 t 中的第 i 个字符需要开销 |s[i] - t[i]|，即两个字符的 ASCII 码值的差的绝对值。

同时给你一个整数 maxCost。

返回 s 的子串在满足开销不超过 maxCost 的条件下，能转换成的与 t 对应子串相同的最大长度。

如果不存在可以转换的子串，返回 0。

示例 1：

输入：s = "abcd", t = "bcdf", maxCost = 3
输出：3
解释：s 中的 "abc" 可以变为 "bcd"，开销为 3，所以最大长度为 3。

示例 2：

输入：s = "abcd", t = "cdef", maxCost = 3
输出：1
解释：s 中的任一字符要想变成 t 中对应的字符，其开销都是 2，因此最大长度为 1。

示例 3：

输入：s = "abcd", t = "acde", maxCost = 0
输出：1
解释：你无法作出任何改动，所以最大长度为 1。

约束条件：

1 <= s.length, t.length <= 10^5
0 <= maxCost <= 10^6
s 和 t 只包含小写英文字母。

"""

from typing import List, Optional


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        costs = [abs(ord(s[i]) - ord(t[i])) for i in range(n)]

        left = 0
        cur_cost = 0
        max_len = 0

        for right in range(n):
            cur_cost += costs[right]
            while cur_cost > maxCost:
                cur_cost -= costs[left]
                left += 1
            max_len = max(max_len, right - left + 1)

        return max_len










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用滑动窗口（双指针）解决子串长度最大化问题。
# 1. 预处理：计算每个位置 i 的转换开销 costs[i] = |s[i] - t[i]|。
# 2. 维护一个可变大小的窗口 [left, right]：
#    - 右指针 right 不断向右扩展，将 costs[right] 加入当前开销 cur_cost。
#    - 当 cur_cost > maxCost 时，左指针 left 右移收缩窗口，直到开销回到预算范围内。
#    - 每次迭代更新最大窗口长度 max_len。
# 3. 因为 right 单调递增，left 也只增不减，每个元素最多进窗口一次、出窗口一次。
#
# 时间复杂度: O(n) - 每个字符被处理两次（进窗口和出窗口）
# 空间复杂度: O(n) - 存储 costs 数组（可优化为 O(1) 即时计算）
#
# 关键点:
# - 滑动窗口适用于"满足某约束条件的最长子数组"类问题
# - 窗口内总开销随右指针扩展递增，随左指针收缩递减，满足单调性
# - while 循环收缩窗口直到满足预算条件
# - 可以优化为不预存 costs 数组，在循环中即时计算开销节省空间
