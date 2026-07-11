"""
LeetCode #1838 - Frequency of the Most Frequent Element
中文题名：最高频元素的频数
https://leetcode.com/problems/frequency-of-the-most-frequent-element/

The frequency of an element is the number of times it occurs in an array.

You are given an integer array `nums` and an integer `k`. In one operation, you can choose an index of `nums` and increment the element at that index by `1`.

Return the maximum possible frequency of an element after performing at most `k` operations.

Example 1:

Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.

Example 2:

Input: nums = [1,4,8,13], k = 5
Output: 2
Explanation: There are multiple optimal solutions:
- Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
- Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
- Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.

Example 3:

Input: nums = [3,9,6], k = 2
Output: 1

Constraints:

`1 <= nums.length <= 105`

`1 <= nums[i] <= 105`

`1 <= k <= 105`

【中文翻译】

元素的频数是它在数组中出现的次数。给定一个整数数组 `nums` 和一个整数 `k`。在一次操作中，你可以选择一个索引并将该索引处的元素加1。

返回最多执行k次操作后，数组中任意元素的最大可能频数。

示例：
输入：nums = [1,2,4], k = 5
输出：3
解释：将第一个元素加3次、第二个元素加2次，数组变为[4,4,4]，数字4的频数为3。

"""

from typing import List, Optional


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        window_sum = 0
        max_freq = 0

        for right in range(len(nums)):
            window_sum += nums[right]
            # 将窗口内所有元素变成nums[right]需要的操作次数
            while (right - left + 1) * nums[right] - window_sum > k:
                window_sum -= nums[left]
                left += 1
            max_freq = max(max_freq, right - left + 1)

        return max_freq










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 排序 + 滑动窗口。将数组排序后，要使窗口内所有元素变为右边界元素的值，
# 需要的操作次数为：(窗口长度) * nums[right] - 窗口内元素之和。
# 如果操作次数超过k，左指针右移缩小窗口。维护最大窗口长度。
#
# 时间复杂度: O(N log N)，排序开销
# 空间复杂度: O(1)，除了排序需要的空间
#
# 关键点:
# - 排序是必要的，因为最优策略总是将一段连续元素变成最大值
# - 滑动窗口：操作次数 = 窗口大小 * target - sum(window)
# - 当操作次数 > k时收缩左边界
