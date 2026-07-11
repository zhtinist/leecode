"""
LeetCode #2957 - Remove Adjacent Almost-Equal Characters
消除相邻近似相等字符
https://leetcode.cn/problems/remove-adjacent-almost-equal-characters/

给你一个下标从 0 开始的字符串 `word` 。
一次操作中，你可以选择 `word` 中任意一个下标 `i` ，将 `word[i]` 修改成任意一个小写英文字母。
请你返回消除 `word` 中所有相邻 近似相等 字符的 最少 操作次数。
两个字符 `a` 和 `b` 如果满足 `a == b` 或者 `a` 和 `b` 在字母表中是相邻的，那么我们称它们是 近似相等 字符。

示例 1：
输入：word = "aaaaa" 输出：2 解释：我们将 word 变为 "acaca" ，该字符串没有相邻近似相等字符。 消除 word 中所有相邻近似相等字符最少需要 2 次操作。
示例 2：
输入：word = "abddez" 输出：2 解释：我们将 word 变为 "ybdoez" ，该字符串没有相邻近似相等字符。 消除 word 中所有相邻近似相等字符最少需要 2 次操作。
示例 3：
输入：word = "zyxyxyz" 输出：3 解释：我们将 word 变为 "zaxaxaz" ，该字符串没有相邻近似相等字符。 消除 word 中所有相邻近似相等字符最少需要 3 次操作

提示：
`1 <= word.length <= 100`
`word` 只包含小写英文字母。
"""

from typing import List, Optional


class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)
        ans = 0
        i = 1
        while i < n:
            if abs(ord(word[i]) - ord(word[i - 1])) <= 1:
                ans += 1
                i += 2  # skip the changed character and move to next pair
            else:
                i += 1
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, String, Dynamic Programming
#
# 解题思路:
# 从左到右扫描，若 word[i-1] 和 word[i] 近似相等（字符相同或字母表相邻），则必须修改其中一个。
# 贪心修改 word[i]（而非 word[i-1]），因为修改后面的不会影响前面已处理的部分。
# 修改后可以选一个与前后都不近似的字符，因此可跳过 i+1 继续（i += 2）。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 近似相等 = 字符相同 或 ASCII 差值为 1
# - 贪心修改后者，跳过一个位置避免重复计数
# - 总共有 26 个字母，一定能找到不与邻居近似相等的替换字符
