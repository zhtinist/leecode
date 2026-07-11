"""
LeetCode #1424 - Diagonal Traverse II
中文题名：对角线遍历 II
https://leetcode.com/problems/diagonal-traverse-ii/

Given a list of lists of integers, `nums`, return all elements of
`nums` in diagonal order as shown in the below images.

Example 1:

Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]

Example 2:

Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]

Example 3:

Input: nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
Output: [1,4,2,5,3,8,6,9,7,10,11]

Example 4:

Input: nums = [[1,2,3,4,5,6]]
Output: [1,2,3,4,5,6]

Constraints:

`1 <= nums.length <= 10^5`

`1 <= nums[i].length <= 10^5`

`1 <= nums[i][j] <= 10^9`

There at most `10^5` elements in `nums`.

【中文翻译】

给定一个整数列表的列表 `nums`，按对角线顺序返回 `nums` 中的所有元素，如下方图片所示。

示例 1：
输入：nums = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,4,2,7,5,3,8,6,9]

示例 2：
输入：nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
输出：[1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]

示例 3：
输入：nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
输出：[1,4,2,5,3,8,6,9,7,10,11]

示例 4：
输入：nums = [[1,2,3,4,5,6]]
输出：[1,2,3,4,5,6]

约束条件：
`1 <= nums.length <= 10^5`
`1 <= nums[i].length <= 10^5`
`1 <= nums[i][j] <= 10^9`
`nums` 中最多有 `10^5` 个元素。

"""

from typing import List, Optional
from collections import defaultdict


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        # 按对角线分组：同一对角线上的元素满足 row + col 相同
        diagonals = defaultdict(list)

        for row in range(len(nums)):
            for col in range(len(nums[row])):
                diagonals[row + col].append(nums[row][col])

        result = []
        # 按对角线和从小到大处理
        for diag_sum in sorted(diagonals.keys()):
            # 同一条对角线上，从底部到顶部（行号从大到小）
            # 因为我们是从上到下遍历行的，所以列表中的顺序是从小行到大行
            # 需要反转以得到从底部到顶部的顺序
            result.extend(reversed(diagonals[diag_sum]))

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 对角线分组法（哈希表 + 排序）：
# 1. 关键观察：在同一条对角线上的所有元素，其 (行号 + 列号) 是相同的。
#    因此可以用 row + col 作为键进行分组。
# 2. 遍历整个二维列表（不规则矩阵），对每个元素计算 row + col，
#    将其值加入对应的对角线分组列表中。
#    注意：由于我们是按行从上到下遍历的，每个对角线分组中的元素
#    已经按行号递增排列。
# 3. 将所有对角线和（diag_sum）从小到大排序。
# 4. 对于每个对角线和，其对应的分组元素需要从底部到顶部输出，
#    即行号大的先输出。由于分组中元素是按行号递增排列的，
#    直接反转（reversed）即可得到从底到顶的顺序。
# 5. 将所有处理后的元素依次加入结果数组。
#
# 时间复杂度: O(N log N)，其中 N 是总元素数。虽然遍历矩阵是 O(N)，
#             但对角线和排序在最坏情况下是 O(N log N)
#            （每个元素可能在单独的对角线上，但实际最多 m+n 条对角线）。
#             可以优化为 O(N) 通过预先生成足够大的数组。
# 空间复杂度: O(N)，存储所有元素。
#
# 关键点:
# - 对角线由 row + col 相同来定义
# - 同一对角线内，按行号从大到小输出（自底向上）
# - 不规则矩阵：每行长度可能不同










