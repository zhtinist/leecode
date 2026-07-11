"""
LeetCode #3180 - Maximum Total Reward Using Operations I
执行操作可获得的最大总奖励 I
https://leetcode.cn/problems/maximum-total-reward-using-operations-i/

给你一个整数数组 `rewardValues`，长度为 `n`，代表奖励的值。
最初，你的总奖励 `x` 为 0，所有下标都是 未标记 的。你可以执行以下操作 任意次 ：
从区间 `[0, n - 1]` 中选择一个 未标记 的下标 `i`。
如果 `rewardValues[i]` 大于 你当前的总奖励 `x`，则将 `rewardValues[i]` 加到 `x` 上（即 `x = x + rewardValues[i]`），并 标记 下标 `i`。
以整数形式返回执行最优操作能够获得的 最大 总奖励。

示例 1：

输入：rewardValues = [1,1,3,3]
输出：4
解释：
依次标记下标 0 和 2，总奖励为 4，这是可获得的最大值。
示例 2：

输入：rewardValues = [1,6,4,3,2]
输出：11
解释：
依次标记下标 0、2 和 1。总奖励为 11，这是可获得的最大值。

提示：
`1 <= rewardValues.length <= 2000`
`1 <= rewardValues[i] <= 2000`
"""

from typing import List, Optional


class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        nums = sorted(set(rewardValues))
        dp = 1  # 二进制位的集合，bit x 表示总和x可达
        for v in nums:
            # 只从 x < v 的状态转移
            mask = (1 << v) - 1  # 低v位为1
            dp |= (dp & mask) << v
        return dp.bit_length() - 1  # 最高位的位置即最大可达和



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Array, Dynamic Programming, Sorting
#
# 解题思路:
# 排序并去重rewardValues。DP用整数bitset表示可达总和：bit x为1表示总和x可达。
# 对于每个奖励值v，只能从当前总和x<v的状态转移（加v得x+v）。
# 用位运算：mask保留低v位，dp |= (dp&mask)<<v。最终dp的最高位即最大可达总和。
#
# 时间复杂度: O(n * M/64)，其中M为总和上限（约2*10^6）
# 空间复杂度: O(M/64)
#
# 关键点:
# - 奖励必须大于当前总和才能使用
# - bitset优化DP，位运算实现批量状态转移
# - mask = (1<<v)-1限制只能从x<v转移
