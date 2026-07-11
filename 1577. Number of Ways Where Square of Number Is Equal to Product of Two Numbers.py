"""
LeetCode #1577 - Number of Ways Where Square of Number Is Equal to Product of Two Numbers
中文题名：数的平方等于两数乘积的方法数
https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/


Given two arrays of integers `nums1` and `nums2`, return
the number of triplets formed (type 1 and type 2) under the following rules:

Type 1: Triplet (i, j, k) if `nums1[i]2 == nums2[j] *
nums2[k]` where `0 <= i < nums1.length` and `0 <=
j < k < nums2.length`.

Type 2: Triplet (i, j, k) if `nums2[i]2 == nums1[j] *
nums1[k]` where `0 <= i < nums2.length` and `0 <=
j < k < nums1.length`.

Example 1:

Input: nums1 = [7,4], nums2 = [5,2,8,9]
Output: 1
Explanation: Type 1: (1,1,2), nums1[1]^2 = nums2[1] * nums2[2]. (4^2 = 2 * 8).

Example 2:

Input: nums1 = [1,1], nums2 = [1,1,1]
Output: 9
Explanation: All Triplets are valid, because 1^2 = 1 * 1.
Type 1: (0,0,1), (0,0,2), (0,1,2), (1,0,1), (1,0,2), (1,1,2).  nums1[i]^2 = nums2[j] * nums2[k].
Type 2: (0,0,1), (1,0,1), (2,0,1). nums2[i]^2 = nums1[j] * nums1[k].

Example 3:

Input: nums1 = [7,7,8,3], nums2 = [1,2,9,7]
Output: 2
Explanation: There are 2 valid triplets.
Type 1: (3,0,2).  nums1[3]^2 = nums2[0] * nums2[2].
Type 2: (3,0,1).  nums2[3]^2 = nums1[0] * nums1[1].

Example 4:

Input: nums1 = [4,7,9,11,23], nums2 = [3,5,1024,12,18]
Output: 0
Explanation: There are no valid triplets.

Constraints:

`1 <= nums1.length, nums2.length <= 1000`

`1 <= nums1[i], nums2[i] <= 10^5`

【中文翻译】
给定两个整数数组 nums1 和 nums2。返回三元组 (i, j, k) 的数量，
使得 nums1[i]^2 = nums2[j] * nums2[k]（j < k）或
nums2[i]^2 = nums1[j] * nums1[k]（j < k）。

示例 1：
输入：nums1 = [7,4], nums2 = [5,2,8,9]
输出：1

示例 2：
输入：nums1 = [1,1], nums2 = [1,1,1]
输出：9
"""

from typing import List, Optional
from collections import Counter


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def count_triplets(a: List[int], b: List[int]) -> int:
            result = 0
            cnt_b = Counter(b)
            for x in a:
                target = x * x
                for y, cy in cnt_b.items():
                    if target % y != 0:
                        continue
                    z = target // y
                    if z == y:
                        result += cy * (cy - 1) // 2
                    elif z > y and z in cnt_b:
                        result += cy * cnt_b[z]
            return result

        return count_triplets(nums1, nums2) + count_triplets(nums2, nums1)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 将问题分为两部分：nums1[i]^2 = nums2[j] * nums2[k] 和 nums2[i]^2 = nums1[j] * nums1[k]。
# 对于每个类型：遍历第一个数组的每个元素 x，计算 target = x^2。
# 使用第二个数组的 Counter 统计频率。对于每个 y，如果 target % y == 0，
# 则 z = target / y。如果 y != z，直接计数；如果 y == z，用组合数 C(cnt[y], 2)。
# 注意使用 z > y 的去重条件避免重复计算。
#
# 时间复杂度: O(N * U) — N 为一数组长度，U 为另一数组不同值的数量
# 空间复杂度: O(U) — Counter
#
# 关键点:
# - 分两种情况独立计算
# - 使用 Counter 加速配对查找
# - y == z 时用组合数，y != z 时确保只算一次












