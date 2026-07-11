"""
LeetCode #1008 - Construct Binary Search Tree from Preorder Traversal
中文题名：前序遍历构造二叉搜索树
https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

Return the root node of a binary search tree that matches the given `preorder`
traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of `node.left` has a value
`<` `node.val`, and any descendant of `node.right`
has a value `>` `node.val`.  Also recall that a preorder
traversal displays the value of the `node` first, then traverses `node.left`,
then traverses `node.right`.)

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Note:

`1 <= preorder.length <= 100`

The values of `preorder` are distinct.

【中文翻译】
返回与给定 `preorder` 前序遍历匹配的二叉搜索树的根节点。

（回想一下，二叉搜索树是一种二叉树，对于每个节点，`node.left` 的任何后代的值都 `<` `node.val`，而 `node.right` 的任何后代的值都 `>` `node.val`。同时回想一下，前序遍历首先显示 `node` 的值，然后遍历 `node.left`，然后遍历 `node.right`。）

示例 1：

输入：[8,5,1,7,10,12]
输出：[8,5,10,1,7,null,12]

注意：

`1 <= preorder.length <= 100`

`preorder` 中的值都是不同的。

"""

from typing import List, Optional


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        i = 1
        while i < len(preorder) and preorder[i] < root.val:
            i += 1
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 前序遍历的第一个元素是根节点。利用 BST 的性质：左子树所有节点值小于根，
# 右子树所有节点值大于根。找到第一个大于根节点值的元素，它就是右子树的开始位置。
# 因此可以将数组分为三部分：[root, left_subtree, right_subtree]。
# 递归构建左子树（preorder[1:i]）和右子树（preorder[i:]）。
# 注意递归终止条件：数组为空时返回 None。
#
# 时间复杂度: O(n) - 虽然每层递归需要扫描找到分割点，但总体每个元素被扫描一次
# 空间复杂度: O(n) - 递归调用栈最深为 n（当树退化为链表时）
#
# 关键点:
# - 利用 BST 性质找到左右子树的分界点（第一个大于根节点的元素）
# - 递归构建时注意切片范围：左子树 preorder[1:i]，右子树 preorder[i:]
# - 元素值互不相同（题目条件），保证了分界点的唯一性
