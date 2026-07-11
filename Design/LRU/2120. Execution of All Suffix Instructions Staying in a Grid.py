"""
LeetCode #2120 - Execution of All Suffix Instructions Staying in a Grid
执行所有后缀指令
https://leetcode.cn/problems/execution-of-all-suffix-instructions-staying-in-a-grid/

现有一个 `n x n` 大小的网格，左上角单元格坐标 `(0, 0)` ，右下角单元格坐标 `(n - 1, n - 1)` 。给你整数 `n` 和一个整数数组 `startPos` ，其中 `startPos = [start_row, start_col]` 表示机器人最开始在坐标为 `(start_row, start_col)` 的单元格上。
另给你一个长度为 `m` 、下标从 0 开始的字符串 `s` ，其中 `s[i]` 是对机器人的第 `i` 条指令：`'L'`（向左移动），`'R'`（向右移动），`'U'`（向上移动）和 `'D'`（向下移动）。
机器人可以从 `s` 中的任一第 `i` 条指令开始执行。它将会逐条执行指令直到 `s` 的末尾，但在满足下述条件之一时，机器人将会停止：
下一条指令将会导致机器人移动到网格外。
没有指令可以执行。
返回一个长度为 `m` 的数组 `answer` ，其中 `answer[i]` 是机器人从第 `i` 条指令 开始 ，可以执行的 指令数目 。

示例 1：

输入：n = 3, startPos = [0,1], s = "RRDDLU" 输出：[1,5,4,3,1,0] 解释：机器人从 startPos 出发，并从第 i 条指令开始执行： - 0: "RRDDLU" 在移动到网格外之前，只能执行一条 "R" 指令。 - 1:  "RDDLU" 可以执行全部五条指令，机器人仍在网格内，最终到达 (0, 0) 。 - 2:   "DDLU" 可以执行全部四条指令，机器人仍在网格内，最终到达 (0, 0) 。 - 3:    "DLU" 可以执行全部三条指令，机器人仍在网格内，最终到达 (0, 0) 。 - 4:     "LU" 在移动到网格外之前，只能执行一条 "L" 指令。 - 5:      "U" 如果向上移动，将会移动到网格外。
示例 2：

输入：n = 2, startPos = [1,1], s = "LURD" 输出：[4,1,0,0] 解释： - 0: "LURD" - 1:  "URD" - 2:   "RD" - 3:    "D"
示例 3：

输入：n = 1, startPos = [0,0], s = "LRUD" 输出：[0,0,0,0] 解释：无论机器人从哪条指令开始执行，都会移动到网格外。

提示：
`m == s.length`
`1 <= n, m <= 500`
`startPos.length == 2`
`0 <= start_row, start_col < n`
`s` 由 `'L'`、`'R'`、`'U'` 和 `'D'` 组成
"""

from typing import List, Optional


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        m = len(s)
        result = []
        dir_map = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

        for i in range(m):
            r, c = startPos
            count = 0
            for j in range(i, m):
                dr, dc = dir_map[s[j]]
                r, c = r + dr, c + dc
                if 0 <= r < n and 0 <= c < n:
                    count += 1
                else:
                    break
            result.append(count)

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: String, Simulation
#
# 解题思路:
# 对于每个起始位置 i，从指令 s[i] 开始模拟执行，直到移出网格或指令执行完毕。
# 使用方向字典将 'L'/'R'/'U'/'D' 映射为坐标偏移量。
# 对每个起始位置，逐条执行后续指令，每次移动后检查是否仍在网格内：
# - 如果在网格内，计数加 1，继续下一条指令。
# - 如果移出网格，停止并记录当前计数。
# 返回每个起始位置对应的可执行指令数。
#
# 时间复杂度: O(m^2)，其中 m 为指令长度。对每个起始位置都要模拟后续指令。
# 空间复杂度: O(1)，不计返回结果。
#
# 关键点:
# - 暴力模拟：对每个起始下标独立模拟
# - 方向映射简化坐标更新逻辑
# - 每次移出网格立即 break，不继续执行后续指令
