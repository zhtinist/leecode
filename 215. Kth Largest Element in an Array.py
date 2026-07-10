"""
LeetCode #215 - Kth Largest Element in an Array
中文题名：数组中的第K个最大元素
https://leetcode.com/problems/kth-largest-element-in-an-array/

Find the kth largest element in an unsorted array. Note that it is the kth
largest element in the sorted order, not the kth distinct element.

Example 1:

Input: `[3,2,1,5,6,4] `and k = 2
Output: 5

Example 2:

Input: `[3,2,3,1,2,4,5,5,6] `and k = 4
Output: 4

Note:

You may assume k is always valid, 1 <= k <= array's length.

【中文翻译】
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1：

输入：`[3,2,1,5,6,4]` 且 k = 2
输出：5

示例 2：

输入：`[3,2,3,1,2,4,5,5,6]` 且 k = 4
输出：4

注意：

你可以假设 k 始终有效，1 <= k <= 数组的长度。
"""

from typing import List, Optional


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # kth largest = (n - k)th smallest (0-indexed)
        target = len(nums) - k

        def quickselect(left, right):
            # Lomuto partition with rightmost element as pivot
            pivot = nums[right]
            p = left
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[right] = nums[right], nums[p]

            if p == target:
                return nums[p]
            elif p < target:
                return quickselect(p + 1, right)
            else:
                return quickselect(left, p - 1)

        return quickselect(0, len(nums) - 1)


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用快速选择算法（Quickselect），平均 O(n) 时间复杂度找到第 K 大的元素。
# 1. 将"第 K 大"转换为"第 n-k 小（0-indexed）"，即 target = len(nums) - k。
# 2. 使用 Lomuto 分区方案，每次选最右元素作为 pivot。
# 3. 遍历时将 <= pivot 的元素交换到左侧，p 记录分界点。
# 4. 若 pivot 的最终位置 p 正好等于 target，则找到答案。
# 5. 若 p < target，在右半部分继续搜索；否则在左半部分搜索。
# 6. 不需要完全排序，每次只需处理一半数据。
#
# 时间复杂度: O(N) 平均，O(N^2) 最坏（可通过随机化 pivot 优化至期望 O(N)）
# 空间复杂度: O(log N)，递归调用栈深度
#
# 关键点:
# - 第 K 大 = 第 len(nums)-k 小（从小到大排序后的索引），转换后统一用 partition
# - Lomuto 分区：p 总是指向第一个 > pivot 的位置，最终将 pivot 放到 p
# - 原地操作不需要额外数组，相比堆解法 O(N log K) 在 k 接近 N 时更优
