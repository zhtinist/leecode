"""
LeetCode #2708 - Maximum Strength of a Group
一个小组的最大实力值
https://leetcode.cn/problems/maximum-strength-of-a-group/

给你一个下标从 0 开始的整数数组 `nums` ，它表示一个班级中所有学生在一次考试中的成绩。老师想选出一部分同学组成一个 非空 小组，且这个小组的 实力值 最大，如果这个小组里的学生下标为 `i_0`, `i_1`, `i_2`, ... , `i_k` ，那么这个小组的实力值定义为 `nums[i_0] * nums[i_1] * nums[i_2] * ... * nums[i_k​]` 。
请你返回老师创建的小组能得到的最大实力值为多少。

示例 1：
输入：nums = [3,-1,-5,2,5,-9] 输出：1350 解释：一种构成最大实力值小组的方案是选择下标为 [0,2,3,4,5] 的学生。实力值为 3 * (-5) * 2 * 5 * (-9) = 1350 ，这是可以得到的最大实力值。
示例 2：
输入：nums = [-4,-5,-4] 输出：20 解释：选择下标为 [0, 1] 的学生。得到的实力值为 20 。我们没法得到更大的实力值。

提示：
`1 <= nums.length <= 13`
`-9 <= nums[i] <= 9`
"""

from typing import List, Optional


class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # sort to handle negatives
        nums.sort()
        n = len(nums)
        ans = 1
        has_positive = False

        # multiply all non-zero elements in pairs from left (negatives)
        i = 0
        # take pairs of negatives (product is positive)
        while i < n - 1 and nums[i] < 0 and nums[i + 1] < 0:
            ans *= nums[i] * nums[i + 1]
            has_positive = True
            i += 2

        # skip remaining single negative (if any)
        # multiply all positives
        for j in range(n):
            if nums[j] > 0:
                ans *= nums[j]
                has_positive = True

        if not has_positive:
            # all non-positive and no pair formed: return max element (might be 0 or single negative)
            return max(nums)

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Bit Manipulation, Array, Dynamic Programming, Backtracking, Enumeration, Sorting
#
# 解题思路:
# 贪心策略。先处理所有负数：负负得正，所以将负数排序后成对相乘（每对产生正贡献）。
# 如果有落单的负数且没有其他正数，需要特殊处理（直接返回该负数或...）。
# 然后将所有正数相乘。特殊情况：只有一个元素时直接返回，全为0或0+负数时返回最大值。
# 由于n<=13，也可以用回溯枚举所有子集。
#
# 时间复杂度: O(n log n)
# 空间复杂度: O(1)
#
# 关键点:
# - 负数成对使用（排序后相邻配对）
# - 正数全部包含
# - 特殊情况：只有一个负数且无正数时，返回该负数（非空子集）
# - n很小(<=13)，暴力枚举也是可行方案
