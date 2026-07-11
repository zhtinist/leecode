"""
LeetCode #915 - Partition Array into Disjoint Intervals
中文题名：分割数组
https://leetcode.com/problems/partition-array-into-disjoint-intervals/

Given an array `A`, partition it into two (contiguous) subarrays `left` and
`right` so that:

Every element in `left` is less than or equal to every element in `right`.

`left` and `right` are non-empty.

`left` has the smallest possible size.

Return the length of `left` after such a partitioning.  It
is guaranteed that such a partitioning exists.

Example 1:

Input: [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]

Example 2:

Input: [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]

【中文翻译】

给定一个数组 A，将其划分为两个（连续的）子数组 left 和 right，使得：
- left 中的每个元素都小于或等于 right 中的每个元素。
- left 和 right 都非空。
- left 的长度尽可能小。
返回划分后 left 的长度。保证这样的划分存在。

"""

from typing import List, Optional


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        """
        Track the running maximum from the left.
        When the running max <= the minimum of the remaining right side,
        we have found the partition point.
        """
        n = len(nums)

        # min_from_right[i] = min(nums[i:])
        min_from_right = [0] * n
        min_from_right[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            min_from_right[i] = min(nums[i], min_from_right[i + 1])

        max_left = nums[0]
        for i in range(1, n):
            if max_left <= min_from_right[i]:
                return i
            max_left = max(max_left, nums[i])

        return -1  # Should never reach here per problem guarantee



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 需要将数组分为 left 和 right 两部分，满足 max(left) <= min(right)，
# 且 left 尽可能短。
# 1. 从右到左预处理 min_from_right 数组，记录每个位置右侧（含当前位置）的最小值。
# 2. 从左到右遍历，维护当前已遍历元素的最大值 max_left。
# 3. 当 max_left <= min_from_right[i] 时，说明前 i 个元素可以构成 left。
#    由于我们要求 left 尽可能短，直接返回 i 即可。
#
# 时间复杂度: O(N)
# 空间复杂度: O(N)，可以优化到 O(1)（只需维护一个变量记录右侧最小值）
#
# 关键点:
# - 需要同时知道左边的最大值和右边的最小值
# - 向右扩展 left 直到 max(left) <= min(right)
