"""
LeetCode #3652 - Best Time to Buy and Sell Stock using Strategy
按策略买卖股票的最佳时机
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-using-strategy/

给你两个整数数组 `prices` 和 `strategy`，其中：
`prices[i]` 表示第 `i` 天某股票的价格。
`strategy[i]` 表示第 `i` 天的交易策略，其中：
`-1` 表示买入一单位股票。
`0` 表示持有股票。
`1` 表示卖出一单位股票。
同时给你一个 偶数 整数 `k`，你可以对 `strategy` 进行 最多一次 修改。一次修改包括：
选择 `strategy` 中恰好 `k` 个 连续 元素。
将前 `k / 2` 个元素设为 `0`（持有）。
将后 `k / 2` 个元素设为 `1`（卖出）。
利润 定义为所有天数中 `strategy[i] * prices[i]` 的 总和 。
返回你可以获得的 最大 可能利润。
注意： 没有预算或股票持有数量的限制，因此所有买入和卖出操作均可行，无需考虑过去的操作。

示例 1：

输入： prices = [4,2,8], strategy = [-1,0,1], k = 2
输出： 10
解释：   	 		 			修改 			策略 			利润计算 			利润 		 	 	 		 			原始 			[-1, 0, 1] 			(-1 × 4) + (0 × 2) + (1 × 8) = -4 + 0 + 8 			4 		 		 			修改 [0, 1] 			[0, 1, 1] 			(0 × 4) + (1 × 2) + (1 × 8) = 0 + 2 + 8 			10 		 		 			修改 [1, 2] 			[-1, 0, 1] 			(-1 × 4) + (0 × 2) + (1 × 8) = -4 + 0 + 8 			4
因此，最大可能利润是 10，通过修改子数组 `[0, 1]` 实现。
示例 2：

输入： prices = [5,4,3], strategy = [1,1,0], k = 2
输出： 9
解释：
修改 			策略 			利润计算 			利润 		 	 	 		 			原始 			[1, 1, 0] 			(1 × 5) + (1 × 4) + (0 × 3) = 5 + 4 + 0 			9 		 		 			修改 [0, 1] 			[0, 1, 0] 			(0 × 5) + (1 × 4) + (0 × 3) = 0 + 4 + 0 			4 		 		 			修改 [1, 2] 			[1, 0, 1] 			(1 × 5) + (0 × 4) + (1 × 3) = 5 + 0 + 3 			8
因此，最大可能利润是 9，无需任何修改即可达成。

提示：
`2 <= prices.length == strategy.length <= 10^5`
`1 <= prices[i] <= 10^5`
`-1 <= strategy[i] <= 1`
`2 <= k <= prices.length`
`k` 是偶数
"""

from typing import List, Optional


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)

        # 原始利润
        original = sum(s * p for s, p in zip(strategy, prices))

        # 修改窗口 [i, i+k-1]:
        # 前 k/2 个变成 0，后 k/2 个变成 1
        # 对于窗口内的第 t 个元素（0-indexed）：
        #   new_val = 0 if t < k/2 else 1
        #   delta = (new_val - old_val) * price
        half = k // 2

        # 计算第一个窗口的 delta
        cur_delta = 0
        for t in range(k):
            old = strategy[t]
            new = 0 if t < half else 1
            cur_delta += (new - old) * prices[t]

        max_delta = cur_delta

        # 滑动窗口
        for i in range(1, n - k + 1):
            # 移除窗口最左侧元素（旧的 t=0，即原 i-1 位置）
            # 它在旧窗口中是第 0 个，new=0
            old_left = strategy[i - 1]
            cur_delta -= (0 - old_left) * prices[i - 1]

            # 窗口内其他元素索引前移一位：
            # 旧的 t=half-1 (new=0) -> 新的 t=half-2 (new=1...不对)
            # 更清晰的做法：重新计算进出窗口的差值

            # 进：索引 i+k-1（新窗口最后一个元素），t=k-1，new=1
            new_right = strategy[i + k - 1]
            cur_delta += (1 - new_right) * prices[i + k - 1]

            # 窗口中间元素：在旧窗口是第 half 个 (new=1)，在新窗口是第 half-1 个 (new=0)
            # net change = (0 - old_mid) - (1 - old_mid) = -1，即贡献减少 prices[mid_idx]
            mid_idx = i - 1 + half
            cur_delta -= prices[mid_idx]

            if cur_delta > max_delta:
                max_delta = cur_delta

        return original + max(0, max_delta)










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Prefix Sum, Sliding Window
#
# 解题思路:
# 先计算不修改时的原始利润：sum(strategy[i] * prices[i])。
# 对于每个长度为 k 的窗口 [i, i+k-1]：
#   修改规则：前 k/2 个变成 0，后 k/2 个变成 1。
#   计算修改这个窗口对总利润的改变量 delta。
#   使用滑动窗口维护 delta 的变化：
#   - 移除最左元素：撤销旧值（t=0, new=0）的贡献
#   - 中间元素 shift：原 t=half 从 new=1 变为 new=0，贡献减少 prices[mid_idx]
#   - 加入最右元素：添加新值（t=k-1, new=1）的贡献
#   答案 = 原始利润 + max(0, 所有窗口的最大 delta)
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 滑动窗口维护 delta 变化，而非重新计算每个窗口
# - 窗口中间元素（第 half 个）从 1 变为 0，贡献恰好减少 prices[mid_idx]
# - 只修改一次或不修改（取 max(0, max_delta)）
