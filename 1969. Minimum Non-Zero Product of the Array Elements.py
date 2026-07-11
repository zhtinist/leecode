"""
LeetCode #1969 - Minimum Non-Zero Product of the Array Elements
数组元素的最小非零乘积
https://leetcode.cn/problems/minimum-non-zero-product-of-the-array-elements/

给你一个正整数 `p` 。你有一个下标从 1 开始的数组 `nums` ，这个数组包含范围 `[1, 2^p - 1]` 内所有整数的二进制形式（两端都 包含）。你可以进行以下操作 任意 次：
从 `nums` 中选择两个元素 `x` 和 `y`  。
选择 `x` 中的一位与 `y` 对应位置的位交换。对应位置指的是两个整数 相同位置 的二进制位。
比方说，如果 `x = 1101` 且 `y = 0011` ，交换右边数起第 `2` 位后，我们得到 `x = 1111` 和 `y = 0001` 。
请你算出进行以上操作 任意次 以后，`nums` 能得到的 最小非零 乘积。将乘积对 `10^9 + 7` 取余 后返回。
注意：答案应为取余 之前 的最小值。

示例 1：
输入：p = 1 输出：1 解释：nums = [1] 。 只有一个元素，所以乘积为该元素。
示例 2：
输入：p = 2 输出：6 解释：nums = [01, 10, 11] 。 所有交换要么使乘积变为 0 ，要么乘积与初始乘积相同。 所以，数组乘积 1 * 2 * 3 = 6 已经是最小值。
示例 3：
输入：p = 3 输出：1512 解释：nums = [001, 010, 011, 100, 101, 110, 111] - 第一次操作中，我们交换第二个和第五个元素最左边的数位。     - 结果数组为 [001, 110, 011, 100, 001, 110, 111] 。 - 第二次操作中，我们交换第三个和第四个元素中间的数位。     - 结果数组为 [001, 110, 001, 110, 001, 110, 111] 。 数组乘积 1 * 6 * 1 * 6 * 1 * 6 * 7 = 1512 是最小乘积。

提示：
`1 <= p <= 60`
"""

from typing import List, Optional


class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        """
        Numbers from 1 to 2^p - 1. Through bit-swap operations, the minimal
        non-zero product is:
        (2^p - 1) * (2^p - 2)^(2^(p-1) - 1) mod MOD
        """
        MOD = 10**9 + 7

        max_val = (1 << p) - 1          # 2^p - 1
        second_max = max_val - 1        # 2^p - 2
        exponent = (1 << (p - 1)) - 1   # 2^(p-1) - 1

        # Fast modular exponentiation
        power = pow(second_max % MOD, exponent, MOD)
        return (max_val % MOD) * power % MOD



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Recursion, Math
#
# 解题思路:
# 通过位交换操作，我们可以将数组中的数重新排列。
# 最小非零乘积的构造方式：保留最大值 2^p - 1 不变，将其余的数尽可能变小。
# 通过位交换，可以将除了最大值外的所有数变成 (2^p - 2) 和 1 的对。
# 总共有 2^(p-1) - 1 对。
# 最终乘积 = (2^p - 1) * (2^p - 2)^(2^(p-1) - 1)
# 使用快速幂取模计算结果。
#
# 时间复杂度: O(log P)，快速幂
# 空间复杂度: O(1)
#
# 关键点:
# - 通过位交换可得到 1 和 2^p-2（因为和最大值 2^p-1 互补）
# - 不能得到 0（乘积需要非零）
# - 使用 Python 内置 pow(base, exp, mod) 进行快速幂取模
