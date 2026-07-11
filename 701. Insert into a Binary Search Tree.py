"""
LeetCode #701 - Insert into a Binary Search Tree
中文题名：二叉搜索树中的插入操作
https://leetcode.com/problems/insert-into-a-binary-search-tree/

Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert
the value into the BST. Return the root node of the BST after the insertion. It is
guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the
tree remains a BST after insertion. You can return any of them.

For example,

Given the tree:
4
/ \
2   7
/ \
1   3
And the value to insert: 5

You can return this binary search tree:

4
/   \
2     7
/ \   /
1   3 5

This tree is also valid:

5
/   \
2     7
/ \
1   3
\
4

【中文翻译】
给定二叉搜索树（BST）的根节点以及要插入树中的一个值，将该值插入 BST。返回插入后 BST 的根节点。保证新值在原始的 BST 中不存在。

请注意，可能存在多种有效的插入方式，只要插入后树仍然是 BST 即可。你可以返回任意一种。

例如，

给定树：
        4
       / \
      2   7
     / \
    1   3
要插入的值：5

你可以返回这棵二叉搜索树：

        4
       / \
      2   7
     / \  /
    1   3 5

下面这棵树也是有效的：

        5
       / \
      2   7
     / \
    1   3
         \
          4
"""

from typing import List, Optional


class Solution:
    def insertIntoBST(self, root: Optional['TreeNode'], val: int) -> Optional['TreeNode']:
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root









# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 利用 BST 性质递归插入。
# - 如果当前节点为空，创建新节点返回。
# - 如果 val < root.val，递归插入到左子树。
# - 如果 val > root.val，递归插入到右子树。
# - 返回当前节点（保持不变或已更新子节点）。
# 也可以使用迭代方式：从根节点出发，根据值大小向左/右走，直到找到空位插入。
#
# 时间复杂度: O(H) - H 为树的高度，最坏 O(n)
# 空间复杂度: O(H) - 递归栈深度；迭代为 O(1)
#
# 关键点:
# - 利用 BST 的左小右大性质定位插入位置
# - 递归实现简洁，将新节点挂到叶子节点上
# - 题目保证待插入的值在树中不存在
