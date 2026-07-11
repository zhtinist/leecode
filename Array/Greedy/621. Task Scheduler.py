"""
LeetCode #621 - Task Scheduler
中文题名：任务调度器
https://leetcode.com/problems/task-scheduler/

Given a char array representing tasks CPU need to do. It contains capital letters A to Z
where different letters represent different tasks. Tasks could be done without original
order. Each task could be done in one interval. For each interval, CPU could finish one task
or just be idle.

However, there is a non-negative cooling interval n that means between two same
tasks, there must be at least n intervals that CPU are doing different tasks or just be
idle.

You need to return the least number of intervals the CPU will take to finish all the
given tasks.

Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

Note:

The number of tasks is in the range [1, 10000].

The integer n is in the range [0, 100].

【中文翻译】
给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含大写字母 A 到 Z 表示不同的任务。
任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。
在任何一个单位时间，CPU 可以完成一个任务，或者处于待命状态。

然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，
因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。

你需要计算完成所有任务所需要的最短时间。

示例：

输入：tasks = ["A","A","A","B","B","B"], n = 2
输出：8
解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B。

注意：

任务的总个数为 [1, 10000]。

n 的取值范围为 [0, 100]。
"""

from typing import List, Optional
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = list(Counter(tasks).values())
        max_freq = max(freq)
        max_count = freq.count(max_freq)
        return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心算法 + 数学推导（填桶法）：
# 1. 统计每种任务的频率，找出最高频率 max_freq。
# 2. 统计有多少种任务的频率等于 max_freq（记为 max_count）。
# 3. 将出现频率最高的任务作为"框架"，将它们排成 max_freq - 1 个间隔（桶），
#    每个间隔长度为 n + 1（包含冷却时间）。
# 4. 最后一个"桶"只需要放 max_count 个最高频率任务。
# 5. 因此最小时间 = max(任务总数, (max_freq - 1) * (n + 1) + max_count)。
# 5. 取 max 是因为如果任务种类足够多，可以填满冷却间隔，不需要待命，
#    此时答案就是任务总数。
#
# 时间复杂度: O(m)，m 为任务种类数（最多 26）
# 空间复杂度: O(1)，只用到大小为 26 的数组
#
# 关键点:
# - 关键是找出最高频率任务作为框架
# - 填桶模型：(max_freq - 1) 个完整桶 + 最后一轮
# - 当冷却时间能被其他任务填满时，最短时间 = 任务总数
# - 不需要真正模拟执行过程，纯数学公式即可
