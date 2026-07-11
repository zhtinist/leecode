"""
LeetCode #2512 - Reward Top K Students
奖励最顶尖的 K 名学生
https://leetcode.cn/problems/reward-top-k-students/

给你两个字符串数组 `positive_feedback` 和 `negative_feedback` ，分别包含表示正面的和负面的词汇。不会 有单词同时是正面的和负面的。
一开始，每位学生分数为 `0` 。每个正面的单词会给学生的分数 加 `3` 分，每个负面的词会给学生的分数 减  `1` 分。
给你 `n` 个学生的评语，用一个下标从 0 开始的字符串数组 `report` 和一个下标从 0 开始的整数数组 `student_id` 表示，其中 `student_id[i]` 表示这名学生的 ID ，这名学生的评语是 `report[i]` 。每名学生的 ID 互不相同。
给你一个整数 `k` ，请你返回按照得分 从高到低 最顶尖的 `k` 名学生。如果有多名学生分数相同，ID 越小排名越前。

示例 1：
输入：positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is studious","the student is smart"], student_id = [1,2], k = 2 输出：[1,2] 解释： 两名学生都有 1 个正面词汇，都得到 3 分，学生 1 的 ID 更小所以排名更前。
示例 2：
输入：positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is not studious","the student is smart"], student_id = [1,2], k = 2 输出：[2,1] 解释： - ID 为 1 的学生有 1 个正面词汇和 1 个负面词汇，所以得分为 3-1=2 分。 - ID 为 2 的学生有 1 个正面词汇，得分为 3 分。 学生 2 分数更高，所以返回 [2,1] 。

提示：
`1 <= positive_feedback.length, negative_feedback.length <= 10^4`
`1 <= positive_feedback[i].length, negative_feedback[j].length <= 100`
`positive_feedback[i]` 和 `negative_feedback[j]` 都只包含小写英文字母。
`positive_feedback` 和 `negative_feedback` 中不会有相同单词。
`n == report.length == student_id.length`
`1 <= n <= 10^4`
`report[i]` 只包含小写英文字母和空格 `' '` 。
`report[i]` 中连续单词之间有单个空格隔开。
`1 <= report[i].length <= 100`
`1 <= student_id[i] <= 10^9`
`student_id[i]` 的值 互不相同 。
`1 <= k <= n`
"""

from typing import List, Optional


class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        pos_set = set(positive_feedback)
        neg_set = set(negative_feedback)

        scores = []
        for i, rep in enumerate(report):
            score = 0
            for word in rep.split():
                if word in pos_set:
                    score += 3
                elif word in neg_set:
                    score -= 1
            scores.append((-score, student_id[i]))

        scores.sort()
        return [sid for _, sid in scores[:k]]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, String, Sorting, Heap (Priority Queue)
#
# 解题思路:
# 将正负面词汇分别存入集合以O(1)查找。遍历每个学生的评语，拆分单词后按规则计算得分
# （正面+3，负面-1）。将得分和学号存入列表，按得分降序、学号升序排序，取前k个。
#
# 时间复杂度: O(M + R + S log S)，其中M为词汇总数，R为报告总单词数，S为学生数
# 空间复杂度: O(P + N + S)
#
# 关键点:
# - 使用set存储词汇实现O(1)查找
# - 用(-score, student_id)实现先按得分降序、再按学号升序的排序
# - 只取前k个结果
