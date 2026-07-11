"""
LeetCode #966 - Vowel Spellchecker
中文题名：元音拼写检查器
https://leetcode.com/problems/vowel-spellchecker/

Given a `wordlist`, we want to implement a spellchecker that converts a query
word into a correct word.

For a given `query` word, the spell checker handles two categories of spelling
mistakes:

Capitalization: If the query matches a word in the wordlist
(case-insensitive), then the query word is returned with the same case
as the case in the wordlist.

Example: `wordlist = ["yellow"]`, `query = "YellOw"`:
`correct = "yellow"`

Example: `wordlist = ["Yellow"]`, `query = "yellow"`:
`correct = "Yellow"`

Example: `wordlist = ["yellow"]`, `query = "yellow"`:
`correct = "yellow"`

Vowel Errors: If after replacing the vowels ('a', 'e', 'i',
'o', 'u') of the query word with any vowel individually, it matches a
word in the wordlist (case-insensitive), then the query word is
returned with the same case as the match in the wordlist.

Example: `wordlist = ["YellOw"]`, `query = "yollow"`:
`correct = "YellOw"`

Example: `wordlist = ["YellOw"]`, `query = "yeellow"`:
`correct = ""` (no match)

Example: `wordlist = ["YellOw"]`, `query = "yllw"`:
`correct = ""` (no match)

In addition, the spell checker operates under the following precedence rules:

When the query exactly matches a word in the wordlist (case-sensitive),
you should return the same word back.

When the query matches a word up to capitlization, you should return the first such
match in the wordlist.

When the query matches a word up to vowel errors, you should return the first such match
in the wordlist.

If the query has no matches in the wordlist, you should return the empty string.

Given some `queries`, return a list of words `answer`, where
`answer[i]` is the correct word for `query = queries[i]`.

Example 1:

Input: wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]

Note:

`1 <= wordlist.length <= 5000`

`1 <= queries.length <= 5000`

`1 <= wordlist[i].length <= 7`

`1 <= queries[i].length <= 7`

All strings in `wordlist` and `queries` consist only of english letters.

【中文翻译】
给定一个单词列表 `wordlist`，我们要实现一个拼写检查器，将查询单词转换为正确的单词。
对于给定的查询单词 `query`，拼写检查器处理两类拼写错误：
1. 大小写：如果查询单词与单词列表中的某个单词匹配（不区分大小写），
   则返回单词列表中相同大小写形式的单词。
2. 元音错误：如果将查询单词中的元音字母（'a', 'e', 'i', 'o', 'u'）替换为任意元音后，
   与单词列表中的某个单词匹配（不区分大小写），则返回单词列表中的匹配项。
优先级规则：
- 当查询单词与单词列表中的单词完全匹配（区分大小写）时，返回该单词。
- 当查询单词匹配到大小写变体时，返回单词列表中第一个匹配项。
- 当查询单词匹配到元音错误变体时，返回单词列表中第一个匹配项。
- 如果查询单词没有匹配项，返回空字符串。

"""

from typing import List, Optional


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = set('aeiou')

        def to_vowel_pattern(word: str) -> str:
            """将单词转为元音通配模式（小写，元音替换为 '*'）"""
            return ''.join('*' if c in vowels else c for c in word.lower())

        exact = {}           # 精确匹配
        case_insensitive = {}  # 不区分大小写
        vowel_pattern = {}     # 元音通配

        for word in wordlist:
            exact.setdefault(word, word)
            case_insensitive.setdefault(word.lower(), word)
            vowel_pattern.setdefault(to_vowel_pattern(word), word)

        result = []
        for query in queries:
            if query in exact:
                result.append(exact[query])
            elif query.lower() in case_insensitive:
                result.append(case_insensitive[query.lower()])
            elif to_vowel_pattern(query) in vowel_pattern:
                result.append(vowel_pattern[to_vowel_pattern(query)])
            else:
                result.append("")

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用三个哈希表分别处理三种匹配优先级：
# 1. exact: 存储原词 -> 原词（精确匹配，区分大小写）
# 2. case_insensitive: 存储小写词 -> 原词（不区分大小写匹配）
# 3. vowel_pattern: 存储元音通配模式 -> 原词（元音错误匹配）
#    元音通配模式：将单词转为小写，所有元音替换为 '*'。
# 使用 setdefault 保证只保留第一个出现的匹配项（满足"返回第一个匹配项"的要求）。
# 查询时按优先级依次检查三个哈希表即可。
#
# 时间复杂度: O(W + Q) — W 为单词列表总长度，Q 为查询列表总长度
# 空间复杂度: O(W) — 三个哈希表存储单词列表
#
# 关键点:
# - 三个哈希表对应三种优先级（精确 > 大小写 > 元音错误）
# - setdefault 确保保留第一个匹配项（符合题目要求）
# - 元音通配模式统一用 '*' 替换所有元音
# - 查询按优先级顺序依次尝试匹配
