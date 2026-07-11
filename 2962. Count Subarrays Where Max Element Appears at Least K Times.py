"""
LeetCode #2962 - Count Subarrays Where Max Element Appears at Least K Times
统计最大元素出现至少 K 次的子数组
https://leetcode.cn/problems/count-subarrays-where-max-element-appears-at-least-k-times/

给你一个整数数组 `nums` 和一个 正整数 `k` 。
请你统计有多少满足 「 `nums` 中的 最大 元素」至少出现 `k` 次的子数组，并返回满足这一条件的子数组的数目。
子数组是数组中的一个连续元素序列。

示例 1：
输入：nums = [1,3,2,3,3], k = 2 输出：6 解释：包含元素 3 至少 2 次的子数组为：[1,3,2,3]、[1,3,2,3,3]、[3,2,3]、[3,2,3,3]、[2,3,3] 和 [3,3] 。
示例 2：
输入：nums = [1,4,2,1], k = 3 输出：0 解释：没有子数组包含元素 4 至少 3 次。

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^6`
`1 <= k <= 10^5`
"""

from typing import List, Optional


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        """
        Sliding window: find all subarrays where the max element
        appears at least k times. Count subarrays using the leftmost
        occurrence position of the max element.
        """
        max_val = max(nums)
        n = len(nums)
        count = 0
        left = 0
        max_count = 0  # count of max_val in current window
        result = 0

        for right in range(n):
            if nums[right] == max_val:
                max_count += 1

            # Shrink window until we have at least k max elements
            while max_count >= k:
                # All subarrays starting from left to positions >= right are valid
                # Actually, for each left where window [left, right] has >= k max elements,
                # all subarrays starting at left and ending anywhere from right to n-1 are valid
                result += n - right
                if nums[left] == max_val:
                    max_count -= 1
                left += 1

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Sliding Window
#
# 解题思路:
# 先找出数组中的最大元素值，然后使用滑动窗口双指针维护当前窗口内最大元素的出现次数。
# 当窗口内最大元素出现次数 >= k 时，以 left 为起点、right 到末尾为终点的所有子数组都满足条件，
# 累加 n - right 到结果中，然后收缩左边界。
#
# 时间复杂度: O(n)，每个元素最多被左右指针各访问一次
# 空间复杂度: O(1)，仅使用常数空间
#
# 关键点:
# - 先确定最大元素值，只关心最大元素的出现次数
# - 滑动窗口的关键：当窗口满足条件时，以 left 开头、right..n-1 结尾的所有子数组都合法
# - 收缩左边界时更新最大元素计数
