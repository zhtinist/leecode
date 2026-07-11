"""
LeetCode #2365 - Task Scheduler II
任务调度器 II
https://leetcode.cn/problems/task-scheduler-ii/

给你一个下标从 0 开始的正整数数组 `tasks` ，表示需要 按顺序 完成的任务，其中 `tasks[i]` 表示第 `i` 件任务的 类型 。
同时给你一个正整数 `space` ，表示一个任务完成 后 ，另一个 相同 类型任务完成前需要间隔的 最少 天数。
在所有任务完成前的每一天，你都必须进行以下两种操作中的一种：
完成 `tasks` 中的下一个任务
休息一天
请你返回完成所有任务所需的 最少 天数。

示例 1：
输入：tasks = [1,2,1,2,3,1], space = 3 输出：9 解释： 9 天完成所有任务的一种方法是： 第 1 天：完成任务 0 。 第 2 天：完成任务 1 。 第 3 天：休息。 第 4 天：休息。 第 5 天：完成任务 2 。 第 6 天：完成任务 3 。 第 7 天：休息。 第 8 天：完成任务 4 。 第 9 天：完成任务 5 。 可以证明无法少于 9 天完成所有任务。
示例 2：
输入：tasks = [5,8,8,5], space = 2 输出：6 解释： 6 天完成所有任务的一种方法是： 第 1 天：完成任务 0 。 第 2 天：完成任务 1 。 第 3 天：休息。 第 4 天：休息。 第 5 天：完成任务 2 。 第 6 天：完成任务 3 。 可以证明无法少于 6 天完成所有任务。

提示：
`1 <= tasks.length <= 10^5`
`1 <= tasks[i] <= 10^9`
`1 <= space <= tasks.length`
"""

from typing import List, Optional


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        last_day = {}
        current_day = 0

        for task in tasks:
            if task in last_day:
                current_day = max(current_day + 1, last_day[task] + space + 1)
            else:
                current_day += 1
            last_day[task] = current_day

        return current_day



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Simulation
#
# 解题思路:
# 使用哈希表记录每种任务类型上一次完成的天数。
# 按顺序遍历每个任务：如果该任务类型之前已完成过，则当前天数为 max(当前天数+1, 上次完成天数+space+1)；
# 如果未完成过，则当前天数+1。更新该任务类型的最后完成天数为当前天数。
# 最终返回当前天数即为完成所有任务所需的最少天数。
#
# 时间复杂度: O(n) 其中 n 为 tasks 数组的长度
# 空间复杂度: O(m) 其中 m 为不同任务类型的数量，最坏情况 O(n)
#
# 关键点:
# - 使用哈希表维护每种任务类型上一次完成的天数
# - 核心逻辑：如果同类型任务需要在 space 天后才能再次执行，则当前天至少为 last_day[task] + space + 1
# - 任务必须按顺序完成，不能跳过或重排
