"""
LeetCode #890 - Find and Replace Pattern
中文题名：查找和替换模式
https://leetcode.com/problems/find-and-replace-pattern/

You have a list of `words` and a `pattern`, and you want to know
which words in `words` matches the pattern.

A word matches the pattern if there exists a permutation of letters `p` so that
after replacing every letter `x` in the pattern with `p(x)`, we get
the desired word.

(Recall that a permutation of letters is a bijection from letters to letters: every
letter maps to another letter, and no two letters map to the same letter.)

Return a list of the words in `words` that match the given pattern.

You may return the answer in any order.

Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.

Note:

`1 <= words.length <= 50`

`1 <= pattern.length = words[i].length <= 20`

【中文翻译】

你有一个单词列表 `words` 和一个模式 `pattern`，你想知道 `words` 中的哪些单词与该模式匹配。

如果存在一个字母排列 `p`，使得将模式中的每个字母 `x` 替换为 `p(x)` 后，我们得到所需的单词，则该单词与模式匹配。

（回想一下，字母排列是从字母到字母的双射：每个字母映射到另一个字母，且没有两个字母映射到同一个字母。）

返回 `words` 中与给定模式匹配的单词列表。

你可以按任意顺序返回答案。

"""

from typing import List, Optional


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def matches(word: str) -> bool:
            if len(word) != len(pattern):
                return False
            w2p = {}  # word -> pattern 映射
            p2w = {}  # pattern -> word 映射
            for w_char, p_char in zip(word, pattern):
                if w_char in w2p:
                    if w2p[w_char] != p_char:
                        return False
                else:
                    w2p[w_char] = p_char
                if p_char in p2w:
                    if p2w[p_char] != w_char:
                        return False
                else:
                    p2w[p_char] = w_char
            return True

        return [word for word in words if matches(word)]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 双射(isomorphism)检查。对每个单词检查是否与 pattern 形成双射关系。
# 使用两个哈希表：
# - w2p: 单词字符 -> 模式字符 的映射
# - p2w: 模式字符 -> 单词字符 的映射
# 遍历每对字符，如果任一方向的映射不一致，则匹配失败。
# 双哈希表确保既满足"每个字母映射到另一个字母"（单射），
# 也满足"没有两个字母映射到同一个字母"（满射）。
#
# 时间复杂度: O(N * K) — N为单词数，K为单词长度
# 空间复杂度: O(K) — 两个映射表的大小（最多26个不同字母）
#
# 关键点:
# - 本质是判断两个字符串是否同构(isomorphic)
# - 需要双向映射保证双射性质
# - 可以直接用 find 方法或规范化签名，但双哈希表最直观
