"""
LeetCode #2895 - Minimum Processing Time
最小处理时间
https://leetcode.cn/problems/minimum-processing-time/

你有 `n` 颗处理器，每颗处理器都有 `4` 个核心。现有 `n * 4` 个待执行任务，每个核心只执行 一次 任务。
给你一个下标从 0 开始的整数数组 `processorTime` ，表示每颗处理器最早空闲时间。另给你一个下标从 0 开始的整数数组 `tasks` ，表示执行每个任务所需的时间。返回所有任务都执行完毕需要的 最小时间 。
注意：每个核心独立执行任务。

示例 1：
输入：processorTime = [8,10], tasks = [2,2,3,1,8,7,4,5] 输出：16 解释： 最优的方案是将下标为 4, 5, 6, 7 的任务分配给第一颗处理器（最早空闲时间 time = 8），下标为 0, 1, 2, 3 的任务分配给第二颗处理器（最早空闲时间 time = 10）。  第一颗处理器执行完所有任务需要花费的时间 = max(8 + 8, 8 + 7, 8 + 4, 8 + 5) = 16 。 第二颗处理器执行完所有任务需要花费的时间 = max(10 + 2, 10 + 2, 10 + 3, 10 + 1) = 13 。 因此，可以证明执行完所有任务需要花费的最小时间是 16 。
示例 2：
输入：processorTime = [10,20], tasks = [2,3,1,2,5,8,4,3] 输出：23 解释： 最优的方案是将下标为 1, 4, 5, 6 的任务分配给第一颗处理器（最早空闲时间 time = 10），下标为 0, 2, 3, 7 的任务分配给第二颗处理器（最早空闲时间 time = 20）。  第一颗处理器执行完所有任务需要花费的时间 = max(10 + 3, 10 + 5, 10 + 8, 10 + 4) = 18 。  第二颗处理器执行完所有任务需要花费的时间 = max(20 + 2, 20 + 1, 20 + 2, 20 + 3) = 23 。  因此，可以证明执行完所有任务需要花费的最小时间是 23 。

提示：
`1 <= n == processorTime.length <= 25000`
`1 <= tasks.length <= 10^5`
`0 <= processorTime[i] <= 10^9`
`1 <= tasks[i] <= 10^9`
`tasks.length == 4 * n`
"""

from typing import List, Optional


class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        n = len(processorTime)
        ans = 0
        for i in range(n):
            ans = max(ans, processorTime[i] + tasks[4 * i])
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Sorting
#
# 解题思路:
# 使用贪心策略：将处理器按空闲时间升序排列，任务按耗时降序排列。
# 每颗处理器有4个核心，分配给每个处理器4个任务。为使最大完成时间最小化，应将耗时最长的任务分配给最早空闲的处理器。
# 答案为 max(processorTime[i] + tasks[4*i])，其中 tasks 已降序排列。
#
# 时间复杂度: O(n log n)
# 空间复杂度: O(1)
#
# 关键点:
# - 贪心：慢任务配早空闲处理器，类似"短板效应"的逆用
# - 排序方向：processorTime 升序，tasks 降序
# - 每处理器固定4个任务，取该处理器中最慢任务计算完成时间
