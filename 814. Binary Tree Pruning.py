"""
LeetCode #814 - Binary Tree Pruning
中文题名：二叉树剪枝
https://leetcode.com/problems/binary-tree-pruning/

We are given the head node `root` of a binary tree, where additionally every
node's value is either a 0 or a 1.

Return the same tree where every subtree (of the given tree) not containing a 1 has been
removed.

(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

Example 1:
Input: [1,null,0,0,1]
Output: [1,null,0,null,1]

Explanation:
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.

Example 2:
Input: [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]

Example 3:
Input: [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]

Note:

The binary tree will have at most `100 nodes`.

The value of each node will only be `0` or `1`.

【中文翻译】
给定树节点 `root`，每个节点的值都是 0 或 1。

返回移除了所有不包含 1 的子树的同一棵树。

（回忆：节点 X 的子树是 X 加上 X 的所有后代节点。）

示例 1：
输入：[1,null,0,0,1]
输出：[1,null,0,null,1]
解释：只有红色节点满足"每个不包含 1 的子树"的属性。右图表示答案。

示例 2：
输入：[1,0,1,0,0,0,1]
输出：[1,null,1,null,1]

示例 3：
输入：[1,1,0,1,1,0,1,0]
输出：[1,1,0,1,1,null,1]

注意：
二叉树最多有 `100 个节点`。
每个节点的值仅为 `0` 或 `1`。
"""

from typing import List, Optional


class Solution:
    def pruneTree(self, root: Optional['TreeNode']) -> Optional['TreeNode']:
        if root is None:
            return None

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        if root.val == 0 and root.left is None and root.right is None:
            return None

        return root



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 后序遍历（DFS）：先递归处理左右子树，再判断当前节点。
# 如果当前节点值为 0 且左右子树都被剪掉（变为 None），
# 说明以当前节点为根的子树不包含任何 1，应剪掉（返回 None）。
# 如果当前节点值为 1，或任一子树不为空（包含 1），
# 则保留当前节点，返回更新后的节点。
#
# 时间复杂度: O(N) - 每个节点访问一次
# 空间复杂度: O(H) - 递归栈深度，H 为树高，最坏 O(N)
#
# 关键点:
# - 后序遍历确保先处理子树再处理根节点
# - 剪枝条件：值为 0 且左右子树都为空
# - 需要将递归结果赋值回 root.left/right
