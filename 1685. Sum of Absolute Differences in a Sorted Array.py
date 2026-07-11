"""
LeetCode #1685 - Sum of Absolute Differences in a Sorted Array
中文题名：有序数组中差绝对值之和
https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

You are given an integer array `nums` sorted in
non-decreasing order.

Build and return an integer array `result` with the same
length as `nums` such that `result[i]` is
equal to the summation of absolute differences between `nums[i]`
and all the other elements in the array.

In other words, `result[i]` is equal to
`sum(|nums[i]-nums[j]|)` where `0 <= j < nums.length`
and `j != i` (0-indexed).

Example 1:

Input: nums = [2,3,5]
Output: [4,3,5]
Explanation: Assuming the arrays are 0-indexed, then
result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4,
result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3,
result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5.

Example 2:

Input: nums = [1,4,6,8,10]
Output: [24,15,13,15,21]

Constraints:

`2 <= nums.length <= 105`

`1 <= nums[i] <= nums[i + 1] <= 104`

【中文翻译】
给定一个按非递减顺序排序的整数数组nums。

构建并返回一个与nums具有相同长度的整数数组result，使得result[i]等于nums[i]与数组中所有其他元素之差的绝对值之和。

换句话说，result[i]等于sum(|nums[i]-nums[j]|)，其中0<=j<nums.length且j!=i（0索引）。

示例1：

输入：nums = [2,3,5]
输出：[4,3,5]
解释：假设数组是0索引的，则
result[0]=|2-2|+|2-3|+|2-5|=0+1+3=4
result[1]=|3-2|+|3-3|+|3-5|=1+0+2=3
result[2]=|5-2|+|5-3|+|5-5|=3+2+0=5

示例2：

输入：nums = [1,4,6,8,10]
输出：[24,15,13,15,21]

约束条件：

2 <= nums.length <= 10^5
1 <= nums[i] <= nums[i+1] <= 10^4

"""

from typing import List, Optional


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # 前缀和
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        result = [0] * n
        for i in range(n):
            # 左侧：nums[i] * i - prefix[i] （i个元素，都比nums[i]小或等）
            left_sum = nums[i] * i - prefix[i]
            # 右侧：prefix[n] - prefix[i+1] - nums[i] * (n - 1 - i)
            right_sum = (prefix[n] - prefix[i + 1]) - nums[i] * (n - 1 - i)
            result[i] = left_sum + right_sum
        return result










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 前缀和。由于数组已排序，对于位置i：
# - 左侧所有元素都 <= nums[i]，绝对差 = nums[i] * i - prefix[i]
# - 右侧所有元素都 >= nums[i]，绝对差 = (prefix[n] - prefix[i+1]) - nums[i] * (n-1-i)
# result[i] = left_sum + right_sum
# 利用前缀和将O(n^2)优化为O(n)。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 利用数组已排序的性质：左侧元素<=nums[i]，右侧元素>=nums[i]
# - 前缀和快速计算区间和
# - 左右分别计算避免重复遍历
