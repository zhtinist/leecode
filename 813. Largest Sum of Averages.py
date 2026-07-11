"""
LeetCode #813 - Largest Sum of Averages
中文题名：最大平均值的和
https://leetcode.com/problems/largest-sum-of-averages/

We partition a row of numbers `A` into at most `K` adjacent
(non-empty) groups, then our score is the sum of the average of each group. What is the
largest score we can achieve?

Note that our partition must use every number in A, and that scores are not necessarily
integers.

Example:
Input:
A = [9,1,2,3,9]
K = 3
Output: 20
Explanation:
The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
We could have also partitioned A into [9, 1], [2], [3, 9], for example.
That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.

Note:

`1 <= A.length <= 100`.

`1 <= A[i] <= 10000`.

`1 <= K <= A.length`.

Answers within `10^-6` of the correct answer will be accepted as correct.

【中文翻译】
我们将一行数字 `A` 划分为最多 `K` 个相邻（非空）的组，得分为每个组的平均值的总和。我们能达到的最大得分是多少？

注意，划分必须使用 A 中的每个数字，得分不一定是整数。

示例：
输入：A = [9,1,2,3,9], K = 3
输出：20
解释：最佳选择是将 A 划分为 [9], [1, 2, 3], [9]。
答案为 9 + (1 + 2 + 3) / 3 + 9 = 20。
我们也可以将 A 划分为 [9, 1], [2], [3, 9] 等。
那种划分的得分为 5 + 2 + 6 = 13，更差。

注意：
`1 <= A.length <= 100`。
`1 <= A[i] <= 10000`。
`1 <= K <= A.length`。
答案与正确答案的误差在 `10^-6` 以内将被接受。
"""

from typing import List, Optional


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        # Prefix sums for O(1) range sum queries
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        def avg(l: int, r: int) -> float:
            """Average of nums[l:r] (r exclusive)."""
            return (prefix[r] - prefix[l]) / (r - l)

        # dp[i][k] = max sum using first i elements with exactly k groups
        # We'll use 1-indexed DP: dp[i] for k groups at current iteration
        dp = [0.0] * (n + 1)
        # Base: k = 1
        for i in range(1, n + 1):
            dp[i] = avg(0, i)

        for groups in range(2, k + 1):
            new_dp = [0.0] * (n + 1)
            for i in range(groups, n + 1):
                best = 0.0
                for j in range(groups - 1, i):
                    best = max(best, dp[j] + avg(j, i))
                new_dp[i] = best
            dp = new_dp

        return dp[n]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 动态规划。使用前缀和数组快速计算区间平均值。
#
# 定义 dp[i] 为将前 i 个元素分成当前组数的最大平均和。
# 外层循环 groups 从 2 到 K：
#   对于每个 i，尝试所有可能的分割点 j < i，
#   将前 j 个元素分成 groups-1 组（dp[j]），
#   剩下的 [j, i) 作为最后一组（avg(j, i)），
#   取所有方案的最大值。
#
# 空间优化：只用两个一维数组轮流更新（只依赖上一组数的 dp 值）。
#
# 时间复杂度: O(K * N^2) - 三层循环（K * N * N）
# 空间复杂度: O(N) - 两个一维 dp 数组 + 前缀和
#
# 关键点:
# - 前缀和实现 O(1) 区间求和
# - dp 定义为"恰好 K 组"，而非"最多 K 组"
#   因为多分组不会减少得分（平均值的和 >= 整体的平均值）
# - 内层 j 的起始值为 groups-1（至少每组一个元素）
# - 结果可能是浮点数
