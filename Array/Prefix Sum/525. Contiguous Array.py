"""
LeetCode #525 - Contiguous Array
中文题名：连续数组
https://leetcode.com/problems/contiguous-array/

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0
and 1.

Example 1:

Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:

Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note:
The length of the given binary array will not exceed 50,000.

【中文翻译】
给定一个二进制数组，找到一个最长的连续子数组，其中 0 和 1 的数量相等。

示例 1：
    输入：[0,1]
    输出：2
    解释：[0, 1] 是最长的包含相同数量 0 和 1 的连续子数组。

示例 2：
    输入：[0,1,0]
    输出：2
    解释：[0, 1]（或 [1, 0]）是最长的包含相同数量 0 和 1 的连续子数组。

说明：给定二进制数组的长度不超过 50,000。
"""

from typing import List, Optional


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Map: running sum -> first index where this sum appears
        # Treat 0 as -1, 1 as +1 so equal 0s and 1s means sum == 0
        prefix_map = {0: -1}
        max_len = 0
        count = 0

        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1

            if count in prefix_map:
                max_len = max(max_len, i - prefix_map[count])
            else:
                prefix_map[count] = i

        return max_len


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 将 0 视为 -1，1 视为 +1，则问题转化为求最长子数组使其和为 0。使用前缀和技巧，
# 用一个哈希表记录每个前缀和第一次出现的下标。遍历数组时计算当前前缀和 count，
# 若 count 之前出现过（在哈希表中），说明从第一次出现位置之后到当前位置的区间和为 0，
# 即 0 和 1 数量相等，更新最大长度。初始化 prefix_map[0] = -1 以处理从数组开头
# 开始的子数组。
#
# 时间复杂度: O(N) — 一次遍历
# 空间复杂度: O(N) — 哈希表存储不同前缀和（最坏情况 N 个不同值）
#
# 关键点:
# - 将 0/1 计数问题转换为和为零的前缀和问题
# - 哈希表存储每个前缀和首次出现的下标，保证最长子数组
# - 初始化 prefix_map[0] = -1 是处理从头开始的有效子数组的关键
