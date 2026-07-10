"""
LeetCode #191 - Number of 1 Bits
https://leetcode.com/problems/number-of-1-bits/

Write a function that takes an unsigned integer and return the number of '1' bits
it has (also known as the Hamming weight).

Example 1:

Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string `00000000000000000000000000001011 has a total of three '1' bits.`

Example 2:

Input: 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

Example 3:

Input: 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

Note:

Note that in some languages such as Java, there is no unsigned integer type. In this
case, the input will be given as signed integer type and should not affect your
implementation, as the internal binary representation of the integer is the same whether
it is signed or unsigned.

In Java, the compiler represents the signed integers using 2's
complement notation. Therefore, in Example 3 above the input
represents the signed integer `-3`.

Follow up:

If this function is called many times, how would you optimize it?
"""

from typing import List, Optional


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= (n - 1)  # Clear the lowest set bit
            count += 1
        return count


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Easy
# Paid Only: No
#
# 解题思路:
# 使用 Brian Kernighan 算法：n & (n - 1) 可以清除 n 的最低位的 1。
# 每次操作清除一个 1，计数器加 1，直到 n 变为 0。循环次数等于 1 的个数，
# 比逐位检查 32 次更高效。
#
# 例如：n = 12 (1100)
# 第一次：n & (n-1) = 1100 & 1011 = 1000 (8), count = 1
# 第二次：n & (n-1) = 1000 & 0111 = 0000 (0), count = 2
#
# 时间复杂度: O(K)，K 为 1 的个数（最坏 O(32)）
# 空间复杂度: O(1)
#
# 关键点:
# - n & (n - 1) 技巧：消除最低位的 1
# - 比逐位循环（for i in range(32)）平均更快
# - Python 中也可用 bin(n).count('1')，但这是 Cheat
