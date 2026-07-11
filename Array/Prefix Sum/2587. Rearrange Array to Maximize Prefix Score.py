"""
LeetCode #2587 - Rearrange Array to Maximize Prefix Score
重排数组以得到最大前缀分数
https://leetcode.cn/problems/rearrange-array-to-maximize-prefix-score/

给你一个下标从 0 开始的整数数组 `nums` 。你可以将 `nums` 中的元素按 任意顺序 重排（包括给定顺序）。
令 `prefix` 为一个数组，它包含了 `nums` 重新排列后的前缀和。换句话说，`prefix[i]` 是 `nums` 重新排列后下标从 `0` 到 `i` 的元素之和。`nums` 的 分数 是 `prefix` 数组中正整数的个数。
返回可以得到的最大分数。

示例 1：
输入：nums = [2,-1,0,1,-3,3,-3] 输出：6 解释：数组重排为 nums = [2,3,1,-1,-3,0,-3] 。 prefix = [2,5,6,5,2,2,-1] ，分数为 6 。 可以证明 6 是能够得到的最大分数。
示例 2：
输入：nums = [-2,-3,0] 输出：0 解释：不管怎么重排数组得到的分数都是 0 。

提示：
`1 <= nums.length <= 10^5`
`-10^6 <= nums[i] <= 10^6`
"""

from typing import List, Optional


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        prefix = 0
        count = 0
        for x in nums:
            prefix += x
            if prefix > 0:
                count += 1
        return count



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Prefix Sum, Sorting
#
# 解题思路:
# 贪心：将数组降序排列（正数在前，越大的数越前）。前缀和从最大正数开始累加，
# 能推迟负数的出现，最大化正前缀和的数量。遍历计算前缀和并统计>0的次数。
#
# 时间复杂度: O(N log N)
# 空间复杂度: O(1)
#
# 关键点:
# - 降序排列保证前缀和尽可能长时间保持正数
# - 只需统计前缀和>0的个数，不需要记录完整前缀和数组
# - 即使有负数，只要前缀和仍>0也算入分数
