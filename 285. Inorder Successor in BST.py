"""
LeetCode #285 - Inorder Successor in BST
中文题名：二叉搜索树中的中序后继
https://leetcode.com/problems/inorder-successor-in-bst/

Given a binary search tree and a node in it, find the in-order successor of that node in the
BST.

The successor of a node `p` is the node with the smallest key greater
than `p.val`.

Example 1:

*

Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.

Example 2:

*

Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is `null`.

Note:

If the given node has no in-order successor in the tree, return `null`.

It's guaranteed that the values of the tree are unique.

【中文翻译】
给定一棵二叉搜索树和一个树中的节点，找到该节点在 BST 中的中序后继。

节点 `p` 的后继是键值大于 `p.val` 的最小键值的节点。

示例 1：

*

输入：root = [2,1,3], p = 1
输出：2
解释：1 的中序后继节点是 2。注意 p 和返回值均为 TreeNode 类型。

示例 2：

*

输入：root = [5,3,6,2,4,null,null,1], p = 6
输出：null
解释：当前节点没有中序后继，因此答案为 `null`。

注意：

如果给定节点在树中没有中序后继，返回 `null`。

保证树中的值是唯一的。
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        """Find the inorder successor of node p in BST.

        Iterative approach: traverse from root, keeping track of the successor.
        If p has a right child, successor is the leftmost node in right subtree.
        Otherwise, successor is the last ancestor where we took a left turn.

        This solution handles both cases in one pass.
        """
        successor = None

        while root:
            if p.val < root.val:
                # Current node could be successor, go left to find smaller
                successor = root
                root = root.left
            else:
                # p.val >= root.val, successor must be in right subtree
                root = root.right

        return successor


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: Yes
#
# 解题思路:
# 利用 BST 的性质，从中序遍历的角度考虑：
# - 中序后继即比 p.val 大的最小节点
# 从根节点开始遍历：
# - 如果 p.val < root.val，当前节点可能是后继（比 p 大），记录为候选，
#   然后向左子树搜索是否有更小的候选
# - 如果 p.val >= root.val，p 的后继一定在右子树中（或不存在），向右搜索
# 遍历结束后，记录的 candidate 就是中序后继。
#
# 时间复杂度: O(H) - 树的高度，平衡树为 O(log N)，最坏 O(N)
# 空间复杂度: O(1) - 迭代解法不需要递归栈
#
# 关键点:
# - 不需要显式中序遍历整个树
# - 利用 BST 性质：左 < 根 < 右
# - 向左走时更新后继候选（因为当前节点 > p，可能是后继）
# - 向右走时不更新（因为当前节点 <= p，不可能是后继）
