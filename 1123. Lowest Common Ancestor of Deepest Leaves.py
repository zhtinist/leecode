"""
LeetCode #1123 - Lowest Common Ancestor of Deepest Leaves
中文题名：最深叶节点的最近公共祖先
https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

Given a rooted binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

The node of a binary tree is a leaf if and only if it has no children

The depth of the root of the tree is 0, and if the depth of a node is
`d`, the depth of each of its children is `d+1`.

The lowest common ancestor of a set `S` of nodes is the node
`A` with the largest depth such that every node in S is in the subtree with
root `A`.

Example 1:

Input: root = [1,2,3]
Output: [1,2,3]
Explanation:
The deepest leaves are the nodes with values 2 and 3.
The lowest common ancestor of these leaves is the node with value 1.
The answer returned is a TreeNode object (not an array) with serialization "[1,2,3]".

Example 2:

Input: root = [1,2,3,4]
Output: [4]

Example 3:

Input: root = [1,2,3,4,5]
Output: [2,4,5]

Constraints:

The given tree will have between 1 and 1000 nodes.

Each node of the tree will have a distinct value between 1 and 1000.

【中文翻译】
给定一棵有根二叉树，返回其最深叶节点的最近公共祖先。

回顾定义：

二叉树的一个节点是叶子节点当且仅当它没有子节点。

树的根节点深度为 0，如果一个节点的深度为 d，则其每个子节点的深度为 d+1。

节点集合 S 的最近公共祖先是深度最大的节点 A，使得 S 中的每个节点都在以 A 为根的子树中。

示例 1：

输入：root = [1,2,3]
输出：[1,2,3]
解释：
最深叶节点是值为 2 和 3 的节点。
这些叶节点的最近公共祖先是值为 1 的节点。
返回的答案是一个 TreeNode 对象（不是数组），其序列化为 "[1,2,3]"。

示例 2：

输入：root = [1,2,3,4]
输出：[4]

示例 3：

输入：root = [1,2,3,4,5]
输出：[2,4,5]

约束条件：

给定的树有 1 到 1000 个节点。

树的每个节点有介于 1 到 1000 之间的不同值。
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return (0, None)
            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)
            if left_depth > right_depth:
                return (left_depth + 1, left_lca)
            elif right_depth > left_depth:
                return (right_depth + 1, right_lca)
            else:
                return (left_depth + 1, node)

        return dfs(root)[1]










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用 DFS 递归自底向上返回 (深度, LCA节点) 对。
# 1. 对于空节点返回 (0, None)。
# 2. 对于每个节点，递归获取左子树和右子树的 (深度, LCA)。
# 3. 比较左右子树的最深叶节点深度：
#    - 若左子树更深：最深叶节点全在左子树，LCA 就是左子树的 LCA，深度 +1。
#    - 若右子树更深：同理，LCA 是右子树的 LCA，深度 +1。
#    - 若左右深度相等：当前节点就是左右最深叶节点的 LCA，深度 +1。
# 4. 最终返回根节点调用结果的 LCA 部分。
#
# 时间复杂度: O(n) - 每个节点访问一次
# 空间复杂度: O(h) - 递归调用栈深度，h 为树高，最坏 O(n)
#
# 关键点:
# - 返回二元组 (深度, LCA)，同时传递深度和 LCA 信息
# - 当左右子树深度相等时，当前节点即为 LCA
# - 此题与 LeetCode #865 完全相同
