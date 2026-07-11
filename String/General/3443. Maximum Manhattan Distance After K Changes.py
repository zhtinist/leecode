"""
LeetCode #3443 - Maximum Manhattan Distance After K Changes
K 次修改后的最大曼哈顿距离
https://leetcode.cn/problems/maximum-manhattan-distance-after-k-changes/

给你一个由字符 `'N'`、`'S'`、`'E'` 和 `'W'` 组成的字符串 `s`，其中 `s[i]` 表示在无限网格中的移动操作：
`'N'`：向北移动 1 个单位。
`'S'`：向南移动 1 个单位。
`'E'`：向东移动 1 个单位。
`'W'`：向西移动 1 个单位。
初始时，你位于原点 `(0, 0)`。你 最多 可以修改 `k` 个字符为任意四个方向之一。
请找出在 按顺序 执行所有移动操作过程中的 任意时刻 ，所能达到的离原点的 最大曼哈顿距离 。
曼哈顿距离 定义为两个坐标点 `(x_i, y_i)` 和 `(x_j, y_j)` 的横向距离绝对值与纵向距离绝对值之和，即 `|x_i - x_j| + |y_i - y_j|`。

示例 1：

输入：s = "NWSE", k = 1
输出：3
解释：
将 `s[2]` 从 `'S'` 改为 `'N'` ，字符串 `s` 变为 `"NWNE"` 。   	 		 			移动操作 			位置 (x, y) 			曼哈顿距离 			最大值 		 	 	 		 			s[0] == 'N' 			(0, 1) 			0 + 1 = 1 			1 		 		 			s[1] == 'W' 			(-1, 1) 			1 + 1 = 2 			2 		 		 			s[2] == 'N' 			(-1, 2) 			1 + 2 = 3 			3 		 		 			s[3] == 'E' 			(0, 2) 			0 + 2 = 2 			3
执行移动操作过程中，距离原点的最大曼哈顿距离是 3 。
示例 2：

输入：s = "NSWWEW", k = 3
输出：6
解释：
将 `s[1]` 从 `'S'` 改为 `'N'` ，将 `s[4]` 从 `'E'` 改为 `'W'` 。字符串 `s` 变为 `"NNWWWW"` 。
执行移动操作过程中，距离原点的最大曼哈顿距离是 6 。

提示：
`1 <= s.length <= 10^5`
`0 <= k <= s.length`
`s` 仅由 `'N'`、`'S'`、`'E'` 和 `'W'` 。
"""

from typing import List, Optional


class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        cnt_N = cnt_S = cnt_E = cnt_W = 0
        ans = 0

        for ch in s:
            if ch == 'N':
                cnt_N += 1
            elif ch == 'S':
                cnt_S += 1
            elif ch == 'E':
                cnt_E += 1
            else:  # 'W'
                cnt_W += 1

            x = cnt_E - cnt_W
            y = cnt_N - cnt_S

            # Four quadrants: (sx, sy) in {(1,1), (1,-1), (-1,1), (-1,-1)}
            # Quadrant 1 (sx=1, sy=1): base = x + y, bad = cnt_S + cnt_W
            val1 = (x + y) + 2 * min(k, cnt_S + cnt_W)
            # Quadrant 2 (sx=1, sy=-1): base = x - y, bad = cnt_N + cnt_W
            val2 = (x - y) + 2 * min(k, cnt_N + cnt_W)
            # Quadrant 3 (sx=-1, sy=1): base = -x + y, bad = cnt_S + cnt_E
            val3 = (-x + y) + 2 * min(k, cnt_S + cnt_E)
            # Quadrant 4 (sx=-1, sy=-1): base = -x - y, bad = cnt_N + cnt_E
            val4 = (-x - y) + 2 * min(k, cnt_N + cnt_E)

            ans = max(ans, val1, val2, val3, val4)

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Hash Table, Math, String, Counting
#
# 解题思路:
# 1. 曼哈顿距离 |x| + |y| = max(x+y, x-y, -x+y, -x-y)，即四个象限的线性组合的最大值
# 2. 对每个前缀位置，维护四个方向 (N, S, E, W) 的计数
# 3. 对于每个象限 (sx, sy)，计算：
#    - base = sx * x + sy * y（当前位置在该象限的投影值）
#    - bad = 该象限中贡献为负的步数
#    - 最多可将 min(k, bad) 个"坏步"改为"好步"，每改一个收益为 +2
#    - 该象限的曼哈顿距离上限 = base + 2 * min(k, bad)
# 4. 四个象限取最大值，再对所有前缀取最大值
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - |x|+|y| 分解为 4 个线性形式，分别最大化
# - 每改变一步使贡献从 -1 变为 +1，净收益为 2
# - 必须遍历每个前缀取最大值（早期前缀可能比完整字符串更优）
