"""
LeetCode #809 - Expressive Words
中文题名：情感丰富的文字
https://leetcode.com/problems/expressive-words/

Sometimes people repeat letters to represent extra feeling, such as "hello" ->
"heeellooo", "hi" -> "hiiii".  In these strings like
"heeellooo", we have groups of adjacent letters that are all the same:
"h", "eee", "ll", "ooo".

For some given string `S`, a query word is stretchy if it can be made to
be equal to `S` by any number of applications of the following extension
operation: choose a group consisting of characters `c`, and add some number
of characters `c` to the group so that the size of the group is 3 or more.

For example, starting with "hello", we could do an extension on the group "o"
to get "hellooo", but we cannot get "helloo" since the group "oo"
has size less than 3.  Also, we could do another extension like "ll" ->
"lllll" to get "helllllooo".  If `S =
"helllllooo"`, then the query word "hello" would be stretchy
because of these two extension operations: `query = "hello" -> "hellooo"
-> "helllllooo" = S`.

Given a list of query words, return the number of words that are stretchy.

Example:
Input:
S = "heeellooo"
words = ["hello", "hi", "helo"]
Output: 1
Explanation:
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.

Notes:

`0 <= len(S) <= 100`.

`0 <= len(words) <= 100`.

`0 <= len(words[i]) <= 100`.

`S` and all words in `words` consist only of lowercase
letters

【中文翻译】
有时候人们会重复字母来表达额外情感，例如 "hello" -> "heeellooo"、"hi" -> "hiiii"。在这些像 "heeellooo" 的字符串中，我们有相邻相同字母的组："h"、"eee"、"ll"、"ooo"。

对于给定的字符串 `S`，如果一个查询单词可以通过任意次以下扩展操作变成 `S`，则该单词是"可伸展的"：选择一个由字符 `c` 构成的组，向该组添加若干字符 `c`，使得组的大小达到 3 或以上。

例如，从 "hello" 开始，我们可以对组 "o" 进行扩展得到 "hellooo"，但不能得到 "helloo"，因为组 "oo" 的大小小于 3。我们也可以再做一次扩展如 "ll" -> "lllll" 得到 "helllllooo"。如果 `S = "helllllooo"`，那么查询单词 "hello" 是"可伸展的"，因为可以通过两次扩展操作：`query = "hello" -> "hellooo" -> "helllllooo" = S`。

给定一个查询单词列表，返回其中"可伸展的"单词数量。

示例：
输入：S = "heeellooo", words = ["hello", "hi", "helo"]
输出：1
解释：我们可以扩展 "hello" 中的 "e" 和 "o" 得到 "heeellooo"。
无法扩展 "helo" 得到 "heeellooo"，因为组 "ll" 的大小不足 3。

注意：
`0 <= len(S) <= 100`。
`0 <= len(words) <= 100`。
`0 <= len(words[i]) <= 100`。
`S` 和 `words` 中的所有单词只包含小写字母。
"""

from typing import List, Optional


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def is_stretchy(word: str) -> bool:
            i = j = 0
            n, m = len(s), len(word)
            while i < n and j < m:
                if s[i] != word[j]:
                    return False
                # Count consecutive chars in S
                cnt_s = 1
                while i + cnt_s < n and s[i + cnt_s] == s[i]:
                    cnt_s += 1
                # Count consecutive chars in word
                cnt_w = 1
                while j + cnt_w < m and word[j + cnt_w] == word[j]:
                    cnt_w += 1
                if cnt_s < cnt_w:
                    return False
                if cnt_s > cnt_w and cnt_s < 3:
                    return False
                i += cnt_s
                j += cnt_w
            return i == n and j == m

        return sum(1 for word in words if is_stretchy(word))



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 双指针逐组比较。对于每个查询单词 word，使用两个指针
# i（遍历 S）和 j（遍历 word）同时前进。对于每组连续相同字符：
#
# 1. 如果 S[i] != word[j]：字符不匹配，不可伸展。
# 2. 计算 S 中当前字符的连续重复次数 cnt_s 和 word 中的 cnt_w。
# 3. 如果 cnt_s < cnt_w：S 中该字符数量更少，无法通过扩展得到。
# 4. 如果 cnt_s > cnt_w 且 cnt_s < 3：扩展操作要求结果组
#    大小至少为 3，不足则不可伸展。
# 5. 指针分别前进 cnt_s 和 cnt_w。
#
# 最后检查两个字符串是否同时耗尽。
#
# 时间复杂度: O(N * (|S| + |W|)) - 其中 N = len(words)，
#   |S| <= 100, |W| 为每个单词的长度
# 空间复杂度: O(1) - 只使用指针和计数器
#
# 关键点:
# - 只能扩展不能缩减：S 中的组长度不能小于 word 中的组长度
# - 扩展后组大小必须 >= 3
# - 字符顺序必须一致
# - 两个字符串必须同时遍历完毕
