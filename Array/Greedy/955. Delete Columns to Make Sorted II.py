"""
LeetCode #955 - Delete Columns to Make Sorted II
中文题名：删列造序 II
https://leetcode.com/problems/delete-columns-to-make-sorted-ii/

We are given an array `A` of `N` lowercase letter strings, all of
the same length.

Now, we may choose any set of deletion indices, and for each string, we delete all the
characters in those indices.

For example, if we have an array `A = ["abcdef","uvwxyz"]` and
deletion indices `{0, 2, 3}`, then the final array after deletions is `["bef","vyz"]`.

Suppose we chose a set of deletion indices `D` such that after deletions, the
final array has its elements in lexicographic order (`A[0] <= A[1]
<= A[2] ... <= A[A.length - 1]`).

Return the minimum possible value of `D.length`.

【中文翻译】
给定一个由 N 个小写字母字符串组成的数组 `A`，每个字符串长度相同。
我们可以选择一组删除索引，对于每个字符串，删除这些索引处的所有字符。
假设我们选择了一组删除索引 `D`，使得删除后的最终数组按字典序排列
（`A[0] <= A[1] <= A[2] ... <= A[A.length - 1]`）。
返回 `D.length` 的最小可能值。

"""

from typing import List, Optional


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        # sorted[i] 表示第 i 行是否已经严格大于前一行
        sorted_rows = [False] * n
        deletions = 0

        for col in range(m):
            # 检查当前列是否需要删除
            need_delete = False
            for row in range(1, n):
                if not sorted_rows[row] and strs[row][col] < strs[row - 1][col]:
                    need_delete = True
                    break

            if need_delete:
                deletions += 1
            else:
                # 当前列保留，更新 sorted_rows
                for row in range(1, n):
                    if strs[row][col] > strs[row - 1][col]:
                        sorted_rows[row] = True

        return deletions



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心算法。逐列扫描，维护一个 sorted_rows 数组表示哪些行已经与前一行形成严格大于关系。
# 对于每一列：
# 1. 检查是否在未排序的行中存在逆序（strs[row][col] < strs[row-1][col]），
#    如果存在则必须删除该列。
# 2. 如果该列保留，更新 sorted_rows：对于 strs[row][col] > strs[row-1][col] 的行，
#    标记为已排序（后续列不再需要比较这些行）。
# 最终返回删除的列数。
#
# 时间复杂度: O(N * M) — N 行 M 列
# 空间复杂度: O(N) — sorted_rows 数组
#
# 关键点:
# - 贪心策略：从左到右处理，能保留的列尽量保留
# - sorted_rows 标记哪些行已经确立顺序，后续无需再比较
# - 只有当某一列在未排序行中出现严格逆序时才删除
