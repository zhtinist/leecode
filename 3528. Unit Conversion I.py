"""
LeetCode #3528 - Unit Conversion I
单位转换 I
https://leetcode.cn/problems/unit-conversion-i/

有 `n` 种单位，编号从 `0` 到 `n - 1`。给你一个二维整数数组 `conversions`，长度为 `n - 1`，其中 `conversions[i] = [sourceUnit_i, targetUnit_i, conversionFactor_i]` ，表示一个 `sourceUnit_i` 类型的单位等于 `conversionFactor_i` 个 `targetUnit_i` 类型的单位。
请你返回一个长度为 `n` 的数组 `baseUnitConversion`，其中 `baseUnitConversion[i]` 表示 一个 0 类型单位等于多少个 i 类型单位。由于结果可能很大，请返回每个 `baseUnitConversion[i]` 对 `10^9 + 7` 取模后的值。

示例 1：

输入： conversions = [[0,1,2],[1,2,3]]
输出： [1,2,6]
解释：
使用 `conversions[0]`：将一个 0 类型单位转换为 2 个 1 类型单位。
使用 `conversions[0]` 和 `conversions[1]` 将一个 0 类型单位转换为 6 个 2 类型单位。
示例 2：

输入： conversions = [[0,1,2],[0,2,3],[1,3,4],[1,4,5],[2,5,2],[4,6,3],[5,7,4]]
输出： [1,2,3,8,10,6,30,24]
解释：
使用 `conversions[0]` 将一个 0 类型单位转换为 2 个 1 类型单位。
使用 `conversions[1]` 将一个 0 类型单位转换为 3 个 2 类型单位。
使用 `conversions[0]` 和 `conversions[2]` 将一个 0 类型单位转换为 8 个 3 类型单位。
使用 `conversions[0]` 和 `conversions[3]` 将一个 0 类型单位转换为 10 个 4 类型单位。
使用 `conversions[1]` 和 `conversions[4]` 将一个 0 类型单位转换为 6 个 5 类型单位。
使用 `conversions[0]`、`conversions[3]` 和 `conversions[5]` 将一个 0 类型单位转换为 30 个 6 类型单位。
使用 `conversions[1]`、`conversions[4]` 和 `conversions[6]` 将一个 0 类型单位转换为 24 个 7 类型单位。

提示：
`2 <= n <= 10^5`
`conversions.length == n - 1`
`0 <= sourceUnit_i, targetUnit_i < n`
`1 <= conversionFactor_i <= 10^9`
保证单位 0 可以通过 唯一 的转换路径（不需要反向转换）转换为任何其他单位。
"""

from typing import List, Optional


class Solution:
    def baseUnitConversion(self, conversions: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7
        n = len(conversions) + 1
        adj = [[] for _ in range(n)]
        for u, v, f in conversions:
            adj[u].append((v, f, True))   # u -> v: 1 u = f * v
            adj[v].append((u, f, False))  # v -> u: 1 v = (1/f) * u

        ans = [0] * n
        ans[0] = 1

        def dfs(u, parent):
            for v, f, is_forward in adj[u]:
                if v == parent:
                    continue
                if is_forward:
                    ans[v] = ans[u] * f % MOD
                else:
                    ans[v] = ans[u] * pow(f, MOD - 2, MOD) % MOD
                dfs(v, u)

        dfs(0, -1)
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Depth-First Search, Breadth-First Search, Graph
#
# 解题思路:
# 1. 转换关系构成一棵树（n 个节点，n-1 条边）
# 2. 建立邻接表，每条边记录方向（source→target 或 target→source）
# 3. 从节点 0 开始 DFS，传播转换因子：
#    - 沿 source→target 方向：ans[child] = ans[parent] * factor % MOD
#    - 沿相反方向：ans[child] = ans[parent] * inv(factor) % MOD
# 4. 模逆元使用费马小定理：inv(f) = f^(MOD-2) % MOD
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 保证从 0 到任意节点路径唯一（树结构）
# - 模运算处理大数
# - 双向边需要记录方向以正确选择乘/除
