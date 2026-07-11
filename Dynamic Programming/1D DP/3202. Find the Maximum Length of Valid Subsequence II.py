"""
LeetCode #3202 - Find the Maximum Length of Valid Subsequence II
找出有效子序列的最大长度 II
https://leetcode.cn/problems/find-the-maximum-length-of-valid-subsequence-ii/

给你一个整数数组 `nums` 和一个 正 整数 `k` 。
`nums` 的一个 子序列 `sub` 的长度为 `x` ，如果其满足以下条件，则称其为 有效子序列 ：
`(sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k`  返回 `nums` 的 最长有效子序列 的长度。

示例 1：

输入：nums = [1,2,3,4,5], k = 2
输出：5
解释：
最长有效子序列是 `[1, 2, 3, 4, 5]` 。
示例 2：

输入：nums = [1,4,2,3,1,4], k = 3
输出：4
解释：
最长有效子序列是 `[1, 4, 1, 4]` 。

提示：
`2 <= nums.length <= 10^3`
`1 <= nums[i] <= 10^7`
`1 <= k <= 10^3`
"""

from typing import List, Optional


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # dp[r] = 以余数 r 结尾的最长有效子序列长度
        # 对所有可能的 m (目标和 % k) 取最大值
        ans = 0
        for m in range(k):
            dp = [0] * k
            for x in nums:
                r = x % k
                prev = (m - r) % k
                # 可以从 prev 结尾的子序列扩展
                dp[r] = max(dp[r], dp[prev] + 1)
            ans = max(ans, max(dp))
        return ans










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Dynamic Programming
#
# 解题思路:
# 条件 (sub[i] + sub[i+1]) % k = m（常数），意味着相邻元素的余数必须满足：
# (r_i + r_{i+1}) % k = m，即 r_{i+1} = (m - r_i) % k
# 因此对于固定的 m，余数序列完全由第一个元素的余数决定，且会在两个余数之间交替。
# 枚举所有可能的 m (0 到 k-1)，对每个 m 用 DP 求解：
# dp[r] = 以余数 r 结尾的最长有效子序列长度
# 对于每个数 x（余数 r），可以从 prev = (m - r) % k 转移过来。
#
# 时间复杂度: O(n * k)
# 空间复杂度: O(k)
#
# 关键点:
# - n 和 k 都 <= 1000，O(n*k) 可行
# - 枚举所有目标和 m，对每个 m 做一次线性 DP
