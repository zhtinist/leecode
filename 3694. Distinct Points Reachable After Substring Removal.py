"""
LeetCode #3694 - Distinct Points Reachable After Substring Removal
删除子字符串后不同的终点
https://leetcode.cn/problems/distinct-points-reachable-after-substring-removal/

给你一个由字符 `'U'`、`'D'`、`'L'` 和 `'R'` 组成的字符串 `s`，表示在无限的二维笛卡尔网格上的移动。
`'U'`: 从 `(x, y)` 移动到 `(x, y + 1)`。
`'D'`: 从 `(x, y)` 移动到 `(x, y - 1)`。
`'L'`: 从 `(x, y)` 移动到 `(x - 1, y)`。
`'R'`: 从 `(x, y)` 移动到 `(x + 1, y)`。
你还得到了一个正整数 `k`。
你 必须 选择并移除 恰好一个 长度为 `k` 的连续子字符串 `s`。然后，从坐标 `(0, 0)` 开始，按顺序执行剩余的移动。
返回可到达的 不同 最终坐标的数量。

示例 1:

输入：s = "LUL", k = 1
输出：2
解释：
移除长度为 1 的子字符串后，`s` 可以是 `"UL"`、`"LL"` 或 `"LU"`。执行这些移动后，最终坐标将分别是 `(-1, 1)`、`(-2, 0)` 和 `(-1, 1)`。有两个不同的点 `(-1, 1)` 和 `(-2, 0)`，因此答案是 2。
示例 2:

输入：s = "UDLR", k = 4
输出：1
解释：
移除长度为 4 的子字符串后，`s` 只能是空字符串。最终坐标将是 `(0, 0)`。只有一个不同的点 `(0, 0)`，因此答案是 1。
示例 3:

输入：s = "UU", k = 1
输出：1
解释：
移除长度为 1 的子字符串后，`s` 变为 `"U"`，它总是以 `(0, 1)` 结束，因此只有一个不同的最终坐标。

提示:
`1 <= s.length <= 10^5`
`s` 只包含 `'U'`、`'D'`、`'L'` 和 `'R'`。
`1 <= k <= s.length`
"""

from typing import List, Optional


class Solution:
    def distinctPositions(self, s: str, k: int) -> int:
        dir_map = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
        n = len(s)

        # Prefix sums of dx, dy
        pref_x = [0] * (n + 1)
        pref_y = [0] * (n + 1)
        for i, ch in enumerate(s):
            dx, dy = dir_map[ch]
            pref_x[i + 1] = pref_x[i] + dx
            pref_y[i + 1] = pref_y[i] + dy

        total_x, total_y = pref_x[n], pref_y[n]
        positions = set()

        # Try removing each window of length k
        for i in range(n - k + 1):
            win_dx = pref_x[i + k] - pref_x[i]
            win_dy = pref_y[i + k] - pref_y[i]
            final_x = total_x - win_dx
            final_y = total_y - win_dy
            positions.add((final_x, final_y))

        return len(positions)










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Hash Table, String, Prefix Sum, Sliding Window
#
# 解题思路:
# 先计算整个移动序列的前缀和（x 和 y 方向上的累计位移）。
# 完整路径的终点是 (total_x, total_y)。
# 对于每个长度为 k 的窗口 [i, i+k-1]，该窗口被移除后，
# 剩余路径的终点 = (total_x - window_dx, total_y - window_dy)。
# 遍历所有可能的移除窗口，用集合收集不同的终点坐标，最后返回集合大小。
#
# 时间复杂度: O(n) — 遍历所有 n-k+1 个窗口，每个 O(1) 计算
# 空间复杂度: O(n) — 存储前缀和数组和结果集合
#
# 关键点:
# - 移除子串相当于从总位移中减去该子串的位移贡献
# - 前缀和将窗口位移计算优化为 O(1)
