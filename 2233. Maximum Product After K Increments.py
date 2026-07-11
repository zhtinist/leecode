"""
LeetCode #2233 - Maximum Product After K Increments
K 次增加后的最大乘积
https://leetcode.cn/problems/maximum-product-after-k-increments/

给你一个非负整数数组 `nums` 和一个整数 `k` 。每次操作，你可以选择 `nums` 中 任一 元素并将它 增加 `1` 。
请你返回 至多 `k` 次操作后，能得到的 `nums`的 最大乘积 。由于答案可能很大，请你将答案对 `10^9 + 7` 取余后返回。

示例 1：
输入：nums = [0,4], k = 5 输出：20 解释：将第一个数增加 5 次。 得到 nums = [5, 4] ，乘积为 5 * 4 = 20 。 可以证明 20 是能得到的最大乘积，所以我们返回 20 。 存在其他增加 nums 的方法，也能得到最大乘积。
示例 2：
输入：nums = [6,3,3,2], k = 2 输出：216 解释：将第二个数增加 1 次，将第四个数增加 1 次。 得到 nums = [6, 4, 3, 3] ，乘积为 6 * 4 * 3 * 3 = 216 。 可以证明 216 是能得到的最大乘积，所以我们返回 216 。 存在其他增加 nums 的方法，也能得到最大乘积。

提示：
`1 <= nums.length, k <= 10^5`
`0 <= nums[i] <= 10^6`
"""

from typing import List, Optional


class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        import heapq

        MOD = 10**9 + 7

        # 使用最小堆，每次取出最小的元素加 1 后放回
        heapq.heapify(nums)

        for _ in range(k):
            smallest = heapq.heappop(nums)
            heapq.heappush(nums, smallest + 1)

        # 计算最终乘积（取模）
        ans = 1
        for num in nums:
            ans = (ans * num) % MOD

        return ans


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Heap (Priority Queue)
#
# 解题思路:
# 贪心策略：每次操作将最小的元素加 1，这样能最大化最终乘积。
# 直观理解：给较小的数 +1 的收益大于给较大的数 +1（类似于固定周长求最大面积，
# 边长越接近乘积越大）。使用最小堆维护数组，每次弹出最小值 +1 后放回。
# 执行 k 次操作后，遍历堆中所有元素累乘并取模 10^9+7。
#
# 时间复杂度: O((N+K) log N) 其中 N 为数组长度，每次堆操作 O(log N)
# 空间复杂度: O(1) 堆化在原数组上，不计额外空间
#
# 关键点:
# - 贪心策略：总是增加当前最小的数
# - 使用最小堆高效获取最小值（O(log N) 每次）
# - 最终乘积需对 10^9+7 取模，注意 Python 大整数不会溢出但需模运算
