"""
LeetCode #2537 - Count the Number of Good Subarrays
统计好子数组的数目
https://leetcode.cn/problems/count-the-number-of-good-subarrays/

给你一个整数数组 `nums` 和一个整数 `k` ，请你返回 `nums` 中 好 子数组的数目。
一个子数组 `arr` 如果有 至少 `k` 对下标 `(i, j)` 满足 `i < j` 且 `arr[i] == arr[j]` ，那么称它是一个 好 子数组。
子数组 是原数组中一段连续 非空 的元素序列。

示例 1：
输入：nums = [1,1,1,1,1], k = 10 输出：1 解释：唯一的好子数组是这个数组本身。
示例 2：
输入：nums = [3,1,4,3,2,2,4], k = 2 输出：4 解释：总共有 4 个不同的好子数组： - [3,1,4,3,2,2] 有 2 对。 - [3,1,4,3,2,2,4] 有 3 对。 - [1,4,3,2,2,4] 有 2 对。 - [4,3,2,2,4] 有 2 对。

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i], k <= 10^9`
"""

from typing import List, Optional


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        cnt = defaultdict(int)
        pairs = 0
        ans = 0
        left = 0

        for right, x in enumerate(nums):
            pairs += cnt[x]
            cnt[x] += 1
            while pairs >= k:
                ans += len(nums) - right
                cnt[nums[left]] -= 1
                pairs -= cnt[nums[left]]
                left += 1

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Sliding Window
#
# 解题思路:
# 滑动窗口+哈希表。右指针扩展时，新元素x与窗口内已有的cnt[x]个x形成cnt[x]对，
# 累加到pairs中。当pairs>=k时，当前窗口和所有以当前右边界结尾的延伸都满足条件，
# 贡献ans += n-right。然后收缩左边界直到pairs<k，继续扩展。
#
# 时间复杂度: O(N)
# 空间复杂度: O(N)
#
# 关键点:
# - 新增元素贡献的对数等于窗口中该元素的当前频次
# - 窗口满足条件时，右边界固定，左边界任意收缩都满足，直接加n-right
# - 收缩窗口时要先从频次中减1，再减少相应的对数
