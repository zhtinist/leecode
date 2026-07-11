"""
LeetCode #3669 - Balanced K-Factor Decomposition
K 因数分解
https://leetcode.cn/problems/balanced-k-factor-decomposition/

给你两个整数 `n` 和 `k`，将数字 `n` 恰好分割成 `k` 个正整数，使得这些整数的 乘积 等于 `n`。
返回一个分割方案，使得这些数字中 最大值 和 最小值 之间的 差值 最小化。结果可以以 任意顺序 返回。

示例 1：

输入：n = 100, k = 2
输出：[10,10]
解释：
分割方案 `[10, 10]` 的结果是 `10 * 10 = 100`，且最大值与最小值的差值为 0，这是最小可能值。
示例 2：

输入：n = 44, k = 3
输出：[2,2,11]
解释：
分割方案 `[1, 1, 44]` 的差值为 43
分割方案 `[1, 2, 22]` 的差值为 21
分割方案 `[1, 4, 11]` 的差值为 10
分割方案 `[2, 2, 11]` 的差值为 9
因此，`[2, 2, 11]` 是最优分割方案，其差值最小，为 9。

提示：
`4 <= n <= 10^5`
`2 <= k <= 5`
`k` 严格小于 `n` 的正因数的总数。
"""

from typing import List, Optional


class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        # 预计算所有数的因子表
        divisors = [[] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(i, n + 1, i):
                divisors[j].append(i)

        ans = None
        path = [0] * k
        best = float('inf')

        def dfs(idx: int, remaining: int, cur_min: int, cur_max: int):
            nonlocal ans, best
            if idx == 0:
                # 最后一个因子直接由 remaining 决定
                d = max(cur_max, remaining) - min(cur_min, remaining)
                if d < best:
                    best = d
                    path[idx] = remaining
                    ans = path[:]
                return
            for d in divisors[remaining]:
                new_min = min(cur_min, d)
                new_max = max(cur_max, d)
                # 剪枝：当前差值已不可能优于最优解
                if new_max - new_min >= best:
                    continue
                path[idx] = d
                dfs(idx - 1, remaining // d, new_min, new_max)

        dfs(k - 1, n, float('inf'), 0)
        return ans if ans else []










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Math, Backtracking, Number Theory
#
# 解题思路:
# 1. 预计算 1 到 n 的所有因子（筛法，O(n*log n)）。
# 2. DFS 回溯搜索恰好 k 个因子使其乘积等于 n：
#    - 每一步选择一个因子 d（d 整除当前 remaining）
#    - 递归处理 remaining // d，因子数减 1
#    - 维护当前已选因子的最小值和最大值
# 3. 当只剩 1 个因子时，由 remaining 确定最后一个因子，计算 max-min 差值并更新最优解。
# 4. 剪枝：如果当前 max-min 已经 >= 已知最优解，提前返回。
# 5. k <= 5 且 n <= 10^5，搜索空间很小，DFS 可以在时限内完成。
#
# 时间复杂度: O(d^k)，其中 d 为因子数量，k <= 5。预处理 O(n*log n)
# 空间复杂度: O(n + k)，因子表 O(n*log n)，递归栈 O(k)
#
# 关键点:
# - 因子可以重复使用（如 100 = 10*10），DFS 中对同一因子可以多次选择
# - 预计算因子表避免每次重复计算 sqrt(n)
# - 剪枝条件 new_max - new_min >= best 大幅减少搜索分支
