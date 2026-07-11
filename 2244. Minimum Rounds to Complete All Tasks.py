"""
LeetCode #2244 - Minimum Rounds to Complete All Tasks
完成所有任务需要的最少轮数
https://leetcode.cn/problems/minimum-rounds-to-complete-all-tasks/

给你一个下标从 0 开始的整数数组 `tasks` ，其中 `tasks[i]` 表示任务的难度级别。在每一轮中，你可以完成 2 个或者 3 个 相同难度级别 的任务。
返回完成所有任务需要的 最少 轮数，如果无法完成所有任务，返回 `-1` 。

示例 1：
输入：tasks = [2,2,3,3,2,4,4,4,4,4] 输出：4 解释：要想完成所有任务，一个可能的计划是： - 第一轮，完成难度级别为 2 的 3 个任务。  - 第二轮，完成难度级别为 3 的 2 个任务。  - 第三轮，完成难度级别为 4 的 3 个任务。  - 第四轮，完成难度级别为 4 的 2 个任务。  可以证明，无法在少于 4 轮的情况下完成所有任务，所以答案为 4 。
示例 2：
输入：tasks = [2,3,3] 输出：-1 解释：难度级别为 2 的任务只有 1 个，但每一轮执行中，只能选择完成 2 个或者 3 个相同难度级别的任务。因此，无法完成所有任务，答案为 -1 。

提示：
`1 <= tasks.length <= 10^5`
`1 <= tasks[i] <= 10^9`
"""

from typing import List, Optional
from collections import Counter


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq = Counter(tasks)
        rounds = 0

        for count in freq.values():
            if count == 1:
                return -1
            # ceil(count / 3) gives the minimum rounds for this difficulty
            rounds += (count + 2) // 3

        return rounds


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Hash Table, Counting
#
# 解题思路:
# 首先统计每种难度级别的任务数量（频率）。
# 对于每种难度级别，设其任务数量为 f：
#   - 如果 f == 1，无法用 2 或 3 完成，返回 -1。
#   - 否则，最少轮数 = ceil(f / 3)。因为优先使用 3 个一组效率最高，
#     余数只可能是 0、1、2：
#       * 余 0：全部用 3 个一组，f/3 轮
#       * 余 1：退一组 3 变为两组 2（3+1=4=2+2），轮数 = (f-4)/3 + 2 = ceil(f/3)
#       * 余 2：加一组 2，轮数 = (f-2)/3 + 1 = ceil(f/3)
#     统一公式：ceil(f/3) = (f + 2) // 3
#
# 时间复杂度: O(n) — 统计频率 O(n)，遍历频率 O(unique tasks) <= O(n)
# 空间复杂度: O(k) — k 为不同难度级别的数量，最坏 O(n)
#
# 关键点:
# - 出现次数为 1 时无法完成，直接返回 -1
# - ceil(f/3) = (f + 2) // 3 的数学推导
# - 使用 collections.Counter 快速统计频率
