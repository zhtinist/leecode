"""
LeetCode #2261 - K Divisible Elements Subarrays
含最多 K 个可整除元素的子数组
https://leetcode.cn/problems/k-divisible-elements-subarrays/

给你一个整数数组 `nums` 和两个整数 `k` 和 `p` ，找出并返回满足要求的不同的子数组数，要求子数组中最多 `k` 个可被 `p` 整除的元素。
如果满足下述条件之一，则认为数组 `nums1` 和 `nums2` 是 不同 数组：
两数组长度 不同 ，或者
存在 至少 一个下标 `i` 满足 `nums1[i] != nums2[i]` 。
子数组 定义为：数组中的连续元素组成的一个 非空 序列。

示例 1：
输入：nums = [2,3,3,2,2], k = 2, p = 2 输出：11 解释： 位于下标 0、3 和 4 的元素都可以被 p = 2 整除。 共计 11 个不同子数组都满足最多含 k = 2 个可以被 2 整除的元素： [2]、[2,3]、[2,3,3]、[2,3,3,2]、[3]、[3,3]、[3,3,2]、[3,3,2,2]、[3,2]、[3,2,2] 和 [2,2] 。 注意，尽管子数组 [2] 和 [3] 在 nums 中出现不止一次，但统计时只计数一次。 子数组 [2,3,3,2,2] 不满足条件，因为其中有 3 个元素可以被 2 整除。
示例 2：
输入：nums = [1,2,3,4], k = 4, p = 1 输出：10 解释： nums 中的所有元素都可以被 p = 1 整除。 此外，nums 中的每个子数组都满足最多 4 个元素可以被 1 整除。 因为所有子数组互不相同，因此满足所有限制条件的子数组总数为 10 。

提示：
`1 <= nums.length <= 200`
`1 <= nums[i], p <= 200`
`1 <= k <= nums.length`

进阶：
你可以设计并实现时间复杂度为 `O(n^2)` 的算法解决此问题吗？
"""

from typing import List, Optional


class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        """
        Count the number of distinct subarrays where at most k elements are divisible by p.
        Since n <= 200, we can enumerate all subarrays and use a set of tuples for deduplication.
        For each starting index i, expand j and track the count of divisible elements.
        If count exceeds k, break the inner loop early.
        """
        n = len(nums)
        seen: set[tuple] = set()

        for i in range(n):
            divisible_count = 0
            for j in range(i, n):
                if nums[j] % p == 0:
                    divisible_count += 1
                if divisible_count > k:
                    break
                # Add the subarray nums[i:j+1] as a tuple for deduplication
                seen.add(tuple(nums[i:j+1]))

        return len(seen)


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Trie, Array, Hash Table, Enumeration, Hash Function, Rolling Hash
#
# 解题思路:
# 题目要求统计不同的子数组数量，满足子数组中能被 p 整除的元素不超过 k 个。
# 由于 n <= 200（规模较小），可以直接枚举所有子数组：
# 对于每个起始位置 i，向右扩展 j，同时统计能被 p 整除的元素个数。
# 当可整除元素数量超过 k 时，提前终止内层循环（剪枝优化）。
# 用 set 存储子数组的元组表示来实现去重，最终返回 set 的大小。
#
# 时间复杂度: O(n^3)，其中 n <= 200。枚举起止位置是 O(n^2)，将子数组转为元组是 O(n)。
# 实际运行中 n=200 时约 8e6 次操作，在 Python 中可以通过。
# 空间复杂度: O(n^2)，最坏情况下存储所有子数组的元组表示。
#
# 关键点:
# - 直接枚举所有子数组（n 很小，暴力可行）
# - 使用 set of tuples 去重，确保只统计不同的子数组
# - 内层循环中当可整除元素超过 k 时提前 break，否则后续子数组必然超限
# - 进阶优化可使用字典树 (Trie) 或滚动哈希进一步减少复杂度
