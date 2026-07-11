"""
LeetCode #400 - Nth Digit
中文题名：第N个数字
https://leetcode.com/problems/nth-digit/

Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8,
9, 10, 11, ...

Note:

n is positive and will fit within the range of a 32-bit signed integer (n 31).

Example 1:

Input:
3

Output:
3

Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.

【中文翻译】
在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 中找到第 n 位数字。

注意：

n 为正数且在 32 位有符号整数范围内（n < 2^31）。

示例 1：

输入：
3

输出：
3

示例 2：

输入：
11

输出：
0

解释：
序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 的第 11 位数字是 0，它是数字 10 的一部分。
"""

from typing import List, Optional


class Solution:
    def findNthDigit(self, n: int) -> int:
        digit_len = 1
        count = 9
        while n > digit_len * count:
            n -= digit_len * count
            digit_len += 1
            count *= 10
        start = 10 ** (digit_len - 1)
        number = start + (n - 1) // digit_len
        digit_index = (n - 1) % digit_len
        return int(str(number)[digit_index])











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 这是一个数学推导问题。先确定第 n 位数字所在的数字范围：
# - 1 位数：1~9，共 9*1 = 9 位
# - 2 位数：10~99，共 90*2 = 180 位
# - 3 位数：100~999，共 900*3 = 2700 位
# - d 位数：9 * 10^(d-1) * d 位
# 逐级减去各位数段的位数，找到 n 所在的位数段。
# 然后确定所在的完整数字：start + (n-1)//digit_len
# 最后从该数字中取出对应的那一位：(n-1) % digit_len。
#
# 时间复杂度: O(log n) - 循环次数为 n 所在数字的位数
# 空间复杂度: O(1) - 仅使用常数额外空间
#
# 关键点:
# - 分三步：定位位数段 → 定位具体数字 → 定位数字中的具体位
# - 1 位数有 9 个（1-9），2 位数 90 个（10-99），3 位数 900 个...
# - 使用 (n-1) 而非 n 是为了将 1-based 索引转换为 0-based
# - 通过字符串转换取位最简单，也可用数学方式取位
