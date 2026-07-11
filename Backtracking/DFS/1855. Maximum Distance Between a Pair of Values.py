"""
LeetCode #1855 - Maximum Distance Between a Pair of Values
中文题名：一对值的最大距离
https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/

You are given two non-increasing 0-indexed integer arrays `nums1`​​​​​​ and `nums2`​​​​​​.

A pair of indices `(i, j)`, where `0 <= i < nums1.length` and `0 <= j < nums2.length`, is valid if both `i <= j` and `nums1[i] <= nums2[j]`. The distance of the pair is `j - i`​​​​.

Return the maximum distance of any valid pair `(i, j)`. If there are no valid pairs, return `0`.

An array `arr` is non-increasing if `arr[i-1] >= arr[i]` for every `1 <= i < arr.length`.

Example 1:

Input: nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]
Output: 2
Explanation: The valid pairs are (0,0), (2,2), (2,3), (2,4), (3,3), (3,4), and (4,4).
The maximum distance is 2 with pair (2,4).

Example 2:

Input: nums1 = [2,2,2], nums2 = [10,10,1]
Output: 1
Explanation: The valid pairs are (0,0), (0,1), and (1,1).
The maximum distance is 1 with pair (0,1).

Example 3:

Input: nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]
Output: 2
Explanation: The valid pairs are (2,2), (2,3), (2,4), (3,3), and (3,4).
The maximum distance is 2 with pair (2,4).

Example 4:

Input: nums1 = [5,4], nums2 = [3,2]
Output: 0
Explanation: There are no valid pairs, so return 0.

Constraints:

`1 <= nums1.length <= 105`

`1 <= nums2.length <= 105`

`1 <= nums1[i], nums2[j] <= 105`

Both `nums1` and `nums2` are non-increasing.

【中文翻译】

给定两个非递增的0索引整数数组 `nums1` 和 `nums2`。

如果满足 `i <= j` 且 `nums1[i] <= nums2[j]`，则索引对 `(i, j)`（其中 0 <= i < nums1.length，0 <= j < nums2.length）是有效的。该对的距离定义为 `j - i`。

返回所有有效对 `(i, j)` 的最大距离。如果没有有效对，返回0。

示例：
输入：nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]
输出：2
解释：有效对有(0,0)、(2,2)、(2,3)、(2,4)等，最大距离为(2,4)时j-i=2。

"""

from typing import List, Optional


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        max_dist = 0

        while i < len(nums1) and j < len(nums2):
            if i <= j and nums1[i] <= nums2[j]:
                max_dist = max(max_dist, j - i)
                j += 1
            else:
                i += 1

        return max_dist










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 双指针法。i指向nums1，j指向nums2。当满足 i <= j 且 nums1[i] <= nums2[j] 时，
# 当前对(i, j)有效，更新最大距离，并尝试扩大j（因为nums2是非递增的，
# 更大的j可能有更大的距离）。当不满足条件时，i右移（因为nums1[i]需要变小
# 才能满足<=条件，而nums1是非递增的）。
#
# 时间复杂度: O(N + M)，N = len(nums1), M = len(nums2)
# 空间复杂度: O(1)
#
# 关键点:
# - 两个数组都是非递增的，双指针可以利用这个单调性
# - 条件满足时增加j（扩大距离），不满足时增加i（让nums1[i]变小）
# - 不需要回溯j，因为nums2是非递增的
