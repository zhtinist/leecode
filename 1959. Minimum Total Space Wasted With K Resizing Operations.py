"""
LeetCode #1959 - Minimum Total Space Wasted With K Resizing Operations
K 次调整数组大小浪费的最小总空间
https://leetcode.cn/problems/minimum-total-space-wasted-with-k-resizing-operations/

你正在设计一个动态数组。给你一个下标从 0 开始的整数数组 `nums` ，其中 `nums[i]` 是 `i` 时刻数组中的元素数目。除此以外，你还有一个整数 `k` ，表示你可以 调整 数组大小的 最多 次数（每次都可以调整成 任意 大小）。
`t` 时刻数组的大小 `size_t` 必须大于等于 `nums[t]` ，因为数组需要有足够的空间容纳所有元素。`t` 时刻 浪费的空间 为 `size_t - nums[t]` ，总 浪费空间为满足 `0 <= t < nums.length` 的每一个时刻 `t` 浪费的空间 之和 。
在调整数组大小不超过 `k` 次的前提下，请你返回 最小总浪费空间 。
注意：数组最开始时可以为 任意大小 ，且 不计入 调整大小的操作次数。

示例 1：
输入：nums = [10,20], k = 0 输出：10 解释：size = [20,20]. 我们可以让数组初始大小为 20 。 总浪费空间为 (20 - 10) + (20 - 20) = 10 。
示例 2：
输入：nums = [10,20,30], k = 1 输出：10 解释：size = [20,20,30]. 我们可以让数组初始大小为 20 ，然后时刻 2 调整大小为 30 。 总浪费空间为 (20 - 10) + (20 - 20) + (30 - 30) = 10 。
示例 3：
输入：nums = [10,20,15,30,20], k = 2 输出：15 解释：size = [10,20,20,30,30]. 我们可以让数组初始大小为 10 ，时刻 1 调整大小为 20 ，时刻 3 调整大小为 30 。 总浪费空间为 (10 - 10) + (20 - 20) + (20 - 15) + (30 - 30) + (30 - 20) = 15 。

提示：
`1 <= nums.length <= 200`
`1 <= nums[i] <= 10^6`
`0 <= k <= nums.length - 1`
"""

from typing import List, Optional


class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        """
        DP: dp[i][t] = min wasted space for first i elements with t resizes.
        Precompute waste[l][r] = wasted space if we use max(nums[l..r]) as size
        for the segment [l, r] (inclusive).
        """
        n = len(nums)
        INF = 10**18

        # waste[l][r]: if we keep same size = max(nums[l..r]) for segment [l, r]
        waste = [[0] * n for _ in range(n)]
        for l in range(n):
            cur_max = 0
            cur_sum = 0
            for r in range(l, n):
                cur_max = max(cur_max, nums[r])
                cur_sum += nums[r]
                waste[l][r] = cur_max * (r - l + 1) - cur_sum

        # dp[i][t]: first i elements (0..i-1), used t resizes (not counting initial)
        # We allow up to k resizes, so t from 0..k
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for t in range(k + 1):
                # The last segment ends at i-1, starts at j
                for j in range(i):
                    if t == 0 and j > 0:
                        continue
                    prev_t = t - 1 if j > 0 else t
                    if prev_t >= 0 and dp[j][prev_t] != INF:
                        dp[i][t] = min(dp[i][t], dp[j][prev_t] + waste[j][i - 1])

        return min(dp[n])



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Dynamic Programming, Prefix Sum
#
# 解题思路:
# 动态规划。dp[i][t] = 处理前 i 个元素、使用了 t 次调整时的最小浪费空间。
# 预处理 waste[l][r]：如果区间 [l, r] 使用同一个 size（即该区间的最大值），
# 产生的浪费空间 = max * len - sum。
# 转移：枚举最后一段的起点 j，dp[i][t] = min(dp[j][t-1] + waste[j][i-1])。
# 初始设大小不算调整次数，所以第一段（j=0）的 t 不变，后面每新开一段 t+1。
#
# 时间复杂度: O(N^2 * K)，N <= 200, K <= N
# 空间复杂度: O(N^2 + N*K)
#
# 关键点:
# - 同一段内保持 size 不变，最优 size 是该段最大值
# - 初始大小不算调整次数
# - N <= 200 使得 O(N^2*K) 可行
