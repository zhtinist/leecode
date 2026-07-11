"""
LeetCode #1689 - Partitioning Into Minimum Number Of Deci-Binary Numbers
中文题名：分割成最少数量的十进制二进制数
https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

A decimal number is called deci-binary if each of its digits is
either `0` or `1` without any leading zeros. For example, `101`
and `1100` are deci-binary, while `112` and
`3001` are not.

Given a string `n` that represents a positive decimal integer, return the
minimum number of positive deci-binary numbers
needed so that they sum up to `n`.

Example 1:

Input: n = "32"
Output: 3
Explanation: 10 + 11 + 11 = 32

Example 2:

Input: n = "82734"
Output: 8

Example 3:

Input: n = "27346209830709182346"
Output: 9

Constraints:

`1 <= n.length <= 105`

`n` consists of only digits.

`n` does not contain any leading zeros and represents a positive
integer.

【中文翻译】
如果一个十进制数字的每一位要么是 `0` 要么是 `1`，且没有前导零，则称该数字为「十进制二进制数」。例如，
`101` 和 `1100` 是十进制二进制数，而 `112` 和 `3001` 不是。

给定一个表示正十进制整数的字符串 `n`，返回使得它们相加等于 `n` 所需的最少正十进制二进制数的数量。

示例 1：

输入: n = "32"
输出: 3
解释: 10 + 11 + 11 = 32

示例 2：

输入: n = "82734"
输出: 8

示例 3：

输入: n = "27346209830709182346"
输出: 9

约束条件：

`1 <= n.length <= 10^5`

`n` 仅由数字组成。

`n` 不包含任何前导零，并表示一个正整数。
"""

from typing import List, Optional


class Solution:
    def minPartitions(self, n: str) -> int:
        """
        每个十进制二进制数的每一位只能是 0 或 1，因此对于 n 的每一位，
        要凑出该位的数字 d，至少需要 d 个十进制二进制数。
        答案就是 n 中的最大数字字符。
        """
        return int(max(n))










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 由于每个十进制二进制数的每一位只能是 0 或 1，因此对于 n 的每一位数字 d，
# 至少需要 d 个十进制二进制数才能使该位之和等于 d。
# 反过来，构造 max_digit 个十进制二进制数一定可以凑出 n：
# 对于每一位，前 d 个数在该位放 1，其余放 0。
# 所以答案就是 n 中的最大数字字符的整数值。
#
# 时间复杂度: O(L)，其中 L 是字符串 n 的长度
# 空间复杂度: O(1)
#
# 关键点:
# - 核心洞察：十进制二进制数的每位只能是 0 或 1，因此每位最多贡献 1
# - 答案就是 max(n 的所有数字)，与 n 的长度无关
# - 无需真正构造这些十进制二进制数，只需找到最大数位
