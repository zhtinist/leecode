"""
LeetCode #669 - Trim a Binary Search Tree
中文题名：修剪二叉搜索树
https://leetcode.com/problems/trim-a-binary-search-tree/

Given a binary search tree and the lowest and highest boundaries as `L` and
`R`, trim the tree so that all its elements lies in `[L, R]` (R >= L).
You might need to change the root of the tree, so the result should return the new root of
the trimmed binary search tree.

Example 1:

Input:
1
/ \
0   2

L = 1
R = 2

Output:
1
\
2

Example 2:

Input:
3
/ \
0   4
\
2
/
1

L = 1
R = 3

Output:
3
/
2
/
1

【中文翻译】
给定一棵二叉搜索树和最低与最高边界 `L` 和 `R`，修剪这棵树使得所有节点的值都在 `[L, R]` 中（R >= L）。你可能需要改变树的根节点，因此结果应返回修剪后的二叉搜索树的新根节点。

示例 1：

输入：
    1
   / \
  0   2

  L = 1
  R = 2

输出：
    1
     \
      2

示例 2：

输入：
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

输出：
      3
     /
    2
   /
  1
"""

from typing import List, Optional


class Solution:
    def trimBST(self, root: Optional['TreeNode'], low: int, high: int) -> Optional['TreeNode']:
        if not root:
            return None

        if root.val < low:
            return self.trimBST(root.right, low, high)
        if root.val > high:
            return self.trimBST(root.left, low, high)

        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 递归修剪二叉搜索树，利用 BST 的有序性质：
# - 如果 root.val < low：当前节点及其左子树都小于 low，
#   全部丢弃，直接返回修剪后的右子树
# - 如果 root.val > high：当前节点及其右子树都大于 high，
#   全部丢弃，直接返回修剪后的左子树
# - 如果 low <= root.val <= high：当前节点保留，
#   递归修剪左右子树并重新挂接，返回当前节点
# 递归终止条件是遇到空节点，返回 None。
#
# 时间复杂度: O(n) - 最多访问每个节点一次
# 空间复杂度: O(h) - 递归栈深度，最坏情况树退化为链 O(n)
#
# 关键点:
# - 充分利用 BST 性质：节点值不在范围内时，可以整棵子树丢弃
# - root.val < low 时，左子树全部小于 low，直接跳到右子树
# - root.val > high 时，右子树全部大于 high，直接跳到左子树
# - 只有当 root.val 在范围内时才需要修剪左右子树
# - 这种"跳跃式"递归避免了无效遍历
