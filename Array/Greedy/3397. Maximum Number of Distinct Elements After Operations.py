"""
LeetCode #3397 - Maximum Number of Distinct Elements After Operations
执行操作后不同元素的最大数量
https://leetcode.cn/problems/maximum-number-of-distinct-elements-after-operations/

给你一个整数数组 `nums` 和一个整数 `k`。
你可以对数组中的每个元素 最多 执行 一次 以下操作：
将一个在范围 `[-k, k]` 内的整数加到该元素上。
返回执行这些操作后，`nums` 中可能拥有的不同元素的 最大 数量。

示例 1：

输入： nums = [1,2,2,3,3,4], k = 2
输出： 6
解释：
对前四个元素执行操作，`nums` 变为 `[-1, 0, 1, 2, 3, 4]`，可以获得 6 个不同的元素。
示例 2：

输入： nums = [4,4,4,4], k = 1
输出： 3
解释：
对 `nums[0]` 加 -1，以及对 `nums[1]` 加 1，`nums` 变为 `[3, 5, 4, 4]`，可以获得 3 个不同的元素。

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^9`
`0 <= k <= 10^9`
"""

from typing import List, Optional


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        last = -10 ** 18
        for x in nums:
            target = max(last + 1, x - k)
            if target <= x + k:
                last = target
                ans += 1
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Sorting
#
# 解题思路:
# 贪心。排序nums后从左到右处理。维护上一个分配的不同值last，对于每个nums[i]，
# 尝试分配值为max(last+1, nums[i]-k)，如果<=nums[i]+k则成功分配一个不同的值并更新last。
# 这样保证尽可能得到更多不同的值。
#
# 时间复杂度: O(n log n)，排序主导
# 空间复杂度: O(1)
#
# 关键点:
# - 排序后贪心分配尽可能小的不同值
# - 每个元素的可达范围是[nums[i]-k, nums[i]+k]
