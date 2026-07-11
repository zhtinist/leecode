"""
LeetCode #3290 - Maximum Multiplication Score
最高乘法得分
https://leetcode.cn/problems/maximum-multiplication-score/

给你一个大小为 4 的整数数组 `a` 和一个大小 至少为 4 的整数数组 `b`。
你需要从数组 `b` 中选择四个下标 `i_0`, `i_1`, `i_2`, 和 `i_3`，并满足 `i_0 < i_1 < i_2 < i_3`。你的得分将是 `a[0] * b[i_0] + a[1] * b[i_1] + a[2] * b[i_2] + a[3] * b[i_3]` 的值。
返回你能够获得的 最大 得分。

示例 1：

输入： a = [3,2,5,6], b = [2,-6,4,-5,-3,2,-7]
输出： 26
解释：
选择下标 0, 1, 2 和 5。得分为 `3 * 2 + 2 * (-6) + 5 * 4 + 6 * 2 = 26`。
示例 2：

输入： a = [-1,4,5,-2], b = [-5,-1,-3,-2,-4]
输出： -1
解释：
选择下标 0, 1, 3 和 4。得分为 `(-1) * (-5) + 4 * (-1) + 5 * (-2) + (-2) * (-4) = -1`。

提示：
`a.length == 4`
`4 <= b.length <= 10^5`
`-10^5 <= a[i], b[i] <= 10^5`
"""

from typing import List, Optional


class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        n = len(b)
        # dp[j] = 选择 j 个元素（0-indexed: j=0..3）后的最大得分
        dp = [float('-inf')] * 4
        for x in b:
            # 从后往前更新，避免覆盖
            for j in range(3, 0, -1):
                if dp[j-1] != float('-inf'):
                    dp[j] = max(dp[j], dp[j-1] + a[j] * x)
            dp[0] = max(dp[0], a[0] * x)
        return dp[3]










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Dynamic Programming
#
# 解题思路:
# 从 b 中选 4 个递增下标 i0<i1<i2<i3，最大化 sum(a[j] * b[ij])。
# DP：dp[j] = 选择了前 j+1 个元素（匹配 a[0..j]）后的最大得分。
# 遍历 b 中每个元素 x，尝试用它来匹配 a[j]：
# dp[j] = max(dp[j], dp[j-1] + a[j] * x)  （j > 0）
# dp[0] = max(dp[0], a[0] * x)
# 从后向前更新避免同一元素被重复使用。
# 最终答案 = dp[3]。
#
# 时间复杂度: O(n) — n = len(b)
# 空间复杂度: O(1)
#
# 关键点:
# - 类似于 LIS 的 DP 思路，固定长度选择
# - 从后向前更新 dp 数组避免覆盖
