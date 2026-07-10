"""
LeetCode #248 - Strobogrammatic Number III
https://leetcode.com/problems/strobogrammatic-number-iii/

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at
upside down).

Write a function to count the total strobogrammatic numbers that exist in the range of low
<= num <= high.

Example:

Input: low = "50", high = "100"
Output: 3
Explanation: 69, 88, and 96 are three strobogrammatic numbers.

Note:

Because the range might be a large number, the *low* and *high* numbers are
represented as string.
"""

from typing import List, Optional


class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        pairs = [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]

        def helper(m: int, n: int) -> List[str]:
            """生成长度在 [m, n] 范围内的所有 strobogrammatic 数"""
            if m == 0:
                return [""]
            if m == 1:
                return ["0", "1", "8"]

            res = []
            # 长度等于 n 时，不能以 '0' 开头
            if m == n:
                for left, right in pairs:
                    if left == '0':
                        continue
                    for inner in helper(m - 2, n):
                        res.append(left + inner + right)
            else:
                for left, right in pairs:
                    for inner in helper(m - 2, n):
                        res.append(left + inner + right)
            return res

        count = 0
        # 遍历 [len(low), len(high)] 的长度范围
        for length in range(len(low), len(high) + 1):
            if length == 1:
                for s in ["0", "1", "8"]:
                    if int(low) <= int(s) <= int(high):
                        count += 1
                continue

            for s in helper(length, length):
                # 字符串比较：先比较长度，再比较字典序（数值字符串同长时字典序=数值大小）
                if len(s) == len(low) and s < low:
                    continue
                if len(s) == len(high) and s > high:
                    continue
                count += 1

        return count


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Hard
# Paid Only: Yes
#
# 解题思路：
# 基于 #247 的递归生成方法。对 [len(low), len(high)] 之间的每个长度，
# 生成所有该长度的 strobogrammatic 数，然后过滤掉不在 [low, high]
# 范围内的。通过字符串比较判断是否在范围内（同长度时字典序即数值序）。
# 注意长度为 1 的特殊处理。
#
# 时间复杂度: O(5^(n/2)) — n 为 high 的长度，生成所有可能的数
# 空间复杂度: O(5^(n/2)) — 存储中间结果
#
# 关键点：
# - 对每个长度生成后按范围过滤
# - 同长度字符串比较：字典序等同于数值大小
# - 边界处理：与 low 和 high 的比较
