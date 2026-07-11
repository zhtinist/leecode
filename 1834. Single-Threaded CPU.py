"""
LeetCode #1834 - Single-Threaded CPU
中文题名：单线程CPU
https://leetcode.com/problems/single-threaded-cpu/

You are given `n`​​​​​​ tasks labeled from `0` to `n - 1` represented by a 2D integer array `tasks`, where `tasks[i] = [enqueueTimei, processingTimei]` means that the `i​​​​​​th`​​​​ task will be available to process at `enqueueTimei` and will take `processingTimei` to finish processing.

You have a single-threaded CPU that can process at most one task at a time and will act in the following way:

If the CPU is idle and there are no available tasks to process, the CPU remains idle.

If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.

Once a task is started, the CPU will process the entire task without stopping.

The CPU can finish a task then start a new one instantly.

Return the order in which the CPU will process the tasks.

Example 1:

Input: tasks = [[1,2],[2,4],[3,2],[4,1]]
Output: [0,2,3,1]
Explanation: The events go as follows:
- At time = 1, task 0 is available to process. Available tasks = {0}.
- Also at time = 1, the idle CPU starts processing task 0. Available tasks = {}.
- At time = 2, task 1 is available to process. Available tasks = {1}.
- At time = 3, task 2 is available to process. Available tasks = {1, 2}.
- Also at time = 3, the CPU finishes task 0 and starts processing task 2 as it is the shortest. Available tasks = {1}.
- At time = 4, task 3 is available to process. Available tasks = {1, 3}.
- At time = 5, the CPU finishes task 2 and starts processing task 3 as it is the shortest. Available tasks = {1}.
- At time = 6, the CPU finishes task 3 and starts processing task 1. Available tasks = {}.
- At time = 10, the CPU finishes task 1 and becomes idle.

Example 2:

Input: tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
Output: [4,3,2,0,1]
Explanation: The events go as follows:
- At time = 7, all the tasks become available. Available tasks = {0,1,2,3,4}.
- Also at time = 7, the idle CPU starts processing task 4. Available tasks = {0,1,2,3}.
- At time = 9, the CPU finishes task 4 and starts processing task 3. Available tasks = {0,1,2}.
- At time = 13, the CPU finishes task 3 and starts processing task 2. Available tasks = {0,1}.
- At time = 18, the CPU finishes task 2 and starts processing task 0. Available tasks = {1}.
- At time = 28, the CPU finishes task 0 and starts processing task 1. Available tasks = {}.
- At time = 40, the CPU finishes task 1 and becomes idle.

Constraints:

`tasks.length == n`

`1 <= n <= 105`

`1 <= enqueueTimei, processingTimei <= 109`

【中文翻译】

给定n个任务，编号从0到n-1，用二维整数数组 `tasks` 表示，`tasks[i] = [enqueueTimei, processingTimei]` 表示第i个任务在 `enqueueTimei` 时可用，需要 `processingTimei` 的时间来完成。

你有一个单线程CPU，同一时间最多处理一个任务，行为如下：
- 如果CPU空闲且没有可用任务，CPU保持空闲。
- 如果CPU空闲且有可用任务，CPU选择处理时间最短的任务。如果有多个任务时间相同，选择索引最小的。
- 一旦任务开始，CPU会不中断地完成整个任务。
- CPU完成一个任务后可以立即开始新任务。

返回CPU处理任务的顺序。

示例：
输入：tasks = [[1,2],[2,4],[3,2],[4,1]]
输出：[0,2,3,1]

"""

from typing import List, Optional


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        import heapq

        # 给每个任务附上原始索引
        indexed_tasks = [(enqueue, process, i)
                         for i, (enqueue, process) in enumerate(tasks)]
        indexed_tasks.sort()  # 按入队时间排序

        heap = []  # 最小堆: (处理时间, 索引)
        result = []
        time = 0
        i = 0
        n = len(tasks)

        while i < n or heap:
            if not heap:
                # CPU空闲，跳到下一个任务的入队时间
                time = max(time, indexed_tasks[i][0])

            # 将所有当前可用的任务加入堆
            while i < n and indexed_tasks[i][0] <= time:
                enqueue, process, idx = indexed_tasks[i]
                heapq.heappush(heap, (process, idx))
                i += 1

            # 处理最短的任务
            process_time, idx = heapq.heappop(heap)
            time += process_time
            result.append(idx)

        return result










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用最小堆模拟CPU调度。先将任务按入队时间排序并附上原始索引。
# 维护一个最小堆，堆中元素为(处理时间, 原始索引)，按处理时间优先（相同则按索引）。
# 模拟时间推进：如果堆为空，时间跳到下一个任务的入队时间。
# 将当前时间之前可用的所有任务加入堆。从堆中弹出最短任务处理。
#
# 时间复杂度: O(N log N)，堆操作的开销
# 空间复杂度: O(N)，堆和索引任务数组
#
# 关键点:
# - 堆的排序规则：(处理时间, 索引) —— 处理时间优先，索引次之
# - CPU空闲时直接跳到下一任务的入队时间
# - 先给每个任务附加原始索引再排序
