"""
LeetCode #2952 - Minimum Number of Coins to be Added
需要添加的硬币的最小数量
https://leetcode.cn/problems/minimum-number-of-coins-to-be-added/

给你一个下标从 0 开始的整数数组 `coins`，表示可用的硬币的面值，以及一个整数 `target` 。
如果存在某个 `coins` 的子序列总和为 `x`，那么整数 `x` 就是一个 可取得的金额 。
返回需要添加到数组中的 任意面值 硬币的 最小数量 ，使范围 `[1, target]` 内的每个整数都属于 可取得的金额 。
数组的 子序列 是通过删除原始数组的一些（可能不删除）元素而形成的新的 非空 数组，删除过程不会改变剩余元素的相对位置。

示例 1：
输入：coins = [1,4,10], target = 19 输出：2 解释：需要添加面值为 2 和 8 的硬币各一枚，得到硬币数组 [1,2,4,8,10] 。 可以证明从 1 到 19 的所有整数都可由数组中的硬币组合得到，且需要添加到数组中的硬币数目最小为 2 。
示例 2：
输入：coins = [1,4,10,5,7,19], target = 19 输出：1 解释：只需要添加一枚面值为 2 的硬币，得到硬币数组 [1,2,4,5,7,10,19] 。 可以证明从 1 到 19 的所有整数都可由数组中的硬币组合得到，且需要添加到数组中的硬币数目最小为 1 。
示例 3：
输入：coins = [1,1,1], target = 20 输出：3 解释： 需要添加面值为 4 、8 和 16 的硬币各一枚，得到硬币数组 [1,1,1,4,8,16] 。  可以证明从 1 到 20 的所有整数都可由数组中的硬币组合得到，且需要添加到数组中的硬币数目最小为 3 。

提示：
`1 <= target <= 10^5`
`1 <= coins.length <= 10^5`
`1 <= coins[i] <= target`
"""

from typing import List, Optional


class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        s = 0  # max reachable sum so far (can form [0, s])
        ans = 0
        i = 0
        n = len(coins)
        while s < target:
            if i < n and coins[i] <= s + 1:
                s += coins[i]
                i += 1
            else:
                # Need to add coin of value s + 1
                s += s + 1
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
# 贪心策略：排序硬币，维护当前可构成的最大金额 s（能构成 [0, s] 的所有整数）。
# 遍历硬币：若当前硬币面值 <= s+1，则扩展到 s+coin；否则需添加一枚面值为 s+1 的硬币（扩展范围到 2s+1）。
# 重复直到 s >= target。这是最小硬币补充问题的经典贪心解法。
#
# 时间复杂度: O(n log n + log(target))
# 空间复杂度: O(1)
#
# 关键点:
# - 维护已能覆盖的连续区间 [0, s]
# - 当 coin > s+1 时出现"缺口"，必须添加 s+1 填补
# - 添加 s+1 后覆盖范围翻倍（s -> 2s+1）
