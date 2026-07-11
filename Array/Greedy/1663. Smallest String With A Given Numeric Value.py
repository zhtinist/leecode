"""
LeetCode #1663 - Smallest String With A Given Numeric Value
中文题名：具有给定数值的最小字符串
https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

The numeric value of a lowercase character is
defined as its position `(1-indexed)` in the alphabet, so the numeric value
of `a` is `1`, the numeric value of `b` is
`2`, the numeric value of `c` is `3`, and so on.

The numeric value of a string consisting of
lowercase characters is defined as the sum of its characters' numeric values. For
example, the numeric value of the string `"abe"` is equal to `1 + 2
+ 5 = 8`.

You are given two integers `n` and `k`. Return the lexicographically
smallest string with length equal to `n` and
numeric value equal to `k`.

Note that a string `x` is lexicographically smaller than string
`y` if `x` comes before `y` in dictionary order,
that is, either `x` is a prefix of `y`, or if `i`
is the first position such that `x[i] != y[i]`, then `x[i]`
comes before `y[i]` in alphabetic order.

Example 1:

Input: n = 3, k = 27
Output: "aay"
Explanation: The numeric value of the string is 1 + 1 + 25 = 27, and it is the smallest string with such a value and length equal to 3.

Example 2:

Input: n = 5, k = 73
Output: "aaszz"

Constraints:

`1 <= n <= 105`

`n <= k <= 26 * n`

【中文翻译】
小写字母的数值定义为它在字母表中的位置（从1开始），即'a'的数值为1，'b'的数值为2，'c'的数值为3，依此类推。

由一个或多个小写字母组成的字符串的数值定义为该字符串中所有字母数值的总和。例如，字符串"abe"的数值等于1+2+5=8。

给定两个整数n和k。返回长度等于n且数值等于k的字典序最小的字符串。

注意，如果字符串x在字典序上小于字符串y，意味着x在字典顺序中排在y之前。具体来说，要么x是y的前缀，要么在第一个x[i]!=y[i]的位置上，x[i]在字母表中排在y[i]之前。

示例1：

输入：n = 3, k = 27
输出："aay"
解释：字符串的数值为1+1+25=27，这是满足长度等于3且数值等于27的最小字符串。

示例2：

输入：n = 5, k = 73
输出："aaszz"

约束条件：

1 <= n <= 10^5
n <= k <= 26 * n

"""

from typing import List, Optional


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        # 从右向左贪心：尽可能填'z'(26)，剩余的值留给左边的位置
        res = [''] * n
        for i in range(n - 1, -1, -1):
            # 当前位置可以选择的最大值：min(26, k - i)
            # k - i 是因为前面 i 个位置至少每个放一个 'a'(1)
            val = min(26, k - i)
            res[i] = chr(ord('a') + val - 1)
            k -= val
        return ''.join(res)










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心法。要得到字典序最小的字符串，应该尽可能让左边的字符小。
# 因此从右向左贪心填充：每个位置尽可能填最大的'z'(值为26)，
# 但要确保前面 i 个位置至少各放一个'a'(值为1)，即当前可填的最大值为 min(26, k - i)。
# 剩余的值继续向左分配。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 贪心策略：从右向左填，优先放'z'(最大值26)
# - 需要保证前面每个位置至少是'a'(值1)，所以当前位置可填的最大值是 min(26, k - i)
# - 答案不需要排序，直接构造即可
