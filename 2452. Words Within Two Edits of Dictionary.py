"""
LeetCode #2452 - Words Within Two Edits of Dictionary
距离字典两次编辑以内的单词
https://leetcode.cn/problems/words-within-two-edits-of-dictionary/

给你两个字符串数组 `queries` 和 `dictionary` 。数组中所有单词都只包含小写英文字母，且长度都相同。
一次 编辑 中，你可以从 `queries` 中选择一个单词，将任意一个字母修改成任何其他字母。从 `queries` 中找到所有满足以下条件的字符串：不超过 两次编辑内，字符串与 `dictionary` 中某个字符串相同。
请你返回 `queries` 中的单词列表，这些单词距离 `dictionary` 中的单词 编辑次数 不超过 两次 。单词返回的顺序需要与 `queries` 中原本顺序相同。

示例 1：
输入：queries = ["word","note","ants","wood"], dictionary = ["wood","joke","moat"] 输出：["word","note","wood"] 解释： - 将 "word" 中的 'r' 换成 'o' ，得到 dictionary 中的单词 "wood" 。 - 将 "note" 中的 'n' 换成 'j' 且将 't' 换成 'k' ，得到 "joke" 。 - "ants" 需要超过 2 次编辑才能得到 dictionary 中的单词。 - "wood" 不需要修改（0 次编辑），就得到 dictionary 中相同的单词。 所以我们返回 ["word","note","wood"] 。
示例 2：
输入：queries = ["yes"], dictionary = ["not"] 输出：[] 解释： "yes" 需要超过 2 次编辑才能得到 "not" 。 所以我们返回空数组。

提示：
`1 <= queries.length, dictionary.length <= 100`
`n == queries[i].length == dictionary[j].length`
`1 <= n <= 100`
所有 `queries[i]` 和 `dictionary[j]` 都只包含小写英文字母。
"""

from typing import List, Optional


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        result = []
        for query in queries:
            for word in dictionary:
                diff = 0
                for c1, c2 in zip(query, word):
                    if c1 != c2:
                        diff += 1
                    if diff > 2:
                        break
                if diff <= 2:
                    result.append(query)
                    break
        return result


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Trie, Array, String
#
# 解题思路:
# 对于每个查询单词，逐一与字典中的每个单词比较。统计两个单词中不同字符的数量（汉明距离）。
# 如果差异数 <= 2，则将该查询单词加入结果并跳出内层循环，继续处理下一个查询单词。
# 由于所有单词长度相同且数据规模小（q, d, n <= 100），暴力比较完全可行。
#
# 时间复杂度: O(q * d * n)，其中 q = 查询数量，d = 字典大小，n = 单词长度
# 空间复杂度: O(1)，不计输出结果
#
# 关键点:
# - 使用 zip 同时遍历两个字符串，逐字符比较
# - 提前剪枝：当 diff > 2 时立即跳出内层循环，不再继续比较
# - 找到一个匹配后 break，继续下一个查询单词
