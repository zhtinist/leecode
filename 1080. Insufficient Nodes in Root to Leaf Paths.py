"""
LeetCode #1080 - Insufficient Nodes in Root to Leaf Paths
中文题名：根到叶路径上的不足节点
https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/

Given the `root` of a binary tree, consider all root to leaf paths:
paths from the root to any leaf.  (A leaf is a node with no children.)

A `node` is insufficient if every such root to leaf
path intersecting this `node` has sum strictly less than `limit`.

Delete all insufficient nodes simultaneously, and return the root of the resulting binary
tree.

Example 1:

Input: root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1

Output: [1,2,3,4,null,null,7,8,9,null,14]

Example 2:

Input: root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22

Output: [5,4,8,11,null,17,4,7,null,null,null,5]

Example 3:

Input: root = [1,2,-3,-5,null,4,null], limit = -1

Output: [1,null,-3,4]

【中文翻译】
给定二叉树的根节点 root，考虑所有从根到叶的路径：从根节点到任意叶子节点的路径。（叶子节点是没有子节点的节点。）

如果交于该节点的每条根到叶路径的总和均严格小于 limit，则该节点是 不足节点。

同时删除所有不足节点，并返回生成的二叉树的根节点。

示例 1：

输入：root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1
输出：[1,2,3,4,null,null,7,8,9,null,14]

示例 2：

输入：root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22
输出：[5,4,8,11,null,17,4,7,null,null,null,5]

示例 3：

输入：root = [1,2,-3,-5,null,4,null], limit = -1
输出：[1,null,-3,4]

"""

from typing import List, Optional


class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def dfs(node, cur_sum):
            if not node:
                return False

            cur_sum += node.val

            if not node.left and not node.right:
                return cur_sum >= limit

            left_ok = dfs(node.left, cur_sum)
            right_ok = dfs(node.right, cur_sum)

            if not left_ok:
                node.left = None
            if not right_ok:
                node.right = None

            return left_ok or right_ok

        root_ok = dfs(root, 0)
        return root if root_ok else None










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用后序遍历（DFS）判断每个节点的路径和是否"充足"。
# 定义 DFS(node, cur_sum)：返回从当前节点到叶子节点的路径和是否 >= limit。
# 1. 如果 node 为空，返回 False。
# 2. 累加当前节点值到 cur_sum。
# 3. 如果是叶子节点，直接判断 cur_sum >= limit。
# 4. 否则递归判断左右子树：left_ok = dfs(node.left, cur_sum)。
# 5. 如果左子树不足（left_ok == False），将 node.left 置为 None（删除）。
# 6. 同理处理右子树。
# 7. 返回 left_ok or right_ok（当前节点是否充足）。
# 最后如果根节点不足（root_ok == False），返回 None；否则返回 root。
#
# 时间复杂度: O(n) - 每个节点访问一次
# 空间复杂度: O(h) - 递归栈深度，h 为树高
#
# 关键点:
# - 后序遍历：先处理子树再处理当前节点
# - 不足节点的定义：经过该节点的所有根到叶路径和都 < limit
# - 叶子节点直接判断当前和
# - 删除操作：将不足子树的引用置为 None
# - 空节点返回 False（不是叶子）
