"""
LeetCode #343 - Integer Break
中文题名：整数拆分
https://leetcode.com/problems/integer-break/

Given a positive integer n, break it into the sum of at least two positive
integers and maximize the product of those integers. Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 &times; 1 = 1.

Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 &times; 3 &times; 4 = 36.

Note: You may assume that n is not less than 2 and not larger than 58.

【中文翻译】
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。返回你可以获得的最大乘积。

示例 1：

输入：2
输出：1
解释：2 = 1 + 1, 1 × 1 = 1。

示例 2：

输入：10
输出：36
解释：10 = 3 + 3 + 4, 3 × 3 × 4 = 36。

注意：你可以假设 n 不小于 2 且不大于 58。
"""

from typing import List, Optional


class Solution:
    def integerBreak(self, n: int) -> int:
        # 对于 n <= 3，必须拆分至少两个数
        if n <= 3:
            return n - 1
        # 贪心：尽可能多地拆出 3
        quotient, remainder = divmod(n, 3)
        if remainder == 0:
            return 3 ** quotient
        elif remainder == 1:
            # 余 1 时，将最后一个 3 和 1 合并为 4 = 2 + 2
            return 3 ** (quotient - 1) * 4
        else:  # remainder == 2
            return 3 ** quotient * 2










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 数学推导可知，将一个正整数拆分为尽可能多的 3 时乘积最大。
# 对于 n <= 3 的特殊情况：n=2 只能拆为 1+1（乘积 1），n=3 只能拆为 1+2（乘积 2）。
# 对于 n >= 4：计算 n 除以 3 的商和余数。
# - 余数为 0：全部拆为 3，结果是 3^quotient。
# - 余数为 1：因为 3×1 < 2×2，所以退一个 3，将 3+1 改为 2+2（乘积 4），结果是 3^(quotient-1) × 4。
# - 余数为 2：直接乘以 2，结果是 3^quotient × 2。
# 也可以使用动态规划：dp[i] = max(dp[i-j] × j) for j in 1..i-1，但数学方法时间 O(1) 更优。
#
# 时间复杂度: O(1) - 仅常数次数学运算
# 空间复杂度: O(1) - 无额外空间使用
#
# 关键点:
# - 核心贪心策略：尽可能多地拆出 3
# - 余数为 1 时需特殊处理，将 3+1 转为 2+2，因为 2×2=4 > 3×1=3
# - 余数为 2 时直接保留
# - n <= 3 的边界情况必须正确处理（必须至少拆成两个数）
