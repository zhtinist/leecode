"""
LeetCode #560 - Subarray Sum Equals K
中文题名：和为 K 的子数组
https://leetcode.com/problems/subarray-sum-equals-k/

Given an array of integers and an integer k, you need to find the total number of
continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2

Note:

The length of the array is in range [1, 20,000].

The range of numbers in the array is [-1000, 1000] and the range of the integer k
is [-1e7, 1e7].

【中文翻译】
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续子数组的个数。

示例 1：

输入：nums = [1,1,1], k = 2
输出：2

注意：

数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000]，且整数 k 的范围是 [-1e7, 1e7]。
"""

from typing import List, Optional
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        for num in nums:
            prefix_sum += num
            target = prefix_sum - k
            if target in prefix_count:
                count += prefix_count[target]
            prefix_count[prefix_sum] += 1

        return count










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 前缀和 + 哈希表：
# 设 prefix_sum[i] 为 nums[0..i] 的和。
# 子数组 nums[i+1..j] 的和 = prefix_sum[j] - prefix_sum[i] = k。
# 即 prefix_sum[j] - k = prefix_sum[i]。
# 遍历数组，维护当前前缀和 prefix_sum：
# 1. 检查 prefix_sum - k 之前出现了几次（即有几个子数组以当前位置结尾且和为 k）。
# 2. 将当前前缀和计入哈希表 prefix_count。
# 初始设置 prefix_count[0] = 1，处理从开头开始的子数组。
#
# 时间复杂度: O(n)，遍历一次
# 空间复杂度: O(n)，哈希表存储所有不同的前缀和
#
# 关键点:
# - 前缀和之差等于子数组和
# - prefix_sum - k 出现的次数即为以当前位置结尾的和为 k 的子数组个数
# - prefix_count[0] = 1 处理从索引 0 开始的子数组
# - 元素可为负数，不能用滑动窗口（滑动窗口要求全正数）
