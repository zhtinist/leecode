"""
LeetCode #2461 - Maximum Sum of Distinct Subarrays With Length K
长度为 K 子数组中的最大和
https://leetcode.cn/problems/maximum-sum-of-distinct-subarrays-with-length-k/

给你一个整数数组 `nums` 和一个整数 `k` 。请你从 `nums` 中满足下述条件的全部子数组中找出最大子数组和：
子数组的长度是 `k`，且
子数组中的所有元素 各不相同 。
返回满足题面要求的最大子数组和。如果不存在子数组满足这些条件，返回 `0` 。
子数组 是数组中一段连续非空的元素序列。

示例 1：
输入：nums = [1,5,4,2,9,9,9], k = 3 输出：15 解释：nums 中长度为 3 的子数组是： - [1,5,4] 满足全部条件，和为 10 。 - [5,4,2] 满足全部条件，和为 11 。 - [4,2,9] 满足全部条件，和为 15 。 - [2,9,9] 不满足全部条件，因为元素 9 出现重复。 - [9,9,9] 不满足全部条件，因为元素 9 出现重复。 因为 15 是满足全部条件的所有子数组中的最大子数组和，所以返回 15 。
示例 2：
输入：nums = [4,4,4], k = 3 输出：0 解释：nums 中长度为 3 的子数组是： - [4,4,4] 不满足全部条件，因为元素 4 出现重复。 因为不存在满足全部条件的子数组，所以返回 0 。

提示：
`1 <= k <= nums.length <= 10^5`
`1 <= nums[i] <= 10^5`
"""

from typing import List, Optional


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        from collections import Counter

        freq = Counter()
        cur_sum = 0
        max_sum = 0
        left = 0

        for right in range(len(nums)):
            # 扩大窗口
            freq[nums[right]] += 1
            cur_sum += nums[right]

            # 当窗口大小达到 k
            if right - left + 1 == k:
                # 如果窗口内所有元素都只出现一次
                if len(freq) == k:
                    max_sum = max(max_sum, cur_sum)

                # 缩小窗口：移除最左元素
                freq[nums[left]] -= 1
                cur_sum -= nums[left]
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

        return max_sum



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Sliding Window
#
# 解题思路:
# 滑动窗口 + 频率统计。维护一个长度为 k 的窗口，同时维护：
#   1. cur_sum：当前窗口内元素之和
#   2. freq：一个 Counter/字典记录窗口内每个元素的出现次数
# 当窗口大小等于 k 时，检查 freq 的大小是否也等于 k（即所有元素互不相同）：
#   若是，则用 cur_sum 更新最大和
# 然后收缩左边界，更新 freq 和 cur_sum。
#
# 时间复杂度: O(n)，其中 n 是 nums 的长度，每个元素最多入窗口一次、出窗口一次
# 空间复杂度: O(k)，freq 字典最多存储 k 个不同的元素
#
# 关键点:
# - 用 len(freq) == k 判断窗口内元素是否全部互不相同
# - 移除元素时若计数变为 0 需从字典中删除（否则 len(freq) 不准确）
# - 维护 cur_sum 避免每次重新计算窗口和
