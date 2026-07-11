"""
LeetCode #1433 - Check If a String Can Break Another String
中文题名：检查一个字符串是否可以打破另一个字符串
https://leetcode.com/problems/check-if-a-string-can-break-another-string/

Given two strings: `s1` and `s2` with the same size,
check if some permutation of string `s1` can break some permutation
of string `s2` or vice-versa (in other words `s2` can break `s1`).

A string `x` can break string `y` (both of size
`n`) if `x[i] >= y[i]` (in alphabetical order) for
all `i` between `0` and `n-1`.

Example 1:

Input: s1 = "abc", s2 = "xya"
Output: true
Explanation: "ayx" is a permutation of s2="xya" which can break to string "abc" which is a permutation of s1="abc".

Example 2:

Input: s1 = "abe", s2 = "acd"
Output: false
Explanation: All permutations for s1="abe" are: "abe", "aeb", "bae", "bea", "eab" and "eba" and all permutation for s2="acd" are: "acd", "adc", "cad", "cda", "dac" and "dca". However, there is not any permutation from s1 which can break some permutation from s2 and vice-versa.

Example 3:

Input: s1 = "leetcodee", s2 = "interview"
Output: true

Constraints:

`s1.length == n`

`s2.length == n`

`1 <= n <= 10^5`

All strings consist of lowercase English letters.

【中文翻译】

给定两个长度相同的字符串 `s1` 和 `s2`，检查 `s1` 的某个排列能否打破 `s2` 的某个排列，反之亦然（即 `s2` 能否打破 `s1`）。

字符串 `x` 可以打破字符串 `y`（两者长度均为 `n`），如果对于所有 `0` 到 `n-1` 之间的 `i`，有 `x[i] >= y[i]`（按字母顺序）。

示例 1：
输入：s1 = "abc", s2 = "xya"
输出：true
解释："ayx" 是 s2="xya" 的一个排列，它可以打破字符串 "abc"（s1="abc" 的一个排列）。

示例 2：
输入：s1 = "abe", s2 = "acd"
输出：false
解释：s1="abe" 的所有排列为："abe", "aeb", "bae", "bea", "eab", "eba"，
     s2="acd" 的所有排列为："acd", "adc", "cad", "cda", "dac", "dca"。
     然而，不存在 s1 的排列可以打破 s2 的某个排列，反之亦然。

示例 3：
输入：s1 = "leetcodee", s2 = "interview"
输出：true

约束条件：
`s1.length == n`
`s2.length == n`
`1 <= n <= 10^5`
所有字符串均由小写英文字母组成。

"""

from typing import List, Optional


class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        # 将两个字符串转为字符列表并排序
        arr1 = sorted(s1)
        arr2 = sorted(s2)

        n = len(arr1)

        # 检查 s1 是否能打破 s2
        can_break_1 = True
        for i in range(n):
            if arr1[i] < arr2[i]:
                can_break_1 = False
                break

        # 检查 s2 是否能打破 s1
        can_break_2 = True
        for i in range(n):
            if arr2[i] < arr1[i]:
                can_break_2 = False
                break

        return can_break_1 or can_break_2



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 排序 + 贪心检查法：
# 1. 将 s1 和 s2 的字符分别排序。
# 2. 对排序后的数组，逐位检查两种可能的打破关系：
#    a. 检查 s1 是否能打破 s2：对每个位置 i，检查 sorted_s1[i] >= sorted_s2[i]。
#       如果全部满足，则 s1 可以打破 s2。
#    b. 检查 s2 是否能打破 s1：对每个位置 i，检查 sorted_s2[i] >= sorted_s1[i]。
#       如果全部满足，则 s2 可以打破 s1。
# 3. 如果其中任意一种关系成立，返回 true；否则返回 false。
#
# 为什么排序是正确的？因为如果某个排列可以打破另一个排列，那么将两个字符串
# 都升序排列后，这种打破关系依然成立。换句话说，判断是否存在某个排列能打破
# 对方，等同于检查排序后的字符串是否一一对应地满足打破关系。
# 这是一个经典结论：升序排列是最优的匹配方式。
#
# 时间复杂度: O(N log N)，排序两个长度为 N 的字符串。
# 空间复杂度: O(N)，排序需要的额外空间（或 O(1) 如果使用原地排序）。
#
# 关键点:
# - 排序 + 逐位比较即可判断是否存在打破关系
# - 需要检查两种方向：s1 打破 s2 或 s2 打破 s1
# - 升序排列是最优的排列方式，贪心匹配总是有效的










