"""
LeetCode #3325 - Count Substrings With K-Frequency Characters I
字符至少出现 K 次的子字符串 I
https://leetcode.cn/problems/count-substrings-with-k-frequency-characters-i/

给你一个字符串 `s` 和一个整数 `k`，在 `s` 的所有子字符串中，请你统计并返回 至少有一个 字符 至少出现 `k` 次的子字符串总数。
子字符串 是字符串中的一个连续、 非空 的字符序列。

示例 1：

输入： s = "abacb", k = 2
输出： 4
解释：
符合条件的子字符串如下：
`"aba"`（字符 `'a'` 出现 2 次）。
`"abac"`（字符 `'a'` 出现 2 次）。
`"abacb"`（字符 `'a'` 出现 2 次）。
`"bacb"`（字符 `'b'` 出现 2 次）。
示例 2：

输入： s = "abcde", k = 1
输出： 15
解释：
所有子字符串都有效，因为每个字符至少出现一次。

提示：
`1 <= s.length <= 3000`
`1 <= k <= s.length`
`s` 仅由小写英文字母组成。
"""

from typing import List, Optional


class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        cnt = [0] * 26
        left = 0
        for right in range(n):
            cnt[ord(s[right]) - 97] += 1
            while any(c >= k for c in cnt):
                cnt[ord(s[left]) - 97] -= 1
                left += 1
            ans += left
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Hash Table, String, Sliding Window
#
# 解题思路:
# 滑动窗口，统计至少有一个字符出现至少k次的子字符串数量。
# 维护窗口内字符频率，当任意字符频率>=k时，当前窗口的所有后缀都是合法子字符串。
# 左指针移动直到没有字符频率>=k，此时left之前的所有位置都可以作为左端点。
# 答案累加left（即所有以right结尾的合法子字符串的左端点数量）。
#
# 时间复杂度: O(n)，每个字符最多被访问两次
# 空间复杂度: O(26) = O(1)，固定大小频率数组
#
# 关键点:
# - 当窗口满足条件时，所有后缀（更小的窗口）不一定满足，所以用left记录
# - 实际上是统计"不满足条件"的最大窗口，然后通过补集计算
