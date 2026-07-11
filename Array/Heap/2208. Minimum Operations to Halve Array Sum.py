"""
LeetCode #2208 - Minimum Operations to Halve Array Sum
将数组和减半的最少操作次数
https://leetcode.cn/problems/minimum-operations-to-halve-array-sum/

给你一个正整数数组 `nums` 。每一次操作中，你可以从 `nums` 中选择 任意 一个数并将它减小到 恰好 一半。（注意，在后续操作中你可以对减半过的数继续执行操作）
请你返回将 `nums` 数组和 至少 减少一半的 最少 操作数。

示例 1：
输入：nums = [5,19,8,1] 输出：3 解释：初始 nums 的和为 5 + 19 + 8 + 1 = 33 。 以下是将数组和减少至少一半的一种方法： 选择数字 19 并减小为 9.5 。 选择数字 9.5 并减小为 4.75 。 选择数字 8 并减小为 4 。 最终数组为 [5, 4.75, 4, 1] ，和为 5 + 4.75 + 4 + 1 = 14.75 。 nums 的和减小了 33 - 14.75 = 18.25 ，减小的部分超过了初始数组和的一半，18.25 >= 33/2 = 16.5 。 我们需要 3 个操作实现题目要求，所以返回 3 。 可以证明，无法通过少于 3 个操作使数组和减少至少一半。
示例 2：
输入：nums = [3,8,20] 输出：3 解释：初始 nums 的和为 3 + 8 + 20 = 31 。 以下是将数组和减少至少一半的一种方法： 选择数字 20 并减小为 10 。 选择数字 10 并减小为 5 。 选择数字 3 并减小为 1.5 。 最终数组为 [1.5, 8, 5] ，和为 1.5 + 8 + 5 = 14.5 。 nums 的和减小了 31 - 14.5 = 16.5 ，减小的部分超过了初始数组和的一半， 16.5 >= 31/2 = 15.5 。 我们需要 3 个操作实现题目要求，所以返回 3 。 可以证明，无法通过少于 3 个操作使数组和减少至少一半。

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^7`
"""

from typing import List, Optional
import heapq


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        # Use max-heap via negating values
        total = sum(nums)
        target = total / 2.0

        # Max-heap: store negative values for Python's min-heap
        heap = [-num for num in nums]
        heapq.heapify(heap)

        reduced = 0.0
        operations = 0

        while reduced < target:
            # Pop the largest element
            max_val = -heapq.heappop(heap)
            # Halve it
            half = max_val / 2.0
            # The amount we reduced from the sum
            reduced += half
            # Push back the halved value
            heapq.heappush(heap, -half)
            operations += 1

        return operations


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Heap (Priority Queue)
#
# 解题思路:
# 1. 核心贪心策略：每次操作选择当前数组中最大的数进行减半，
#    因为减半一个更大的数能带来更大的绝对减少量。
# 2. 使用最大堆（大顶堆）来高效获取当前最大值。
#    Python 的 heapq 是最小堆，因此通过存储负数来模拟最大堆。
# 3. 算法流程：
#    a) 计算初始数组总和 total，目标减少量为 total / 2。
#    b) 将所有元素取负后构建最大堆。
#    c) 循环：取出堆顶（当前最大值），将其减半，
#       累计减少量 reduced += half（注意减半操作减少的量为原值的一半），
#       将减半后的值推回堆中，操作次数 +1。
#    d) 当累计减少量 >= target 时停止，返回操作次数。
#
# 时间复杂度: O(N + K * log N)，其中 N 为数组长度，K 为操作次数。
#             建堆 O(N)，每次操作 O(log N)。
# 空间复杂度: O(N)，堆中存储所有元素。
#
# 关键点:
# - 贪心策略的正确性：每次减半最大元素是减少总和的最优方式（类似霍夫曼编码的思想）。
# - 使用浮点数运算：减半后的值可能是小数，reduced 累加的量也使用浮点数。
# - 需要将减半后的值推回堆中，因为它可能在后续操作中继续被选中。
# - Python heapq 是最小堆，取负值实现最大堆是标准技巧。
