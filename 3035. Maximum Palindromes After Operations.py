"""
LeetCode #3035 - Maximum Palindromes After Operations
回文字符串的最大数量
https://leetcode.cn/problems/maximum-palindromes-after-operations/

给你一个下标从 0 开始的字符串数组 `words` ，数组的长度为 `n` ，且包含下标从 0 开始的若干字符串。
你可以执行以下操作 任意 次数（包括零次）：
选择整数`i`、`j`、`x`和`y`，满足`0 <= i, j < n`，`0 <= x < words[i].length`，`0 <= y < words[j].length`，交换 字符 `words[i][x]` 和 `words[j][y]` 。
返回一个整数，表示在执行一些操作后，`words` 中可以包含的回文串的 最大 数量。
注意：在操作过程中，`i` 和 `j` 可以相等。

示例 1：
输入：words = ["abbb","ba","aa"] 输出：3 解释：在这个例子中，获得最多回文字符串的一种方式是： 选择 i = 0, j = 1, x = 0, y = 0，交换 words[0][0] 和 words[1][0] 。words 变成了 ["bbbb","aa","aa"] 。 words 中的所有字符串都是回文。 因此，可实现的回文字符串的最大数量是 3 。
示例 2：
输入：words = ["abc","ab"] 输出：2 解释：在这个例子中，获得最多回文字符串的一种方式是：  选择 i = 0, j = 1, x = 1, y = 0，交换 words[0][1] 和 words[1][0] 。words 变成了 ["aac","bb"] 。 选择 i = 0, j = 0, x = 1, y = 2，交换 words[0][1] 和 words[0][2] 。words 变成了 ["aca","bb"] 。 两个字符串都是回文 。 因此，可实现的回文字符串的最大数量是 2。
示例 3：
输入：words = ["cd","ef","a"] 输出：1 解释：在这个例子中，没有必要执行任何操作。 words 中有一个回文 "a" 。 可以证明，在执行任何次数操作后，无法得到更多回文。 因此，答案是 1 。

提示：
`1 <= words.length <= 1000`
`1 <= words[i].length <= 100`
`words[i]` 仅由小写英文字母组成。
"""

from typing import List, Optional


class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        """
        Count total pairs of identical characters available.
        Sort words by length ascending. Greedily fill shortest words first:
        each word needs length // 2 pairs and (if odd) one center character.
        Centers can consume singles or break a pair into two singles.
        """
        from collections import Counter

        # Count all characters across all words
        total_chars = 0
        char_count = Counter()
        for w in words:
            total_chars += len(w)
            for c in w:
                char_count[c] += 1

        # Total pairs of identical characters
        pairs = sum(v // 2 for v in char_count.values())
        singles = total_chars - 2 * pairs

        # Sort words by length ascending
        words.sort(key=len)
        ans = 0

        for w in words:
            L = len(w)
            need_pairs = L // 2
            need_center = L % 2

            # Handle center first (may consume singles or break a pair)
            if need_center == 1:
                if singles > 0:
                    singles -= 1
                elif pairs > 0:
                    # Break one pair into two singles, use one as center
                    pairs -= 1
                    singles += 1  # the other half becomes a single
                else:
                    continue  # can't form this palindrome

            # Check if enough pairs remain for symmetric positions
            if need_pairs > pairs:
                continue

            pairs -= need_pairs
            ans += 1

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Hash Table, String, Counting, Sorting
#
# 解题思路:
# 统计所有单词中每个字母的出现次数，计算出可用的"字符对"数量（每对相同字符用于回文的对称位置）
# 和"单字符"数量。将单词按长度升序排列，贪心地从最短单词开始尝试构造回文：
# 回文需要 floor(len/2) 对字符放在对称位置，奇数长度还需一个中心字符。
# 中心字符优先使用未配对的单字符，若无则拆散一对字符。
#
# 时间复杂度: O(N + L log L)，N 为总字符数，L 为单词数
# 空间复杂度: O(26) = O(1)，字母计数
#
# 关键点:
# - 全局字符可任意交换，因此只需考虑字符数量约束而非位置
# - 贪心策略：优先构造短单词（消耗更少资源）
# - 中心字符可通过拆散一对相同字符获得（一对变成两个单字符）
