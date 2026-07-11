"""
LeetCode #2958 - Length of Longest Subarray With at Most K Frequency
最多 K 个重复元素的最长子数组
https://leetcode.cn/problems/length-of-longest-subarray-with-at-most-k-frequency/

给你一个整数数组 `nums` 和一个整数 `k` 。
一个元素 `x` 在数组中的 频率 指的是它在数组中的出现次数。
如果一个数组中所有元素的频率都 小于等于 `k` ，那么我们称这个数组是 好 数组。
请你返回 `nums` 中 最长好 子数组的长度。
子数组 指的是一个数组中一段连续非空的元素序列。

示例 1：
输入：nums = [1,2,3,1,2,3,1,2], k = 2 输出：6 解释：最长好子数组是 [1,2,3,1,2,3] ，值 1 ，2 和 3 在子数组中的频率都没有超过 k = 2 。[2,3,1,2,3,1] 和 [3,1,2,3,1,2] 也是好子数组。 最长好子数组的长度为 6 。
示例 2：
输入：nums = [1,2,1,2,1,2,1,2], k = 1 输出：2 解释：最长好子数组是 [1,2] ，值 1 和 2 在子数组中的频率都没有超过 k = 1 。[2,1] 也是好子数组。 最长好子数组的长度为 2 。
示例 3：
输入：nums = [5,5,5,5,5,5,5], k = 4 输出：4 解释：最长好子数组是 [5,5,5,5] ，值 5 在子数组中的频率没有超过 k = 4 。 最长好子数组的长度为 4 。

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^9`
`1 <= k <= nums.length`
"""

from typing import List, Optional


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        from collections import Counter
        freq = Counter()
        left = 0
        ans = 0
        for right, x in enumerate(nums):
            freq[x] += 1
            while freq[x] > k:
                freq[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Sliding Window
#
# 解题思路:
# 滑动窗口：维护窗口 [left, right] 内每个元素的频率。当某个元素频率超过 k 时，收缩左边界直到该元素频率 <= k。
# 每次扩展右边界后更新最大窗口长度。所有元素频率均 <= k 时窗口合法。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 滑动窗口保证所有元素频率 <= k
# - 当 freq[x] > k 时持续右移 left 直到条件恢复
# - 窗口收缩时只更新被移出元素的频率
