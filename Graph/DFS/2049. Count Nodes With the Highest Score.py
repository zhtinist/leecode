"""
LeetCode #2049 - Count Nodes With the Highest Score
统计最高分的节点数目
https://leetcode.cn/problems/count-nodes-with-the-highest-score/

给你一棵根节点为 `0` 的 二叉树 ，它总共有 `n` 个节点，节点编号为 `0` 到 `n - 1` 。同时给你一个下标从 0 开始的整数数组 `parents` 表示这棵树，其中 `parents[i]` 是节点 `i` 的父节点。由于节点 `0` 是根，所以 `parents[0] == -1` 。
一个子树的 大小 为这个子树内节点的数目。每个节点都有一个与之关联的 分数 。求出某个节点分数的方法是，将这个节点和与它相连的边全部 删除 ，剩余部分是若干个 非空 子树，这个节点的 分数 为所有这些子树 大小的乘积 。
请你返回有 最高得分 节点的 数目 。

示例 1:

输入：parents = [-1,2,0,2,0] 输出：3 解释： - 节点 0 的分数为：3 * 1 = 3 - 节点 1 的分数为：4 = 4 - 节点 2 的分数为：1 * 1 * 2 = 2 - 节点 3 的分数为：4 = 4 - 节点 4 的分数为：4 = 4 最高得分为 4 ，有三个节点得分为 4 （分别是节点 1，3 和 4 ）。
示例 2：

输入：parents = [-1,2,0] 输出：2 解释： - 节点 0 的分数为：2 = 2 - 节点 1 的分数为：2 = 2 - 节点 2 的分数为：1 * 1 = 1 最高分数为 2 ，有两个节点分数为 2 （分别为节点 0 和 1 ）。

提示：
`n == parents.length`
`2 <= n <= 10^5`
`parents[0] == -1`
对于 `i != 0` ，有 `0 <= parents[i] <= n - 1`
`parents` 表示一棵二叉树。
"""

from typing import List, Optional


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        # Build children lists
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parents[i]].append(i)

        # Store size of each subtree
        size = [0] * n

        def dfs(node: int) -> int:
            total = 1
            for child in children[node]:
                total += dfs(child)
            size[node] = total
            return total

        dfs(0)

        max_score = 0
        count = 0

        for i in range(n):
            # Score = product of sizes of remaining components after removing node i
            product = 1
            remaining = n - 1  # nodes excluding i itself
            for child in children[i]:
                product *= size[child]
                remaining -= size[child]
            # The remaining part (parent side) if not root
            if remaining > 0:
                product *= remaining

            if product > max_score:
                max_score = product
                count = 1
            elif product == max_score:
                count += 1

        return count



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Tree, Depth-First Search, Array, Binary Tree
#
# 解题思路:
# 构建树的子节点列表，使用DFS计算每个节点的子树大小。
# 对于节点i，移除后的剩余部分包括：各子树（大小=size[child]）和父节点方向部分
# （大小=n-1-所有子树大小之和）。分数 = 这些部分大小的乘积。
# 遍历所有节点计算得分，统计最高分的节点数量。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - DFS后序遍历计算子树大小
# - 父节点方向部分 = n - 1 - sum(子树大小)
# - 使用乘积可能很大，但Python支持大整数
