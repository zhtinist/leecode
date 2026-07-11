"""
LeetCode #1144 - Decrease Elements To Make Array Zigzag
中文题名：递减元素使数组呈锯齿状
https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/

Given an array `nums` of integers, a move consists of choosing any
element and decreasing it by 1.

An array `A` is a zigzag array if either:

Every even-indexed element is greater than adjacent elements, ie. `A[0] >
A[1] < A[2] > A[3] < A[4] > ...`

OR, every odd-indexed element is greater than adjacent elements, ie. `A[0]
< A[1] > A[2] < A[3] > A[4] < ...`

Return the minimum number of moves to transform the given array `nums` into a
zigzag array.

Example 1:

Input: nums = [1,2,3]
Output: 2
Explanation: We can decrease 2 to 0 or 3 to 1.

Example 2:

Input: nums = [9,6,1,6,2]
Output: 4

Constraints:

`1 <= nums.length <= 1000`

`1 <= nums[i] <= 1000`

【中文翻译】
给定一个整数数组 nums，每次操作可以选择任意一个元素并将其减少 1。

如果数组 A 满足以下任一条件，则它是一个锯齿数组：

每个偶数索引的元素都大于其相邻元素，即 A[0] > A[1] < A[2] > A[3] < A[4] > ...

或者，每个奇数索引的元素都大于其相邻元素，即 A[0] < A[1] > A[2] < A[3] > A[4] < ...

返回将给定数组 nums 转换为锯齿数组所需的最少操作次数。

示例 1：

输入：nums = [1,2,3]
输出：2
解释：我们可以将 2 减少到 0，或将 3 减少到 1。

示例 2：

输入：nums = [9,6,1,6,2]
输出：4

约束条件：

`1 <= nums.length <= 1000`

`1 <= nums[i] <= 1000`
"""

from typing import List, Optional


class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)

        def moves_to_make_small(start: int) -> int:
            """
            Make elements at indices start, start+2, start+4, ...
            smaller than their neighbors.
            start=0 means even indices are peaks (odd indices smaller).
            start=1 means odd indices are peaks (even indices smaller).
            """
            moves = 0
            for i in range(start, n, 2):
                target = nums[i]
                if i > 0:
                    target = min(target, nums[i - 1] - 1)
                if i < n - 1:
                    target = min(target, nums[i + 1] - 1)
                if target < nums[i]:
                    moves += nums[i] - max(target, 0)
            return moves

        # Case 1: even indices are peaks (odd indices smaller)
        # Case 2: odd indices are peaks (even indices smaller)
        return min(moves_to_make_small(1), moves_to_make_small(0))










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 锯齿数组有两种模式：
# 模式一：偶数索引是峰顶（A[0] > A[1] < A[2] > A[3] < ...）
#   即奇数索引的元素需要小于相邻元素。
# 模式二：奇数索引是峰顶（A[0] < A[1] > A[2] < A[3] > ...）
#   即偶数索引的元素需要小于相邻元素。
#
# 由于只能减少元素，对于需要变小的位置（波谷位置），将其减少到
# min(左邻居 - 1, 右邻居 - 1)，并确保不小于 0。计算这种操作的总次数。
# 分别计算两种模式所需的操作数，取最小值即可。
#
# 对于每个需要变小的位置 i：
# - target 初始为 nums[i]
# - 如果 i > 0，target = min(target, nums[i-1] - 1)
# - 如果 i < n-1，target = min(target, nums[i+1] - 1)
# - 操作次数 = nums[i] - max(target, 0)
#
# 时间复杂度: O(n) - 两次遍历数组，每次 O(n)
# 空间复杂度: O(1) - 只使用常数额外空间
#
# 关键点:
# - 只能"减少"元素，不能增加，所以只需考虑将波谷位置的元素降低
# - 波峰位置不需要操作，减小只会增加操作次数
# - 两种模式分别计算，取最小值
# - 注意边界条件：首尾元素只有一个邻居
