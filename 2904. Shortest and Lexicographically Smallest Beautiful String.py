"""
LeetCode #2904 - Shortest and Lexicographically Smallest Beautiful String
最短且字典序最小的美丽子字符串
https://leetcode.cn/problems/shortest-and-lexicographically-smallest-beautiful-string/

给你一个二进制字符串 `s` 和一个正整数 `k` 。
如果 `s` 的某个子字符串中 `1` 的个数恰好等于 `k` ，则称这个子字符串是一个 美丽子字符串 。
令 `len` 等于 最短 美丽子字符串的长度。
返回长度等于 `len` 且字典序 最小 的美丽子字符串。如果 `s` 中不含美丽子字符串，则返回一个 空 字符串。
对于相同长度的两个字符串 `a` 和 `b` ，如果在 `a` 和 `b` 出现不同的第一个位置上，`a` 中该位置上的字符严格大于 `b` 中的对应字符，则认为字符串 `a` 字典序 大于 字符串 `b` 。
例如，`"abcd"` 的字典序大于 `"abcc"` ，因为两个字符串出现不同的第一个位置对应第四个字符，而 `d` 大于 `c` 。

示例 1：
输入：s = "100011001", k = 3 输出："11001" 解释：示例中共有 7 个美丽子字符串： 1. 子字符串 "100011001" 。 2. 子字符串 "100011001" 。 3. 子字符串 "100011001" 。 4. 子字符串 "100011001" 。 5. 子字符串 "100011001" 。 6. 子字符串 "100011001" 。 7. 子字符串 "100011001" 。 最短美丽子字符串的长度是 5 。 长度为 5 且字典序最小的美丽子字符串是子字符串 "11001" 。
示例 2：
输入：s = "1011", k = 2 输出："11" 解释：示例中共有 3 个美丽子字符串： 1. 子字符串 "1011" 。 2. 子字符串 "1011" 。 3. 子字符串 "1011" 。 最短美丽子字符串的长度是 2 。 长度为 2 且字典序最小的美丽子字符串是子字符串 "11" 。
示例 3：
输入：s = "000", k = 1 输出："" 解释：示例中不存在美丽子字符串。

提示：
`1 <= s.length <= 100`
`1 <= k <= s.length`
"""

from typing import List, Optional


class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        best = None
        for i in range(n):
            ones = 0
            for j in range(i, n):
                if s[j] == '1':
                    ones += 1
                if ones == k:
                    sub = s[i:j + 1]
                    if best is None:
                        best = sub
                    elif len(sub) < len(best):
                        best = sub
                    elif len(sub) == len(best) and sub < best:
                        best = sub
                    break  # no need to extend further for this i
        return best if best is not None else ""



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: String, Sliding Window
#
# 解题思路:
# 暴力枚举所有子字符串，统计其中1的个数。当1的个数等于 k 时，记录子串。在所有满足条件的子串中，
# 优先选择长度最短的，若长度相同则选择字典序最小的。由于 n <= 100，O(n^2) 枚举完全可行。
# 一旦对于固定的起点找到第一个 k 个1 的子串即可停止扩展（再扩展只会更长）。
#
# 时间复杂度: O(n^2)
# 空间复杂度: O(1)
#
# 关键点:
# - 暴力枚举所有子串（n <= 100）
# - 找到恰好 k 个1的子串后停止扩展该起点（因为再长不可能是最短）
# - 比较时先比长度再比字典序
