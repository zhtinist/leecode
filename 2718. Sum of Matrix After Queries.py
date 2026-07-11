"""
LeetCode #2718 - Sum of Matrix After Queries
查询后矩阵的和
https://leetcode.cn/problems/sum-of-matrix-after-queries/

给你一个整数 `n` 和一个下标从 0 开始的 二维数组 `queries` ，其中 `queries[i] = [type_i, index_i, val_i]` 。
一开始，给你一个下标从 0 开始的 `n x n` 矩阵，所有元素均为 `0` 。每一个查询，你需要执行以下操作之一：
如果 `type_i == 0` ，将第 `index_i` 行的元素全部修改为 `val_i` ，覆盖任何之前的值。
如果 `type_i == 1` ，将第 `index_i` 列的元素全部修改为 `val_i` ，覆盖任何之前的值。
请你执行完所有查询以后，返回矩阵中所有整数的和。

示例 1：

输入：n = 3, queries = [[0,0,1],[1,2,2],[0,2,3],[1,0,4]] 输出：23 解释：上图展示了每个查询以后矩阵的值。所有操作执行完以后，矩阵元素之和为 23 。
示例 2：

输入：n = 3, queries = [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]] 输出：17 解释：上图展示了每一个查询操作之后的矩阵。所有操作执行完以后，矩阵元素之和为 17 。

提示：
`1 <= n <= 10^4`
`1 <= queries.length <= 5 * 10^4`
`queries[i].length == 3`
`0 <= type_i <= 1`
`0 <= index_i < n`
`0 <= val_i <= 10^5`
"""

from typing import List, Optional


class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        row_seen = set()
        col_seen = set()
        ans = 0
        for type_i, index_i, val_i in reversed(queries):
            if type_i == 0:
                if index_i not in row_seen:
                    row_seen.add(index_i)
                    ans += val_i * (n - len(col_seen))
            else:
                if index_i not in col_seen:
                    col_seen.add(index_i)
                    ans += val_i * (n - len(row_seen))
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table
#
# 解题思路:
# 从后往前处理查询。后面的查询会覆盖前面的，所以最后执行的查询对最终结果贡献最大。
# 用集合记录已被覆盖的行和列。当处理某行/列时，该行/列中尚未被后续查询覆盖的单元格数量为 n-len(col_seen) 或 n-len(row_seen)。
# 每个查询的贡献 = val * (该行/列中未被覆盖的单元格数量)。
#
# 时间复杂度: O(q) 其中 q 是查询数量
# 空间复杂度: O(n) 用于存储行/列集合
#
# 关键点:
# - 反向遍历是关键：后面的查询会覆盖前面的
# - 用集合追踪已处理的行/列，避免重复计算被覆盖的单元格
# - 每次处理一行时，剩余列数 = n - len(col_seen)
