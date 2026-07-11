"""
LeetCode #1962 - Remove Stones to Minimize the Total
移除石子使总数最小
https://leetcode.cn/problems/remove-stones-to-minimize-the-total/

给你一个整数数组 `piles` ，数组 下标从 0 开始 ，其中 `piles[i]` 表示第 `i` 堆石子中的石子数量。另给你一个整数 `k` ，请你执行下述操作 恰好 `k` 次：
选出任一石子堆 `piles[i]` ，并从中 移除 `floor(piles[i] / 2)` 颗石子。
注意：你可以对 同一堆 石子多次执行此操作。
返回执行 `k` 次操作后，剩下石子的 最小 总数。
`floor(x)` 为 小于 或 等于 `x` 的 最大 整数。（即，对 `x` 向下取整）。

示例 1：
输入：piles = [5,4,9], k = 2 输出：12 解释：可能的执行情景如下： - 对第 2 堆石子执行移除操作，石子分布情况变成 [5,4,5] 。 - 对第 0 堆石子执行移除操作，石子分布情况变成 [3,4,5] 。 剩下石子的总数为 12 。
示例 2：
输入：piles = [4,3,6,7], k = 3 输出：12 解释：可能的执行情景如下： - 对第 2 堆石子执行移除操作，石子分布情况变成 [4,3,3,7] 。 - 对第 3 堆石子执行移除操作，石子分布情况变成 [4,3,3,4] 。 - 对第 0 堆石子执行移除操作，石子分布情况变成 [2,3,3,4] 。 剩下石子的总数为 12 。

提示：
`1 <= piles.length <= 10^5`
`1 <= piles[i] <= 10^4`
`1 <= k <= 10^5`
"""

from typing import List, Optional


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        """
        Always remove from the largest pile (max-heap). Repeat k times.
        """
        import heapq

        # Use negative values for max-heap
        heap = [-p for p in piles]
        heapq.heapify(heap)

        for _ in range(k):
            max_pile = -heapq.heappop(heap)
            removed = max_pile // 2
            heapq.heappush(heap, -(max_pile - removed))

        return -sum(heap)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Heap (Priority Queue)
#
# 解题思路:
# 贪心策略：每次操作从当前最大的堆中移除 floor(pile/2) 颗石子。
# 使用最大堆维护所有堆的大小。每次：
# 1. 弹出最大堆
# 2. 计算移除量 = pile // 2
# 3. 将剩余的 pile - removed 放回堆中
# 重复 k 次后，堆中所有元素之和即为答案。
# 正确性：每次从中移除一半对总量的减少最大，贪心最优。
#
# 时间复杂度: O((N + K) log N)，堆初始化和 k 次操作
# 空间复杂度: O(N)，堆的存储
#
# 关键点:
# - Python 的 heapq 是最小堆，用负数模拟最大堆
# - 每次选择最大的堆是最优的贪心策略
# - floor(x/2) = x // 2（Python 整数除法）
