"""
LeetCode #863 - All Nodes Distance K in Binary Tree
中文题名：二叉树中所有距离为 K 的节点
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

We are given a binary tree (with root node `root`), a `target`
node, and an integer value `K`.

Return a list of the values of all nodes that have a distance `K` from the
`target` node.  The answer can be returned in any order.

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation:
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.

Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.

Note:

The given tree is non-empty.

Each node in the tree has unique values `0 <= node.val <= 500`.

The `target` node is a node in the tree.

`0 <= K <= 1000`.

【中文翻译】
给定一个二叉树（根节点为 root）、一个目标节点 target 和一个整数值 K。

返回所有与 target 节点距离为 K 的节点的值列表。答案可以以任意顺序返回。

注意：输入中的 "root" 和 "target" 实际上是 TreeNode 类型。上述输入描述只是这些对象的序列化形式。

"""

from typing import List, Optional


class Solution:
    def distanceK(self, root: 'TreeNode', target: 'TreeNode', k: int) -> List[int]:
        # Build parent pointers via DFS
        from collections import deque

        parent = {}

        def dfs(node: 'TreeNode', par: 'TreeNode') -> None:
            if not node:
                return
            parent[node] = par
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        # BFS from target node to find all nodes at distance K
        queue = deque([(target, 0)])
        visited = {target}
        result = []

        while queue:
            node, dist = queue.popleft()
            if dist == k:
                result.append(node.val)
                continue  # Don't explore further from nodes at distance K
            if dist > k:
                continue

            # Neighbors: left child, right child, parent
            for neighbor in (node.left, node.right, parent.get(node)):
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 将二叉树视为无向图，因为距离可以向上（通过父节点）和向下（通过子节点）。
# 步骤 1：DFS 遍历树，为每个节点记录其父节点（parent 字典）。
# 步骤 2：从 target 节点开始进行 BFS，将左子节点、右子节点和父节点视为邻居。
# 使用 visited 集合防止重复访问。当 dist == K 时，将节点值加入结果列表。
# 当 dist == K 时不需要继续探索邻居（因为会更远）。
#
# 时间复杂度: O(N) 每个节点最多被访问两次（一次 DFS 建图，一次 BFS）
# 空间复杂度: O(N) parent 字典 + BFS 队列 + visited 集合
#
# 关键点:
# - 将二叉树视为无向图，通过记录父节点来实现向上遍历
# - BFS 从 target 出发，逐层扩展；当距离达到 K 时收集节点
# - 使用 visited 集合防止重复访问（特别是向上和向下可能形成环）
# - dist == K 后不需要继续扩展，可提前剪枝（continue）
