"""
LeetCode #523 - Continuous Subarray Sum
中文题名：连续的子数组和
https://leetcode.com/problems/continuous-subarray-sum/

Given a list of non-negative numbers and a target integer k, write a function
to check if the array has a continuous subarray of size at least 2 that sums up to a
multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.

Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.

Note:

The length of the array won't exceed 10,000.

You may assume the sum of all the numbers is in the range of a signed 32-bit integer.

【中文翻译】
给定一个非负整数数组和一个目标整数 k，编写一个函数判断该数组是否含有
长度至少为 2 的连续子数组，其元素总和是 k 的倍数（即总和为 n*k，n 为整数）。

示例 1：
    输入：[23, 2, 4, 6, 7], k=6
    输出：True
    解释：[2, 4] 是一个长度为 2 的连续子数组，其和为 6。

示例 2：
    输入：[23, 2, 6, 4, 7], k=6
    输出：True
    解释：[23, 2, 6, 4, 7] 是一个长度为 5 的连续子数组，其和为 42。

注意：
数组长度不超过 10,000。
所有数字之和保证在 32 位有符号整数范围内。
"""

from typing import List, Optional


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # 余数 -> 该余数首次出现的索引
        seen = {0: -1}
        prefix_sum = 0

        for i, num in enumerate(nums):
            prefix_sum += num
            if k != 0:
                prefix_sum %= k
            if prefix_sum in seen:
                if i - seen[prefix_sum] >= 2:
                    return True
            else:
                seen[prefix_sum] = i

        return False


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 前缀和 + 哈希表（同余定理）。核心原理：如果两个前缀和对 k 取模的余数相等，
# 那么这两个前缀和之间的子数组和就是 k 的倍数。
# 遍历数组计算前缀和并对 k 取模，用哈希表记录每个余数首次出现的索引。
# 若当前余数已在哈希表中且索引差 >= 2（子数组长度至少为 2），返回 True。
# 哈希表初始化为 {0: -1}，处理子数组从索引 0 开始的情况。
#
# 时间复杂度: O(N) — 一次遍历
# 空间复杂度: O(min(N, k)) — 哈希表最多存储 k 个不同余数
#
# 关键点:
# - 同余定理：prefix[j] % k == prefix[i-1] % k ⟹ sum(nums[i..j]) % k == 0
# - 哈希表初始化为 {0: -1} 处理从头开始的子数组
# - 索引差 >= 2 保证子数组长度至少为 2
# - k = 0 时特殊处理：直接比较前缀和（不对 0 取模），相同的和出现两次且索引差 >= 2
