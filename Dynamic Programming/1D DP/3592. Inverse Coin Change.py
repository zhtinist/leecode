"""
LeetCode #3592 - Inverse Coin Change
硬币面值还原
https://leetcode.cn/problems/inverse-coin-change/

给你一个 从 1 开始计数 的整数数组 `numWays`，其中 `numWays[i]` 表示使用某些 固定 面值的硬币（每种面值可以使用无限次）凑出总金额 `i` 的方法数。每种面值都是一个 正整数 ，并且其值 最多 为 `numWays.length`。
然而，具体的硬币面值已经 丢失 。你的任务是还原出可能生成这个 `numWays` 数组的面值集合。
返回一个按从小到大顺序排列的数组，其中包含所有可能的 唯一 整数面值。
如果不存在这样的集合，返回一个 空 数组。

示例 1：

输入： numWays = [0,1,0,2,0,3,0,4,0,5]
输出： [2,4,6]
解释：   	 		 			金额 			方法数 			解释 		 		 			1 			0 			无法用硬币凑出总金额 1。 		 		 			2 			1 			唯一的方法是 `[2]`。 		 		 			3 			0 			无法用硬币凑出总金额 3。 		 		 			4 			2 			可以用 `[2, 2]` 或 `[4]`。 		 		 			5 			0 			无法用硬币凑出总金额 5。 		 		 			6 			3 			可以用 `[2, 2, 2]`、`[2, 4]` 或 `[6]`。 		 		 			7 			0 			无法用硬币凑出总金额 7。 		 		 			8 			4 			可以用 `[2, 2, 2, 2]`、`[2, 2, 4]`、`[2, 6]` 或 `[4, 4]`。 		 		 			9 			0 			无法用硬币凑出总金额 9。 		 		 			10 			5 			可以用 `[2, 2, 2, 2, 2]`、`[2, 2, 2, 4]`、`[2, 4, 4]`、`[2, 2, 6]` 或 `[4, 6]`。
示例 2：

输入： numWays = [1,2,2,3,4]
输出： [1,2,5]
解释：   	 		 			金额 			方法数 			解释 		 		 			1 			1 			唯一的方法是 `[1]`。 		 		 			2 			2 			可以用 `[1, 1]` 或 `[2]`。 		 		 			3 			2 			可以用 `[1, 1, 1]` 或 `[1, 2]`。 		 		 			4 			3 			可以用 `[1, 1, 1, 1]`、`[1, 1, 2]` 或 `[2, 2]`。 		 		 			5 			4 			可以用 `[1, 1, 1, 1, 1]`、`[1, 1, 1, 2]`、`[1, 2, 2]` 或 `[5]`。
示例 3：

输入： numWays = [1,2,3,4,15]
输出： []
解释：
没有任何面值集合可以生成该数组。

提示：
`1 <= numWays.length <= 100`
`0 <= numWays[i] <= 2 * 10^8`
"""

from typing import List, Optional


class Solution:
    def inverseCoinChange(self, numWays: List[int]) -> List[int]:
        """numWays is 1-indexed: numWays[i] = ways to make amount i+1.
        Return sorted unique coin denominations, or [] if impossible."""
        n = len(numWays)
        # dp[i] = number of ways to make amount i using coins identified so far
        # dp[0] = 1 (one way to make amount 0: use no coins)
        dp = [0] * (n + 1)
        dp[0] = 1

        coins = []

        for amount in range(1, n + 1):
            # dp[amount] is the number of ways using only coins < amount
            # numWays[amount - 1] is the target number of ways

            if dp[amount] == numWays[amount - 1]:
                # Already matches, amount is NOT a coin
                continue
            elif dp[amount] < numWays[amount - 1]:
                # Need additional ways. amount could be a coin
                # Adding coin of value 'amount' adds dp[0] = 1 way
                # (the single coin of value 'amount')
                # We also need to propagate this coin's effect to larger amounts
                diff = numWays[amount - 1] - dp[amount]
                # Check if diff can be explained by adding coin 'amount'
                # For a single new coin of value 'amount', the contribution to
                # numWays[amount-1] (target for amount) is dp[0] = 1.
                # Actually, adding a coin of value c increases dp[j] by dp[j-c]
                # for all j >= c. So for j=amount, the increase is dp[0] = 1.
                # But we also need to verify consistency across all amounts.

                # Let's check if we need to add exactly one coin of value 'amount'
                # The new coin adds dp_before[amount - amount] = dp_before[0] = 1
                # to dp[amount]. If the difference is exactly 1, good.
                # If diff > 1, it might mean multiple coins of different values
                # contribute. But we process in increasing order, so all coins
                # < amount are already accounted for. The only coin that can
                # contribute new ways to amount without affecting smaller amounts
                # is the coin of value 'amount' itself.
                if diff != 1:
                    # This shouldn't happen if the data is consistent, but
                    # let's check if multiple coins of value 'amount' could work.
                    # The problem says coins are unique, so only one coin per value.
                    return []

                coins.append(amount)
                # Update dp for all larger amounts using this new coin
                # dp[j] += dp[j - amount] using dp values from BEFORE adding this coin
                # We need to use the OLD dp for the update
                # Standard coin change: for coin in coins: for j from coin to n: dp[j] += dp[j-coin]
                # Since we're adding coins one by one, we can update in-place
                for j in range(amount, n + 1):
                    dp[j] += dp[j - amount]
            else:
                # dp[amount] > numWays[amount - 1]
                # We already have more ways than the target, impossible
                return []

        return coins











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Dynamic Programming
#
# 解题思路:
# 这是经典硬币找零问题的逆问题。已知每种金额的组合方法数，还原硬币面值。
#
# 核心贪心算法：
# 1. 从金额 1 到 n 依次判断每个金额是否为硬币面值：
#    - dp[a] 表示仅使用已确定的小于 a 的硬币凑出金额 a 的方法数。
#    - 目标值为 numWays[a-1]（题目是 1-indexed）。
# 2. 如果 dp[a] == numWays[a-1]，说明现有硬币已能解释该金额，a 不是硬币。
# 3. 如果 dp[a] < numWays[a-1]：
#    - 差距必须恰好为 1（因为新加一枚面值为 a 的硬币只能增加 dp[0]=1 种方法）。
#    - 若差距不为 1，说明输入不合法，返回空数组。
#    - 否则将 a 加入硬币集合，并按标准完全背包 DP 更新所有更大金额的 dp 值：
#      for j in [a, n]: dp[j] += dp[j-a]（原地更新允许重复使用）。
# 4. 如果 dp[a] > numWays[a-1]，不可能发生，直接返回空数组。
#
# 时间复杂度: O(N^2)，其中 N = len(numWays)。每个硬币会使内层循环遍历 O(N) 个金额
# 空间复杂度: O(N)，dp 数组
#
# 关键点:
# - 原问题（硬币找零）是完全背包 DP：dp[j] += dp[j-coin]
# - 逆向推理：小面值硬币总是优先被确定，因为大面值无法影响小金额
# - 面值为 a 的硬币对金额 a 的贡献精确为 1，因此差距必然为 0 或 1
# - 原地更新 dp 数组恰好对应完全背包（每种硬币无限使用）
