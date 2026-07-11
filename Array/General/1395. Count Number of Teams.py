"""
LeetCode #1395 - Count Number of Teams
中文题名：统计作战单位数
https://leetcode.com/problems/count-number-of-teams/

There are `n` soldiers standing in a line. Each soldier is
assigned a unique `rating` value.

You have to form a team of 3 soldiers amongst them under the following
rules:

Choose 3 soldiers with index (`i`, `j`, `k`)
with rating (`rating[i]`, `rating[j]`, `rating[k]`).

A team is valid if:  (`rating[i] < rating[j] < rating[k]`)
or (`rating[i] > rating[j] > rating[k]`) where (`0 <=
i < j < k < n`).

Return the number of teams you can form given the conditions. (soldiers can be part
of multiple teams).

Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1).

Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.

Example 3:

Input: rating = [1,2,3,4]
Output: 4

Constraints:

`n == rating.length`

`1 <= n <= 200`

`1 <= rating[i] <= 10^5`

【中文翻译】

有 n 名士兵站成一排。每名士兵有一个独一无二的评价值 rating。

你需要按以下规则组建一个三人小队：
选择 3 名士兵，索引为 (i, j, k)，评价值为 (rating[i], rating[j], rating[k])。
一个小队有效当且仅当：(rating[i] < rating[j] < rating[k]) 或 (rating[i] > rating[j] > rating[k])（其中 0 <= i < j < k < n）。

返回在给定条件下可以组建的小队数量（士兵可以属于多个小队）。

示例 1：
输入：rating = [2,5,3,4,1]
输出：3
解释：可以组建三个满足条件的小队：(2,3,4), (5,4,1), (5,3,1)。

示例 2：
输入：rating = [2,1,3]
输出：0
解释：无法组建任何满足条件的小队。

示例 3：
输入：rating = [1,2,3,4]
输出：4

约束条件：
n == rating.length
1 <= n <= 200
1 <= rating[i] <= 10^5
"""

from typing import List, Optional


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        total = 0

        for j in range(n):
            left_smaller = left_larger = 0
            right_smaller = right_larger = 0

            # 统计左侧
            for i in range(j):
                if rating[i] < rating[j]:
                    left_smaller += 1
                elif rating[i] > rating[j]:
                    left_larger += 1

            # 统计右侧
            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    right_smaller += 1
                elif rating[k] > rating[j]:
                    right_larger += 1

            # 以 j 为中间元素的小队数
            total += left_smaller * right_larger  # 递增序列
            total += left_larger * right_smaller  # 递减序列

        return total



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 以每个士兵作为中间元素（索引 j），计算：
# - 左侧比 rating[j] 小的数量（left_smaller）和大的数量（left_larger）
# - 右侧比 rating[j] 小的数量（right_smaller）和大的数量（right_larger）
# 以 j 为中间的递增小队数 = left_smaller * right_larger
# 以 j 为中间的递减小队数 = left_larger * right_smaller
# 累加所有 j 的贡献即可。
#
# 时间复杂度: O(N^2)  对每个中间元素扫描左右两侧
# 空间复杂度: O(1)  只使用常数个变量
#
# 关键点:
# - 固定中间元素是简化问题的关键思路
# - 不需要具体的 i 和 k 的值，只需要知道有多少个比中间大/小的数
# - 排列组合：左侧选一个、右侧选一个的乘法原理










