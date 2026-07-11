"""
LeetCode #2447 - Number of Subarrays With GCD Equal to K
最大公因数等于 K 的子数组数目
https://leetcode.cn/problems/number-of-subarrays-with-gcd-equal-to-k/

给你一个整数数组 `nums` 和一个整数 `k` ，请你统计并返回 `nums` 的子数组中元素的最大公因数等于 `k` 的子数组数目。
子数组 是数组中一个连续的非空序列。
数组的最大公因数 是能整除数组中所有元素的最大整数。

示例 1：
输入：nums = [9,3,1,2,6,3], k = 3 输出：4 解释：nums 的子数组中，以 3 作为最大公因数的子数组如下： - [9,3,1,2,6,3] - [9,3,1,2,6,3] - [9,3,1,2,6,3] - [9,3,1,2,6,3]
示例 2：
输入：nums = [4], k = 7 输出：0 解释：不存在以 7 作为最大公因数的子数组。

提示：
`1 <= nums.length <= 1000`
`1 <= nums[i], k <= 10^9`
"""

from typing import List, Optional


from math import gcd


class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            current_gcd = 0
            for j in range(i, n):
                current_gcd = gcd(current_gcd, nums[j])
                if current_gcd == k:
                    count += 1
                # If current_gcd is not divisible by k, no further extension can yield exactly k
                if current_gcd % k != 0:
                    break
        return count


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Math, Number Theory
#
# 解题思路:
# 枚举所有子数组（以 i 为起点，j 为终点）。对于每个 i 开始的子数组，维护当前 GCD。
# 如果当前 GCD 等于 k，计数加一。如果当前 GCD 不能被 k 整除，则后续的 GCD 也不可能等于 k
# （因为 GCD 只会递减），直接 break 剪枝。nums 长度 <= 1000，O(n^2) 可行。
#
# 时间复杂度: O(n^2 * log M)，其中 M 是数组中元素的最大值
# 空间复杂度: O(1)
#
# 关键点:
# - GCD 的单调性：在固定起点 i 扩展子数组时，GCD 是非递增的
# - 剪枝条件：当 current_gcd % k != 0 时 break，因为后续 GCD 只会更小，不可能等于 k
# - 初始 current_gcd 设为 0，因为 gcd(0, x) = x
