"""
LeetCode #1856 - Maximum Subarray Min-Product
中文题名：子数组的最小乘积的最大值
https://leetcode.com/problems/maximum-subarray-min-product/

The min-product of an array is equal to the minimum value in the array multiplied by the array's sum.

For example, the array `[3,2,5]` (minimum value is `2`) has a min-product of `2 * (3+2+5) = 2 * 10 = 20`.

Given an array of integers `nums`, return the maximum min-product of any non-empty subarray of `nums`. Since the answer may be large, return it modulo `109 + 7`.

Note that the min-product should be maximized before performing the modulo operation. Testcases are generated such that the maximum min-product without modulo will fit in a 64-bit signed integer.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [1,2,3,2]
Output: 14
Explanation: The maximum min-product is achieved with the subarray [2,3,2] (minimum value is 2).
2 * (2+3+2) = 2 * 7 = 14.

Example 2:

Input: nums = [2,3,3,1,2]
Output: 18
Explanation: The maximum min-product is achieved with the subarray [3,3] (minimum value is 3).
3 * (3+3) = 3 * 6 = 18.

Example 3:

Input: nums = [3,1,5,6,4,2]
Output: 60
Explanation: The maximum min-product is achieved with the subarray [5,6,4] (minimum value is 4).
4 * (5+6+4) = 4 * 15 = 60.

Constraints:

`1 <= nums.length <= 105`

`1 <= nums[i] <= 107`

【中文翻译】

数组的"最小乘积"(min-product)等于数组中最小值乘以数组的总和。例如，数组 [3,2,5]（最小值2）的最小乘积为 2*(3+2+5) = 20。

给定一个整数数组 `nums`，返回 `nums` 中任意非空子数组的最大最小乘积。由于答案可能很大，对 10^9 + 7 取模。

注意：最小乘积应在取模操作之前最大化。测试用例保证取模前的最大最小乘积适合64位有符号整数。

示例：
输入：nums = [1,2,3,2]
输出：14
解释：最大最小乘积由子数组[2,3,2]实现（最小值为2）。2*(2+3+2) = 14。

"""

from typing import List, Optional


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)

        # 前缀和
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # 单调栈找左侧第一个更小元素
        left = [-1] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        # 单调栈找右侧第一个更小元素
        right = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        # 计算以每个元素为最小值的子数组的最小乘积
        max_product = 0
        for i in range(n):
            subarray_sum = prefix[right[i]] - prefix[left[i] + 1]
            max_product = max(max_product, nums[i] * subarray_sum)

        return max_product % MOD










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 单调栈 + 前缀和。对于每个元素nums[i]，找到它作为最小值的最大子数组范围：
# 左侧第一个小于nums[i]的位置(left[i])和右侧第一个小于nums[i]的位置(right[i])。
# 在该范围内nums[i]是最小值，子数组和为prefix[right] - prefix[left+1]。
# 最小乘积 = nums[i] * 子数组和。对所有位置取最大值，最后对MOD取模。
#
# 时间复杂度: O(N)，三次遍历（前缀和、左边界、右边界）
# 空间复杂度: O(N)，前缀和、左右边界数组和栈
#
# 关键点:
# - 单调栈用于找下一个更小元素（Next Smaller Element）
# - 前缀和快速计算任意子数组的和
# - 先取最大值再取模，避免中间取模影响比较
