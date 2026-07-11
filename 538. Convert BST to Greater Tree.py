"""
LeetCode #538 - Convert BST to Greater Tree
中文题名：把二叉搜索树转换为累加树
https://leetcode.com/problems/convert-bst-to-greater-tree/

Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the
original BST is changed to the original key plus sum of all keys greater than the original
key in BST.

Example:

Input: The root of a Binary Search Tree like this:
5
/   \
2     13

Output: The root of a Greater Tree like this:
18
/   \
20     13

【中文翻译】
给定一棵二叉搜索树（BST），将其转换为累加树（Greater Tree），使每个节点的值变为原有值加上
BST 中所有比它大的节点值之和。

示例：
    输入：二叉搜索树如下：
        5
       / \
      2   13
    输出：累加树如下：
        18
       /  \
      20   13
    解释：节点 5 变为 5+13=18；节点 2 变为 2+5+13=20；节点 13 没有比它大的节点，保持 13
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.running_sum = 0

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            # Reverse in-order: right -> root -> left
            dfs(node.right)
            self.running_sum += node.val
            node.val = self.running_sum
            dfs(node.left)

        dfs(root)
        return root










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 利用 BST 的中序遍历有序性质，但采用"反中序"遍历（右 → 根 → 左），
# 这样节点会从大到小被访问。维护一个累加和 running_sum，每访问一个节点：
# 1. 将当前节点值加到 running_sum
# 2. 将 running_sum 赋值给当前节点
# 这样每个节点值就被替换为比它大的所有节点值之和。
#
# 时间复杂度: O(N) — 每个节点被访问恰好一次
# 空间复杂度: O(H) — 递归栈深度等于树高，最坏 O(N)（退化成链表），平均 O(log N)
#
# 关键点:
# - 反中序遍历（右→根→左）确保从大到小访问
# - 用一个外部变量记录累加和，在遍历过程中不断更新
# - 注意：543 是另一道相关题目，本题仅要求修改节点值
# - 也可以使用迭代 + 栈的方式实现，避免递归栈溢出
