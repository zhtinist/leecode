"""
LeetCode #3255 - Find the Power of K-Size Subarrays II
长度为 K 的子数组的能量值 II
https://leetcode.cn/problems/find-the-power-of-k-size-subarrays-ii/

给你一个长度为 `n` 的整数数组 `nums` 和一个正整数 `k` 。
一个数组的 能量值 定义为：
如果 所有 元素都是依次 连续（即 `nums[i] + 1 = nums[i + 1]`，`i < n`）且 上升 的，那么能量值为 最大 的元素。
否则为 -1 。
你需要求出 `nums` 中所有长度为 `k` 的 子数组 的能量值。
请你返回一个长度为 `n - k + 1` 的整数数组 `results` ，其中 `results[i]` 是子数组 `nums[i..(i + k - 1)]` 的能量值。

示例 1：

输入：nums = [1,2,3,4,3,2,5], k = 3
输出：[3,4,-1,-1,-1]
解释：
`nums` 中总共有 5 个长度为 3 的子数组：
`[1, 2, 3]` 中最大元素为 3 。
`[2, 3, 4]` 中最大元素为 4 。
`[3, 4, 3]` 中元素 不是 连续的。
`[4, 3, 2]` 中元素 不是 上升的。
`[3, 2, 5]` 中元素 不是 连续的。
示例 2：

输入：nums = [2,2,2,2,2], k = 4
输出：[-1,-1]
示例 3：

输入：nums = [3,2,3,2,3,2], k = 2
输出：[-1,3,-1,3,-1]

提示：
`1 <= n == nums.length <= 10^5`
`1 <= nums[i] <= 10^6`
`1 <= k <= n`
"""

from typing import List, Optional


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        cnt = 1
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1] + 1:
                cnt += 1
            else:
                cnt = 1
            if i >= k - 1:
                if cnt >= k:
                    ans.append(nums[i])
                else:
                    ans.append(-1)
        return ans










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Sliding Window
#
# 解题思路:
# 与 3254 I 完全相同，只是数据范围更大（n <= 10^5 vs n <= 500）。
# 同样的 O(n) 滑动窗口/连续长度方法适用。
# 维护当前连续递增的长度 cnt，当 cnt >= k 时答案为 nums[i]，否则为 -1。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 与 I 相同的线性解法，复杂度不受数据规模影响
# - 连续递增的条件：nums[i] + 1 == nums[i+1]
