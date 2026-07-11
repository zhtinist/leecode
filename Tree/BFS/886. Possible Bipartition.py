"""
LeetCode #886 - Possible Bipartition
中文题名：可能的二分法
https://leetcode.com/problems/possible-bipartition/

Given a set of `N` people (numbered `1, 2, ..., N`), we would like
to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same
group.

Formally, if `dislikes[i] = [a, b]`, it means it is not allowed to put the people
numbered `a` and `b` into the same group.

Return `true` if and only if it is possible to split everyone into two groups
in this way.

【中文翻译】

给定 `N` 个人（编号从 `1` 到 `N`），我们希望将所有人分成任意大小的两组。

每个人可能不喜欢某些其他人，他们不应该被分到同一组。

形式上，如果 `dislikes[i] = [a, b]`，表示不允许将编号为 `a` 和 `b` 的人分到同一组。

当且仅当可以按这种方式将所有人分成两组时，返回 `true`。

"""

from typing import List, Optional


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        # 构建邻接表（1-indexed）
        graph = [[] for _ in range(N + 1)]
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        # 0: 未染色, 1: 红色, -1: 蓝色
        color = [0] * (N + 1)

        def dfs(node: int, c: int) -> bool:
            color[node] = c
            for neighbor in graph[node]:
                if color[neighbor] == c:
                    return False  # 邻居颜色相同，冲突
                if color[neighbor] == 0 and not dfs(neighbor, -c):
                    return False
            return True

        for i in range(1, N + 1):
            if color[i] == 0:
                if not dfs(i, 1):
                    return False

        return True



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 二分图检测问题。将 dislikes 关系构造成无向图。
# 使用 DFS 对图进行染色（二着色）：
# - 从每个未染色的节点开始，染成颜色1
# - 对其所有邻居染相反颜色(-1)
# - 如果发现邻居颜色与当前节点相同，则冲突，返回 False
# - 遍历所有节点确保所有连通分量都被检查
#
# 时间复杂度: O(N + E) — N为人数，E为dislikes关系数
# 空间复杂度: O(N + E) — 邻接表和颜色数组
#
# 关键点:
# - 等价于判断图是否为二分图
# - 图可能不连通，需要遍历所有节点
# - BFS 也可以实现，思路相同
