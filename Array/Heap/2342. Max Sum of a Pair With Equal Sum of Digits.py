"""
LeetCode #2342 - Max Sum of a Pair With Equal Sum of Digits
数位和相等数对的最大和
https://leetcode.cn/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

给你一个下标从 0 开始的数组 `nums` ，数组中的元素都是 正 整数。请你选出两个下标 `i` 和 `j`（`i != j`），且 `nums[i]` 的数位和 与  `nums[j]` 的数位和相等。
请你找出所有满足条件的下标 `i` 和 `j` ，找出并返回 `nums[i] + nums[j]` 可以得到的 最大值。如果不存在这样的下标对，返回 -1。

示例 1：
输入：nums = [18,43,36,13,7] 输出：54 解释：满足条件的数对 (i, j) 为： - (0, 2) ，两个数字的数位和都是 9 ，相加得到 18 + 36 = 54 。 - (1, 4) ，两个数字的数位和都是 7 ，相加得到 43 + 7 = 50 。 所以可以获得的最大和是 54 。
示例 2：
输入：nums = [10,12,19,14] 输出：-1 解释：不存在满足条件的数对，返回 -1 。

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        """
        For each number, compute its digit sum.
        Use a hash map to track the maximum number seen so far for each digit sum.
        When we encounter a number whose digit sum we've seen before,
        we can form a pair with the stored maximum, updating the global answer.
        """
        def digit_sum(n: int) -> int:
            s = 0
            while n:
                s += n % 10
                n //= 10
            return s

        best = {}  # digit_sum -> max number seen so far
        ans = -1

        for num in nums:
            ds = digit_sum(num)
            if ds in best:
                ans = max(ans, best[ds] + num)
                best[ds] = max(best[ds], num)
            else:
                best[ds] = num

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Sorting, Heap (Priority Queue)
#
# 解题思路:
# 1. 定义一个辅助函数计算数字的数位和（各位数字之和）。
# 2. 使用哈希表 best 记录当前已遍历元素中，每个数位和对应的最大元素值。
# 3. 遍历数组 nums：
#    - 计算当前数字的数位和 ds
#    - 若 ds 已在 best 中，则当前数字与 best[ds] 构成一个有效数对，
#      用 best[ds] + num 更新全局最大和 ans，并更新 best[ds] 为更大值
#    - 若 ds 尚未出现，将当前数字存入 best
# 4. 若遍历结束 ans 仍为 -1，说明不存在满足条件的数对。
#
# 时间复杂度: O(n * log M) — 其中 n 为数组长度，log M 为数位和计算的复杂度
#   （M 最大为 10^9，最多 10 位数，可视为常数）
# 空间复杂度: O(n) — 哈希表最多存储 n 个不同的数位和
#
# 关键点:
# - 只需要保留每个数位和对应的最大值即可贪心地得到最大和
# - 对于同一数位和有多个数字的情况，只需保留最大的一个与当前数字配对
# - 数位和计算通过取模和整除即可，无需转换为字符串
