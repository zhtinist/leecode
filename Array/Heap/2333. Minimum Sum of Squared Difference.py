"""
LeetCode #2333 - Minimum Sum of Squared Difference
最小差值平方和
https://leetcode.cn/problems/minimum-sum-of-squared-difference/

给你两个下标从 0 开始的整数数组 `nums1` 和 `nums2` ，长度为 `n` 。
数组 `nums1` 和 `nums2` 的 差值平方和 定义为所有满足 `0 <= i < n` 的 `(nums1[i] - nums2[i])^2` 之和。
同时给你两个正整数 `k1` 和 `k2` 。你可以将 `nums1` 中的任意元素 `+1` 或者 `-1` 至多 `k1` 次。类似的，你可以将 `nums2` 中的任意元素 `+1` 或者 `-1` 至多 `k2` 次。
请你返回修改数组 `nums1` 至多 `k1` 次且修改数组 `nums2` 至多 `k2` 次后的最小 差值平方和 。
注意：你可以将数组中的元素变成 负 整数。

示例 1：
输入：nums1 = [1,2,3,4], nums2 = [2,10,20,19], k1 = 0, k2 = 0 输出：579 解释：nums1 和 nums2 中的元素不能修改，因为 k1 = 0 和 k2 = 0 。 差值平方和为：(1 - 2)^2 + (2 - 10)^2 + (3 - 20)^2 + (4 - 19)^2 = 579 。
示例 2：
输入：nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1 输出：43 解释：一种得到最小差值平方和的方式为： - 将 nums1[0] 增加一次。 - 将 nums2[2] 增加一次。 最小差值平方和为： (2 - 5)^2 + (4 - 8)^2 + (10 - 7)^2 + (12 - 9)^2 = 43 。 注意，也有其他方式可以得到最小差值平方和，但没有得到比 43 更小答案的方案。

提示：
`n == nums1.length == nums2.length`
`1 <= n <= 10^5`
`0 <= nums1[i], nums2[i] <= 10^5`
`0 <= k1, k2 <= 10^9`
"""

from typing import List, Optional


class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        """
        First, compute the absolute differences between corresponding elements.
        Since modifying nums1[i] by +1/-1 is equivalent to modifying nums2[i] by
        -1/+1 in terms of reducing the difference, we can combine k1 + k2 into
        a single budget k of total operations.

        Key insight: reducing a large difference by 1 reduces the squared sum
        more than reducing a small difference by 1. So we want to level down
        the largest differences first.

        Approach: binary search on the target maximum difference (threshold).
        Find the smallest T such that we can reduce all differences to at most T
        using at most k operations. Then apply remaining operations to reduce
        some threshold-level differences to T-1.
        """
        diffs = [abs(nums1[i] - nums2[i]) for i in range(len(nums1))]
        k = k1 + k2

        # Binary search for the minimum achievable threshold
        lo, hi = 0, max(diffs)
        while lo < hi:
            mid = (lo + hi) // 2
            ops_needed = 0
            for d in diffs:
                if d > mid:
                    ops_needed += d - mid
            if ops_needed <= k:
                hi = mid
            else:
                lo = mid + 1

        threshold = lo

        # Reduce all differences exceeding threshold down to threshold
        for i in range(len(diffs)):
            if diffs[i] > threshold:
                reduction = diffs[i] - threshold
                k -= reduction
                diffs[i] = threshold

        # Apply any remaining operations: each reduces one threshold diff by 1
        for i in range(len(diffs)):
            if k > 0 and diffs[i] > 0 and diffs[i] == threshold:
                diffs[i] -= 1
                k -= 1

        return sum(d * d for d in diffs)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Binary Search, Sorting, Heap (Priority Queue)
#
# 解题思路:
# 1. 计算每对 nums1[i] 和 nums2[i] 的绝对差值 diffs[i]。
#    对 nums1 或 nums2 的任意修改都可以减少差值，因此总操作次数 k = k1 + k2。
# 2. 核心贪心思想：减少较大的差值能比减少较小的差值更多地降低平方和。
#    因此我们应该优先削减最大的差值，将所有差值"削平"到某个阈值。
# 3. 使用二分查找确定最小阈值 T，使得将所有大于 T 的差值降至 T 所需
#    操作次数不超过 k。
# 4. 将所有大于阈值的差值降至阈值，然后利用剩余操作次数将部分阈值级别
#    的差值再减 1。
#
# 时间复杂度: O(n log M) — 其中 M = max(diffs)，二分查找每次 O(n) 检查可行性
# 空间复杂度: O(n) — 存储差值数组
#
# 关键点:
# - k1 和 k2 可以合并为总操作次数 k，因为修改 nums1 或 nums2 对减小差值效果相同
# - 平方函数的凸性决定了优先削减大差值的贪心策略是最优的
# - 二分查找阈值后需处理剩余操作次数，将部分阈值级差值再减 1
# - 差值不能小于 0
