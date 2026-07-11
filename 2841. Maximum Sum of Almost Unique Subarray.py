"""
LeetCode #2841 - Maximum Sum of Almost Unique Subarray
几乎唯一子数组的最大和
https://leetcode.cn/problems/maximum-sum-of-almost-unique-subarray/

给你一个整数数组 `nums` 和两个正整数 `m` 和 `k` 。
请你返回 `nums` 中长度为 `k` 的 几乎唯一 子数组的 最大和 ，如果不存在几乎唯一子数组，请你返回 `0` 。
如果 `nums` 的一个子数组有至少 `m` 个互不相同的元素，我们称它是 几乎唯一 子数组。
子数组指的是一个数组中一段连续 非空 的元素序列。

示例 1：
输入：nums = [2,6,7,3,1,7], m = 3, k = 4 输出：18 解释：总共有 3 个长度为 k = 4 的几乎唯一子数组。分别为 [2, 6, 7, 3] ，[6, 7, 3, 1] 和 [7, 3, 1, 7] 。这些子数组中，和最大的是 [2, 6, 7, 3] ，和为 18 。
示例 2：
输入：nums = [5,9,9,2,4,5,4], m = 1, k = 3 输出：23 解释：总共有 5 个长度为 k = 3 的几乎唯一子数组。分别为 [5, 9, 9] ，[9, 9, 2] ，[9, 2, 4] ，[2, 4, 5] 和 [4, 5, 4] 。这些子数组中，和最大的是 [5, 9, 9] ，和为 23 。
示例 3：
输入：nums = [1,2,1,2,1,2,1], m = 3, k = 3 输出：0 解释：输入数组中不存在长度为 `k = 3` 的子数组含有至少  `m = 3` 个互不相同元素的子数组。所以不存在几乎唯一子数组，最大和为 0 。

提示：
`1 <= nums.length <= 2 * 10^4`
`1 <= m <= k <= nums.length`
`1 <= nums[i] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        from collections import Counter
        freq = Counter()
        cur_sum = 0
        ans = 0
        unique_cnt = 0
        for i, x in enumerate(nums):
            freq[x] += 1
            if freq[x] == 1:
                unique_cnt += 1
            cur_sum += x
            if i >= k:
                left = nums[i - k]
                freq[left] -= 1
                if freq[left] == 0:
                    unique_cnt -= 1
                cur_sum -= left
            if i >= k - 1 and unique_cnt >= m:
                ans = max(ans, cur_sum)
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Sliding Window
#
# 解题思路:
# 使用固定大小的滑动窗口（长度为 k），维护窗口内元素频率和当前和。
# 当窗口形成后（i >= k-1），检查不同元素个数是否 >= m，若是则更新最大和。
# 滑动时移除最左侧元素并添加新元素，同时更新频率与不同元素计数。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 固定窗口滑动，维护频率 Counter 和不同元素计数 unique_cnt
# - 仅当窗口大小为 k 且不同元素数 >= m 时更新答案
# - 使用 hash map 在 O(1) 时间更新频率
