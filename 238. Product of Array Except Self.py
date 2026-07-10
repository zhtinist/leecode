"""
LeetCode #238 - Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/

Given an array `nums` of *n* integers where *n* > 1,  return
an array `output` such that `output[i]` is equal to the product of all
the elements of `nums` except `nums[i]`.

Example:

Input:  `[1,2,3,4]`
Output: `[24,12,8,6]`

Note: Please solve it without division and in O(*n*).

Follow up:

Could you solve it with constant space complexity? (The output array does
not count as extra space for the purpose of space complexity analysis.)
"""

from typing import List, Optional


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 两次遍历，利用前缀积和后缀积。
# 要求不能使用除法，且 O(n) 时间，O(1) 额外空间(输出数组不算)。
# 1. 第一遍(左到右): res[i] 存储 nums[0] ~ nums[i-1] 的乘积(前缀积)。
#    维护 prefix 变量，每次先将 prefix 赋给 res[i]，然后 prefix *= nums[i]。
#    第一遍后 res[i] = nums[0] * nums[1] * ... * nums[i-1]。
# 2. 第二遍(右到左): res[i] *= suffix (后缀积，即 nums[i+1] ~ nums[n-1] 的乘积)。
#    维护 suffix 变量，每次先将 res[i] *= suffix，然后 suffix *= nums[i]。
#    第二遍后 res[i] = 前缀积 * 后缀积 = 除 nums[i] 外所有元素的乘积。
# 例如 nums = [1, 2, 3, 4]：
#   第一遍后: res = [1, 1, 2, 6]  (前缀积)
#   第二遍后: suffix 依次为 1, 4, 12, 24
#     res[3] *= 1  → 6;  suffix = 4
#     res[2] *= 4  → 8;  suffix = 12
#     res[1] *= 12 → 12; suffix = 24
#     res[0] *= 24 → 24
#   最终: res = [24, 12, 8, 6]
#
# 时间复杂度: O(n) - 两次遍历
# 空间复杂度: O(1) - 输出数组不算额外空间，只用了 prefix 和 suffix 两个变量
#
# 关键点:
# - 输出数组不算额外空间(题目说明)，这是实现 O(1) 空间的关键
# - 第一遍存储前缀积，第二遍乘以后缀积
# - 两次遍历互补，最终 res[i] 等于除 nums[i] 外所有元素的乘积
# - 禁止除法是因为如果数组含 0，除法方案需要额外处理
