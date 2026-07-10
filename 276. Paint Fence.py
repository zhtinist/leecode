"""
LeetCode #276 - Paint Fence
https://leetcode.com/problems/paint-fence/

There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same
color.

Return the total number of ways you can paint the fence.

Note:

n and k are non-negative integers.

Example:

Input: n = 3, k = 2
Output: 6
Explanation: Take c1 as color 1, c2 as color 2. All possible ways are:

post1  post2  post3
-----      -----  -----  -----
1         c1     c1     c2
2         c1     c2     c1
3         c1     c2     c2
4         c2     c1     c1
5         c2     c1     c2
6         c2     c2     c1
"""

from typing import List, Optional


class Solution:
    def numWays(self, n: int, k: int) -> int:
        """Return number of ways to paint fence with n posts using k colors.
        Constraint: no more than 2 adjacent posts can have the same color.

        DP with two states:
        - same[i]: ways to paint first i posts where post i has SAME color as post i-1
        - diff[i]: ways to paint first i posts where post i has DIFFERENT color from post i-1

        Recurrence:
        - same[i] = diff[i-1]  (must be different from i-2, so same as i-1)
        - diff[i] = (same[i-1] + diff[i-1]) * (k - 1)
        Total = same[n-1] + diff[n-1]
        """
        if n == 0:
            return 0
        if n == 1:
            return k

        same = k          # post 0 and post 1 same color
        diff = k * (k - 1)  # post 0 and post 1 different color

        for i in range(2, n):
            new_same = diff
            new_diff = (same + diff) * (k - 1)
            same, diff = new_same, new_diff

        return same + diff


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: Yes
#
# 解题思路:
# 动态规划。定义两个状态：
# - same[i]: 前 i 个柱子涂完且第 i 个柱子与第 i-1 个颜色相同的方案数
# - diff[i]: 前 i 个柱子涂完且第 i 个柱子与第 i-1 个颜色不同的方案数
#
# 状态转移：
# - same[i] = diff[i-1]（只有当 i-1 与 i-2 颜色不同时，i 才能与 i-1 同色）
# - diff[i] = (same[i-1] + diff[i-1]) * (k-1)（无论 i-1 与 i-2 关系如何，
#   i 都有 k-1 种不同于 i-1 的选择）
# 最终答案 = same[n-1] + diff[n-1]
#
# 时间复杂度: O(N) - 一次遍历
# 空间复杂度: O(1) - 只使用常数个变量
#
# 关键点:
# - 核心限制：不能有连续三个柱子同色
# - DP 的两个状态定义是关键
# - same[i] 只能从 diff[i-1] 转移来
# - diff[i] 可以从两种状态都转移来
