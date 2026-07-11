"""
LeetCode #3603 - Minimum Cost Path with Alternating Directions II
交替方向的最小路径代价 II
https://leetcode.cn/problems/minimum-cost-path-with-alternating-directions-ii/

给你两个整数 `m` 和 `n`，分别表示网格的行数和列数。
进入单元格 `(i, j)` 的成本定义为 `(i + 1) * (j + 1)`。
另外给你一个二维整数数组 `waitCost`，其中 `waitCost[i][j]` 定义了在该单元格 等待 的成本。
路径始终从第 1 步进入单元格 `(0, 0)` 并支付入场花费开始。
每一步，你都遵循交替模式：
在 奇数秒 ，你必须向 右 或向 下 移动到 相邻 的单元格，并支付其进入成本。
在 偶数秒 ，你必须原地 等待恰好 1 秒并在 1 秒期间支付 `waitCost[i][j]`。
返回到达 `(m - 1, n - 1)` 所需的 最小 总成本。

示例 1：

输入：m = 1, n = 2, waitCost = [[1,2]]
输出：3
解释：
最佳路径为：
从第 1 秒开始在单元格 `(0, 0)`，进入成本为 `(0 + 1) * (0 + 1) = 1`。
第 1 秒：向右移动到单元格 `(0, 1)`，进入成本为 `(0 + 1) * (1 + 1) = 2`。
因此，总成本为 `1 + 2 = 3`。
示例 2：

输入：m = 2, n = 2, waitCost = [[3,5],[2,4]]
输出：9
解释：
最佳路径为：
从第 1 秒开始在单元格 `(0, 0)`，进入成本为 `(0 + 1) * (0 + 1) = 1`。
第 1 秒：向下移动到单元格 `(1, 0)`，进入成本为 `(1 + 1) * (0 + 1) = 2`。
第 2 秒：在单元格 `(1, 0)` 等待，支付 `waitCost[1][0] = 2`。
第 3 秒：向右移动到单元格 `(1, 1)`，进入成本为 `(1 + 1) * (1 + 1) = 4`。
因此，总成本为 `1 + 2 + 2 + 4 = 9`。
示例 3：

输入：m = 2, n = 3, waitCost = [[6,1,4],[3,2,5]]
输出：16
解释：
最佳路径为：
从第 1 秒开始在单元格 `(0, 0)`，进入成本为 `(0 + 1) * (0 + 1) = 1`。
第 1 秒：向右移动到单元格 `(0, 1)`，进入成本为 `(0 + 1) * (1 + 1) = 2`。
第 2 秒：在单元格 `(0, 1)` 等待，支付 `waitCost[0][1] = 1`。
第 3 秒：向下移动到单元格 `(1, 1)`，进入成本为 `(1 + 1) * (1 + 1) = 4`。
第 4 秒：在单元格 `(1, 1)` 等待，支付 `waitCost[1][1] = 2`。
第 5 秒：向右移动到单元格 `(1, 2)`，进入成本为 `(1 + 1) * (2 + 1) = 6`。
因此，总成本为 `1 + 2 + 1 + 4 + 2 + 6 = 16`。

提示：
`1 <= m, n <= 10^5`
`2 <= m * n <= 10^5`
`waitCost.length == m`
`waitCost[0].length == n`
`0 <= waitCost[i][j] <= 10^5`
"""

from typing import List, Optional


class Solution:
    def minCostPath(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        """
        DP approach:
        - dp_odd[i][j]: min cost when at (i,j), next second is ODD (must move).
          This state is reached after waiting at (i,j) on an even second.
        - dp_even[i][j]: min cost when at (i,j), next second is EVEN (must wait).
          This state is reached after moving into (i,j) on an odd second.

        Transitions:
        - From dp_even[i][j] (just moved in): wait -> dp_odd[i][j]
          dp_odd[i][j] = dp_even[i][j] + waitCost[i][j]
        - From dp_odd[i][j] (just waited): move right/down -> neighbor's dp_even
          dp_even[i+1][j] = dp_odd[i][j] + entry(i+1, j)
          dp_even[i][j+1] = dp_odd[i][j] + entry(i, j+1)
        """

        INF = float('inf')
        dp_odd = [[INF] * n for _ in range(m)]
        dp_even = [[INF] * n for _ in range(m)]

        # Initial state: entered (0,0) at start, next second is ODD (move)
        dp_odd[0][0] = (0 + 1) * (0 + 1)  # = 1

        for i in range(m):
            for j in range(n):
                # Step 1: From dp_even (just moved in) -> wait -> dp_odd
                if dp_even[i][j] != INF:
                    # If this is the target, we can stop (arrived, no need to wait)
                    if i == m - 1 and j == n - 1:
                        continue
                    new_cost = dp_even[i][j] + waitCost[i][j]
                    if new_cost < dp_odd[i][j]:
                        dp_odd[i][j] = new_cost

                # Step 2: From dp_odd (just waited) -> move -> neighbor's dp_even
                if dp_odd[i][j] != INF:
                    # Move down to (i+1, j)
                    if i + 1 < m:
                        entry_cost = (i + 2) * (j + 1)
                        new_cost = dp_odd[i][j] + entry_cost
                        if new_cost < dp_even[i + 1][j]:
                            dp_even[i + 1][j] = new_cost
                    # Move right to (i, j+1)
                    if j + 1 < n:
                        entry_cost = (i + 1) * (j + 2)
                        new_cost = dp_odd[i][j] + entry_cost
                        if new_cost < dp_even[i][j + 1]:
                            dp_even[i][j + 1] = new_cost

        return dp_even[m - 1][n - 1]











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Dynamic Programming, Matrix
#
# 解题思路:
# 这是一个特殊的网格最短路径问题。关键洞察是移动和等待的交替模式：
#
# DP 状态定义：
# - dp_odd[i][j]: 在单元格 (i,j) 刚完成等待（偶数秒结束），下一步为奇数秒（必须移动）
# - dp_even[i][j]: 在单元格 (i,j) 刚完成移动（奇数秒结束），下一步为偶数秒（必须等待）
#
# 转移：
# 1. 等待（even -> odd）：dp_odd[i][j] = dp_even[i][j] + waitCost[i][j]
#    在偶数秒原地等待 1 秒并支付等待成本。
# 2. 移动（odd -> even）：
#    - 向下移动：dp_even[i+1][j] = dp_odd[i][j] + (i+2)*(j+1)
#    - 向右移动：dp_even[i][j+1] = dp_odd[i][j] + (i+1)*(j+2)
#    在奇数秒移动到相邻单元格并支付该单元格的进入成本。
#
# 初始状态：dp_odd[0][0] = 1（初始进入 (0,0)，支付进入成本，下一步为奇数秒）
# 终止条件：到达 (m-1, n-1) 后可以立即停止（不需要等待），答案 = dp_even[m-1][n-1]
#
# 按行优先顺序遍历单元格，因为所有转移都是从左/上到右/下，
# 加上同单元格的等待边（even->odd），构成一个 DAG。
#
# 时间复杂度: O(M * N)，每个单元格处理一次
# 空间复杂度: O(M * N)，存储两个 DP 矩阵
#
# 关键点:
# - 初始进入 (0,0) 的成本是 1（(0+1)*(0+1)），这发生在第一步（奇数秒）之前
# - 进入 (0,0) 后不需要等待，直接进入第一个奇数秒开始移动
# - 只能在到达目标单元格后的奇数秒结束（刚移动进去），不需要等待
# - 由于移动只能向右/向下，DP 按行优先顺序天然满足拓扑序
