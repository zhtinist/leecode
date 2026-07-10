"""
LeetCode #280 - Wiggle Sort
https://leetcode.com/problems/wiggle-sort/

Given an unsorted array `nums`, reorder it in-place such that `nums[0]
<= nums[1] >= nums[2] <= nums[3]...`.

Example:

Input: `nums = [3,5,2,1,6,4]`
Output: One possible answer is [3,5,1,6,2,4]
"""

from typing import List, Optional


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """Reorder array in-place: nums[0] <= nums[1] >= nums[2] <= nums[3]...

        One-pass greedy: For each index i from 0 to n-2:
        - If i is even (should be <= next): ensure nums[i] <= nums[i+1], else swap
        - If i is odd (should be >= next): ensure nums[i] >= nums[i+1], else swap
        """
        for i in range(len(nums) - 1):
            if i % 2 == 0:
                # Even index: should be <= next
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            else:
                # Odd index: should be >= next
                if nums[i] < nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: Yes
#
# 解题思路:
# 一遍扫描贪心法。遍历数组，对于每个索引 i：
# - 如果 i 是偶数（nums[i] 应 <= nums[i+1]），若 nums[i] > nums[i+1] 则交换
# - 如果 i 是奇数（nums[i] 应 >= nums[i+1]），若 nums[i] < nums[i+1] 则交换
#
# 这个方法的正确性基于：交换不会破坏前面已经满足的条件。
# 例如，当 i 是偶数且 nums[i-1] >= nums[i] 时，如果 nums[i] > nums[i+1]，
# 交换后 nums[i-1] >= nums[i+1]（因为 nums[i] > nums[i+1] 且 nums[i-1] >= nums[i]），
# 所以之前的条件不会被破坏。
#
# 时间复杂度: O(N) - 一次遍历
# 空间复杂度: O(1) - 原地操作
#
# 关键点:
# - 奇偶位置分别要求 >= 和 <=
# - 交换操作不会破坏前面已满足的摇摆条件
# - 不需要排序，只需局部调整相邻元素
