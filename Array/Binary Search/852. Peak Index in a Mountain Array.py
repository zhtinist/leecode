"""
LeetCode #852 - Peak Index in a Mountain Array
中文题名：山脉数组的峰顶索引
https://leetcode.com/problems/peak-index-in-a-mountain-array/

Let's call an array `A` a mountain if the following properties
hold:

`A.length >= 3`

There exists some `0 < i < A.length - 1` such that `A[0] <
A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]`

Given an array that is definitely a mountain, return any `i` such that `A[0]
< A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]`.

Example 1:

Input: [0,1,0]
Output: 1

Example 2:

Input: [0,2,1,0]
Output: 1

【中文翻译】
如果一个数组 A 满足以下性质，我们称之为山脉数组：
- A.length >= 3
- 存在某个 0 < i < A.length - 1，使得 A[0] < A[1] < ... < A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]

给定一个一定是山脉数组的数组，返回任意满足上述条件的索引 i。

"""

from typing import List, Optional


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                # Still ascending, peak is to the right
                left = mid + 1
            else:
                # Already descending, peak is at mid or to the left
                right = mid
        return left



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 山脉数组先递增后递减，峰值是唯一满足 A[i] > A[i-1] 且 A[i] > A[i+1] 的位置。
# 使用二分查找：取中间位置 mid，比较 A[mid] 和 A[mid+1]。
# 如果 A[mid] < A[mid+1]，说明还在递增阶段，峰值在 mid 右侧，移动 left = mid + 1。
# 如果 A[mid] >= A[mid+1]（即 A[mid] > A[mid+1]），说明已经在递减阶段或就是峰值，
# 峰值在 mid 或左侧，移动 right = mid。
# 最终 left == right 时即为峰值索引。
#
# 时间复杂度: O(log N)
# 空间复杂度: O(1)
#
# 关键点:
# - 二分查找模板：比较 A[mid] 和 A[mid+1] 来判断是在递增还是递减阶段
# - 不需要找左邻居 A[mid-1]，只需要比较右邻居即可确定峰值方向
# - 保证输入一定是山脉数组，所以二分一定收敛
