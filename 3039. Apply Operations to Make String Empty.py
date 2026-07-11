"""
LeetCode #3039 - Apply Operations to Make String Empty
进行操作使字符串为空
https://leetcode.cn/problems/apply-operations-to-make-string-empty/

给你一个字符串 `s` 。
请你进行以下操作直到 `s` 为 空 ：
每次操作 依次 遍历 `'a'` 到 `'z'`，如果当前字符出现在 `s` 中，那么删除出现位置 最早 的该字符（如果存在的话）。
例如，最初 `s = "aabcbbca"`。我们执行下述操作：
移除下划线的字符  `s = "aabcbbca"`。结果字符串为 `s = "abbca"`。
移除下划线的字符  `s = "abbca"`。结果字符串为 `s = "ba"`。
移除下划线的字符  `s = "ba"`。结果字符串为 `s = ""`。
请你返回进行 最后 一次操作 之前 的字符串 `s` 。在上面的例子中，答案是 `"ba"`。

示例 1：
输入：s = "aabcbbca" 输出："ba" 解释：已经在题目描述中解释。
示例 2：
输入：s = "abcd" 输出："abcd" 解释：我们进行以下操作： - 删除 s = "abcd" 中加粗加斜字符，得到字符串 s = "" 。 进行最后一次操作之前的字符串为 "abcd" 。

提示：
`1 <= s.length <= 5 * 10^5`
`s` 只包含小写英文字母。
"""

from typing import List, Optional


class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        """
        Each operation deletes the earliest occurrence of each character
        present in s. The characters with maximum frequency survive
        the longest. Before the last operation, each max-frequency
        character has exactly one occurrence left (its last one).
        """
        from collections import Counter

        count = Counter(s)
        max_freq = max(count.values())

        # Track last occurrence position of each character
        last_pos = {}
        for i, c in enumerate(s):
            last_pos[c] = i

        # Characters with max frequency, ordered by their last occurrence
        result_chars = [
            (last_pos[c], c)
            for c in count
            if count[c] == max_freq
        ]
        result_chars.sort()  # sort by position

        return ''.join(c for _, c in result_chars)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Counting, Sorting
#
# 解题思路:
# 每次操作删除当前字符串中每个字母最早出现的一次。出现次数最多的字母（max_freq）能"存活"最久。
# 在执行 max_freq - 1 次操作后，所有出现次数为 max_freq 的字母都仅剩一个（最后一个未被删除的）。
# 最后一次操作前的字符串由这些字母按它们在原字符串中最后出现的位置排序组成。
#
# 时间复杂度: O(n)，遍历字符串统计和找最后位置
# 空间复杂度: O(26) = O(1)，字母计数
#
# 关键点:
# - 每次操作删除每个字母的"最早"出现，相当于每轮消耗每个字母的一个副本
# - 出现次数最多的字母决定了操作总轮数
# - 最后剩下的字符顺序由其最后出现位置决定
