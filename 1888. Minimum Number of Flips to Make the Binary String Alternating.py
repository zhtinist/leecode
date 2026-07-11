"""
LeetCode #1888 - Minimum Number of Flips to Make the Binary String Alternating
使二进制字符串字符交替的最少反转次数
https://leetcode.cn/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/

给你一个二进制字符串 `s` 。你可以按任意顺序执行以下两种操作任意次：
类型 1 ：删除 字符串 `s` 的第一个字符并将它 添加 到字符串结尾。
类型 2 ：选择 字符串 `s` 中任意一个字符并将该字符 反转 ，也就是如果值为 `'0'` ，则反转得到 `'1'` ，反之亦然。
请你返回使 `s` 变成 交替 字符串的前提下， 类型 2 的 最少 操作次数 。
我们称一个字符串是 交替 的，需要满足任意相邻字符都不同。
比方说，字符串 `"010"` 和 `"1010"` 都是交替的，但是字符串 `"0100"` 不是。

示例 1：
输入：s = "111000" 输出：2 解释：执行第一种操作两次，得到 s = "100011" 。 然后对第三个和第六个字符执行第二种操作，得到 s = "101010" 。
示例 2：
输入：s = "010" 输出：0 解释：字符串已经是交替的。
示例 3：
输入：s = "1110" 输出：1 解释：对第二个字符执行第二种操作，得到 s = "1010" 。

提示：
`1 <= s.length <= 10^5`
`s[i]` 要么是 `'0'` ，要么是 `'1'` 。
"""

from typing import List, Optional


class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        # Double the string to handle type-1 operations (cyclic rotation)
        t = s + s

        # Build two target alternating patterns of length 2n
        # Pattern 1: "0101..."
        # Pattern 2: "1010..."

        # diff1[i] = mismatches if target starts with '0'
        # diff2[i] = mismatches if target starts with '1'
        diff1 = [0] * (2 * n)
        diff2 = [0] * (2 * n)

        for i in range(2 * n):
            expected0 = '0' if i % 2 == 0 else '1'
            expected1 = '1' if i % 2 == 0 else '0'

            prev1 = diff1[i - 1] if i > 0 else 0
            prev2 = diff2[i - 1] if i > 0 else 0

            diff1[i] = prev1 + (1 if t[i] != expected0 else 0)
            diff2[i] = prev2 + (1 if t[i] != expected1 else 0)

        # For each window of length n, compute mismatches
        ans = n
        for i in range(n):
            # Window: t[i .. i+n-1]
            # For pattern starting with '0'
            mismatches1 = diff1[i + n - 1] - (diff1[i - 1] if i > 0 else 0)
            mismatches2 = diff2[i + n - 1] - (diff2[i - 1] if i > 0 else 0)
            ans = min(ans, mismatches1, mismatches2)

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: String, Dynamic Programming, Sliding Window
#
# 解题思路:
# 类型1操作（循环移位）等价于在扩展字符串 s+s 上取长度为 n 的窗口。
# 1. 将 s 扩展为 t = s + s，处理循环移位的所有可能。
# 2. 构建前缀差异数组：对于 "0101..." 和 "1010..." 两种交替模式，
#    计算前缀中不匹配的字符数。
# 3. 对每个长度为 n 的窗口，使用前缀和 O(1) 计算不匹配数。
# 4. 取所有窗口和两种模式的最小值。
#
# 时间复杂度: O(n) — 遍历扩展字符串和窗口
# 空间复杂度: O(n) — 前缀差异数组
#
# 关键点:
# - 字符串翻倍处理循环移位
# - 前缀和优化窗口内不匹配字符的计数
# - 两种交替模式都需要检查
# - 类型1操作可以在类型2操作之前执行任意次
