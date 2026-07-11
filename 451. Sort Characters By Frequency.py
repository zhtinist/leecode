"""
LeetCode #451 - Sort Characters By Frequency
中文题名：根据字符出现频率排序
https://leetcode.com/problems/sort-characters-by-frequency/

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

【中文翻译】
给定一个字符串，按字符出现频率降序排列。

示例 1：
输入："tree"
输出："eert"
解释：'e' 出现两次，'r' 和 't' 各出现一次。所以 'e' 必须排在 'r' 和 't' 之前。"eetr" 也是一个有效答案。

示例 2：
输入："cccaaa"
输出："cccaaa"
解释：'c' 和 'a' 各出现三次，"aaaccc" 也是有效答案。注意 "cacaca" 不正确，相同字符必须连续出现。

示例 3：
输入："Aabb"
输出："bbAa"
解释："bbaA" 也是有效答案，但 "Aabb" 不正确。注意 'A' 和 'a' 被视为两个不同的字符。
"""

from typing import List, Optional
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        # Count frequency of each character
        freq = Counter(s)

        # Sort characters by frequency in descending order
        sorted_chars = sorted(freq.keys(), key=lambda c: freq[c], reverse=True)

        # Build result string
        result = []
        for c in sorted_chars:
            result.append(c * freq[c])

        return "".join(result)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用 Counter 统计每个字符的出现频率。然后按频率降序对字符排序，最后按频率重复每个字符拼接成结果字符串。
# 也可以使用桶排序优化：以频率为桶的下标，将相同频率的字符放入同一个桶中，从高到低收集字符。
#
# 时间复杂度: O(N + K log K) — N 为字符串长度，K 为不同字符数。排序 K 个字符，最坏 O(N log N)
# 空间复杂度: O(N) — Counter 存储频率，以及输出字符串
#
# 关键点:
# - 相同字符必须连续出现，不能交错
# - 大小写字母视为不同字符
# - 频率相同时，字符顺序可以任意（多种有效答案）
# - 桶排序可优化到 O(N) 时间
