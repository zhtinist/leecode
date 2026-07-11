"""
LeetCode #3779 - Minimum Number of Operations to Have Distinct Elements
得到互不相同元素的最少操作次数
https://leetcode.cn/problems/minimum-number-of-operations-to-have-distinct-elements/

给你一个整数数组 `nums`。
在一次操作中，你需要移除当前数组的 前三个元素。如果剩余元素少于三个，则移除 所有 剩余元素。
重复此操作，直到数组为空或不包含任何重复元素为止。
返回一个整数，表示所需的操作次数。

示例 1:

输入: nums = [3,8,3,6,5,8]
输出: 1
解释:
在第一次操作中，我们移除前三个元素。剩余的元素 `[6, 5, 8]` 互不相同，因此停止。仅需要一次操作。
示例 2:

输入: nums = [2,2]
输出: 1
解释:
经过一次操作后，数组变为空，满足停止条件。
示例 3:

输入: nums = [4,3,5,1,2]
输出: 0
解释:
数组中的所有元素都是互不相同的，因此不需要任何操作。

提示:
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^5`
"""

from typing import List, Optional


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        seen = set()
        boundary = -1  # rightmost index where a duplicate exists in suffix

        for i in range(n - 1, -1, -1):
            if nums[i] in seen:
                boundary = i
                break
            seen.add(nums[i])

        if boundary == -1:
            return 0  # already all distinct

        # Need to skip past boundary: start must be > boundary
        # Each operation removes 3 elements from the front
        # start = 0 initially, ops needed = ceil((boundary + 1) / 3)
        return (boundary // 3) + 1










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table
#
# 解题思路:
# 从右到左扫描，找到最靠右的出现重复元素的位置 boundary。
# 在 boundary 及之前的位置开始的子数组一定包含重复元素。
# 每次操作移除前 3 个元素，所以需要 ceil((boundary + 1) / 3) 次操作
# 才能保证剩余数组从 boundary+1 开始（全不重复）。
# 公式：(boundary // 3) + 1 等价于 ceil((boundary + 1) / 3)。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 从右向左扫描确定第一个重复位置
# - 操作次数 = ceil((boundary+1)/3)
