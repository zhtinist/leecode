"""
LeetCode #186 - Reverse Words in a String II
https://leetcode.com/problems/reverse-words-in-a-string-ii/

Given an input string* *, reverse the string word by word.

Example:

Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

Note:

A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces.

The words are always separated by a single space.

Follow up: Could you do it *in-place* without allocating extra
space?
"""

from typing import List, Optional


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(l: int, r: int) -> None:
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        # Step 1: Reverse the entire array
        reverse(0, len(s) - 1)

        # Step 2: Reverse each word
        left = 0
        for right in range(len(s)):
            if s[right] == " ":
                reverse(left, right - 1)
                left = right + 1
        # Reverse the last word
        reverse(left, len(s) - 1)


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: Yes
#
# 解题思路:
# 两次反转法：先将整个字符数组整体反转，此时单词的顺序被逆转了，但每个单词
# 内部的字符也被反转了。然后遍历数组，找到每个单词的边界（以空格分隔），将每个
# 单词单独反转回来，从而恢复每个单词的正确拼写。
#
# 例如：["t","h","e"," ","s","k","y"]
# 第一步（整体反转）：["y","k","s"," ","e","h","t"]
# 第二步（每个单词反转）：["s","k","y"," ","t","h","e"]
#
# 时间复杂度: O(N) — 每个字符被交换两次
# 空间复杂度: O(1) — 原地操作
#
# 关键点:
# - 两次反转技巧：整体反转 + 单词反转 = 单词顺序反转
# - 原地操作，不使用额外数组
# - 注意处理最后一个单词（没有尾随空格的情况）
