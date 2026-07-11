"""
LeetCode #2840 - Check if Strings Can be Made Equal With Operations II
判断通过操作能否让字符串相等 II
https://leetcode.cn/problems/check-if-strings-can-be-made-equal-with-operations-ii/

给你两个字符串 `s1` 和 `s2` ，两个字符串长度都为 `n` ，且只包含 小写 英文字母。
你可以对两个字符串中的 任意一个 执行以下操作 任意 次：
选择两个下标 `i` 和 `j` ，满足 `i < j` 且 `j - i` 是 偶数，然后 交换 这个字符串中两个下标对应的字符。

如果你可以让字符串 `s1` 和 `s2` 相等，那么返回 `true` ，否则返回 `false` 。

示例 1：
输入：s1 = "abcdba", s2 = "cabdab" 输出：true 解释：我们可以对 s1 执行以下操作： - 选择下标 i = 0 ，j = 2 ，得到字符串 s1 = "cbadba" 。 - 选择下标 i = 2 ，j = 4 ，得到字符串 s1 = "cbbdaa" 。 - 选择下标 i = 1 ，j = 5 ，得到字符串 s1 = "cabdab" = s2 。
示例 2：
输入：s1 = "abe", s2 = "bea" 输出：false 解释：无法让两个字符串相等。

提示：
`n == s1.length == s2.length`
`1 <= n <= 10^5`
`s1` 和 `s2` 只包含小写英文字母。
"""

from typing import List, Optional


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n = len(s1)
        even1, odd1 = [], []
        even2, odd2 = [], []
        for i in range(n):
            if i % 2 == 0:
                even1.append(s1[i])
                even2.append(s2[i])
            else:
                odd1.append(s1[i])
                odd2.append(s2[i])
        even1.sort()
        even2.sort()
        odd1.sort()
        odd2.sort()
        return even1 == even2 and odd1 == odd2



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Hash Table, String, Sorting
#
# 解题思路:
# 由于只能交换距离为偶数的两个位置，因此偶数索引位置之间可以任意交换，奇数索引位置之间可以任意交换，
# 但奇偶之间不能交换。只需分别取出 s1 和 s2 的偶数位置字符和奇数位置字符，排序后比较是否相等即可。
#
# 时间复杂度: O(n log n)
# 空间复杂度: O(n)
#
# 关键点:
# - 操作只能在同一奇偶性索引之间进行，奇偶位置之间无法交换
# - 分别收集奇偶位置的字符，排序后比较
# - 两个字符串相等当且仅当奇偶位置的字符集合完全相同
