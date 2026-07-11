"""
LeetCode #2645 - Minimum Additions to Make Valid String
构造有效字符串的最少插入数
https://leetcode.cn/problems/minimum-additions-to-make-valid-string/

给你一个字符串 `word` ，你可以向其中任何位置插入 "a"、"b" 或 "c" 任意次，返回使 `word` 有效 需要插入的最少字母数。
如果字符串可以由 "abc" 串联多次得到，则认为该字符串 有效 。

示例 1：
输入：word = "b" 输出：2 解释：在 "b" 之前插入 "a" ，在 "b" 之后插入 "c" 可以得到有效字符串 "abc" 。
示例 2：
输入：word = "aaa" 输出：6 解释：在每个 "a" 之后依次插入 "b" 和 "c" 可以得到有效字符串 "abcabcabc" 。
示例 3：
输入：word = "abc" 输出：0 解释：word 已经是有效字符串，不需要进行修改。

提示：
`1 <= word.length <= 50`
`word` 仅由字母 "a"、"b" 和 "c" 组成。
"""

from typing import List, Optional


class Solution:
    def addMinimum(self, word: str) -> int:
        # count how many "abc" groups are needed
        # each character must appear in its proper order within abc pattern
        ans = 0
        n = len(word)
        i = 0
        while i < n:
            # start a new "abc" group
            for expected in ('a', 'b', 'c'):
                if i < n and word[i] == expected:
                    i += 1
                else:
                    ans += 1
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Stack, Greedy, String, Dynamic Programming
#
# 解题思路:
# 贪心匹配"abc"模式。遍历word，对每个字符按a->b->c的顺序匹配。
# 如果当前字符与期望的字符匹配则前进word指针，否则需要插入一个字符。
# 每个"abc"组中跳过的不匹配位置都需要插入，直到word全部匹配完成。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 有效字符串是"abc"的重复，所以按a->b->c循环匹配
# - 贪心策略：尽量让每个word字符匹配到它应该出现的位置
# - 不匹配时计数插入，但保留word指针继续尝试匹配下一个期望字符
