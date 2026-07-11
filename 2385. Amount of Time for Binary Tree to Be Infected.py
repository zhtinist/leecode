"""
LeetCode #2385 - Amount of Time for Binary Tree to Be Infected
感染二叉树需要的总时间
https://leetcode.cn/problems/amount-of-time-for-binary-tree-to-be-infected/

给你一棵二叉树的根节点 `root` ，二叉树中节点的值 互不相同 。另给你一个整数 `start` 。在第 `0` 分钟，感染 将会从值为 `start` 的节点开始爆发。
每分钟，如果节点满足以下全部条件，就会被感染：
节点此前还没有感染。
节点与一个已感染节点相邻。
返回感染整棵树需要的分钟数。

示例 1：
输入：root = [1,5,3,null,4,10,6,9,2], start = 3 输出：4 解释：节点按以下过程被感染： - 第 0 分钟：节点 3 - 第 1 分钟：节点 1、10、6 - 第 2 分钟：节点5 - 第 3 分钟：节点 4 - 第 4 分钟：节点 9 和 2 感染整棵树需要 4 分钟，所以返回 4 。
示例 2：
输入：root = [1], start = 1 输出：0 解释：第 0 分钟，树中唯一一个节点处于感染状态，返回 0 。

提示：
树中节点的数目在范围 `[1, 10^5]` 内
`1 <= Node.val <= 10^5`
每个节点的值 互不相同
树中必定存在值为 `start` 的节点
"""

from typing import List, Optional


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        """
        Build a parent map via DFS to treat the tree as an undirected graph,
        then BFS from the start node to find the maximum distance.
        """
        from collections import deque

        # Step 1: Build parent map and locate the start node
        parent = {}
        start_node = None

        def dfs(node: Optional[TreeNode], par: Optional[TreeNode]) -> None:
            nonlocal start_node
            if not node:
                return
            if node.val == start:
                start_node = node
            if par:
                parent[node] = par
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        # Step 2: BFS from start_node to find max distance
        queue = deque([start_node])
        visited = {start_node}
        minutes = -1

        while queue:
            minutes += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                # Check neighbors: parent, left child, right child
                neighbors = []
                if node in parent:
                    neighbors.append(parent[node])
                if node.left:
                    neighbors.append(node.left)
                if node.right:
                    neighbors.append(node.right)

                for nei in neighbors:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)

        return minutes



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Tree, Depth-First Search, Breadth-First Search, Hash Table, Binary Tree
#
# 解题思路:
# 1. 使用 DFS 遍历整棵树，建立每个节点到其父节点的映射（parent map），同时定位值为 start 的节点。
# 2. 将树视为无向图：每个节点有三条边（父节点、左子节点、右子节点）。
# 3. 从 start 节点开始 BFS，层序遍历。每遍历一层，分钟数+1。
# 4. BFS 结束时，分钟数即为感染整棵树所需的最长时间（最大距离）。
#
# 时间复杂度: O(n) — 每个节点在 DFS 和 BFS 中各访问一次
# 空间复杂度: O(n) — parent map 和 visited set 以及 BFS 队列
#
# 关键点:
# - 核心是将二叉树转换为无向图（通过父节点映射）
# - BFS 层序遍历天然适合计算"传播时间"这类逐层扩展的问题
# - 注意 parent map 的构建：根节点没有父节点
