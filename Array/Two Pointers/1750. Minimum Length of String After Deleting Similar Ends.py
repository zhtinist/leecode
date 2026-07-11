"""
LeetCode #1750 - Minimum Length of String After Deleting Similar Ends
中文题名：删除字符串两端相同字符后的最短长度
https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/

Given a string `s` consisting only of characters `'a'`, `'b'`, and `'c'`. You are asked to apply the following algorithm on the string any number of times:

Pick a non-empty prefix from the string `s` where all the characters in the prefix are equal.

Pick a non-empty suffix from the string `s` where all the characters in this suffix are equal.

The prefix and the suffix should not intersect at any index.

The characters from the prefix and suffix must be the same.

Delete both the prefix and the suffix.

Return the minimum length of `s` after performing the above operation any number of times (possibly zero times).

Example 1:

Input: s = "ca"
Output: 2
Explanation: You can't remove any characters, so the string stays as is.

Example 2:

Input: s = "cabaabac"
Output: 0
Explanation: An optimal sequence of operations is:
- Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
- Take prefix = "a" and suffix = "a" and remove them, s = "baab".
- Take prefix = "b" and suffix = "b" and remove them, s = "aa".
- Take prefix = "a" and suffix = "a" and remove them, s = "".

Example 3:

Input: s = "aabccabba"
Output: 3
Explanation: An optimal sequence of operations is:
- Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
- Take prefix = "b" and suffix = "bb" and remove them, s = "cca".

Constraints:

`1 <= s.length <= 105`

`s` only consists of characters `'a'`, `'b'`, and `'c'`.

【中文翻译】
给定一个只包含字符 'a'、'b' 和 'c' 的字符串 s。可以执行以下操作任意次：
- 选择前缀中所有相同字符，将它们全部删除
- 选择后缀中所有相同字符，将它们全部删除
- 前缀和后缀所选的字符必须相同
求最终字符串的最短长度。

示例 1：
输入: s = "ca"
输出: 2
解释: 前缀和后缀字符不同（'c' vs 'a'），无法操作。

示例 2：
输入: s = "cabaabac"
输出: 0
解释: 删前缀"c"→"abaabac"；删后缀"c"→"abaaba"；删前后"a"→"baab"；删前后"b"→"aa"；删前后"a"→""。
"""

from typing import List, Optional


class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1

        while left < right and s[left] == s[right]:
            ch = s[left]
            # 删除左边所有相同字符
            while left <= right and s[left] == ch:
                left += 1
            # 删除右边所有相同字符
            while left <= right and s[right] == ch:
                right -= 1

        return right - left + 1
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 双指针。while left < right 且 s[left] == s[right]：
# 1. 记录当前端点字符 ch
# 2. 左指针跳过左边所有等于 ch 的字符
# 3. 右指针跳过右边所有等于 ch 的字符
# 4. 重复直到 left >= right 或 s[left] != s[right]
# 最终剩余长度 = right - left + 1。
#
# 时间复杂度: O(N) — 每个字符最多访问两次
# 空间复杂度: O(1)
#
# 关键点:
# - 关键是同时删除前后缀中相同的字符（允许操作多次）
# - 双指针向内收缩，一次跳过所有相同字符
# - 注意边界条件 left <= right
