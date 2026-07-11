"""
LeetCode #1315 - Sum of Nodes with Even-Valued Grandparent
中文题名：祖父节点值为偶数的节点和
https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

Given a binary tree, return the sum of values of nodes with even-valued grandparent.
(A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return `0`.

Example 1:

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.

Constraints:

The number of nodes in the tree is
between `1` and `10^4`.

The value of nodes is between `1` and `100`.

【中文翻译】
给定一棵二叉树，返回所有祖父节点值为偶数的节点值之和。
（一个节点的祖父节点是其父节点的父节点，如果存在的话。）

如果不存在祖父节点值为偶数的节点，返回 0。

示例 1：
输入：root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
输出：18
解释：图中红色节点为祖父节点值为偶数的节点，蓝色节点为偶数祖父节点。

约束条件：
树中节点的数量在 1 到 10^4 之间。
节点的值在 1 到 100 之间。
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], parent: int, grandparent: int) -> int:
            if not node:
                return 0

            total = 0
            if grandparent is not None and grandparent % 2 == 0:
                total += node.val

            total += dfs(node.left, node.val, parent)
            total += dfs(node.right, node.val, parent)
            return total

        return dfs(root, None, None)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用 DFS 遍历二叉树，在递归过程中传递当前节点的父节点值和祖父节点值。
# 在访问每个节点时，检查其祖父节点值是否为偶数：
#   - 如果是偶数，将当前节点的值累加到结果中
#   - 如果祖父节点为 None（当前节点是根节点或根节点的子节点，没有祖父），跳过
# 递归时更新参数：当前节点值成为下一层的"父节点值"，
# 当前层的"父节点值"成为下一层的"祖父节点值"。
#
# 时间复杂度: O(N)，每个节点访问一次
# 空间复杂度: O(H)，递归调用栈深度为树的高度 H，最坏 O(N)（链状树），平均 O(log N)
#
# 关键点:
# - 通过递归参数传递祖先信息，避免额外数据存储
# - root 节点使用 parent=None, grandparent=None 初始化
# - 偶数的判断：grandparent % 2 == 0
# - 注意区分：代码要求的是"祖父为偶数的节点值之和"，不是"值为偶数的祖父"
# - 参数传递模式：每向下递归一层，parent -> grandparent, node.val -> parent
# - 也可以使用 BFS + 记录每个节点的父节点，但 DFS 更简洁










