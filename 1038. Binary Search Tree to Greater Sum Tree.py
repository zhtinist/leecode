"""
LeetCode #1038 - Binary Search Tree to Greater Sum Tree
中文题名：从二叉搜索树到更大和树
https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

Given the root of a binary search tree with distinct values, modify it so
that every `node` has a new value equal to the sum of the values of the
original tree that are greater than or equal to `node.val`.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the
node's key.

The right subtree of a node contains only nodes with keys greater
than the node's key.

Both the left and right subtrees must also be binary search trees.

Example 1:

Input: [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

【中文翻译】
给定一棵具有不同值的二叉搜索树的根节点，修改它使得每个节点 node 的新值等于原始树中大于或等于 node.val 的值之和。

提醒一下，二叉搜索树是一棵满足以下约束的树：

节点的左子树只包含键值小于该节点键值的节点。
节点的右子树只包含键值大于该节点键值的节点。
左子树和右子树也必须是二叉搜索树。

示例 1：

输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
"""

from typing import List, Optional


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.running_sum = 0

        def reverse_inorder(node: TreeNode):
            if not node:
                return
            reverse_inorder(node.right)
            self.running_sum += node.val
            node.val = self.running_sum
            reverse_inorder(node.left)

        reverse_inorder(root)
        return root










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用反中序遍历（右->根->左）遍历BST。BST的性质是：左子树所有值 < 根 < 右子树所有值。
# 反中序遍历使得我们按从大到小的顺序访问节点。维护一个累加和 running_sum，
# 每访问一个节点，将其值加到 running_sum，然后将 running_sum 赋给该节点。
# 这样每个节点的新值就是所有大于等于它的节点值之和。
#
# 时间复杂度: O(N) - 每个节点访问一次
# 空间复杂度: O(H) - 递归栈深度，H为树高
#
# 关键点:
# - 反中序遍历（右->根->左）确保按从大到小顺序访问
# - 累加和维护所有已访问（即大于等于当前节点的）节点之和
# - 与 LeetCode #538 完全相同的题目
