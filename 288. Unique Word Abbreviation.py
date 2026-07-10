"""
LeetCode #288 - Unique Word Abbreviation
https://leetcode.com/problems/unique-word-abbreviation/

An abbreviation of a word follows the form <first letter><number><last letter>.
Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

1
&darr;
b) d|o|g                   --> d1g

1    1  1
1---5----0----5--8
&darr;   &darr;    &darr;    &darr;  &darr;
c) i|nternationalizatio|n  --> i18n

1
1---5----0
&darr;   &darr;    &darr;
d) l|ocalizatio|n          --> l10n

Assume you have a dictionary and given a word, find whether its abbreviation is unique in the
dictionary. A word's abbreviation is unique if no *other* word from the dictionary
has the same abbreviation.

Example:

Given dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") -> `false`
isUnique("cart") -> `true`
isUnique("cane") -> `false`
isUnique("make") -> `true`
"""

from typing import List, Optional


class ValidWordAbbr:
    """Validate if a word's abbreviation is unique in the dictionary.

    A word's abbreviation is unique if no OTHER word in the dictionary
    has the same abbreviation.
    """

    def __init__(self, dictionary: List[str]):
        # Map from abbreviation to set of words with that abbreviation
        self.abbr_map = {}
        for word in dictionary:
            abbr = self._get_abbr(word)
            if abbr not in self.abbr_map:
                self.abbr_map[abbr] = set()
            self.abbr_map[abbr].add(word)

    def _get_abbr(self, word: str) -> str:
        """Get abbreviation: first letter + middle count + last letter."""
        if len(word) <= 2:
            return word
        return word[0] + str(len(word) - 2) + word[-1]

    def isUnique(self, word: str) -> bool:
        """Check if word's abbreviation is unique."""
        abbr = self._get_abbr(word)
        if abbr not in self.abbr_map:
            return True
        # Unique if the only word with this abbreviation is the word itself
        words_with_abbr = self.abbr_map[abbr]
        return len(words_with_abbr) == 1 and word in words_with_abbr


class Solution:
    """
    This problem uses ValidWordAbbr class, not Solution.
    The ValidWordAbbr implementation above is the complete solution.
    """
    pass


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: Yes
#
# 解题思路:
# 使用哈希表存储缩写到单词集合的映射。
# 初始化时，遍历字典中的所有单词，计算每个单词的缩写，将单词加入对应缩写的集合。
# 缩写规则：对于长度 <= 2 的单词，缩写就是单词本身。否则缩写为首字母
# + 中间字母数量 + 尾字母（如 "dog" -> "d1g", "internationalization" -> "i18n"）。
# isUnique 检查：如果缩写不在映射中，返回 True。如果在，只有当集合中只有
# 该单词本身时才返回 True（因为 unique 的定义是"没有其他单词有相同的缩写"）。
#
# 时间复杂度: O(N * L) 初始化（N 个单词，每个计算缩写 O(1)）
#   isUnique: O(1) 平均
# 空间复杂度: O(N) - 存储所有单词的缩写映射
#
# 关键点:
# - 缩写唯一性定义：没有**其他**单词有相同的缩写（单词自身可以匹配）
# - 用 set 存储同一缩写下的所有单词，方便判断
# - 长度 <= 2 的单词不需要缩写
# - 注意：如果 dictionary 有重复单词，它们共享同一个缩写，也算 unique
