"""
LeetCode #2576 - Find the Maximum Number of Marked Indices
求出最多标记下标
https://leetcode.cn/problems/find-the-maximum-number-of-marked-indices/

给你一个下标从 0 开始的整数数组 `nums` 。
一开始，所有下标都没有被标记。你可以执行以下操作任意次：
选择两个 互不相同且未标记 的下标 `i` 和 `j` ，满足 `2 * nums[i] <= nums[j]` ，标记下标 `i` 和 `j` 。
请你执行上述操作任意次，返回 `nums` 中最多可以标记的下标数目。

示例 1：
输入：nums = [3,5,2,4] 输出：2 解释：第一次操作中，选择 i = 2 和 j = 1 ，操作可以执行的原因是 2 * nums[2] <= nums[1] ，标记下标 2 和 1 。 没有其他更多可执行的操作，所以答案为 2 。
示例 2：
输入：nums = [9,2,5,4] 输出：4 解释：第一次操作中，选择 i = 3 和 j = 0 ，操作可以执行的原因是 2 * nums[3] <= nums[0] ，标记下标 3 和 0 。 第二次操作中，选择 i = 1 和 j = 2 ，操作可以执行的原因是 2 * nums[1] <= nums[2] ，标记下标 1 和 2 。 没有其他更多可执行的操作，所以答案为 4 。
示例 3：
输入：nums = [7,6,8] 输出：0 解释：没有任何可以执行的操作，所以答案为 0 。

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        i, j = 0, n // 2
        pairs = 0
        while i < n // 2 and j < n:
            if 2 * nums[i] <= nums[j]:
                pairs += 1
                i += 1
                j += 1
            else:
                j += 1
        return pairs * 2



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Two Pointers, Binary Search, Sorting
#
# 解题思路:
# 排序后使用双指针贪心匹配。将数组分为较小的一半和较大的一半，用指针i遍历较小半、
# 指针j遍历较大半。若2*nums[i]<=nums[j]则匹配成功，i和j都前进；否则只有j前进。
# 这保证了尽可能多地配对较小的数与较大的数。每匹配一对，标记2个下标。
#
# 时间复杂度: O(N log N)
# 空间复杂度: O(1)
#
# 关键点:
# - 贪心：较小的i匹配最小的满足2*num[i]<=num[j]的j
# - 两半划分：前n/2和后n/2，因为每个i至少有一个不同的j满足条件
# - 排序确保每一对被标记的是不同下标，不会冲突
