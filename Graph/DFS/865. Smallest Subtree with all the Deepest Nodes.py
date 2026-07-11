"""
LeetCode #865 - Smallest Subtree with all the Deepest Nodes
中文题名：具有所有最深节点的最小子树
https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

Given a binary tree rooted at `root`, the depth of each node is the
shortest distance to the root.

A node is deepest if it has the largest depth possible among any node in the
entire tree.

The subtree of a node is that node, plus the set of all descendants of that node.

Return the node with the largest depth such that it contains all the deepest nodes in its
subtree.

Example 1:

Input: [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation:

We return the node with value 2, colored in yellow in the diagram.
The nodes colored in blue are the deepest nodes of the tree.
The input "[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]" is a serialization of the given tree.
The output "[2, 7, 4]" is a serialization of the subtree rooted at the node with value 2.
Both the input and output have TreeNode type.

Note:

The number of nodes in the tree will be between 1 and 500.

The values of each node are unique.

【中文翻译】
给定一个以 root 为根的二叉树，每个节点的深度是它到根的最短距离。

如果一个节点在整棵树中具有可能的最大深度，则它是"最深"的节点。

一个节点的子树包含该节点及其所有后代节点。

返回具有最大深度的节点，使得它的子树包含所有最深节点。

"""

from typing import List, Optional


class Solution:
    def subtreeWithAllDeepest(self, root: 'TreeNode') -> 'TreeNode':
        # DFS that returns (depth, LCA_subtree_root)
        def dfs(node: 'TreeNode') -> tuple:
            if not node:
                return (0, None)

            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)

            if left_depth > right_depth:
                return (left_depth + 1, left_lca)
            if right_depth > left_depth:
                return (right_depth + 1, right_lca)
            # Equal depths: current node is the LCA of deepest nodes on both sides
            return (left_depth + 1, node)

        _, lca = dfs(root)
        return lca



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用后序遍历（自底向上）DFS，同时返回两个信息：(子树深度, 子树中所有最深节点的LCA)。
# 递归处理：
# - 空节点返回 (0, None)
# - 递归处理左右子树
# - 比较左右子树深度：
#   - 如果左深度 > 右深度，说明最深节点只在左子树中，LCA 就是左子树的 LCA
#   - 如果右深度 > 左深度，同理 LCA 是右子树的 LCA
#   - 如果两边深度相等，说明当前节点是左右最深节点的 LCA，返回当前节点
# - 深度 +1 返回给上一层
# 这和"求最深叶节点的最近公共祖先"是同一个问题。
#
# 时间复杂度: O(N) 每个节点访问一次
# 空间复杂度: O(H) 递归栈深度，H 为树的高度
#
# 关键点:
# - 后序遍历返回 (深度, LCA子树)，一次遍历同时获取两个信息
# - 左右深度相等时，当前节点就是 LCA（包含所有最深节点的最小子树）
# - 实质是求最深叶节点的最近公共祖先（LCA of deepest leaves）
# - 与 LeetCode #1123 是同一道题
