"""
LeetCode #233 - Number of Digit One
https://leetcode.com/problems/number-of-digit-one/

Given an integer n, count the total number of digit 1 appearing in all non-negative integers
less than or equal to n.

Example:

Input: 13
Output: 6
Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
"""

from typing import List, Optional


class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        d = 1
        while d <= n:
            count += (n // (d * 10)) * d + min(max(n % (d * 10) - d + 1, 0), d)
            d *= 10
        return count










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Hard
# Paid Only: No
#
# 解题思路:
# 数学归纳法，逐位统计数字 1 出现的次数。
# 对于每一位(个位、十位、百位...)，将数字分为三部分: 高位、当前位、低位。
# 设当前位权值为 d (1, 10, 100, ...)：
# - 高位部分 = n // (d * 10)：每完整经过 d*10 个数，当前位会出现 d 次 1
# - 低位部分 = n % (d * 10)：处理不完整的周期
#   - 若低位 < d，当前位贡献 0
#   - 若 d <= 低位 < 2d，当前位贡献 (低位 - d + 1)
#   - 若低位 >= 2d，当前位贡献 d
# 公式: count += (n // (d * 10)) * d + min(max(n % (d * 10) - d + 1, 0), d)
# 例如 n = 13:
#   个位(d=1): (13//10)*1 + min(max(13%10-1+1,0), 1) = 1 + min(3,1) = 2 (数字 1, 11)
#   十位(d=10): (13//100)*10 + min(max(13%100-10+1,0), 10) = 0 + min(4,10) = 4 (数字 10-13 的十位)
#   总计: 2 + 4 = 6
#
# 时间复杂度: O(log n) - 遍历每一位(十进制位数)
# 空间复杂度: O(1) - 只使用常数变量
#
# 关键点:
# - 核心思想是逐位分析，而非逐个数字检查
# - 高位贡献 = 完整周期数 * 每个周期包含的 1 的数量
# - 低位贡献 = 不完整周期中 1 的个数，用 min(max(...), d) 夹逼计算
# - 这是经典的数字统计问题(数位 DP 入门)
