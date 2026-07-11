"""
LeetCode #1737 - Change Minimum Characters to Satisfy One of Three Conditions
中文题名：满足三条件之一需改变的最少字符数
https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/

You are given two strings `a` and `b` that consist of
lowercase letters. In one operation, you can change any character in `a` or
`b` to any lowercase letter.

Your goal is to satisfy one of the following three conditions:

Every letter in `a` is strictly
less than every letter in `b` in the
alphabet.

Every letter in `b` is strictly
less than every letter in `a` in the
alphabet.

Both `a` and `b` consist of only
one distinct letter.

Return the minimum number of operations needed to achieve your
goal.

Example 1:

Input: a = "aba", b = "caa"
Output: 2
Explanation: Consider the best way to make each condition true:
1) Change b to "ccc" in 2 operations, then every letter in a is less than every letter in b.
2) Change a to "bbb" and b to "aaa" in 3 operations, then every letter in b is less than every letter in a.
3) Change a to "aaa" and b to "aaa" in 2 operations, then a and b consist of one distinct letter.
The best way was done in 2 operations (either condition 1 or condition 3).

Example 2:

Input: a = "dabadd", b = "cda"
Output: 3
Explanation: The best way is to make condition 1 true by changing b to "eee".

Constraints:

`1 <= a.length, b.length <= 105`

`a` and `b` consist only of lowercase letters.

【中文翻译】
给定两个字符串 a 和 b，只包含小写字母。每次操作可以将一个字符改为任意小写字母。
求满足以下三个条件之一的最少操作次数：
1. a 中的每个字母严格小于 b 中的每个字母
2. b 中的每个字母严格小于 a 中的每个字母
3. a 和 b 都只包含同一个字母

示例 1：
输入: a = "aba", b = "caa"
输出: 2
解释: 条件1：将a的'b'改为'c'前面(如'b'→'a', 'c'→'d')...最优是条件3：将所有字符改为'a'需3次操作，改为'c'需4次...实际答案是改为全部'b'。
"""

from typing import List, Optional


class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        count_a = [0] * 26
        count_b = [0] * 26
        for ch in a:
            count_a[ord(ch) - 97] += 1
        for ch in b:
            count_b[ord(ch) - 97] += 1

        m, n = len(a), len(b)
        ans = float('inf')

        # 条件3：都变成同一个字符
        for i in range(26):
            ans = min(ans, m + n - count_a[i] - count_b[i])

        # 条件1：a 中所有字母 < b 中所有字母
        # 选择分割点 i，a 中的字母 < i，b 中的字母 >= i
        prefix_a = 0
        prefix_b = 0
        for i in range(25):  # i 是分割字母的索引
            prefix_a += count_a[i]
            prefix_b += count_b[i]
            # a 中 >= (i+1) 的需改成 < (i+1)，b 中 <= i 的需改成 > i
            cost1 = (m - prefix_a) + prefix_b
            ans = min(ans, cost1)

        # 条件2：b 中所有字母 < a 中所有字母
        prefix_a = 0
        prefix_b = 0
        for i in range(25):
            prefix_a += count_a[i]
            prefix_b += count_b[i]
            cost2 = (n - prefix_b) + prefix_a
            ans = min(ans, cost2)

        return ans
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 统计两个字符串中每个字符的频率。
# 条件3：枚举目标字符，需要改变的数量 = 总长度 - 该字符在两个字符串中出现的次数。
# 条件1：枚举分割字母 i（0-24），使 a 只含 <=i 的字母，b 只含 >i 的字母。
#   需要改变：a 中 >i 的字母 + b 中 <=i 的字母。
# 条件2：同理，b 的字母 < a 的字母。
# 取三种条件的最小值。
#
# 时间复杂度: O(N + M + 26) — 统计 + 枚举26个字母
# 空间复杂度: O(1) — 固定大小计数数组
#
# 关键点:
# - 三个条件独立计算后取最小值
# - 条件1和2的分割字母枚举只需 O(26)
# - 前缀和维护快速计算改变数
