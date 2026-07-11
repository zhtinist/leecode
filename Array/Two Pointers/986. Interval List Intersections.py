"""
LeetCode #986 - Interval List Intersections
中文题名：区间列表的交集
https://leetcode.com/problems/interval-list-intersections/

给定两个由一些闭区间组成的列表，每个区间列表都是成对不相交的，并且已经排序。

返回这两个区间列表的交集。

（形式上，闭区间 [a, b]（其中 a <= b）表示实数 x 的集合，满足 a <= x <= b。两个闭区间的交集是一组实数，要么为空集，要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3]。）

示例 1：

输入：A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
输出：[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
提示：输入和所需的输出都是区间对象组成的列表，而不是数组或列表。

注意：

0 <= A.length < 1000
0 <= B.length < 1000
0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9

注意：输入类型于 2019 年 4 月 15 日更改。请重置为默认代码定义以获取新的方法签名。

【中文翻译】
给定两个已排序的、各自内部不相交的区间列表，求两个列表中所有区间的交集。交集本身也是区间列表。

"""

from typing import List, Optional


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        result = []
        while i < len(firstList) and j < len(secondList):
            # Find intersection of firstList[i] and secondList[j]
            lo = max(firstList[i][0], secondList[j][0])
            hi = min(firstList[i][1], secondList[j][1])
            if lo <= hi:
                result.append([lo, hi])
            # Move the pointer that ends earlier
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 双指针法（合并区间的变形）：
# 1. 使用两个指针 i 和 j 分别遍历 firstList 和 secondList。
# 2. 对于当前两个区间 A = firstList[i] 和 B = secondList[j]：
#    - 交集区间为 [max(A.start, B.start), min(A.end, B.end)]。
#    - 如果 start <= end，说明有交集，加入结果。
#    - 比较两个区间的结束点，结束更早的区间指针前移（因为它不可能与后续区间再有交集了）。
# 3. 继续直到某个列表遍历完毕。
#
# 时间复杂度: O(M + N)，M 和 N 分别为两个区间列表的长度。每个区间最多被访问一次
# 空间复杂度: O(1)，不计算输出结果。输出结果大小最坏为 O(M + N)
#
# 关键点:
# - 两个区间有交集的充要条件：max(lo1, lo2) <= min(hi1, hi2)
# - 交集区间 = [max(lo1, lo2), min(hi1, hi2)]
# - 移动指针的依据：结束更早的区间（hi 更小的那个）前移
# - 等价于合并两个已排序列表，找重叠部分
