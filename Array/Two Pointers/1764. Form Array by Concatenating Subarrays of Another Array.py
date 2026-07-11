"""
LeetCode #1764 - Form Array by Concatenating Subarrays of Another Array
中文题名：通过连接另一个数组的子数组得到一个数组
https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/

You are given a 2D integer array `groups` of length `n`. You are also given an integer array `nums`.

You are asked if you can choose `n` disjoint subarrays from the array `nums` such that the `ith` subarray is equal to `groups[i]` (0-indexed), and if `i > 0`, the `(i-1)th` subarray appears before the `ith` subarray in `nums` (i.e. the subarrays must be in the same order as `groups`).

Return `true` if you can do this task, and `false` otherwise.

Note that the subarrays are disjoint if and only if there is no index `k` such that `nums[k]` belongs to more than one subarray. A subarray is a contiguous sequence of elements within an array.

Example 1:

Input: groups = [[1,-1,-1],[3,-2,0]], nums = [1,-1,0,1,-1,-1,3,-2,0]
Output: true
Explanation: You can choose the 0th subarray as [1,-1,0,1,-1,-1,3,-2,0] and the 1st one as [1,-1,0,1,-1,-1,3,-2,0].
These subarrays are disjoint as they share no common nums[k] element.

Example 2:

Input: groups = [[10,-2],[1,2,3,4]], nums = [1,2,3,4,10,-2]
Output: false
Explanation: Note that choosing the subarrays [1,2,3,4,10,-2] and [1,2,3,4,10,-2] is incorrect because they are not in the same order as in groups.
[10,-2] must come before [1,2,3,4].

Example 3:

Input: groups = [[1,2,3],[3,4]], nums = [7,7,1,2,3,4,7,7]
Output: false
Explanation: Note that choosing the subarrays [7,7,1,2,3,4,7,7] and [7,7,1,2,3,4,7,7] is invalid because they are not disjoint.
They share a common elements nums[4] (0-indexed).

Constraints:

`groups.length == n`

`1 <= n <= 103`

`1 <= groups[i].length, sum(groups[i].length) <= 103`

`1 <= nums.length <= 103`

`-107 <= groups[i][j], nums[k] <= 107`

【中文翻译】
给定一个二维整数数组 groups（每个 groups[i] 是一个子数组）和一个整数数组 nums。
判断是否可以从 nums 中选择若干不相交的子数组（保持顺序），使得这些子数组按顺序完全等于 groups 中的每个子数组。

示例 1：
输入: groups = [[1,-1,-1],[3,-2,0]], nums = [1,-1,0,1,-1,-1,3,-2,0]
输出: true
解释: 选择 nums[0..2]=[1,-1,0]?不对...应该选择 [1,-1,-1] 和 [3,-2,0]。
"""

from typing import List, Optional


class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        i = 0  # nums 的当前位置
        for group in groups:
            found = False
            while i + len(group) <= len(nums):
                # 检查从 i 开始是否匹配 group
                if nums[i:i + len(group)] == group:
                    i += len(group)
                    found = True
                    break
                i += 1
            if not found:
                return False
        return True
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心 + 双指针。按顺序处理每个 group，在 nums 中从前向后查找该 group。
# 对于每个 group：从当前位置 i 开始向右搜索，找到第一个匹配的位置。
# 找到后 i 跳到匹配结束位置。如果找不到返回 false。
# 贪心正确性：因为 groups 必须按顺序匹配，并且子数组不能重叠，
# 越早匹配当前 group 留给后面 group 的搜索空间越大。
#
# 时间复杂度: O(N * G) — N 为 nums 长度，G 为 groups 总元素数
# 空间复杂度: O(1)
#
# 关键点:
# - 必须按顺序匹配 groups
# - 贪心：最早匹配即可，因为后续 group 需要后面的空间
# - 用切片比较简化代码
