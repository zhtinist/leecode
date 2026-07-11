"""
LeetCode #2944 - Minimum Number of Coins for Fruits
购买水果需要的最少金币数
https://leetcode.cn/problems/minimum-number-of-coins-for-fruits/

给你一个 下标从 0 开始的 整数数组 `prices` ，其中 `prices[i]` 表示你购买第 `i + 1` 个水果需要花费的金币数目。
水果超市有如下促销活动：
如果你花费 `prices[i]` 购买了下标为 `i + 1` 的水果，那么你可以免费获得下标范围在 `[i + 1, i + i]` 的水果。
注意 ，即使你 可以 免费获得水果 `j` ，你仍然可以花费 `prices[j - 1]` 个金币去购买它以获得它的奖励。
请你返回获得所有水果所需要的 最少 金币数。

示例 1：

输入：prices = [3,1,2]
输出：4
解释：
用 `prices[0] = 3` 个金币购买第 1 个水果，你可以免费获得第 2 个水果。
用 `prices[1] = 1` 个金币购买第 2 个水果，你可以免费获得第 3 个水果。
免费获得第 3 个水果。
请注意，即使您可以免费获得第 2 个水果作为购买第 1 个水果的奖励，但您购买它是为了获得其奖励，这是更优化的。
示例 2：

输入：prices = [1,10,1,1]
输出：2
解释：
用 `prices[0] = 1` 个金币购买第 1 个水果，你可以免费获得第 2 个水果。
免费获得第 2 个水果。
用 `prices[2] = 1` 个金币购买第 3 个水果，你可以免费获得第 4 个水果。
免费获得第 4 个水果。
示例 3：

输入：prices = [26,18,6,12,49,7,45,45]
输出：39
解释：
用 `prices[0] = 26` 个金币购买第 1 个水果，你可以免费获得第 2 个水果。
免费获得第 2 个水果。
用 `prices[2] = 6` 个金币购买第 3 个水果，你可以免费获得第 4，5，6（接下来的三个）水果。
免费获得第 4 个水果。
免费获得第 5 个水果。
用 `prices[5] = 7` 个金币购买第 6 个水果，你可以免费获得第 7 和 第 8 个水果。
免费获得第 7 个水果。
免费获得第 8 个水果。
请注意，即使您可以免费获得第 6 个水果作为购买第 3 个水果的奖励，但您购买它是为了获得其奖励，这是更优化的。

提示：
`1 <= prices.length <= 1000`
`1 <= prices[i] <= 10^5`
"""

from typing import List, Optional


class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        INF = 10**18
        dp = [INF] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            # Buy fruit i: covers i..min(2*i, n)
            max_cover = min(2 * i, n)
            for k in range(i, max_cover + 1):
                if dp[i - 1] + prices[i - 1] < dp[k]:
                    dp[k] = dp[i - 1] + prices[i - 1]
        return dp[n]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Queue, Array, Dynamic Programming, Monotonic Queue, Heap (Priority Queue)
#
# 解题思路:
# DP: dp[i] = 获得前 i 个水果的最小花费。对于每个水果 i（1-indexed），购买它可以覆盖 [i, 2i] 范围的水果。
# 遍历 i 从 1 到 n，用 dp[i-1] + prices[i-1] 更新 dp[k]（k 从 i 到 min(2i, n)）。
# 最终答案为 dp[n]。
#
# 时间复杂度: O(n^2)
# 空间复杂度: O(n)
#
# 关键点:
# - 购买水果 i 可免费获得 [i+1, 2i]，相当于覆盖范围 [i, 2i]
# - dp[i] 定义为覆盖前 i 个水果的最小花费
# - 对每个 i，用其购买成本更新所有能被覆盖到的位置
