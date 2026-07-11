"""
LeetCode #3040 - Maximum Number of Operations With the Same Score II
相同分数的最大操作数目 II
https://leetcode.cn/problems/maximum-number-of-operations-with-the-same-score-ii/

给你一个整数数组 `nums` ，如果 `nums` 至少 包含 `2` 个元素，你可以执行以下操作中的 任意 一个：
选择 `nums` 中最前面两个元素并且删除它们。
选择 `nums` 中最后两个元素并且删除它们。
选择 `nums` 中第一个和最后一个元素并且删除它们。
一次操作的 分数 是被删除元素的和。
在确保 所有操作分数相同 的前提下，请你求出 最多 能进行多少次操作。
请你返回按照上述要求 最多 可以进行的操作次数。

示例 1：
输入：nums = [3,2,1,2,3,4] 输出：3 解释：我们执行以下操作： - 删除前两个元素，分数为 3 + 2 = 5 ，nums = [1,2,3,4] 。 - 删除第一个元素和最后一个元素，分数为 1 + 4 = 5 ，nums = [2,3] 。 - 删除第一个元素和最后一个元素，分数为 2 + 3 = 5 ，nums = [] 。 由于 nums 为空，我们无法继续进行任何操作。
示例 2：
输入：nums = [3,2,6,1,4] 输出：2 解释：我们执行以下操作： - 删除前两个元素，分数为 3 + 2 = 5 ，nums = [6,1,4] 。 - 删除最后两个元素，分数为 1 + 4 = 5 ，nums = [6] 。 至多进行 2 次操作。

提示：
`2 <= nums.length <= 2000`
`1 <= nums[i] <= 1000`
"""

from typing import List, Optional


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        """
        Only 3 possible scores from the first operation.
        For each candidate score, use interval DP to find max operations.
        Iterative DP to avoid recursion depth issues.
        """
        n = len(nums)
        if n < 2:
            return 0

        # Three candidate scores
        candidates = {
            nums[0] + nums[1],
            nums[-2] + nums[-1],
            nums[0] + nums[-1],
        }

        def max_ops_for_target(target: int) -> int:
            # dp[l][r] = max operations on subarray [l, r] (inclusive)
            dp = [[0] * n for _ in range(n)]

            # Compute by increasing length
            for length in range(2, n + 1):
                for l in range(n - length + 1):
                    r = l + length - 1
                    best = 0
                    # Delete first two
                    if nums[l] + nums[l + 1] == target:
                        best = max(best, 1 + (dp[l + 2][r] if l + 2 <= r else 0))
                    # Delete last two
                    if nums[r - 1] + nums[r] == target:
                        best = max(best, 1 + (dp[l][r - 2] if l <= r - 2 else 0))
                    # Delete first and last
                    if nums[l] + nums[r] == target:
                        best = max(best, 1 + (dp[l + 1][r - 1] if l + 1 <= r - 1 else 0))
                    dp[l][r] = best

            return dp[0][n - 1]

        ans = 0
        for target in candidates:
            ans = max(ans, max_ops_for_target(target))

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Memoization, Array, Dynamic Programming
#
# 解题思路:
# 第一次操作决定分数。只有三种可能分数：前两个、后两个、或首尾两个元素之和。
# 对每种候选分数，使用区间 DP 计算最大操作次数。
# dp[l][r] 表示在子数组 nums[l..r] 上最多能进行多少次操作。
# 从短区间向长区间递推，每个状态考虑三种删除选择。
#
# 时间复杂度: O(n^2)，三种候选分数各需要一次 O(n^2) 的 DP
# 空间复杂度: O(n^2)，DP 表
#
# 关键点:
# - 第一次操作只有三种可能，分别尝试即可
# - 区间 DP：dp[l][r] = max(三种删除方式)
# - 使用迭代 DP 避免递归深度超限（n 可达 2000）
