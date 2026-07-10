"""
LeetCode #199 - Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/

Given a binary tree, imagine yourself standing on the *right* side of it, return the
values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

1            <---
/   \
2     3         <---
\     \
5     4       <---
"""

from typing import List, Optional


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        from collections import deque
        queue = deque([root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                # The last node in each level is visible from the right side
                if i == level_size - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用 BFS（层序遍历）。从右侧看二叉树，每一层只能看到最右边的节点。
# 因此做层序遍历时，记录每层最后一个节点即可。
#
# 具体步骤：
# 1. 使用队列进行 BFS，每次处理一层
# 2. 对于每层的所有节点，记录最后一个节点（i == level_size - 1）
# 3. 将子节点按左-右顺序入队（确保右侧节点在队尾）
#
# 时间复杂度: O(N) — 每个节点访问一次
# 空间复杂度: O(W) — 队列最大宽度，最坏 O(N)
#
# 关键点:
# - BFS 天然按层处理
# - 每层最后被处理的节点就是右视图看到的节点
# - 也可以用 DFS（根-右-左遍历，记录每层第一个访问的节点）
