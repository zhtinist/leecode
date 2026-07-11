"""
LeetCode #2294 - Partition Array Such That Maximum Difference Is K
划分数组使最大差为 K
https://leetcode.cn/problems/partition-array-such-that-maximum-difference-is-k/

给你一个整数数组 `nums` 和一个整数 `k` 。你可以将 `nums` 划分成一个或多个 子序列 ，使 `nums` 中的每个元素都 恰好 出现在一个子序列中。
在满足每个子序列中最大值和最小值之间的差值最多为 `k` 的前提下，返回需要划分的 最少 子序列数目。
子序列 本质是一个序列，可以通过删除另一个序列中的某些元素（或者不删除）但不改变剩下元素的顺序得到。

示例 1：
输入：nums = [3,6,1,2,5], k = 2 输出：2 解释： 可以将 nums 划分为两个子序列 [3,1,2] 和 [6,5] 。 第一个子序列中最大值和最小值的差值是 3 - 1 = 2 。 第二个子序列中最大值和最小值的差值是 6 - 5 = 1 。 由于创建了两个子序列，返回 2 。可以证明需要划分的最少子序列数目就是 2 。
示例 2：
输入：nums = [1,2,3], k = 1 输出：2 解释： 可以将 nums 划分为两个子序列 [1,2] 和 [3] 。 第一个子序列中最大值和最小值的差值是 2 - 1 = 1 。 第二个子序列中最大值和最小值的差值是 3 - 3 = 0 。 由于创建了两个子序列，返回 2 。注意，另一种最优解法是将 nums 划分成子序列 [1] 和 [2,3] 。
示例 3：
输入：nums = [2,2,4,5], k = 0 输出：3 解释： 可以将 nums 划分为三个子序列 [2,2]、[4] 和 [5] 。 第一个子序列中最大值和最小值的差值是 2 - 2 = 0 。 第二个子序列中最大值和最小值的差值是 4 - 4 = 0 。 第三个子序列中最大值和最小值的差值是 5 - 5 = 0 。 由于创建了三个子序列，返回 3 。可以证明需要划分的最少子序列数目就是 3 。

提示：
`1 <= nums.length <= 10^5`
`0 <= nums[i] <= 10^5`
`0 <= k <= 10^5`
"""

from typing import List, Optional


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        """
        Sort the array and greedily group elements into subsequences. Start a
        new subsequence when the current element exceeds min_of_group + k.
        The number of groups is the minimum number of subsequences needed.
        """
        nums.sort()

        count = 0
        i = 0
        n = len(nums)

        while i < n:
            count += 1
            group_min = nums[i]

            # Include all elements within [group_min, group_min + k]
            while i < n and nums[i] <= group_min + k:
                i += 1

        return count


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Sorting
#
# 解题思路:
# 1. 子序列不要求保持原数组顺序，因此可以先将数组排序。
# 2. 排序后，贪心地将相邻元素分组：从一个新的子序列开始，以当前未分配的最小元素作为该
#    子序列的起点（最小值），然后尽可能多地包含后续元素，只要它们不超过 min + k。
# 3. 当遇到一个元素 > min + k 时，必须开启一个新的子序列，计数器加 1。
# 4. 这样贪心得到的分组数就是最少子序列数。
#
# 时间复杂度: O(N log N)，主要由排序决定
# 空间复杂度: O(1) 或 O(N)（取决于排序算法是否原地）
#
# 关键点:
# - 关键观察：子序列不要求保持原顺序，所以排序不会破坏解的可行性
# - 贪心策略：每次从剩余最小元素开始，尽可能多地纳入元素，直到差值超过 k
# - 排序简化了问题：排序后只需线性扫描组队
# - 无需实际分配元素到具体的子序列，只需统计需要多少组
