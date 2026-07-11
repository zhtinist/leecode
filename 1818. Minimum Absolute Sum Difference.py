"""
LeetCode #1818 - Minimum Absolute Sum Difference
中文题名：最小绝对差值和
https://leetcode.com/problems/minimum-absolute-sum-difference/

You are given two positive integer arrays `nums1` and `nums2`, both of length `n`.

The absolute sum difference of arrays `nums1` and `nums2` is defined as the sum of `|nums1[i] - nums2[i]|` for each `0 <= i < n` (0-indexed).

You can replace at most one element of `nums1` with any other element in `nums1` to minimize the absolute sum difference.

Return the minimum absolute sum difference after replacing at most one element in the array `nums1`. Since the answer may be large, return it modulo `109 + 7`.

`|x|` is defined as:

`x` if `x >= 0`, or

`-x` if `x < 0`.

Example 1:

Input: nums1 = [1,7,5], nums2 = [2,3,5]
Output: 3
Explanation: There are two possible optimal solutions:
- Replace the second element with the first: [1,7,5] => [1,1,5], or
- Replace the second element with the third: [1,7,5] => [1,5,5].
Both will yield an absolute sum difference of `|1-2| + (|1-3| or |5-3|) + |5-5| = `3.

Example 2:

Input: nums1 = [2,4,6,8,10], nums2 = [2,4,6,8,10]
Output: 0
Explanation: nums1 is equal to nums2 so no replacement is needed. This will result in an
absolute sum difference of 0.

Example 3:

Input: nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4]
Output: 20
Explanation: Replace the first element with the second: [1,10,4,4,2,7] => [10,10,4,4,2,7].
This yields an absolute sum difference of `|10-9| + |10-3| + |4-5| + |4-1| + |2-7| + |7-4| = 20`

Constraints:

`n == nums1.length`

`n == nums2.length`

`1 <= n <= 105`

`1 <= nums1[i], nums2[i] <= 105`

【中文翻译】

给定两个正整数数组 `nums1` 和 `nums2`，长度均为n。绝对差值和定义为 `sum(|nums1[i] - nums2[i]|) for i in [0, n-1]`。

你可以将 `nums1` 中的至多一个元素替换为 `nums1` 中的任何其他元素，以最小化绝对差值和。返回替换后的最小绝对差值和，答案可能很大，对 10^9 + 7 取模。

示例：
输入：nums1 = [1,7,5], nums2 = [2,3,5]
输出：3
解释：将第二个元素替换为第一个[1,1,5]或第三个[1,5,5]，得到绝对差值和|1-2|+(|1-3|或|5-3|)+|5-5|=3。

"""

from typing import List, Optional


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        import bisect
        MOD = 10 ** 9 + 7
        n = len(nums1)
        total_diff = sum(abs(nums1[i] - nums2[i]) for i in range(n))

        sorted_nums1 = sorted(nums1)
        max_reduction = 0

        for i in range(n):
            original = abs(nums1[i] - nums2[i])
            idx = bisect.bisect_left(sorted_nums1, nums2[i])

            if idx < n:
                max_reduction = max(
                    max_reduction,
                    original - abs(sorted_nums1[idx] - nums2[i])
                )
            if idx > 0:
                max_reduction = max(
                    max_reduction,
                    original - abs(sorted_nums1[idx - 1] - nums2[i])
                )

        return (total_diff - max_reduction) % MOD










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 首先计算原始的绝对差值和total。然后对nums1排序，对于每个nums2[i]，
# 在排序后的nums1中二分查找最接近nums2[i]的值。计算用该最接近值替换
# 原始nums1[i]后能减少的差值。取最大减少量，答案 = (total - 最大减少量) % MOD。
#
# 时间复杂度: O(N log N)，排序和每次二分的开销
# 空间复杂度: O(N)，排序后的nums1数组
#
# 关键点:
# - 每个位置i有两种候选替换值：>= nums2[i]的最小值和< nums2[i]的最大值
# - 使用bisect_left找到插入位置后检查idx和idx-1两个候选
# - 答案需要对10^9+7取模
