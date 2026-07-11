"""
LeetCode #2762 - Continuous Subarrays
不间断子数组
https://leetcode.cn/problems/continuous-subarrays/

给你一个下标从 0 开始的整数数组 `nums` 。`nums` 的一个子数组如果满足以下条件，那么它是 不间断 的：
`i`，`i + 1` ，...，`j`_  表示子数组中的下标。对于所有满足 `i <= i_1, i_2 <= j` 的下标对，都有 `0 <= |nums[i_1] - nums[i_2]| <= 2` 。
请你返回 不间断 子数组的总数目。
子数组是一个数组中一段连续 非空 的元素序列。

示例 1：
输入：nums = [5,4,2,4] 输出：8 解释： 大小为 1 的不间断子数组：[5], [4], [2], [4] 。 大小为 2 的不间断子数组：[5,4], [4,2], [2,4] 。 大小为 3 的不间断子数组：[4,2,4] 。 没有大小为 4 的不间断子数组。 不间断子数组的总数目为 4 + 3 + 1 = 8 。 除了这些以外，没有别的不间断子数组。
示例 2：
输入：nums = [1,2,3] 输出：6 解释： 大小为 1 的不间断子数组：[1], [2], [3] 。 大小为 2 的不间断子数组：[1,2], [2,3] 。 大小为 3 的不间断子数组：[1,2,3] 。 不间断子数组的总数目为 3 + 2 + 1 = 6 。

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^9`
"""

from typing import List, Optional


from collections import deque

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        max_q = deque()
        min_q = deque()
        left = 0
        for right in range(n):
            while max_q and nums[max_q[-1]] <= nums[right]:
                max_q.pop()
            max_q.append(right)
            while min_q and nums[min_q[-1]] >= nums[right]:
                min_q.pop()
            min_q.append(right)
            while nums[max_q[0]] - nums[min_q[0]] > 2:
                left += 1
                if max_q[0] < left:
                    max_q.popleft()
                if min_q[0] < left:
                    min_q.popleft()
            ans += right - left + 1
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Queue, Array, Ordered Set, Sliding Window, Monotonic Queue, Heap (Priority Queue)
#
# 解题思路:
# 滑动窗口 + 单调队列。维护窗口内最大值和最小值之差不超过 2。
# 使用两个单调队列：max_q 递减存最大值候选，min_q 递增存最小值候选。
# 右指针扩展时更新两个队列，若 max-min > 2 则收缩左指针。
# 以 right 结尾的有效子数组数量 = right - left + 1。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 单调队列分别追踪窗口内的最大值和最小值
# - 当 max - min > 2 时，必须移动 left 直到条件满足
# - 每次以 right 结尾的子数组计数累加到答案
