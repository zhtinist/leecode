"""
LeetCode #164 - Maximum Gap
https://leetcode.com/problems/maximum-gap/

Given an integer array nums, return the maximum difference between two successive
elements in its sorted form. If the array contains less than two elements,
return 0.

You must write an algorithm that runs in linear time and uses linear extra
space.

Example 1:
    Input: nums = [3,6,9,1]
    Output: 3
    Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or
    (6,9) has the maximum difference 3.

Example 2:
    Input: nums = [10]
    Output: 0

Constraints:
    1 <= nums.length <= 10^5
    0 <= nums[i] <= 10^9
"""

from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        min_val, max_val = min(nums), max(nums)
        if min_val == max_val:
            return 0

        bucket_size = max(1, (max_val - min_val) // (n - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1
        buckets_min = [float("inf")] * bucket_count
        buckets_max = [float("-inf")] * bucket_count

        for num in nums:
            idx = (num - min_val) // bucket_size
            buckets_min[idx] = min(buckets_min[idx], num)
            buckets_max[idx] = max(buckets_max[idx], num)

        max_gap = 0
        prev_max = buckets_max[0]

        for i in range(1, bucket_count):
            if buckets_min[i] == float("inf"):
                continue
            max_gap = max(max_gap, buckets_min[i] - prev_max)
            prev_max = buckets_max[i]

        return max_gap
