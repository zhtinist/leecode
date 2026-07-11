"""
LeetCode #2104 - Sum of Subarray Ranges
子数组范围和
https://leetcode.cn/problems/sum-of-subarray-ranges/

给你一个整数数组 `nums` 。`nums` 中，子数组的 范围 是子数组中最大元素和最小元素的差值。
返回 `nums` 中 所有 子数组范围的 和 。
子数组是数组中一个连续 非空 的元素序列。

示例 1：
输入：nums = [1,2,3] 输出：4 解释：nums 的 6 个子数组如下所示： [1]，范围 = 最大 - 最小 = 1 - 1 = 0  [2]，范围 = 2 - 2 = 0 [3]，范围 = 3 - 3 = 0 [1,2]，范围 = 2 - 1 = 1 [2,3]，范围 = 3 - 2 = 1 [1,2,3]，范围 = 3 - 1 = 2 所有范围的和是 0 + 0 + 0 + 1 + 1 + 2 = 4
示例 2：
输入：nums = [1,3,3] 输出：4 解释：nums 的 6 个子数组如下所示： [1]，范围 = 最大 - 最小 = 1 - 1 = 0 [3]，范围 = 3 - 3 = 0 [3]，范围 = 3 - 3 = 0 [1,3]，范围 = 3 - 1 = 2 [3,3]，范围 = 3 - 3 = 0 [1,3,3]，范围 = 3 - 1 = 2 所有范围的和是 0 + 0 + 0 + 2 + 0 + 2 = 4
示例 3：
输入：nums = [4,-2,-3,4,1] 输出：59 解释：nums 中所有子数组范围的和是 59

提示：
`1 <= nums.length <= 1000`
`-10^9 <= nums[i] <= 10^9`

进阶：你可以设计一种时间复杂度为 `O(n)` 的解决方案吗？
"""

from typing import List, Optional


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)

        def sum_contributions(is_max):
            total = 0
            stack = []
            for i in range(n + 1):
                cur = nums[i] if i < n else (float('inf') if is_max else float('-inf'))
                while stack and (
                    (is_max and cur > nums[stack[-1]]) or
                    (not is_max and cur < nums[stack[-1]])
                ):
                    j = stack.pop()
                    left = stack[-1] if stack else -1
                    total += nums[j] * (i - j) * (j - left)
                stack.append(i)
            return total

        return sum_contributions(True) - sum_contributions(False)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Stack, Array, Monotonic Stack
#
# 解题思路:
# 所有子数组范围之和 = 所有子数组最大值之和 - 所有子数组最小值之和。
# 使用单调栈计算每个元素作为最大值和最小值的贡献次数：
# 对于元素 nums[j]，在单调栈中找到左边第一个比它大/小的位置 left，
# 和右边第一个比它大/小的位置 right。
# 则以 nums[j] 为最大/最小值的子数组数量 = (j - left) * (right - j)。
# 该元素的总贡献 = nums[j] * (j - left) * (right - j)。
# 最后用最大贡献总和减去最小贡献总和即得答案。
#
# 时间复杂度: O(N)，每个元素入栈出栈各一次。
# 空间复杂度: O(N)，单调栈的空间开销。
#
# 关键点:
# - 将"子数组范围"拆分为"最大值贡献"和"最小值贡献"两个子问题。
# - 单调栈维护严格递增/递减，确保每个子数组的极值只被计数一次。
# - 哨兵值（正无穷/负无穷）确保所有元素最终都被弹出处理。
