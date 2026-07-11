"""
LeetCode #3523 - Make Array Non-decreasing
非递减数组的最大长度
https://leetcode.cn/problems/make-array-non-decreasing/

给你一个整数数组 `nums`。在一次操作中，你可以选择一个子数组，并将其替换为一个等于该子数组 最大值 的单个元素。
返回经过零次或多次操作后，数组仍为 非递减 的情况下，数组 可能的最大长度。
子数组 是数组中一个连续、非空 的元素序列。

示例 1：

输入： nums = [4,2,5,3,5]
输出： 3
解释：
实现最大长度的一种方法是：
将子数组 `nums[1..2] = [2, 5]` 替换为 `5` → `[4, 5, 3, 5]`。
将子数组 `nums[2..3] = [3, 5]` 替换为 `5` → `[4, 5, 5]`。
最终数组 `[4, 5, 5]` 是非递减的，长度为 3。
示例 2：

输入： nums = [1,2,3]
输出： 3
解释：
无需任何操作，因为数组 `[1,2,3]` 已经是非递减的。

提示：
`1 <= nums.length <= 2 * 10^5`
`1 <= nums[i] <= 2 * 10^5`
"""

from typing import List, Optional


class Solution:
    def maxLength(self, nums: List[int]) -> int:
        stack = []  # each element is (max_val, count_of_groups_merged)
        for x in nums:
            if not stack or x >= stack[-1][0]:
                # Can start a new group
                stack.append([x, 1])
            else:
                # Must merge into the last group
                # The max of the last group stays the same (since x < last_max)
                stack[-1][1] += 1
        return len(stack)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Stack, Greedy, Array, Monotonic Stack
#
# 解题思路:
# 1. 操作将子数组替换为其最大值，等价于将一些相邻元素分组，每组用最大值代表
# 2. 目标是最大化组数，同时保持各组代表值非递减
# 3. 贪心策略：遍历数组，维护栈（每组代表最大值）
#    - 若当前元素 >= 栈顶最大值：可以开始新组（增加长度），将 (x, 1) 入栈
#    - 若当前元素 < 栈顶最大值：必须合并到最后一组（组数不变），栈顶组的元素数 +1
#      因为合并进来更小的元素不会改变该组的最大值
# 4. 栈的大小即为最大可能的数组长度
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 新组只能在其代表值 >= 前一组的代表值时创建
# - 合并更小的元素不会降低组的最大值，因此不影响非递减性质
# - 贪心"能开新组就开"是最优的
