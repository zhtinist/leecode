"""
LeetCode #283 - Move Zeroes
https://leetcode.com/problems/move-zeroes/

Given an array `nums`, write a function to move all `0`'s to the
end of it while maintaining the relative order of the non-zero elements.

Example:

Input: `[0,1,0,3,12]`
Output: `[1,3,12,0,0]`

Note:

You must do this in-place without making a copy of the array.

Minimize the total number of operations.
"""

from typing import List, Optional


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """Move all zeros to the end of the array in-place.

        Two-pointer approach:
        - insert_pos: where the next non-zero element should be placed
        - i: current scanning position
        After placing all non-zeros at the front, fill remaining positions with zeros.
        """
        insert_pos = 0  # position to place next non-zero element

        # Move all non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                insert_pos += 1

        # Fill the rest with zeros
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Easy
# Paid Only: No
#
# 解题思路:
# 双指针法。使用一个指针 insert_pos 记录下一个非零元素应该放置的位置。
# 遍历数组，遇到非零元素就放到 insert_pos 位置，然后 insert_pos 右移。
# 遍历完成后，从 insert_pos 到数组末尾的所有位置填入 0。
# 这种方法保持了非零元素的相对顺序，且操作次数最少。
#
# 时间复杂度: O(N) - 一次遍历放置非零元素，一次填充零
# 空间复杂度: O(1) - 原地操作
#
# 关键点:
# - 使用 insert_pos 作为"写指针"
# - 非零元素的相对顺序保持不变
# - 遍历完成后再统一填充零（避免交换操作）
# - 也可以使用交换法：遇到非零就与 insert_pos 交换
