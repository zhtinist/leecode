"""
LeetCode #190 - Reverse Bits
https://leetcode.com/problems/reverse-bits/

Reverse bits of a given 32 bits unsigned integer.

Example 1:

Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

Example 2:

Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10101111110010110010011101101001.

Note:

Note that in some languages such as Java, there is no unsigned integer type. In this
case, both input and output will be given as signed integer type and should not affect
your implementation, as the internal binary representation of the integer is the same
whether it is signed or unsigned.

In Java, the compiler represents the signed integers using 2's
complement notation. Therefore, in Example 2 above the input
represents the signed integer `-3` and the output represents the signed
integer `-1073741825`.

Follow up:

If this function is called many times, how would you optimize it?
"""

from typing import List, Optional


class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            # Extract the last bit of n
            bit = n & 1
            # Shift result left and add the extracted bit
            result = (result << 1) | bit
            # Shift n right to process the next bit
            n >>= 1
        return result


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Easy
# Paid Only: No
#
# 解题思路:
# 逐位处理。循环 32 次，每次：
# 1. 用 n & 1 取出 n 的最低位（最右边的比特）
# 2. 将 result 左移一位（result << 1），为下一个比特腾出位置
# 3. 用 | bit 将取出的比特放到 result 的最低位
# 4. 将 n 右移一位（n >>= 1），处理下一个比特
#
# 这样经过 32 次迭代后，n 的 bit[0] 到了 result 的 bit[31]，
# n 的 bit[31] 到了 result 的 bit[0]，实现了镜像反转。
#
# 时间复杂度: O(1) — 固定 32 次迭代
# 空间复杂度: O(1) — 只使用常数变量
#
# 关键点:
# - 遍历 32 位，逐位反转
# - result << 1 为下一位腾出空间
# - n >>= 1 处理下一位
# - 也可使用分治法（如交换相邻位、交换半字节等）优化速度
