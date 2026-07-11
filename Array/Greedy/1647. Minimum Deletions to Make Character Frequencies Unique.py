"""
LeetCode #1647 - Minimum Deletions to Make Character Frequencies Unique
中文题名：字符频次唯一的最小删除数
https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

A string `s` is called good if there are no two
different characters in `s` that have the same frequency.

Given a string `s`, return the minimum number of
characters you need to delete to make `s` good.

The frequency of a character in a string is the number of times it
appears in the string. For example, in the string `"aab"`, the frequency
of `'a'` is `2`, while the frequency of
`'b'` is `1`.

Example 1:

Input: s = "aab"
Output: 0
Explanation: `s` is already good.

Example 2:

Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".

Example 3:

Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).

Constraints:

`1 <= s.length <= 105`

`s` contains only lowercase English letters.

【中文翻译】
字符串 s 是好的当且仅当没有两个不同字符有相同的出现频率。给定字符串 s，每次操作可以删除一个字符。
返回使 s 成为好的字符串所需的最少删除次数。

示例 1：
输入: s = "aab"
输出: 0
解释: 'a'出现2次，'b'出现1次。频率已经唯一。

示例 2：
输入: s = "aaabbbcc"
输出: 2
解释: 删除两个 'b'，则 'a':3, 'b':1, 'c':2（频率都唯一）。
"""

from typing import List, Optional
from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        freq = list(Counter(s).values())
        freq.sort(reverse=True)

        deletions = 0
        prev = freq[0]

        for i in range(1, len(freq)):
            if freq[i] >= prev:
                target = max(0, prev - 1)
                deletions += freq[i] - target
                prev = target
            else:
                prev = freq[i]

        return deletions
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 统计每个字符的出现频率，按从大到小排序。
# 遍历排序后的频率，维护 prev（前一个字符调整后的频率）。
# 如果当前频率 >= prev，必须将其减少到 prev-1（最小为0），累加删除次数。
#
# 时间复杂度: O(N + K log K) — N 为字符串长度，K 为不同字符数
# 空间复杂度: O(K) — 频率数组
#
# 关键点:
# - 频率降序排序，贪心使后面的频率严格小于前面的
# - 频率减到 0 意味着完全删除该字符
