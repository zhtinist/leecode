"""
LeetCode #257 - Binary Tree Paths
中文题名：二叉树的所有路径
https://leetcode.com/problems/binary-tree-paths/

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

1
/   \
2     3
\
5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

【中文翻译】
给定一个二叉树，返回所有从根节点到叶子节点的路径。

注意：叶子节点是指没有子节点的节点。

示例：

输入：

1
/   \
2     3
\
5

输出：["1->2->5", "1->3"]

解释：所有根到叶的路径为：1->2->5, 1->3
"""

from typing import List, Optional


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def dfs(node, path):
            if not node:
                return

            # 追加当前节点值
            if path:
                path += "->" + str(node.val)
            else:
                path = str(node.val)

            # 叶子节点：记录路径
            if not node.left and not node.right:
                res.append(path)
                return

            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")
        return res


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Easy
# Paid Only: No
#
# 解题思路：
# 使用深度优先搜索（DFS），从根节点出发，沿途构建路径字符串。
# 每次递归将当前节点值追加到路径中（非根节点前加 "->"）。
# 到达叶子节点（左右子节点均为空）时将完整路径加入结果列表。
#
# 时间复杂度: O(n) — 每个节点访问一次
# 空间复杂度: O(h) — 递归栈深度，h 为树高
#
# 关键点：
# - DFS 前序遍历
# - 叶子节点的判断：左右均为空
# - 路径字符串构建：用 "->" 连接节点值
