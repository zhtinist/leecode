"""
LeetCode #2563 - Count the Number of Fair Pairs
统计公平数对的数目
https://leetcode.cn/problems/count-the-number-of-fair-pairs/

给你一个下标从 0 开始、长度为 `n` 的整数数组 `nums` ，和两个整数 `lower` 和 `upper` ，返回 公平数对的数目 。
如果 `(i, j)` 数对满足以下情况，则认为它是一个 公平数对 ：
`0 <= i < j < n`，且
`lower <= nums[i] + nums[j] <= upper`

示例 1：
输入：nums = [0,1,7,4,4,5], lower = 3, upper = 6 输出：6 解释：共计 6 个公平数对：(0,3)、(0,4)、(0,5)、(1,3)、(1,4) 和 (1,5) 。
示例 2：
输入：nums = [1,7,9,2,5], lower = 11, upper = 11 输出：1 解释：只有单个公平数对：(2,3) 。

提示：
`1 <= nums.length <= 10^5`
`nums.length == n`
`-10^9 <= nums[i] <= 10^9`
`-10^9 <= lower <= upper <= 10^9`
"""

from typing import List, Optional


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        import bisect
        nums.sort()
        ans = 0
        for i, x in enumerate(nums):
            # find j > i such that lower <= x + nums[j] <= upper
            left = bisect.bisect_left(nums, lower - x, i + 1)
            right = bisect.bisect_right(nums, upper - x, i + 1)
            ans += right - left
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Two Pointers, Binary Search, Sorting
#
# 解题思路:
# 排序后对每个元素x，用二分查找找到满足lower-x <= nums[j] <= upper-x的j范围。
# 使用bisect_left找左边界，bisect_right找右边界（从i+1开始确保j>i）。
# 将每对(i,j)的j数量累加得到答案。
#
# 时间复杂度: O(N log N)
# 空间复杂度: O(1)（排序可能O(N)）
#
# 关键点:
# - 固定i，j的取值是一个连续区间
# - bisect_left和bisect_right高效定位区间边界
# - 排序不会影响答案（数对只关心值不关心顺序）
