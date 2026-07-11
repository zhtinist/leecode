"""
LeetCode #2405 - Optimal Partition of String
子字符串的最优划分
https://leetcode.cn/problems/optimal-partition-of-string/

给你一个字符串 `s` ，请你将该字符串划分成一个或多个 子字符串 ，并满足每个子字符串中的字符都是 唯一 的。也就是说，在单个子字符串中，字母的出现次数都不超过 一次 。
满足题目要求的情况下，返回 最少 需要划分多少个子字符串。
注意，划分后，原字符串中的每个字符都应该恰好属于一个子字符串。

示例 1：
输入：s = "abacaba" 输出：4 解释： 两种可行的划分方法分别是 ("a","ba","cab","a") 和 ("ab","a","ca","ba") 。 可以证明最少需要划分 4 个子字符串。
示例 2：
输入：s = "ssssss" 输出：6 解释： 只存在一种可行的划分方法 ("s","s","s","s","s","s") 。

提示：
`1 <= s.length <= 10^5`
`s` 仅由小写英文字母组成
"""

from typing import List, Optional


class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        count = 1
        for ch in s:
            if ch in seen:
                count += 1
                seen.clear()
            seen.add(ch)
        return count



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Hash Table, String
#
# 解题思路:
# 贪心策略：遍历字符串，使用集合记录当前子串中出现的字符。
# 当遇到重复字符时，表示当前子串需要结束，划分计数加一，清空集合并重新开始。
# 最后返回划分的子串数量。
#
# 时间复杂度: O(n)，n为字符串长度，只需一次遍历。
# 空间复杂度: O(1)，集合最多存储26个小写字母。
#
# 关键点:
# - 贪心划分：每次遇到重复字符就切分，能保证最少子串数。
# - 使用set快速判断字符是否在当前子串中出现过。
