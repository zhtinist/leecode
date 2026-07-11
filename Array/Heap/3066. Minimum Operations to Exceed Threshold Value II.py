"""
LeetCode #3066 - Minimum Operations to Exceed Threshold Value II
超过阈值的最少操作数 II
https://leetcode.cn/problems/minimum-operations-to-exceed-threshold-value-ii/

给你一个下标从 0 开始的整数数组 `nums` 和一个整数 `k` 。
你可以对 `nums` 执行一些操作，在一次操作中，你可以：
选择 `nums` 中 最小 的两个整数 `x` 和 `y` 。
将 `x` 和 `y` 从 `nums` 中删除。
将 `min(x, y) * 2 + max(x, y)` 添加到数组中的任意位置。
注意，只有当 `nums` 至少 包含两个元素时，你才可以执行以上操作。
你需要使数组中的所有元素都 大于或等于 `k` ，请你返回需要的 最少 操作次数。

示例 1：

输入：nums = [2,11,10,1,3], k = 10
输出：2
解释：
第一次操作中，我们删除元素 1 和 2 ，然后添加 `1 * 2 + 2` 到 `nums` 中，`nums` 变为 `[4, 11, 10, 3]` 。
第二次操作中，我们删除元素 3 和 4 ，然后添加 `3 * 2 + 4` 到 `nums` 中，`nums` 变为 `[10, 11, 10]` 。
此时，数组中的所有元素都大于等于 10 ，所以我们停止操作。
可以证明使数组中所有元素都大于等于 10 需要的最少操作次数为 2 。

示例 2：

输入：nums = [1,1,2,4,9], k = 20
输出：4
解释：
第一次操作后，`nums` 变为 `[2, 4, 9, 3]`。
第二次操作后，`nums` 变为 `[7, 4, 9]`。
第三次操作后，`nums` 变为 `[15, 9]`。
第四次操作后，`nums` 变为 `[33]`。
此时，`nums` 中的所有元素都大于等于 20 ，所以我们停止操作。
可以证明使数组中所有元素都大于等于 20 需要的最少操作次数为 4 。

提示：
`2 <= nums.length <= 2 * 10^5`
`1 <= nums[i] <= 10^9`
`1 <= k <= 10^9`
输入保证答案一定存在，也就是说，在进行某些次数的操作后，数组中所有元素都大于等于 `k` 。
"""

from typing import List, Optional


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        """
        Use a min-heap. Repeatedly extract two smallest elements x <= y,
        compute new = x * 2 + y, push back, until all elements >= k.
        """
        import heapq

        heapq.heapify(nums)
        ops = 0

        while len(nums) >= 2 and nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            new_val = x * 2 + y
            heapq.heappush(nums, new_val)
            ops += 1

        return ops



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Simulation, Heap (Priority Queue)
#
# 解题思路:
# 使用最小堆模拟操作过程。每次取出最小的两个元素 x 和 y（x <= y），
# 计算新值 x * 2 + y 并放回堆中。重复操作直到堆中所有元素都 >= k 或元素不足两个。
# 每次操作后新值可能变大，但最小堆保证了始终选择最小的两个元素。
#
# 时间复杂度: O(n log n)，每次堆操作 O(log n)，最多操作次数约为 n
# 空间复杂度: O(n)，堆存储
#
# 关键点:
# - 贪心策略：始终合并最小的两个元素（类似哈夫曼编码）
# - 堆保证每次获取最小值的效率
# - 新值 x*2+y 可能比 k 大，但放入堆后不影响继续取最小的两个
