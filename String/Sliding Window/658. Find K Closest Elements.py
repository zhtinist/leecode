"""
LeetCode #658 - Find K Closest Elements
中文题名：找到 K 个最接近的元素
https://leetcode.com/problems/find-k-closest-elements/

Given a sorted array, two integers `k` and `x`, find the
`k` closest elements to `x` in the array. The result should also be
sorted in ascending order.
If there is a tie, the smaller elements are always preferred.

Example 1:

Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]

Example 2:

Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]

Note:

The value k is positive and will always be smaller than the length of the sorted
array.

Length of the given array is positive and will not exceed 104

Absolute value of elements in the array and x will not exceed 104

UPDATE (2017/9/19):

The arr parameter had been changed to an array of integers (instead of a list
of integers). Please reload the code definition to get the latest changes.

【中文翻译】
给定一个已排序的数组，两个整数 `k` 和 `x`，找出数组中最接近 `x` 的 `k` 个元素。结果也应按升序排序。

如果有平局，总是选择更小的元素。

示例 1：

输入：[1,2,3,4,5]，k=4，x=3
输出：[1,2,3,4]

示例 2：

输入：[1,2,3,4,5]，k=4，x=-1
输出：[1,2,3,4]

注意：

k 的值为正数，且始终小于排序数组的长度。

给定数组的长度为正数，且不会超过 10^4。

数组中元素和 x 的绝对值不会超过 10^4。
"""

from typing import List, Optional


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k

        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用二分查找直接定位 k 个元素的起始索引。
# 搜索空间为 [0, len(arr) - k]，二分判断条件：
# 比较 arr[mid] 和 arr[mid + k] 与 x 的距离：
# - 如果 x - arr[mid] > arr[mid + k] - x：
#   说明 arr[mid] 距离 x 更远，窗口应右移，left = mid + 1
# - 否则（包括相等的情况）：
#   作为滑动窗口合理位置，right = mid
# 当 left == right 时，找到了最优的起始索引，返回 arr[left:left+k]。
# 平局情况利用 else 分支自动选择了更小的 arr[mid]。
#
# 时间复杂度: O(log(n - k) + k) - 二分查找 O(log n)，切片输出 O(k)
# 空间复杂度: O(k) - 结果列表（或 O(1) 不算输出）
#
# 关键点:
# - 精妙的二分查找思路：直接查找 k 个元素的起始位置
# - 比较 arr[mid] vs arr[mid+k] 到 x 的距离来决定窗口移动方向
# - 平局时选择更小元素：通过 else (<=) 分支实现
# - 也可以用双指针从两端收缩 O(n)，但二分更优
