"""
LeetCode #912 - Sort an Array
中文题名：排序数组
https://leetcode.com/problems/sort-an-array/

Given an array of integers `nums`, sort the array in ascending order.

Example 1:

Input: [5,2,3,1]
Output: [1,2,3,5]

Example 2:

Input: [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]

Note:

`1 <= A.length <= 10000`

`-50000 <= A[i] <= 50000`

【中文翻译】

给定一个整数数组 nums，将其按升序排序并返回排序后的数组。

"""

from typing import List, Optional


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Merge sort implementation — stable O(n log n).
        """
        def merge_sort(arr: List[int]) -> List[int]:
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)

        def merge(left: List[int], right: List[int]) -> List[int]:
            result = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result

        return merge_sort(nums)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用归并排序（Merge Sort）：
# 1. 递归地将数组分成两半，直到每部分长度为 1。
# 2. 合并两个有序数组，使用双指针依次比较并放入结果数组。
# 归并排序保证了 O(N log N) 的时间复杂度且是稳定的排序算法。
#
# 时间复杂度: O(N log N)
# 空间复杂度: O(N)（递归调用栈 + 合并时的临时数组）
#
# 关键点:
# - 归并排序是分治法的经典应用
# - 也可以使用快速排序或堆排序，但要注意避免最坏情况
# - Python 内置的 Timsort 也是基于归并排序的
