"""
LeetCode #2275 - Largest Combination With Bitwise AND Greater Than Zero
按位与结果大于零的最长组合
https://leetcode.cn/problems/largest-combination-with-bitwise-and-greater-than-zero/

对数组 `nums` 执行 按位与 相当于对数组 `nums` 中的所有整数执行 按位与 。
例如，对 `nums = [1, 5, 3]` 来说，按位与等于 `1 & 5 & 3 = 1` 。
同样，对 `nums = [7]` 而言，按位与等于 `7` 。
给你一个正整数数组 `candidates` 。计算 `candidates` 中的数字每种组合下 按位与 的结果。
返回按位与结果大于 `0` 的 最长 组合的长度。

示例 1：
输入：candidates = [16,17,71,62,12,24,14] 输出：4 解释：组合 [16,17,62,24] 的按位与结果是 16 & 17 & 62 & 24 = 16 > 0 。 组合长度是 4 。 可以证明不存在按位与结果大于 0 且长度大于 4 的组合。 注意，符合长度最大的组合可能不止一种。 例如，组合 [62,12,24,14] 的按位与结果是 62 & 12 & 24 & 14 = 8 > 0 。
示例 2：
输入：candidates = [8,8] 输出：2 解释：最长组合是 [8,8] ，按位与结果 8 & 8 = 8 > 0 。 组合长度是 2 ，所以返回 2 。

提示：
`1 <= candidates.length <= 10^5`
`1 <= candidates[i] <= 10^7`
"""

from typing import List, Optional


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        """
        Return the size of the largest combination with bitwise AND > 0.

        For the bitwise AND of a group to be > 0, there must be at least one
        bit position where EVERY number in the group has a 1. So the answer
        is the maximum count of numbers that have a 1 at any given bit position.
        """
        # Count how many numbers set each bit (up to 24 bits since max value is 10^7 < 2^24)
        ans = 0
        for bit in range(24):
            cnt = 0
            for num in candidates:
                if num & (1 << bit):
                    cnt += 1
            ans = max(ans, cnt)
        return ans


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Array, Hash Table, Counting
#
# 解题思路:
# 对于一个组合的按位与结果 > 0，意味着存在至少一个二进制位，在该位上组合中所有数字
# 都是 1。因此，我们不需要枚举所有组合，只需要统计在每个二进制位上，有多少个数字的
# 该位是 1。对于第 k 位，如果 cnt_k 个数字在该位是 1，那么这 cnt_k 个数字的任意
# 子集的按位与结果在该位上仍然是 1，因此它们可以构成一个按位与大于 0 的组合。
# 最大值就是 max(cnt_k) for all k。
#
# 时间复杂度: O(24 * N) = O(N)，N 为 candidates 长度。candidates[i] <= 10^7 < 2^24，
# 最多检查 24 位。
# 空间复杂度: O(1)，仅使用常数空间。
#
# 关键点:
# - 按位与结果 > 0 等价于存在某个二进制位所有数字在该位上都是 1
# - 不需要枚举组合，只需要统计每个位上 1 的个数
# - candidates[i] <= 10^7 < 2^24，所以只需检查 24 位
# - 每一位之间的计数是独立的，取最大值即可
