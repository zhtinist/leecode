"""
LeetCode #2542 - Maximum Subsequence Score
最大子序列的分数
https://leetcode.cn/problems/maximum-subsequence-score/

给你两个下标从 0 开始的整数数组 `nums1` 和 `nums2` ，两者长度都是 `n` ，再给你一个正整数 `k` 。你必须从 `nums1` 中选一个长度为 `k` 的 子序列 对应的下标。
对于选择的下标 `i_0` ，`i_1` ，...， `i_k - 1` ，你的 分数 定义如下：
`nums1` 中下标对应元素求和，乘以 `nums2` 中下标对应元素的 最小值 。
用公式表示： `(nums1[i_0] + nums1[i_1] +...+ nums1[i_k - 1]) * min(nums2[i_0] , nums2[i_1], ... ,nums2[i_k - 1])` 。
请你返回 最大 可能的分数。
一个数组的 子序列 下标是集合 `{0, 1, ..., n-1}` 中删除若干元素得到的剩余集合，也可以不删除任何元素。

示例 1：
输入：nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3 输出：12 解释： 四个可能的子序列分数为： - 选择下标 0 ，1 和 2 ，得到分数 (1+3+3) * min(2,1,3) = 7 。 - 选择下标 0 ，1 和 3 ，得到分数 (1+3+2) * min(2,1,4) = 6 。 - 选择下标 0 ，2 和 3 ，得到分数 (1+3+2) * min(2,3,4) = 12 。 - 选择下标 1 ，2 和 3 ，得到分数 (3+3+2) * min(1,3,4) = 8 。 所以最大分数为 12 。
示例 2：
输入：nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1 输出：30 解释： 选择下标 2 最优：nums1[2] * nums2[2] = 3 * 10 = 30 是最大可能分数。

提示：
`n == nums1.length == nums2.length`
`1 <= n <= 10^5`
`0 <= nums1[i], nums2[j] <= 10^5`
`1 <= k <= n`
"""

from typing import List, Optional


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        import heapq
        pairs = list(zip(nums2, nums1))
        pairs.sort(reverse=True)  # sort by nums2 descending

        heap = []
        cur_sum = 0
        ans = 0

        for n2, n1 in pairs:
            heapq.heappush(heap, n1)
            cur_sum += n1
            if len(heap) > k:
                cur_sum -= heapq.heappop(heap)
            if len(heap) == k:
                ans = max(ans, cur_sum * n2)

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Sorting, Heap (Priority Queue)
#
# 解题思路:
# 将nums1和nums2配对后按nums2降序排序。遍历时，当前元素的nums2作为子序列的最小值的候选。
# 用最小堆维护已选的k个最大的nums1值和。当堆满k个时，用cur_sum * n2更新答案。
# 排序保证n2是从大到小遍历的，堆保证cur_sum是当前可选的最大k个nums1之和。
#
# 时间复杂度: O(N log N)
# 空间复杂度: O(N)
#
# 关键点:
# - 按nums2降序排序后，当前n2自动成为子序列的最小值
# - 最小堆维护最大的k个nums1值，超过k时弹出最小的
# - 遍历完所有元素后找到全局最大值
