"""
LeetCode #3310 - Remove Methods From Project
移除可疑的方法
https://leetcode.cn/problems/remove-methods-from-project/

你正在维护一个项目，该项目有 `n` 个方法，编号从 `0` 到 `n - 1`。
给你两个整数 `n` 和 `k`，以及一个二维整数数组 `invocations`，其中 `invocations[i] = [a_i, b_i]` 表示方法 `a_i` 调用了方法 `b_i`。
已知如果方法 `k` 存在一个已知的 bug。那么方法 `k` 以及它直接或间接调用的任何方法都被视为 可疑方法 ，我们需要从项目中移除这些方法。
只有当一组方法没有被这组之外的任何方法调用时，这组方法才能被移除。
返回一个数组，包含移除所有 可疑方法 后剩下的所有方法。你可以以任意顺序返回答案。如果无法移除 所有 可疑方法，则 不 移除任何方法。

示例 1:

输入: n = 4, k = 1, invocations = [[1,2],[0,1],[3,2]]
输出: [0,1,2,3]
解释:

方法 2 和方法 1 是可疑方法，但它们分别直接被方法 3 和方法 0 调用。由于方法 3 和方法 0 不是可疑方法，我们无法移除任何方法，故返回所有方法。
示例 2:

输入: n = 5, k = 0, invocations = [[1,2],[0,2],[0,1],[3,4]]
输出: [3,4]
解释:

方法 0、方法 1 和方法 2 是可疑方法，且没有被任何其他方法直接调用。我们可以移除它们。
示例 3:

输入: n = 3, k = 2, invocations = [[1,2],[0,1],[2,0]]
输出: []
解释:

所有方法都是可疑方法。我们可以移除它们。

提示:
`1 <= n <= 10^5`
`0 <= k <= n - 1`
`0 <= invocations.length <= 2 * 10^5`
`invocations[i] == [a_i, b_i]`
`0 <= a_i, b_i <= n - 1`
`a_i != b_i`
`invocations[i] != invocations[j]`
"""

from typing import List, Optional


class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # 构建邻接表
        adj = [[] for _ in range(n)]
        in_degree = [[] for _ in range(n)]  # 反向边：谁调用了谁
        for a, b in invocations:
            adj[a].append(b)
            in_degree[b].append(a)

        # DFS 找到所有可疑方法（从 k 可达的）
        suspicious = set()
        stack = [k]
        while stack:
            u = stack.pop()
            if u in suspicious:
                continue
            suspicious.add(u)
            for v in adj[u]:
                if v not in suspicious:
                    stack.append(v)

        # 检查是否有外部方法调用了可疑方法
        can_remove = True
        for u in suspicious:
            for caller in in_degree[u]:
                if caller not in suspicious:
                    can_remove = False
                    break
            if not can_remove:
                break

        if can_remove:
            return [i for i in range(n) if i not in suspicious]
        else:
            return list(range(n))










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Depth-First Search, Breadth-First Search, Graph
#
# 解题思路:
# 1. 用 DFS/BFS 从方法 k 出发，找到所有可达的方法（可疑方法集合）。
# 2. 检查可疑方法是否被外部方法调用：遍历可疑集合中每个方法，
#    检查其调用者（反向边）是否有来自可疑集合外部的。
# 3. 如果满足移除条件（所有调用都来自可疑集合内部），
#    返回非可疑方法；否则返回全部方法。
#
# 时间复杂度: O(n + m) — m = len(invocations)
# 空间复杂度: O(n + m)
#
# 关键点:
# - 构建正向图（DFS 找可疑方法）和反向图（检查外部调用）
# - 移除条件：可疑方法不能在外部有调用者
