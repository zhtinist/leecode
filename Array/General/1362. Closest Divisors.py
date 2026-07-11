"""
LeetCode #1362 - Closest Divisors
中文题名：最接近的因数
https://leetcode.com/problems/closest-divisors/

Given an integer `num`, find the closest two integers in absolute
difference whose product equals `num + 1` or `num + 2`.

Return the two integers in any order.

Example 1:

Input: num = 8
Output: [3,3]
Explanation: For num + 1 = 9, the closest divisors are 3 & 3, for num + 2 = 10, the closest divisors are 2 & 5, hence 3 & 3 is chosen.

Example 2:

Input: num = 123
Output: [5,25]

Example 3:

Input: num = 999
Output: [40,25]

Constraints:

`1 <= num <= 10^9`

【中文翻译】
给定一个整数 `num`，找出乘积等于 `num + 1` 或 `num + 2` 且绝对差最小的两个整数。

以任意顺序返回这两个整数。

示例 1：
输入：num = 8
输出：[3,3]
解释：对于 num + 1 = 9，最接近的因数是 3 和 3；对于 num + 2 = 10，最接近的因数是 2 和 5，因此选择 [3,3]。

示例 2：
输入：num = 123
输出：[5,25]

示例 3：
输入：num = 999
输出：[40,25]
"""

from typing import List
import math


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def find_closest(target: int) -> List[int]:
            # 从 sqrt(target) 向下遍历找最接近的因数对
            for i in range(int(math.isqrt(target)), 0, -1):
                if target % i == 0:
                    return [i, target // i]
            return [1, target]

        a = find_closest(num + 1)
        b = find_closest(num + 2)

        # 返回绝对差更小的那对
        if abs(a[0] - a[1]) < abs(b[0] - b[1]):
            return a
        return b



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 要使两个因数的绝对差最小，应选择最接近 sqrt(target) 的因数对。
# 1. 分别对 num+1 和 num+2 寻找最接近的一对因数。
#    从 sqrt(target) 向下遍历到 1，第一个能整除 target 的 i 就是最接近 sqrt 的因数，
#    此时因数对为 [i, target // i]。
# 2. 比较两对因数的绝对差，返回差值更小的那对。
#
# 时间复杂度: O(sqrt(N))，最坏情况下需遍历到 1 才找到因数（当 num 为质数时）
# 空间复杂度: O(1)
#
# 关键点:
# - 因数越接近 sqrt(target)，绝对差越小
# - 从 sqrt 向下遍历确保第一个匹配的就是最优解
# - 对 num+1 和 num+2 分别求解，取更优者













