"""
LeetCode #2462 - Total Cost to Hire K Workers
雇佣 K 位工人的总代价
https://leetcode.cn/problems/total-cost-to-hire-k-workers/

给你一个下标从 0 开始的整数数组 `costs` ，其中 `costs[i]` 是雇佣第 `i` 位工人的代价。
同时给你两个整数 `k` 和 `candidates` 。我们想根据以下规则恰好雇佣 `k` 位工人：
总共进行 `k` 轮雇佣，且每一轮恰好雇佣一位工人。
在每一轮雇佣中，从最前面 `candidates` 和最后面 `candidates` 人中选出代价最小的一位工人，如果有多位代价相同且最小的工人，选择下标更小的一位工人。
比方说，`costs = [3,2,7,7,1,2]` 且 `candidates = 2` ，第一轮雇佣中，我们选择第 `4` 位工人，因为他的代价最小 `[3,2,7,7,1,2]` 。
第二轮雇佣，我们选择第 `1` 位工人，因为他们的代价与第 `4` 位工人一样都是最小代价，而且下标更小，`[3,2,7,7,2]` 。注意每一轮雇佣后，剩余工人的下标可能会发生变化。
如果剩余员工数目不足 `candidates` 人，那么下一轮雇佣他们中代价最小的一人，如果有多位代价相同且最小的工人，选择下标更小的一位工人。
一位工人只能被选择一次。
返回雇佣恰好 `k` 位工人的总代价。

示例 1：
输入：costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4 输出：11 解释：我们总共雇佣 3 位工人。总代价一开始为 0 。 - 第一轮雇佣，我们从 [17,12,10,2,7,2,11,20,8] 中选择。最小代价是 2 ，有两位工人，我们选择下标更小的一位工人，即第 3 位工人。总代价是 0 + 2 = 2 。 - 第二轮雇佣，我们从 [17,12,10,7,2,11,20,8] 中选择。最小代价是 2 ，下标为 4 ，总代价是 2 + 2 = 4 。 - 第三轮雇佣，我们从 [17,12,10,7,11,20,8] 中选择，最小代价是 7 ，下标为 3 ，总代价是 4 + 7 = 11 。注意下标为 3 的工人同时在最前面和最后面 4 位工人中。 总雇佣代价是 11 。
示例 2：
输入：costs = [1,2,4,1], k = 3, candidates = 3 输出：4 解释：我们总共雇佣 3 位工人。总代价一开始为 0 。 - 第一轮雇佣，我们从 [1,2,4,1] 中选择。最小代价为 1 ，有两位工人，我们选择下标更小的一位工人，即第 0 位工人，总代价是 0 + 1 = 1 。注意，下标为 1 和 2 的工人同时在最前面和最后面 3 位工人中。 - 第二轮雇佣，我们从 [2,4,1] 中选择。最小代价为 1 ，下标为 2 ，总代价是 1 + 1 = 2 。 - 第三轮雇佣，少于 3 位工人，我们从剩余工人 [2,4] 中选择。最小代价是 2 ，下标为 0 。总代价为 2 + 2 = 4 。 总雇佣代价是 4 。

提示：
`1 <= costs.length <= 10^5 `
`1 <= costs[i] <= 10^5`
`1 <= k, candidates <= costs.length`
"""

from typing import List, Optional


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        import heapq

        n = len(costs)
        # 两个指针：left 从左到右，right 从右到左
        left = 0
        right = n - 1
        left_heap = []   # (cost, index) 的元组，小顶堆
        right_heap = []

        # 初始化：将前 candidates 个元素放入 left_heap
        for i in range(candidates):
            if left <= right:
                heapq.heappush(left_heap, (costs[left], left))
                left += 1

        # 初始化：将后 candidates 个元素放入 right_heap
        for i in range(candidates):
            if left <= right:
                heapq.heappush(right_heap, (costs[right], right))
                right -= 1

        total = 0

        for _ in range(k):
            # 选择两个堆顶中代价更小的
            if not right_heap or (left_heap and left_heap[0][0] <= right_heap[0][0]):
                # 当代价相等时，左堆下标更小，所以用 <=
                cost, idx = heapq.heappop(left_heap)
                total += cost
                # 如果还有剩余工人，将下一个加入左堆
                if left <= right:
                    heapq.heappush(left_heap, (costs[left], left))
                    left += 1
            else:
                cost, idx = heapq.heappop(right_heap)
                total += cost
                if left <= right:
                    heapq.heappush(right_heap, (costs[right], right))
                    right -= 1

        return total



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Two Pointers, Simulation, Heap (Priority Queue)
#
# 解题思路:
# 使用两个最小堆（优先队列）和双指针模拟每一轮雇佣过程：
#   1. 左堆 left_heap 存储前 candidates 个候选元素（cost, index）
#   2. 右堆 right_heap 存储后 candidates 个候选元素（cost, index）
#   3. 用双指针 left 和 right 标记已入堆和未入堆的边界
#   4. 每轮比较两个堆顶（最小代价），选择较小的那个：
#      - 代价相同时选下标更小的（左堆优先）
#      - 弹出后若 left <= right（还有未入堆的工人），将边界元素推入对应堆
#   5. 累计 k 轮的总代价并返回
#
# 时间复杂度: O((candidates + k) * log(candidates))
#   初始化填堆 O(candidates * log(candidates))，k 轮每轮 O(log(candidates))
# 空间复杂度: O(candidates)，两个堆最多共存储约 2*candidates 个元素
#
# 关键点:
# - 用 (cost, index) 元组入堆，使堆按 cost 排序，相等时按 index
# - 当两个堆顶 cost 相等时优先选左堆（因为左堆下标更小）
# - 注意边界条件：当 left > right 时不再有新元素入堆
