"""
LeetCode #3254 - Find the Power of K-Size Subarrays I
长度为 K 的子数组的能量值 I
https://leetcode.cn/problems/find-the-power-of-k-size-subarrays-i/

给你一个长度为 `n` 的整数数组 `nums` 和一个正整数 `k` 。
一个数组的 能量值 定义为：
如果 所有 元素都是依次 连续 且 上升 的，那么能量值为 最大 的元素。
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
`1 <= n == nums.length <= 500`
`1 <= nums[i] <= 10^5`
`1 <= k <= n`
"""

from typing import List, Optional


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        # 统计连续上升的长度
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
# 子数组需要满足元素连续且递增（nums[i] + 1 == nums[i+1]）。
# 维护当前连续递增的长度 cnt：
# - 如果 nums[i] == nums[i-1] + 1：cnt += 1
# - 否则：cnt = 1
# 当 i >= k-1 时，检查 cnt >= k：如果是，能量值为 nums[i]（最大元素即最后一个），否则为 -1。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)（输出数组不计）
#
# 关键点:
# - 维护连续上升序列的长度，O(n) 一次遍历即可
# - 连续上升序列的最大元素始终是序列的最后一个元素
