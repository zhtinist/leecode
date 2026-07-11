"""
LeetCode #2289 - Steps to Make Array Non-decreasing
使数组按非递减顺序排列
https://leetcode.cn/problems/steps-to-make-array-non-decreasing/

给你一个下标从 0 开始的整数数组 `nums` 。在一步操作中，移除所有满足 `nums[i - 1] > nums[i]` 的 `nums[i]` ，其中 `0 < i < nums.length` 。
重复执行步骤，直到 `nums` 变为 非递减 数组，返回所需执行的操作数。

示例 1：
输入：nums = [5,3,4,4,7,3,6,11,8,5,11] 输出：3 解释：执行下述几个步骤： - 步骤 1 ：[5,3,4,4,7,3,6,11,8,5,11] 变为 [5,4,4,7,6,11,11] - 步骤 2 ：[5,4,4,7,6,11,11] 变为 [5,4,7,11,11] - 步骤 3 ：[5,4,7,11,11] 变为 [5,7,11,11] [5,7,11,11] 是一个非递减数组，因此，返回 3 。
示例 2：
输入：nums = [4,5,7,7,13] 输出：0 解释：nums 已经是一个非递减数组，因此，返回 0 。

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        """
        Use a monotonic decreasing stack to track how many steps each element
        survives before being removed. The answer is the maximum steps any
        element takes to be removed.
        """
        # Stack stores (value, steps_to_remove_this_element)
        stack = []
        max_steps = 0

        for num in nums:
            cur_steps = 0

            # Pop all elements <= current num, recording max steps among them.
            # Those smaller elements get removed before current num does.
            while stack and stack[-1][0] <= num:
                cur_steps = max(cur_steps, stack.pop()[1])

            # If stack still has elements, there is a larger element to the
            # left that will eventually remove current num (after one more step).
            if stack:
                cur_steps += 1
            else:
                # No larger element to the left; this element will never be removed.
                cur_steps = 0

            max_steps = max(max_steps, cur_steps)
            stack.append((num, cur_steps))

        return max_steps


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Stack, Array, Linked List, Dynamic Programming, Monotonic Stack, Simulation
#
# 解题思路:
# 1. 关键洞察：一个元素 nums[i] 会在某一步被它左边第一个大于它的元素移除。
# 2. 但移除时间不是立即的，因为左边的元素可能在更早的步骤中被移除。
# 3. 使用单调递减栈，栈中存储 (元素值, 该元素被移除需要的步数)。
# 4. 遍历数组时：
#    a) 弹出所有 <= 当前值的栈顶元素（这些较小的元素会被当前元素阻挡/提前移除），
#       记录这些被弹出元素的最大步数 cur_steps。
#    b) 如果栈非空（存在更大的左侧元素），当前元素最终会被移除，步数为 cur_steps + 1。
#    c) 如果栈为空（没有更大的左侧元素），当前元素永远不会被移除，步数为 0。
# 5. 答案就是所有元素中被移除所需的最大步数。
#
# 时间复杂度: O(N)，每个元素最多入栈出栈一次
# 空间复杂度: O(N)，栈的大小最多为数组长度
#
# 关键点:
# - 单调递减栈维护左侧的"屏障"元素
# - 弹出较小元素时继承它们的最大步数（因为它们必须先被移除，当前元素才能被移除）
# - 弹出 <= 当前值的元素（等于也要弹出，因为相等的元素不会阻止移除）
# - 步数 +1 是因为需要等待一个额外步骤让当前元素之后被移除
