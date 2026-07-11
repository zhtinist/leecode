"""
LeetCode #893 - Groups of Special-Equivalent Strings
中文题名：特殊等价字符串组
https://leetcode.com/problems/groups-of-special-equivalent-strings/

You are given an array `A` of strings.

Two strings `S` and `T` are special-equivalent if
after any number of moves, S == T.

A move consists of choosing two indices `i` and `j` with
`i % 2 == j % 2`, and swapping `S[i]` with `S[j]`.

Now, a group of special-equivalent strings from `A` is a non-empty
subset S of `A` such that any string not in S is not special-equivalent
with any string in S.

Return the number of groups of special-equivalent strings from `A`.

Example 1:

Input: ["a","b","c","a","c","c"]
Output: 3
Explanation: 3 groups ["a","a"], ["b"], ["c","c","c"]

Example 2:

Input: ["aa","bb","ab","ba"]
Output: 4
Explanation: 4 groups ["aa"], ["bb"], ["ab"], ["ba"]

Example 3:

Input: ["abc","acb","bac","bca","cab","cba"]
Output: 3
Explanation: 3 groups ["abc","cba"], ["acb","bca"], ["bac","cab"]

Example 4:

Input: ["abcd","cdab","adcb","cbad"]
Output: 1
Explanation: 1 group ["abcd","cdab","adcb","cbad"]

Note:

`1 <= A.length <= 1000`

`1 <= A[i].length <= 20`

All `A[i]` have the same length.

All `A[i]` consist of only lowercase letters.

【中文翻译】

给定一个字符串数组 `A`。

如果经过任意次数的移动后，两个字符串 `S` 和 `T` 可以变得相等，则称它们是特殊等价的。

一次移动包括选择两个下标 `i` 和 `j`，其中 `i % 2 == j % 2`，然后交换 `S[i]` 与 `S[j]`。

`A` 中的一个特殊等价字符串组是 `A` 的一个非空子集 S，使得任何不在 S 中的字符串与 S 中的任何字符串都不是特殊等价的。

返回 `A` 中特殊等价字符串组的数量。

"""

from typing import List, Optional


class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        def get_signature(s: str) -> tuple:
            # 偶数位字符排序 + 奇数位字符排序 作为唯一签名
            even_chars = sorted(s[0::2])
            odd_chars = sorted(s[1::2])
            return (tuple(even_chars), tuple(odd_chars))

        groups = set()
        for s in A:
            groups.add(get_signature(s))

        return len(groups)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 关键洞察：由于只能交换相同奇偶性的位置（i%2 == j%2），
# 偶数位置的字符可以在偶数位之间任意排列，奇数位同理。
# 因此，两个字符串特殊等价 <=> 它们的偶数位字符排序后相同 且 奇数位字符排序后相同。
# 为每个字符串生成签名：(sorted(even_chars), sorted(odd_chars))
# 用集合统计不同签名的数量即为组数。
#
# 时间复杂度: O(N * K log K) — N为字符串数，K为字符串长度（排序开销）
# 空间复杂度: O(N * K) — 集合存储所有签名
#
# 关键点:
# - 交换限制意味着偶/奇位置各自独立可任意排列
# - 排序后比较是判断特殊等价的充要条件
# - 所有字符串长度相同（题目保证）
