"""
LeetCode #2429 - Minimize XOR
最小异或
https://leetcode.cn/problems/minimize-xor/

给你两个正整数 `num1` 和 `num2` ，找出满足下述条件的正整数 `x` ：
`x` 的置位数和 `num2` 相同，且
`x XOR num1` 的值 最小
注意 `XOR` 是按位异或运算。
返回整数 `x` 。题目保证，对于生成的测试用例， `x` 是 唯一确定 的。
整数的 置位数 是其二进制表示中 `1` 的数目。

示例 1：
输入：num1 = 3, num2 = 5 输出：3 解释： num1 和 num2 的二进制表示分别是 0011 和 0101 。 整数 3 的置位数与 num2 相同，且 `3 XOR 3 = 0` 是最小的。
示例 2：
输入：num1 = 1, num2 = 12 输出：3 解释： num1 和 num2 的二进制表示分别是 0001 和 1100 。 整数 3 的置位数与 num2 相同，且 `3 XOR 1 = 2` 是最小的。

提示：
`1 <= num1, num2 <= 10^9`
"""

from typing import List, Optional


class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        target_bits = num2.bit_count()

        x = 0

        # Step 1: Set bits from highest to lowest matching num1's set bits.
        # This cancels out the largest possible bits in num1, minimizing XOR.
        for bit in range(31, -1, -1):
            if target_bits == 0:
                break
            if num1 & (1 << bit):
                x |= (1 << bit)
                target_bits -= 1

        # Step 2: If we still have bits to place, set them from lowest
        # to highest in positions where x currently has 0.
        # This minimizes the XOR because lower bits contribute smaller values.
        for bit in range(32):
            if target_bits == 0:
                break
            if not (x & (1 << bit)):
                x |= (1 << bit)
                target_bits -= 1

        return x



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Bit Manipulation
#
# 解题思路:
# 目标是找到一个数 x，其置位数（二进制中 1 的个数）等于 num2，且
# 使得 x XOR num1 最小。策略分两步：
# 1. 从高位到低位扫描 num1 的二进制位，将 x 中对应位设为 1。
#    这样做可以抵消 num1 的高位，从而大幅减小 XOR 结果。
#    直到用完所需的置位数或 num1 的置位已全部匹配。
# 2. 如果还有剩余的置位数需要设置，从低位到高位扫描 x 中为 0 的位
#    并设为 1。低位贡献更小的 XOR 值，因此优先填充低位。
#    这样可以确保 XOR 结果最小。
#
# 时间复杂度: O(1) — 只扫描 32 个比特位
# 空间复杂度: O(1) — 只使用常数额外空间
#
# 关键点:
# - 贪心策略：优先匹配 num1 的高位置位以消除大值
# - 剩余置位从低位填充，使 XOR 增量最小
# - bit_count() 方法获取二进制中 1 的个数（Python 3.8+）
# - 由于整数范围仅到 10^9（30 位足够），32 位扫描是常数时间
