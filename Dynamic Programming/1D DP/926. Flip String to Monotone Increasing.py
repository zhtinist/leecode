"""
LeetCode #926 - Flip String to Monotone Increasing
中文题名：将字符串翻转到单调递增
https://leetcode.com/problems/flip-string-to-monotone-increasing/

A string of `'0'`s and `'1'`s is monotone
increasing if it consists of some number of `'0'`s (possibly 0),
followed by some number of `'1'`s (also possibly 0.)

We are given a string `S` of `'0'`s and
`'1'`s, and we may flip any `'0'` to a `'1'`
or a `'1'` to a `'0'`.

Return the minimum number of flips to make `S` monotone increasing.

Example 1:

Input: "00110"
Output: 1
Explanation: We flip the last digit to get 00111.

Example 2:

Input: "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.

Example 3:

Input: "00011000"
Output: 2
Explanation: We flip to get 00000000.

Note:

`1 <= S.length <= 20000`

`S` only consists of `'0'` and
`'1'` characters.

【中文翻译】

一个由 '0' 和 '1' 组成的字符串，如果它由若干个 '0'（可能为 0 个）后跟
若干个 '1'（也可能为 0 个）组成，则称其为单调递增的。
给定一个由 '0' 和 '1' 组成的字符串 S，我们可以将任意 '0' 翻转为 '1' 或
将任意 '1' 翻转为 '0'。返回使 S 单调递增所需的最小翻转次数。

"""

from typing import List, Optional


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        """
        DP approach: track minimum flips to end with '0' or '1'.
        For each character:
        - To end with '0': must flip '1'→'0', and previous must end with '0'
        - To end with '1': can come from '0' or '1', choose min flips
        """
        # flips to make prefix monotone ending with '0' or '1'
        end_with_0 = 0  # flips to end with 0 so far
        end_with_1 = 0  # flips to end with 1 so far

        for ch in s:
            if ch == '0':
                # To end with 0: no flip needed, keep end_with_0
                # To end with 1: must flip '0'→'1', min of previous states + 1
                end_with_1 = min(end_with_0, end_with_1) + 1
                # end_with_0 stays the same (no flip for 0)
            else:  # ch == '1'
                # To end with 0: must flip '1'→'0', end_with_0 + 1
                # To end with 1: no flip needed, min of previous states
                end_with_1 = min(end_with_0, end_with_1)
                end_with_0 = end_with_0 + 1

        return min(end_with_0, end_with_1)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 动态规划：维护两个状态
# - end_with_0：使前缀变为以 '0' 结尾的单调递增字符串所需的最小翻转次数
# - end_with_1：使前缀变为以 '1' 结尾的单调递增字符串所需的最小翻转次数
#
# 遍历每个字符：
# - 如果当前字符是 '0'：
#   - 以 '0' 结尾：不需要翻转，保持 end_with_0
#   - 以 '1' 结尾：必须翻转为 '1'，翻转次数 = min(end_with_0, end_with_1) + 1
# - 如果当前字符是 '1'：
#   - 以 '0' 结尾：必须翻转为 '0'，翻转次数 = end_with_0 + 1
#   - 以 '1' 结尾：不需要翻转，翻转次数 = min(end_with_0, end_with_1)
#
# 时间复杂度: O(N)
# 空间复杂度: O(1)
#
# 关键点:
# - 单调递增意味着最终形式是 0...01...1
# - 也可以枚举分界点：对每个位置 i，将前 i 个全变成 0，后面全变成 1
# - DP 方法更简洁且空间效率更高
