"""
LeetCode #1792 - Maximum Average Pass Ratio
中文题名：最大平均通过率
https://leetcode.com/problems/maximum-average-pass-ratio/

There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array `classes`, where `classes[i] = [passi, totali]`. You know beforehand that in the `ith` class, there are `totali` total students, but only `passi` number of students will pass the exam.

You are also given an integer `extraStudents`. There are another `extraStudents` brilliant students that are guaranteed to pass the exam of any class they are assigned to. You want to assign each of the `extraStudents` students to a class in a way that maximizes the average pass ratio across all the classes.

The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.

Return the maximum possible average pass ratio after assigning the `extraStudents` students. Answers within `10-5` of the actual answer will be accepted.

Example 1:

Input: classes = [[1,2],[3,5],[2,2]], `extraStudents` = 2
Output: 0.78333
Explanation: You can assign the two extra students to the first class. The average pass ratio will be equal to (3/4 + 3/5 + 2/2) / 3 = 0.78333.

Example 2:

Input: classes = [[2,4],[3,9],[4,5],[2,10]], `extraStudents` = 4
Output: 0.53485

Constraints:

`1 <= classes.length <= 105`

`classes[i].length == 2`

`1 <= passi <= totali <= 105`

`1 <= extraStudents <= 105`

【中文翻译】
给定 classes 数组，classes[i] = [pass_i, total_i] 表示第 i 个班级的通过人数和总人数。
还有 extraStudents 个额外的聪明学生可以分配。将每个聪明学生分配到一个班级后，
该班级的通过率变为 (pass_i + 1)/(total_i + 1)。
求分配后所有班级的平均通过率的最大可能值。

示例 1：
输入: classes = [[1,2],[3,5],[2,2]], extraStudents = 2
输出: 0.78333
解释: 将学生分配到第一个和第二个班级。
"""

from typing import List, Optional
import heapq


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(p: int, t: int) -> float:
            # 增加一个学生带来的通过率提升
            return (p + 1) / (t + 1) - p / t

        # 建立最大堆（Python 是最小堆，所以存负的 gain）
        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)

        for _ in range(extraStudents):
            g, p, t = heapq.heappop(heap)
            p, t = p + 1, t + 1
            heapq.heappush(heap, (-gain(p, t), p, t))

        total_ratio = sum(p / t for _, p, t in heap)
        return total_ratio / len(classes)
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心 + 最大堆。每次将额外学生分配到能带来最大边增益的班级。
# 边增益 = (pass+1)/(total+1) - pass/total。
# 使用最大堆动态维护每个班级的边增益，每次弹出增益最大的班级，
# 更新其 pass 和 total，重新计算增益并放回堆。
# repeat extraStudents 次。
#
# 时间复杂度: O((C + E) log C) — C 为班级数，E 为额外学生数
# 空间复杂度: O(C) — 堆
#
# 关键点:
# - 贪心选择边际增益最大的班级
# - 由于增益函数是凸的（递减），贪心正确
# - 最大堆用负数实现（Python heapq 是最小堆）
