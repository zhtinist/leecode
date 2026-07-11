"""
LeetCode #2679 - Sum in a Matrix
矩阵中的和
https://leetcode.cn/problems/sum-in-a-matrix/

给你一个下标从 0 开始的二维整数数组 `nums` 。一开始你的分数为 `0` 。你需要执行以下操作直到矩阵变为空：
矩阵中每一行选取最大的一个数，并删除它。如果一行中有多个最大的数，选择任意一个并删除。
在步骤 1 删除的所有数字中找到最大的一个数字，将它添加到你的 分数 中。
请你返回最后的 分数 。

示例 1：
输入：nums = [[7,2,1],[6,4,2],[6,5,3],[3,2,1]] 输出：15 解释：第一步操作中，我们删除 7 ，6 ，6 和 3 ，将分数增加 7 。下一步操作中，删除 2 ，4 ，5 和 2 ，将分数增加 5 。最后删除 1 ，2 ，3 和 1 ，将分数增加 3 。所以总得分为 7 + 5 + 3 = 15 。
示例 2：
输入：nums = [[1]] 输出：1 解释：我们删除 1 并将分数增加 1 ，所以返回 1 。

提示：
`1 <= nums.length <= 300`
`1 <= nums[i].length <= 500`
`0 <= nums[i][j] <= 10^3`
"""

from typing import List, Optional


class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        # sort each row in descending order
        for row in nums:
            row.sort(reverse=True)

        m, n = len(nums), len(nums[0])
        score = 0
        for col in range(n):
            max_in_col = max(nums[row][col] for row in range(m))
            score += max_in_col

        return score



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Matrix, Sorting, Simulation, Heap (Priority Queue)
#
# 解题思路:
# 将每一行降序排序。模拟操作过程：每次从每行取最大的数，将所有行的最大数中再取最大加到分数。
# 由于行已排序，第j次操作取的是每行的第j大元素。因此遍历每列，取该列的最大值累加即可。
#
# 时间复杂度: O(m * n log n)
# 空间复杂度: O(1)
#
# 关键点:
# - 排序后，第j次操作选择每行第j大的数
# - 每次操作加的分数 = 各列的最大值
# - 不必真正模拟删除过程，排序后每列独立
