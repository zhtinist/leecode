"""
LeetCode #378 - Kth Smallest Element in a Sorted Matrix
中文题名：有序矩阵中第K小的元素
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

Given a n x n matrix where each of the rows and columns are sorted in ascending
order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
[ 1,  5,  9],
[10, 11, 13],
[12, 13, 15]
],
k = 8,

return 13.

Note:

You may assume k is always valid, 1 <= k <= n2.

【中文翻译】
给定一个 n x n 矩阵，其中每行和每列都按升序排列，找出矩阵中第 k 小的元素。

请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。

示例：

matrix = [
[ 1,  5,  9],
[10, 11, 13],
[12, 13, 15]
],
k = 8,

返回 13。

注意：

你可以假设 k 始终有效，1 <= k <= n^2。
"""

from typing import List, Optional


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        lo, hi = matrix[0][0], matrix[n - 1][n - 1]

        # 统计矩阵中小于等于 mid 的元素个数（利用行列有序性从左下角出发）
        def count_leq(mid: int) -> int:
            count = 0
            row, col = n - 1, 0
            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    # 当前列从第 0 行到第 row 行的元素都 <= mid
                    count += row + 1
                    col += 1
                else:
                    row -= 1
            return count

        # 二分查找第一个使得 count_leq(mid) >= k 的值
        while lo < hi:
            mid = (lo + hi) // 2
            if count_leq(mid) < k:
                lo = mid + 1
            else:
                hi = mid

        return lo











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 本题要求在一个行列均有序的矩阵中找出第 k 小的元素。矩阵每行每列都是升序，
# 但整体不一定是全局有序的，不能直接拼成一维数组排序（那样是 O(N^2 log N)）。
#
# 使用 二分搜索 在值域上进行查找：
# 1. 确定搜索范围：lo = matrix[0][0]（最小值），hi = matrix[n-1][n-1]（最大值）
# 2. 编写 count_leq(mid) 函数，统计矩阵中小于等于 mid 的元素个数
#    - 利用矩阵行列有序的性质，从左下角出发
#    - 如果 matrix[row][col] <= mid，则该列 row+1 个元素都 <= mid，右移
#    - 如果 matrix[row][col] > mid，上移
#    - 复杂度 O(N)
# 3. 二分搜索：如果 count_leq(mid) < k，说明第 k 小元素在 (mid, hi] 范围
#    如果 count_leq(mid) >= k，说明第 k 小元素在 [lo, mid] 范围
# 4. 循环结束时 lo == hi，即为答案
#
# 时间复杂度: O(N * log(max - min)) - 每次 count_leq 为 O(N)，二分搜索 O(log(max-min))
# 空间复杂度: O(1) - 只使用常数额外空间
#
# 关键点:
# - 值域二分而非索引二分：题目没有要求返回索引，只需返回值
# - count_leq 函数利用行列有序性在 O(N) 内完成统计（从右上角或左下角出发）
# - 注意处理重复元素：题目要求的是"第 k 小"，不是"第 k 个不同"，所以 >= k 时右边界收缩到 mid
# - 另一种解法是使用最小堆（归并 k 次），时间复杂度 O(k log N)，但当 k 接近 N^2 时不如二分
