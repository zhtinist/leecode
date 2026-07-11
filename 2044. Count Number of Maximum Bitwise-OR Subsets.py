"""
LeetCode #2044 - Count Number of Maximum Bitwise-OR Subsets
统计按位或能得到最大值的子集数目
https://leetcode.cn/problems/count-number-of-maximum-bitwise-or-subsets/

给你一个整数数组 `nums` ，请你找出 `nums` 子集 按位或 可能得到的 最大值 ，并返回按位或能得到最大值的 不同非空子集的数目 。
如果数组 `a` 可以由数组 `b` 删除一些元素（或不删除）得到，则认为数组 `a` 是数组 `b` 的一个 子集 。如果选中的元素下标位置不一样，则认为两个子集 不同 。
对数组 `a` 执行 按位或 ，结果等于 `a[0] OR a[1] OR ... OR a[a.length - 1]`（下标从 0 开始）。

示例 1：
输入：nums = [3,1] 输出：2 解释：子集按位或能得到的最大值是 3 。有 2 个子集按位或可以得到 3 ： - [3] - [3,1]
示例 2：
输入：nums = [2,2,2] 输出：7 解释：[2,2,2] 的所有非空子集的按位或都可以得到 2 。总共有 2^3 - 1 = 7 个子集。
示例 3：
输入：nums = [3,2,1,5] 输出：6 解释：子集按位或可能的最大值是 7 。有 6 个子集按位或可以得到 7 ： - [3,5] - [3,1,5] - [3,2,5] - [3,2,1,5] - [2,5] - [2,1,5]

提示：
`1 <= nums.length <= 16`
`1 <= nums[i] <= 10^5`
"""

from typing import List, Optional


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for v in nums:
            max_or |= v

        n = len(nums)
        self.count = 0

        def backtrack(index: int, cur_or: int):
            if index == n:
                if cur_or == max_or:
                    self.count += 1
                return
            # Include nums[index]
            backtrack(index + 1, cur_or | nums[index])
            # Exclude nums[index]
            backtrack(index + 1, cur_or)

        backtrack(0, 0)
        return self.count



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Array, Backtracking, Enumeration
#
# 解题思路:
# 最大OR值 = 所有元素的OR。然后使用回溯法枚举所有非空子集，
# 统计OR值等于最大OR值的子集数量。n <= 16，2^16 = 65536，回溯完全可行。
#
# 时间复杂度: O(2^n)
# 空间复杂度: O(n) 递归深度
#
# 关键点:
# - 最大OR值即所有元素OR的结果
# - 回溯枚举所有子集
# - n <= 16 确保2^n可行
