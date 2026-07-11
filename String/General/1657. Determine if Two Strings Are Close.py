"""
LeetCode #1657 - Determine if Two Strings Are Close
中文题名：确定两个字符串是否接近
https://leetcode.com/problems/determine-if-two-strings-are-close/

Two strings are considered close if you can attain one from the
other using the following operations:

Operation 1: Swap any two existing characters.

For example, `abcde -> aecdb`

Operation 2: Transform every occurrence of one
existing character into another existing
character, and do the same with the other character.

For example, `aacabb ->
bbcbaa` (all `a`'s turn into
`b`'s, and all `b`'s turn into `a`'s)

You can use the operations on either string as many times as necessary.

Given two strings, `word1` and `word2`, return
`true` if `word1` and `word2`
are close, and `false` otherwise.

Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"

Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

Example 3:

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
`Apply Operation 2: "`caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"

Example 4:

Input: word1 = "cabbba", word2 = "aabbss"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any amount of operations.

Constraints:

`1 <= word1.length, word2.length <= 105`

`word1` and `word2` contain only lowercase English
letters.

【中文翻译】
两个字符串是接近的如果可以通过以下操作将一个字符串转换为另一个：
- 操作1：交换任意两个字符的位置
- 操作2：交换两种字符的所有出现（例如将所有的 'a' 变为 'b'，同时所有的 'b' 变为 'a'）
给定 word1 和 word2，判断它们是否接近。

示例 1：
输入: word1 = "abc", word2 = "bca"
输出: true
解释: 通过2次操作可实现：交换'a'和'c'得到"cba"，交换'c'和'b'得到"bca"。
"""

from typing import List, Optional
from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        c1, c2 = Counter(word1), Counter(word2)

        if set(c1.keys()) != set(c2.keys()):
            return False

        return sorted(c1.values()) == sorted(c2.values())
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 分析两个操作的效果：
# - 操作1（交换任意两个字符位置）：相当于可以任意重新排列字符串
# - 操作2（交换两种字符的所有出现）：相当于可以交换任意两个字符的频率
# 因此两个字符串接近的条件是：
# 1. 字符集合相同（因为操作2只能交换已有字符，不能创建新字符）
# 2. 频率集合相同（因为操作2可以任意交换频率值）
#
# 时间复杂度: O(N log K) — N 为字符串长度，K 为不同字符数（最多26）
# 空间复杂度: O(K) — Counter 存储
#
# 关键点:
# - 操作2不能改变字符集合，只能交换频率
# - 只需检查集合相同 + 排序后的频率列表相同
