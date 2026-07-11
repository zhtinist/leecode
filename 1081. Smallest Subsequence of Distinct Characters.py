"""
LeetCode #1081 - Smallest Subsequence of Distinct Characters
中文题名：不同字符的最小子序列
https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

Return the lexicographically smallest subsequence of `text` that contains all the
distinct characters of `text` exactly once.

Example 1:

Input: "cdadabcc"
Output: "adbc"

Example 2:

Input: "abcd"
Output: "abcd"

Example 3:

Input: "ecbacba"
Output: "eacb"

Example 4:

Input: "leetcode"
Output: "letcod"

Note:

`1 <= text.length <= 1000`

`text` consists of lowercase English letters.

【中文翻译】
返回字符串 text 中按字典序排列最小的子序列，该子序列包含 text 中所有不同字符各一次。

示例 1：

输入："cdadabcc"
输出："adbc"

示例 2：

输入："abcd"
输出："abcd"

示例 3：

输入："ecbacba"
输出："eacb"

示例 4：

输入："leetcode"
输出："letcod"

注意：

1 <= text.length <= 1000
text 由小写英文字母组成。

"""

from typing import List, Optional


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        from collections import Counter

        last_occurrence = {ch: i for i, ch in enumerate(s)}
        stack = []
        in_stack = set()

        for i, ch in enumerate(s):
            if ch in in_stack:
                continue

            while (stack and stack[-1] > ch
                   and last_occurrence[stack[-1]] > i):
                removed = stack.pop()
                in_stack.remove(removed)

            stack.append(ch)
            in_stack.add(ch)

        return ''.join(stack)










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用单调栈 + 贪心。与 #316 Remove Duplicate Letters 完全相同。
# 目标：在保持所有不同字符各出现一次的前提下，得到字典序最小的序列。
# 1. 记录每个字符最后一次出现的位置（last_occurrence）。
# 2. 遍历字符串，使用单调递增栈维护结果序列。
# 3. 如果当前字符已在栈中，跳过（保证每个字符只出现一次）。
# 4. 当栈顶字符大于当前字符，且栈顶字符在之后还会出现（last_occurrence > i），
#    则弹出栈顶字符（让更小的字符在前，得到更小字典序）。
# 5. 将当前字符入栈，记录在 in_stack 集合中。
#
# 时间复杂度: O(n) - 每个字符最多入栈出栈一次
# 空间复杂度: O(1) - 栈和集合最多存储 26 个字符
#
# 关键点:
# - 单调递增栈：保证字典序最小
# - last_occurrence 判断是否可以弹出（后面还有该字符）
# - in_stack 集合保证每个字符只出现一次
# - 与 #316 完全相同的解法
