"""
LeetCode #1014 - Best Sightseeing Pair
中文题名：最佳观光组合
https://leetcode.com/problems/best-sightseeing-pair/

Given an array `A` of positive integers, `A[i]` represents the value of
the `i`-th sightseeing spot, and two sightseeing spots `i` and
`j` have distance `j - i` between them.

The score of a pair (`i < j`) of sightseeing spots is (`A[i]
+ A[j] + i - j)` : the sum of the values of the sightseeing spots,
minus the distance between them.

Return the maximum score of a pair of sightseeing spots.

Example 1:

Input: [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, `A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11`

Note:

`2 <= A.length <= 50000`

`1 <= A[i] <= 1000`

【中文翻译】
给定一个正整数数组 `A`，`A[i]` 表示第 `i` 个观光景点的评分，两个景点 `i` 和 `j` 之间的距离为 `j - i`。

一对景点（`i < j`）的得分为（`A[i] + A[j] + i - j)`）：景点评分之和减去它们之间的距离。

返回一对观光景点能获得的最高分。

示例 1：

输入：[8,1,5,2,6]
输出：11
解释：i = 0, j = 2, `A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11`

注意：

`2 <= A.length <= 50000`

`1 <= A[i] <= 1000`

"""

from typing import List, Optional


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        max_i = A[0]  # A[i] + i for i = 0
        res = 0
        for j in range(1, len(A)):
            res = max(res, max_i + A[j] - j)
            max_i = max(max_i, A[j] + j)
        return res










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 将得分公式 A[i] + A[j] + i - j 拆分为 (A[i] + i) + (A[j] - j)。
# 对于固定的 j，要最大化总分，只需要前面找一个 i < j 使 A[i] + i 最大。
# 遍历数组，维护两个变量：
# - max_i：记录到当前位置之前最大的 A[i] + i 值
# - res：记录全局最大得分
# 对于每个位置 j，用 max_i + A[j] - j 更新 res，然后用 A[j] + j 更新 max_i。
#
# 时间复杂度: O(n) - 一次遍历
# 空间复杂度: O(1) - 只使用两个变量
#
# 关键点:
# - 将公式拆分为 (A[i] + i) + (A[j] - j)，分离 i 和 j 的贡献
# - 遍历同时维护"前 i 个元素中的最大 A[i]+i"，避免 O(n^2) 的双重循环
# - 注意更新顺序：先用旧的 max_i 加上 A[j] - j 更新结果，再更新 max_i
