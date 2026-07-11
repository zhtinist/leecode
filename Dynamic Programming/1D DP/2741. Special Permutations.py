"""
LeetCode #2741 - Special Permutations
特别的排列
https://leetcode.cn/problems/special-permutations/

给你一个下标从 0 开始的整数数组 `nums` ，它包含 `n` 个 互不相同 的正整数。如果 `nums` 的一个排列满足以下条件，我们称它是一个特别的排列：
对于 `0 <= i < n - 1` 的下标 `i` ，要么 `nums[i] % nums[i+1] == 0` ，要么 `nums[i+1] % nums[i] == 0` 。
请你返回特别排列的总数目，由于答案可能很大，请将它对 `10^9 + 7` 取余 后返回。

示例 1：
输入：nums = [2,3,6] 输出：2 解释：[3,6,2] 和 [2,6,3] 是 nums 两个特别的排列。
示例 2：
输入：nums = [1,4,3] 输出：2 解释：[3,1,4] 和 [4,1,3] 是 nums 两个特别的排列。

提示：
`2 <= nums.length <= 14`
`1 <= nums[i] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        full_mask = (1 << n) - 1

        dp = [[0] * n for _ in range(1 << n)]
        for i in range(n):
            dp[1 << i][i] = 1

        for mask in range(1 << n):
            for last in range(n):
                if dp[mask][last] == 0:
                    continue
                for nxt in range(n):
                    if mask & (1 << nxt):
                        continue
                    if nums[last] % nums[nxt] == 0 or nums[nxt] % nums[last] == 0:
                        new_mask = mask | (1 << nxt)
                        dp[new_mask][nxt] = (dp[new_mask][nxt] + dp[mask][last]) % MOD

        ans = 0
        for last in range(n):
            ans = (ans + dp[full_mask][last]) % MOD
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Array, Dynamic Programming, Bitmask
#
# 解题思路:
# 状态压缩 DP。dp[mask][last] 表示已使用 mask 表示的元素集合、最后放置的元素是 last 的排列数。
# 初始化：每个单独元素作为一种排列的起点。
# 转移：枚举下一个可以放置的元素 nxt（未使用且与 last 满足整除关系）。
# 最终答案为 sum(dp[full_mask][last]) 对所有可能的 last。
#
# 时间复杂度: O(2^n * n^2)，其中 n <= 14
# 空间复杂度: O(2^n * n)
#
# 关键点:
# - n <= 14 提示使用状态压缩 DP（2^14 = 16384）
# - dp[mask][last] 记录"以 last 结尾"的排列数，便于判断下一个元素是否满足整除条件
# - 两层循环枚举 mask 和 last，内层枚举下一个元素 nxt
