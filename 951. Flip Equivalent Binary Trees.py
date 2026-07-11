"""
LeetCode #951 - Flip Equivalent Binary Trees
中文题名：翻转等价二叉树
https://leetcode.com/problems/flip-equivalent-binary-trees/

For a binary tree T, we can define a flip operation as follows: choose any node, and swap the
left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can
make X equal to Y after some number of flip operations.

Write a function that determines whether two binary trees are flip equivalent.
The trees are given by root nodes `root1` and `root2`.

Example 1:

Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.

Note:

Each tree will have at most `100` nodes.

Each value in each tree will be a unique integer in the range `[0, 99]`.

【中文翻译】
对于二叉树 T，我们可以定义一个翻转操作如下：选择任意节点，然后交换它的
左右子树。

二叉树 X 翻转等价于二叉树 Y 当且仅当我们可以通过若干次翻转操作使得
X 与 Y 相等。

编写一个函数来判断两棵二叉树是否翻转等价。
树由根节点 root1 和 root2 给出。

"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False

        # Two possibilities: no flip needed, or flip needed
        return (
            self.flipEquiv(root1.left, root2.left)
            and self.flipEquiv(root1.right, root2.right)
        ) or (
            self.flipEquiv(root1.left, root2.right)
            and self.flipEquiv(root1.right, root2.left)
        )



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 递归定义：两棵树翻转等价，当且仅当：
#    - 两个根节点都为空（true），或
#    - 其中一个为空（false），或
#    - 两个根节点值不相等（false）
#    - 两个根节点值相等，且满足以下两者之一：
#      a) 不翻转：左子树与左子树翻转等价，且右子树与右子树翻转等价
#      b) 翻转：左子树与右子树翻转等价，且右子树与左子树翻转等价
# 2. 递归出口：根节点为空、单边为空、值不等。
# 3. 递归检查：对"不翻转"和"翻转"两种情况分别递归，取逻辑或。
#
# 时间复杂度: O(min(N1, N2)) — 其中 N1, N2 分别为两棵树的节点数。每个节点对最多被访问一次。
# 空间复杂度: O(min(H1, H2)) — 递归调用栈的深度，取决于较矮树的高度。
#
# 关键点:
# - 递归定义自然而然包含了"允许任意节点翻转"的语义
# - 每个节点有两种选择：翻转或不翻转
# - 由于每个树的值唯一（题目给定），不需要担心值相同但结构不同的歧义
