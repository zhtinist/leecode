"""
LeetCode #450 - Delete Node in a BST
中文题名：删除二叉搜索树中的节点
https://leetcode.com/problems/delete-node-in-a-bst/

Given a root node reference of a BST and a key, delete the node with the given key in the
BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.

If the node is found, delete the node.

Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7

【中文翻译】
给定二叉搜索树（BST）的根节点和一个键值 key，删除 BST 中值为 key 的节点。返回更新后的根节点。

删除分为两步：
1. 搜索要删除的节点。
2. 如果找到该节点，删除它。

示例：
root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

给定要删除的 key 是 3。因此找到值为 3 的节点并删除它。

一个有效答案是 [5,4,6,2,null,null,7]，对应如下 BST：

    5
   / \
  4   6
 /     \
2       7

另一个有效答案是 [5,2,6,null,4,null,7]：

    5
   / \
  2   6
   \   \
    4   7
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node to delete found
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # Node has two children: find inorder successor (smallest in right subtree)
            successor = root.right
            while successor.left:
                successor = successor.left
            # Replace root's value with successor's value
            root.val = successor.val
            # Delete the successor from right subtree
            root.right = self.deleteNode(root.right, successor.val)

        return root










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 利用 BST 的性质递归查找要删除的节点。如果 key 小于当前节点值，递归到左子树；大于则递归到右子树。
# 找到目标节点后有三种情况：(1) 无子节点，直接删除；(2) 只有一个子节点，用该子节点替换；
# (3) 有两个子节点，找到中序后继（右子树中的最小节点），用其后继值替换当前节点值，再递归删除后继节点。
#
# 时间复杂度: O(H) — H 为树的高度，最坏情况 O(N)（退化为链表），平均 O(log N)
# 空间复杂度: O(H) — 递归栈深度，最坏 O(N)，平均 O(log N)
#
# 关键点:
# - BST 的删除需要维护 BST 性质（左 < 根 < 右）
# - 双子节点情况：用右子树最小节点（中序后继）替换当前节点，然后删除后继
# - 也可以用左子树最大节点（中序前驱）替代
