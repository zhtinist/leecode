"""
LeetCode #191 - Number of 1 Bits
中文题名：位1的个数
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

【中文翻译】
编写一个函数，输入一个无符号整数，返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。

示例 1：

输入：00000000000000000000000000001011
输出：3
解释：输入二进制字符串 `00000000000000000000000000001011` 共有三个 '1' 位。

示例 2：

输入：00000000000000000000000010000000
输出：1
解释：输入二进制字符串 00000000000000000000000010000000 共有一个 '1' 位。

示例 3：

输入：11111111111111111111111111111101
输出：31
解释：输入二进制字符串 11111111111111111111111111111101 共有三十一个 '1' 位。

注意：

请注意，在某些语言（如 Java）中没有无符号整数类型。在这种情况下，输入将作为有符号整数类型给出，不应影响你的实现，因为整数的内部二进制表示在有无符号时是一样的。

在 Java 中，编译器使用 2 的补码表示法表示有符号整数。因此，在上面的示例 3 中，输入表示有符号整数 `-3`。

进阶：

如果此函数被多次调用，你将如何优化它？
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
