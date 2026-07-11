"""
LeetCode #1382 - Balance a Binary Search Tree
中文题名：将二叉搜索树变平衡
https://leetcode.com/problems/balance-a-binary-search-tree/

Given a binary search tree, return a balanced binary search tree
with the same node values.

A binary search tree is balanced if and only if the depth of the two
subtrees of every node never differ by more than 1.

If there is more than one answer, return any of them.

Example 1:

Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.

Constraints:

The number of nodes in the tree is
between `1` and `10^4`.

The tree nodes will have distinct values between `1` and `10^5`.

【中文翻译】

给定一个二叉搜索树，返回一个具有相同节点值的平衡二叉搜索树。

如果二叉搜索树每个节点的两个子树深度差不超过 1，则称为平衡的。

如果有多个答案，返回其中任意一个。

示例 1：

输入：root = [1,null,2,null,3,null,4,null,null]
输出：[2,1,3,null,null,null,4]
解释：这不是唯一正确的答案，[3,1,4,null,2,null,null] 也是正确的。

约束条件：
树中节点数量在 1 到 10^4 之间。
树节点值互不相同，在 1 到 10^5 之间。
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Step 1: 中序遍历得到有序数组
        vals = []

        def inorder(node: TreeNode) -> None:
            if not node:
                return
            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)

        inorder(root)

        # Step 2: 从有序数组构建平衡 BST（取中间为根）
        def build(l: int, r: int) -> TreeNode | None:
            if l > r:
                return None
            mid = (l + r) // 2
            node = TreeNode(vals[mid])
            node.left = build(l, mid - 1)
            node.right = build(mid + 1, r)
            return node

        return build(0, len(vals) - 1)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 分两步解决：
# 1. 对原 BST 进行中序遍历，得到按升序排列的节点值数组。
#    BST 的中序遍历天然有序。
# 2. 用二分法从有序数组中间位置递归构建平衡 BST：
#    取中间元素作为根节点，左半部分构建左子树，右半部分构建右子树。
#    这样保证左右子树节点数尽可能接近，从而达到平衡。
#
# 时间复杂度: O(N)  中序遍历 O(N) + 构建树 O(N)
# 空间复杂度: O(N)  存储数组 O(N) + 递归栈 O(log N)
#
# 关键点:
# - BST 中序遍历得到的是严格升序序列
# - 从有序数组构建平衡 BST 的关键是每次取中间元素作为根
# - 递归构建左右子树即可保证平衡










