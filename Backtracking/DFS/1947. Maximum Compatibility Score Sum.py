"""
LeetCode #1947 - Maximum Compatibility Score Sum
最大兼容性评分和
https://leetcode.cn/problems/maximum-compatibility-score-sum/

有一份由 `n` 个问题组成的调查问卷，每个问题的答案要么是 `0`（no，否），要么是 `1`（yes，是）。
这份调查问卷被分发给 `m` 名学生和 `m` 名导师，学生和导师的编号都是从 `0` 到 `m - 1` 。学生的答案用一个二维整数数组 `students` 表示，其中 `students[i]` 是一个整数数组，包含第 `i` 名学生对调查问卷给出的答案（下标从 0 开始）。导师的答案用一个二维整数数组 `mentors` 表示，其中 `mentors[j]` 是一个整数数组，包含第 `j` 名导师对调查问卷给出的答案（下标从 0 开始）。
每个学生都会被分配给 一名 导师，而每位导师也会分配到 一名 学生。配对的学生与导师之间的兼容性评分等于学生和导师答案相同的次数。
例如，学生答案为`[1, 0, 1]` 而导师答案为 `[0, 0, 1]` ，那么他们的兼容性评分为 2 ，因为只有第二个和第三个答案相同。
请你找出最优的学生与导师的配对方案，以 最大程度上 提高 兼容性评分和 。
给你 `students` 和 `mentors` ，返回可以得到的 最大兼容性评分和 。

示例 1：
输入：students = [[1,1,0],[1,0,1],[0,0,1]], mentors = [[1,0,0],[0,0,1],[1,1,0]] 输出：8 解释：按下述方式分配学生和导师： - 学生 0 分配给导师 2 ，兼容性评分为 3 。 - 学生 1 分配给导师 0 ，兼容性评分为 2 。 - 学生 2 分配给导师 1 ，兼容性评分为 3 。 最大兼容性评分和为 3 + 2 + 3 = 8 。
示例 2：
输入：students = [[0,0],[0,0],[0,0]], mentors = [[1,1],[1,1],[1,1]] 输出：0 解释：任意学生与导师配对的兼容性评分都是 0 。

提示：
`m == students.length == mentors.length`
`n == students[i].length == mentors[j].length`
`1 <= m, n <= 8`
`students[i][k]` 为 `0` 或 `1`
`mentors[j][k]` 为 `0` 或 `1`
"""

from typing import List, Optional


class Solution:
    def maxCompatibilitySum(
        self, students: List[List[int]], mentors: List[List[int]]
    ) -> int:
        """
        DP with bitmask: assign mentors to students to maximize total score.
        m <= 8, so 2^m states are feasible.
        """
        m, n = len(students), len(students[0])

        # Precompute compatibility matrix: score[i][j]
        score = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                score[i][j] = sum(
                    1 for k in range(n) if students[i][k] == mentors[j][k]
                )

        # DP[mask] = max score after assigning mentors in `mask` to first k students
        size = 1 << m
        dp = [0] * size

        for mask in range(size):
            i = mask.bit_count()  # number of students already assigned
            if i >= m:
                continue
            for j in range(m):
                if not (mask & (1 << j)):
                    new_mask = mask | (1 << j)
                    dp[new_mask] = max(dp[new_mask], dp[mask] + score[i][j])

        return dp[size - 1]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Array, Dynamic Programming, Backtracking, Bitmask
#
# 解题思路:
# 状态压缩 DP。m <= 8，可以用 bitmask 表示哪些导师已被分配。
# 预处理兼容性矩阵 score[i][j] = 学生 i 和导师 j 的匹配分数。
# dp[mask] = 已分配 mask 中的导师给前 k 个学生时的最大总分。
# 转移：对于每个未分配的导师 j，分配给第 i = popcount(mask) 个学生。
# dp[new_mask] = max(dp[new_mask], dp[mask] + score[i][j])
#
# 时间复杂度: O(M^2 * N + M * 2^M)，其中 M 为学生数
# 空间复杂度: O(2^M)
#
# 关键点:
# - bitmask 表示导师分配状态
# - mask.bit_count() 确定当前分配到第几个学生
# - M <= 8 使得状态空间 2^8 = 256 可行
