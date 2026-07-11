"""
LeetCode #3618 - Split Array by Prime Indices
根据质数下标分割数组
https://leetcode.cn/problems/split-array-by-prime-indices/

给你一个整数数组 `nums`。
根据以下规则将 `nums` 分割成两个数组 `A` 和 `B`：
`nums` 中位于 质数 下标的元素必须放入数组 `A`。
所有其他元素必须放入数组 `B`。
返回两个数组和的 绝对 差值：`|sum(A) - sum(B)|`。
质数 是一个大于 1 的自然数，它只有两个因子，1和它本身。
注意：空数组的和为 0。

示例 1:

输入: nums = [2,3,4]
输出: 1
解释:
数组中唯一的质数下标是 2，所以 `nums[2] = 4` 被放入数组 `A`。
其余元素 `nums[0] = 2` 和 `nums[1] = 3` 被放入数组 `B`。
`sum(A) = 4`，`sum(B) = 2 + 3 = 5`。
绝对差值是 `|4 - 5| = 1`。
示例 2:

输入: nums = [-1,5,7,0]
输出: 3
解释:
数组中的质数下标是 2 和 3，所以 `nums[2] = 7` 和 `nums[3] = 0` 被放入数组 `A`。
其余元素 `nums[0] = -1` 和 `nums[1] = 5` 被放入数组 `B`。
`sum(A) = 7 + 0 = 7`，`sum(B) = -1 + 5 = 4`。
绝对差值是 `|7 - 4| = 3`。

提示:
`1 <= nums.length <= 10^5`
`-10^9 <= nums[i] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def splitArrayByPrimeIndices(self, nums: List[int]) -> int:
        n = len(nums)

        # Sieve of Eratosthenes to mark primes up to n-1
        is_prime = [True] * n
        if n > 0:
            is_prime[0] = False  # index 0 is not prime
        if n > 1:
            is_prime[1] = False  # index 1 is not prime

        limit = int(n ** 0.5)
        for i in range(2, limit + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False

        sum_a = 0  # elements at prime indices
        sum_b = 0  # elements at non-prime indices
        for i in range(n):
            if is_prime[i]:
                sum_a += nums[i]
            else:
                sum_b += nums[i]

        return abs(sum_a - sum_b)










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Math, Number Theory
#
# 解题思路:
# 问题要求按索引是否为质数将数组元素分成两组 A（质数索引）和 B（非质数索引），
# 计算 |sum(A) - sum(B)|。
#
# 1. 使用埃拉托斯特尼筛法预处理 0 到 n-1 中哪些是质数
#    - 索引 0 和 1 不是质数
#    - 从 2 开始标记质数的倍数为非质数
# 2. 遍历数组，根据 is_prime[i] 累加到 sum_a 或 sum_b
# 3. 返回 |sum_a - sum_b|
#
# 时间复杂度: O(N * log(log N)) — 筛法复杂度, N = len(nums)
# 空间复杂度: O(N) — is_prime 布尔数组
#
# 关键点:
# - 质数判断的是索引而非元素值
# - 索引 0 和 1 不是质数（质数定义为大于 1）
# - 筛法上限为 sqrt(n)，效率更高
# - 空数组的和为 0（但 n >= 1 根据约束）
