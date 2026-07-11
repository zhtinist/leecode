"""
LeetCode #2279 - Maximum Bags With Full Capacity of Rocks
装满石头的背包的最大数量
https://leetcode.cn/problems/maximum-bags-with-full-capacity-of-rocks/

现有编号从 `0` 到 `n - 1` 的 `n` 个背包。给你两个下标从 0 开始的整数数组 `capacity` 和 `rocks` 。第 `i` 个背包最大可以装 `capacity[i]` 块石头，当前已经装了 `rocks[i]` 块石头。另给你一个整数 `additionalRocks` ，表示你可以放置的额外石头数量，石头可以往 任意 背包中放置。
请你将额外的石头放入一些背包中，并返回放置后装满石头的背包的 最大 数量。

示例 1：
输入：capacity = [2,3,4,5], rocks = [1,2,4,4], additionalRocks = 2 输出：3 解释： 1 块石头放入背包 0 ，1 块石头放入背包 1 。 每个背包中的石头总数是 [2,3,4,4] 。 背包 0 、背包 1 和 背包 2 都装满石头。 总计 3 个背包装满石头，所以返回 3 。 可以证明不存在超过 3 个背包装满石头的情况。 注意，可能存在其他放置石头的方案同样能够得到 3 这个结果。
示例 2：
输入：capacity = [10,2,2], rocks = [2,2,0], additionalRocks = 100 输出：3 解释： 8 块石头放入背包 0 ，2 块石头放入背包 2 。 每个背包中的石头总数是 [10,2,2] 。 背包 0 、背包 1 和背包 2 都装满石头。 总计 3 个背包装满石头，所以返回 3 。 可以证明不存在超过 3 个背包装满石头的情况。 注意，不必用完所有的额外石头。

提示：
`n == capacity.length == rocks.length`
`1 <= n <= 5 * 10^4`
`1 <= capacity[i] <= 10^9`
`0 <= rocks[i] <= capacity[i]`
`1 <= additionalRocks <= 10^9`
"""

from typing import List, Optional


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        """
        Return the maximum number of bags that can be filled to capacity
        using at most additionalRocks extra stones.
        """
        n = len(capacity)
        # Calculate remaining capacity needed for each bag
        remaining = [capacity[i] - rocks[i] for i in range(n)]
        remaining.sort()

        ans = 0
        for need in remaining:
            if need == 0:
                ans += 1
            elif additionalRocks >= need:
                additionalRocks -= need
                ans += 1
            else:
                break

        return ans


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Sorting
#
# 解题思路:
# 贪心策略：要使装满的背包数量最大化，应该优先装满"剩余容量最小"的背包，
# 因为用更少的石头就能多获得一个满背包。具体步骤：
# 1. 计算每个背包还差多少石头才能装满：remaining[i] = capacity[i] - rocks[i]
# 2. 将 remaining 数组从小到大排序
# 3. 从剩余容量最小的背包开始装，每装满一个就从 additionalRocks 中扣除对应石头
# 4. 当 additionalRocks 不足以装满下一个背包时停止
#
# 时间复杂度: O(N log N)，N 为背包数量。排序占据主要时间。
# 空间复杂度: O(N)，用于存储 remaining 数组。
#
# 关键点:
# - 贪心策略正确性：每个背包"装满"的价值相同（都是 +1），但成本不同（剩余容量），
#   选择成本最低的背包能最大化数量
# - 已经装满的背包（remaining = 0）无条件计入答案
# - 排序后从头遍历，用额外石头填充容量最小的背包
# - 不必用完所有额外石头
