"""
LeetCode #1079 - Letter Tile Possibilities
中文题名：活字印刷
https://leetcode.com/problems/letter-tile-possibilities/

You have a set of `tiles`, where each tile has one letter `tiles[i]`
printed on it.  Return the number of possible non-empty sequences of letters you can
make.

Example 1:

Input: "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

Example 2:

Input: "AAABBC"
Output: 188

【中文翻译】
你有一套活字字模 tiles，其中每个字模上都刻有一个字母 tiles[i]。返回你可以印出的非空字母序列的数目。

示例 1：

输入："AAB"
输出：8
解释：可能的序列为 "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA"。

示例 2：

输入："AAABBC"
输出：188

"""

from typing import List, Optional


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        from collections import Counter

        count = Counter(tiles)

        def backtrack():
            total = 0
            for ch in count:
                if count[ch] > 0:
                    total += 1
                    count[ch] -= 1
                    total += backtrack()
                    count[ch] += 1
            return total

        return backtrack()










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用回溯法（Backtracking）统计所有可能的排列组合。
# 由于 tiles 中可能包含重复字符，使用字符计数器 Counter 来避免重复排列。
# 回溯函数 backtrack() 返回以当前状态为起点的所有可能序列数：
# 1. 遍历所有可用字符（count[ch] > 0）。
# 2. 选择该字符，计数 +1（当前序列本身）。
# 3. 将该字符的计数减 1，递归统计后续字符能构成的序列数。
# 4. 回溯：将该字符的计数加 1 恢复状态。
# 最终返回所有非空序列的总数。
#
# 时间复杂度: O(n!) - 最坏情况下所有字符不同，生成所有排列
# 空间复杂度: O(n) - 递归栈深度和计数器空间
#
# 关键点:
# - 使用 Counter 处理重复字符，避免生成重复序列
# - 每次选择一个字符后递归统计后续序列
# - 当前选中的字符构成的序列本身也算一种（+1）
# - 回溯恢复状态（计数加回）
