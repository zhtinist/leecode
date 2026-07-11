"""
LeetCode #3566 - Partition Array into Two Equal Product Subsets
等积子集的划分方案
https://leetcode.cn/problems/partition-array-into-two-equal-product-subsets/

给你一个整数数组 `nums`，其中包含的正整数 互不相同 ，另给你一个整数 `target`。
请判断是否可以将 `nums` 分成两个 非空、互不相交 的 子集 ，并且每个元素必须  恰好 属于 一个 子集，使得这两个子集中元素的乘积都等于 `target`。
如果存在这样的划分，返回 `true`；否则，返回 `false`。
子集 是数组中元素的一个选择集合。

示例 1：

输入： nums = [3,1,6,8,4], target = 24
输出： true
解释：子集 `[3, 8]` 和 `[1, 6, 4]` 的乘积均为 24。因此，输出为 true 。
示例 2：

输入： nums = [2,5,3,7], target = 15
输出： false
解释：无法将 `nums` 划分为两个非空的互不相交子集，使得它们的乘积均为 15。因此，输出为 false。

提示：
`3 <= nums.length <= 12`
`1 <= target <= 10^15`
`1 <= nums[i] <= 100`
`nums` 中的所有元素互不相同。
"""

from typing import List, Optional


class Solution:
    def canPartition(self, nums: List[int], target: int) -> bool:
        n = len(nums)

        # Pre-filter: if any element > target, it cannot be in a subset
        # Also if target == 1, we need each subset product = 1, which only works
        # if all elements are 1 (since distinct positive integers)
        # But nums are distinct positive integers, handle general case.

        # Enumerate all non-empty subsets using bitmask
        # n <= 12, 2^n <= 4096
        for mask in range(1, (1 << n) - 1):  # exclude empty set and full set
            prod = 1
            for i in range(n):
                if mask & (1 << i):
                    prod *= nums[i]
                    if prod > target:
                        break
            if prod == target:
                # Check if the complement also has product == target
                complement_prod = 1
                for i in range(n):
                    if not (mask & (1 << i)):
                        complement_prod *= nums[i]
                        if complement_prod > target:
                            break
                if complement_prod == target:
                    return True

        return False










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Recursion, Array, Enumeration
#
# 解题思路:
# 使用位掩码枚举所有可能的子集划分。nums 长度最多为 12，子集总数为 2^12 = 4096，枚举可行。
# 对于每个非空且非全集的子集（用 mask 表示），计算该子集中所有元素的乘积。
# 如果乘积等于 target，再计算补集（不在该子集中的元素）的乘积是否也等于 target。
# 如果双双相等，返回 true。遍历所有子集未找到则返回 false。
# 注意中途乘积超过 target 时可以提前 break 以加速判断。
#
# 时间复杂度: O(2^n * n)，其中 n = len(nums) <= 12。枚举 2^n 个子集，每个计算 O(n) 乘积。
#   总操作约 4096 * 12 ≈ 5 万次，非常快。
# 空间复杂度: O(1)，只使用常数个变量。
#
# 关键点:
# - n 很小（<=12），子集枚举是最简单可靠的解法。
# - 排除空集（mask=0）和全集（mask=2^n-1），因为要求两个子集都非空。
# - 乘积可能很大（target 最大 10^15），使用 Python 的任意精度整数安全处理。
