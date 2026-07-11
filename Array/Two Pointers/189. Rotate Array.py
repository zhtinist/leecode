"""
LeetCode #189 - Rotate Array
中文题名：轮转数组
https://leetcode.com/problems/rotate-array/

Given an array, rotate the array to the right by *k* steps, where *k* is
non-negative.

Example 1:

Input: `[1,2,3,4,5,6,7]` and *k* = 3
Output: `[5,6,7,1,2,3,4]`
Explanation:
rotate 1 steps to the right: `[7,1,2,3,4,5,6]`
rotate 2 steps to the right: `[6,7,1,2,3,4,5]
`rotate 3 steps to the right: `[5,6,7,1,2,3,4]`

Example 2:

Input: `[-1,-100,3,99]` and *k* = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Note:

Try to come up as many solutions as you can, there are at least 3 different ways to
solve this problem.

Could you do it in-place with O(1) extra space?

【中文翻译】
给定一个数组，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

示例 1：

输入：`[1,2,3,4,5,6,7]` 且 *k* = 3
输出：`[5,6,7,1,2,3,4]`
解释：
向右轮转 1 步：`[7,1,2,3,4,5,6]`
向右轮转 2 步：`[6,7,1,2,3,4,5]`
向右轮转 3 步：`[5,6,7,1,2,3,4]`

示例 2：

输入：`[-1,-100,3,99]` 且 *k* = 2
输出：[3,99,-1,-100]
解释：
向右轮转 1 步：[99,-1,-100,3]
向右轮转 2 步：[3,99,-1,-100]

注意：

尽量想出多种解法，至少有 3 种不同的方法可以解决此问题。

能否使用 O(1) 额外空间的原地算法？
"""

from typing import List, Optional


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        def reverse(l: int, r: int) -> None:
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        # Reverse entire array
        reverse(0, n - 1)
        # Reverse first k elements
        reverse(0, k - 1)
        # Reverse remaining n-k elements
        reverse(k, n - 1)


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 三次反转法。设 n = len(nums)，k %= n 处理 k 大于 n 的情况。
# 第一步：反转整个数组 [0, n-1]
# 第二步：反转前 k 个元素 [0, k-1]
# 第三步：反转剩余 n-k 个元素 [k, n-1]
#
# 例如：[1,2,3,4,5,6,7], k=3
# 第一次反转：[7,6,5,4,3,2,1]
# 第二次反转：[5,6,7,4,3,2,1]
# 第三次反转：[5,6,7,1,2,3,4]
#
# 时间复杂度: O(N) — 每个元素被交换两次
# 空间复杂度: O(1) — 原地操作，无额外空间
#
# 关键点:
# - 先 k %= n 处理 k 大于 n 的情况
# - 三次反转的巧妙思想：整体反转让元素到达大致位置，再分别反转调整顺序
# - 另一种思路：使用额外数组复制，但空间 O(N)
