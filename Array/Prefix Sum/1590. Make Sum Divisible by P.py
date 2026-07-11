"""
LeetCode #1590 - Make Sum Divisible by P
中文题名：使数组和能被 P 整除
https://leetcode.com/problems/make-sum-divisible-by-p/


Given an array of positive integers `nums`, remove the
smallest subarray (possibly empty) such that the
sum of the remaining elements is divisible by `p`. It is
not allowed to remove the whole array.

Return the length of the smallest subarray that you need to remove,
or `-1` if it's impossible.

A subarray is defined as a contiguous block of elements in the
array.

Example 1:

Input: nums = [3,1,4,2], p = 6
Output: 1
Explanation: The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.

Example 2:

Input: nums = [6,3,5,2], p = 9
Output: 2
Explanation: We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.

Example 3:

Input: nums = [1,2,3], p = 3
Output: 0
Explanation: Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.

Example 4:

Input: nums = [1,2,3], p = 7
Output: -1
Explanation: There is no way to remove a subarray in order to get a sum divisible by 7.

Example 5:

Input: nums = [1000000000,1000000000,1000000000], p = 3
Output: 0

Constraints:

`1 <= nums.length <= 105`

`1 <= nums[i] <= 109`

`1 <= p <= 109`

【中文翻译】
给定正整数数组 nums 和正整数 p。移除一个子数组（可为空），使得剩余元素的和能被 p 整除。
返回需要移除的最短子数组的长度。如果无法做到，返回 -1。

示例 1：输入：nums = [3,1,4,2], p = 6
输出：1
解释：移除 [4]，剩余 [3,1,2] 和为 6，能被 6 整除。

示例 2：输入：nums = [6,3,5,2], p = 9
输出：2

示例 3：输入：nums = [1,2,3], p = 3
输出：0
"""

from typing import List, Optional


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums) % p
        if total == 0:
            return 0
        prefix = 0
        last_seen = {0: -1}
        result = len(nums)
        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            target = (prefix - total + p) % p
            if target in last_seen:
                result = min(result, i - last_seen[target])
            last_seen[prefix] = i
        return result if result < len(nums) else -1



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 计算总和 % p = total。如果 total == 0，答案为 0（不需要移除）。
# 需要找到一个最短子数组，其和 % p == total（这样移除后剩余和 % p == 0）。
# 使用前缀和模 p 的方法：维护 last_seen 字典记录每个前缀和模 p 值最后出现的位置。
# 对于当前位置 i，需要找到之前某个位置 j 使得 (prefix_i - prefix_j) % p == total。
#
# 时间复杂度: O(N) — 一次遍历
# 空间复杂度: O(min(N, p)) — 哈希表最多 p 个键
#
# 关键点:
# - 子数组和 % p = (prefix_j - prefix_i) % p
# - 问题转化为寻找和 % p == total 的最短子数组
# - last_seen 初始包含 {0: -1}












