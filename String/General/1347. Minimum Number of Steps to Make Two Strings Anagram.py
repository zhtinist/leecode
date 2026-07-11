"""
LeetCode #1347 - Minimum Number of Steps to Make Two Strings Anagram
中文题名：制造字母异位词的最小步骤数
https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

Given two equal-size strings `s` and `t`. In one step you can
choose any character of `t` and replace it with another
character.

Return the minimum number of steps to make `t` an anagram of
`s`.

An Anagram of a string is a string that contains
the same characters with a different (or the same) ordering.

Example 1:

Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.

Example 2:

Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.

Example 3:

Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams.

Example 4:

Input: s = "xxyyzz", t = "xxyyzz"
Output: 0

Example 5:

Input: s = "friend", t = "family"
Output: 4

Constraints:

`1 <= s.length <= 50000`

`s.length == t.length`

`s` and `t` contain lower-case English letters only.

【中文翻译】
给定两个长度相等的字符串 `s` 和 `t`。每一步操作中，你可以选择 `t` 中的任意一个字符
并将其替换为另一个字符。

返回使 `t` 成为 `s` 的字母异位词所需的最少步数。

字母异位词是指包含相同字符但顺序可能不同的字符串。

示例 1：

输入: s = "bab", t = "aba"
输出: 1
解释: 将 t 中的第一个 'a' 替换为 'b'，t 变为 "bba"，它是 s 的字母异位词。

示例 2：

输入: s = "leetcode", t = "practice"
输出: 5
解释: 将 t 中的 'p'、'r'、'a'、'i'、'c' 替换为合适的字符，使 t 成为 s 的字母异位词。

示例 3：

输入: s = "anagram", t = "mangaar"
输出: 0
解释: "anagram" 和 "mangaar" 已经是字母异位词。

示例 4：

输入: s = "xxyyzz", t = "xxyyzz"
输出: 0

示例 5：

输入: s = "friend", t = "family"
输出: 4
解释: f 和 i 已经匹配，需要替换其他 4 个不同字符。

约束条件：

`1 <= s.length <= 50000`

`s.length == t.length`

`s` 和 `t` 仅包含小写英文字母。
"""

from typing import List, Optional


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter

        count_s = Counter(s)
        count_t = Counter(t)

        steps = 0
        # 对于每个在 s 中出现频率高于 t 中的字符，需要补足差值
        for char in count_s:
            if count_s[char] > count_t.get(char, 0):
                steps += count_s[char] - count_t[char]

        return steps



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 要使 t 成为 s 的字母异位词，需要 t 中每种字符的数量与 s 中相同。
# 2. 统计 s 和 t 中每种字符的出现次数（使用 Counter）。
# 3. 遍历 s 中的每种字符：
#    - 如果 s 中该字符的数量大于 t 中的数量，说明 t 缺少这些字符，
#      需要将 t 中的多余字符替换为该字符，缺多少就需要多少步。
#    - 累计所有字符的差值，即为最少替换步数。
# 4. 等价解释：只统计 s 比 t 多的部分，因为长度相等，s 多的总数一定等于 t 多的总数。
#
# 时间复杂度: O(N) — 遍历两个字符串各一次
# 空间复杂度: O(1) — Counter 最多存储 26 个英文字母
#
# 关键点:
# - 只需考虑 s 中"多出"的字符，步数等于这些多出数量之和
# - 由于两字符串等长，总多余量一致
# - 只有 26 个小写字母，空间复杂度为 O(1)
# - Counter.get(char, 0) 处理 t 中不存在的字符










