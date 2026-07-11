"""
LeetCode #187 - Repeated DNA Sequences
中文题名：重复的DNA序列
https://leetcode.com/problems/repeated-dna-sequences/

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for
example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify
repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur
more than once in a DNA molecule.

Example:
    Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    Output: ["AAAAACCCCC", "CCCCCAAAAA"]

【中文翻译】
DNA 由 A、C、G、T 四种核苷酸组成。研究 DNA 时，有时需要找出其中重复出现的序列。

编写函数，找出所有在 DNA 分子中出现超过一次的、长度为 10 的序列（子串）。

示例：
    输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    输出：["AAAAACCCCC", "CCCCCAAAAA"]
"""

from typing import List, Optional


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []

        seen = set()
        repeated = set()

        for i in range(len(s) - 9):
            sub = s[i:i + 10]
            if sub in seen:
                repeated.add(sub)
            else:
                seen.add(sub)

        return list(repeated)


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用滑动窗口 + 哈希集合。遍历字符串 s，每次取长度为 10 的子串。维护两个集合：
# seen 记录已经见过的子串，repeated 记录出现超过一次的子串。
# 如果当前子串已在 seen 中，说明之前出现过至少一次，将其加入 repeated；
# 否则将其加入 seen。最后将 repeated 转为列表返回。
#
# 时间复杂度: O(N) — 遍历一次字符串，每次取子串 O(1)（实际为 O(10)=O(1)）
# 空间复杂度: O(N) — seen 和 repeated 集合最多存储 N-9 个子串
#
# 关键点:
# - 固定长度 10 的子串，滑动窗口天然适用
# - 使用两个集合区分"见过一次"和"重复出现"
# - 利用集合自动去重（repeated 中每个序列只出现一次）
