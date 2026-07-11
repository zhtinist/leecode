"""
LeetCode #957 - Prison Cells After N Days
中文题名：N 天后的牢房
https://leetcode.com/problems/prison-cells-after-n-days/

There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following
rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then
the cell becomes occupied.

Otherwise, it becomes vacant.

(Note that because the prison is a row, the first and the last cells in the row can't
have two adjacent neighbors.)

We describe the current state of the prison in the following way: `cells[i] ==
1` if the `i`-th cell is occupied, else `cells[i] == 0`.

Given the initial state of the prison, return the state of the prison after `N`
days (and `N` such changes described above.)

【中文翻译】
一排有 8 间牢房，每间牢房要么被占用要么空置。
每天，牢房的状态按以下规则变化：
如果一个牢房的两个相邻邻居都被占用或都空置，则该牢房变为被占用。
否则，变为空置。
（注意，因为牢房是一排，所以第一个和最后一个牢房没有两个相邻邻居。）
给定监狱的初始状态，返回 N 天后的监狱状态。

"""

from typing import List, Optional


class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen = {}
        state = tuple(cells)

        while n > 0:
            if state in seen:
                # 发现循环，跳过重复周期
                cycle_len = seen[state] - n
                n %= cycle_len
                if n == 0:
                    break

            seen[state] = n

            # 计算下一天的状态
            next_cells = [0] * 8
            for i in range(1, 7):
                next_cells[i] = 1 if state[i - 1] == state[i + 1] else 0

            state = tuple(next_cells)
            n -= 1

        return list(state)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 由于只有 8 个牢房，且首尾牢房每天后必然变为 0，因此状态空间最多有 2^6 = 64 种。
# 使用哈希表记录每个状态首次出现的天数，当遇到重复状态时即发现循环。
# 此时可通过取模运算跳过剩余循环：N = N % cycle_length。
# 之后继续模拟剩余天数即可。
#
# 时间复杂度: O(min(N, 64)) — 最多模拟 64 天就能发现循环
# 空间复杂度: O(1) — 状态空间上限为 64 种
#
# 关键点:
# - 状态空间有限（最多 64 种），必然会出现循环
# - 使用元组作为哈希表的键来记录状态
# - 首尾牢房始终变为 0（因为没有两个相邻邻居）
# - 循环检测后使用取模跳过重复周期
