"""
LeetCode #1438 - Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
中文题名：绝对差不超过限制的最长连续子数组
https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

Given an array of integers `nums` and an integer
`limit`, return the size of the longest continuous subarray such that the
absolute difference between any two elements is less than or equal
to `limit`.

In case there is no subarray satisfying the given condition return 0.

Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2
Explanation: All subarrays are:
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4.
Therefore, the size of the longest subarray is 2.

Example 2:

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.

Example 3:

Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3

Constraints:

`1 <= nums.length <= 10^5`

`1 <= nums[i] <= 10^9`

`0 <= limit <= 10^9`

【中文翻译】
给定一个整数数组 `nums` 和一个整数 `limit`，返回最长连续子数组的长度，
使得该子数组中的任意两个元素之间的绝对差小于或等于 `limit`。
如果不存在满足条件的子数组，返回 0。

示例 1：

输入：nums = [8,2,4,7], limit = 4
输出：2
解释：所有子数组如下：
[8] 的最大绝对差 |8-8| = 0 <= 4。
[8,2] 的最大绝对差 |8-2| = 6 > 4。
[8,2,4] 的最大绝对差 |8-2| = 6 > 4。
[8,2,4,7] 的最大绝对差 |8-2| = 6 > 4。
[2] 的最大绝对差 |2-2| = 0 <= 4。
[2,4] 的最大绝对差 |2-4| = 2 <= 4。
[2,4,7] 的最大绝对差 |2-7| = 5 > 4。
[4] 的最大绝对差 |4-4| = 0 <= 4。
[4,7] 的最大绝对差 |4-7| = 3 <= 4。
[7] 的最大绝对差 |7-7| = 0 <= 4。
因此，最长子数组的长度为 2。

示例 2：

输入：nums = [10,1,2,4,7,2], limit = 5
输出：4
解释：子数组 [2,4,7,2] 是最长的，因为最大绝对差 |2-7| = 5 <= 5。

示例 3：

输入：nums = [4,2,2,2,4,4,2,2], limit = 0
输出：3

约束条件：

`1 <= nums.length <= 10^5`

`1 <= nums[i] <= 10^9`

`0 <= limit <= 10^9`
"""

from typing import List, Optional


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        from collections import deque
        max_deque, min_deque = deque(), deque()
        left = 0
        ans = 0
        for right, val in enumerate(nums):
            while max_deque and nums[max_deque[-1]] <= val:
                max_deque.pop()
            max_deque.append(right)
            while min_deque and nums[min_deque[-1]] >= val:
                min_deque.pop()
            min_deque.append(right)
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                left += 1
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()
            ans = max(ans, right - left + 1)
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用两个单调队列（一个维护窗口内最大值，一个维护窗口内最小值）配合滑动窗口。
# 扩展右指针，将当前元素加入两个单调队列（最大值队列递减，最小值队列递增）。
# 当窗口内的最大值减最小值超过 limit 时，收缩左指针：
# 如果队列头部元素的下标小于左指针，则从队列头部弹出。
# 每一步更新最大窗口长度作为答案。
#
# 时间复杂度: O(N)  -- 每个元素最多入队出队各一次
# 空间复杂度: O(N)  -- 两个双端队列最多各存储 N 个元素
#
# 关键点:
# - 单调队列维护滑动窗口内的最值，避免每次重新扫描 O(K) 的开销
# - 窗口不满足条件时收缩左边界，同时清理过期队列元素
# - 使用下标而非值存储到队列中，方便判断是否在窗口内









