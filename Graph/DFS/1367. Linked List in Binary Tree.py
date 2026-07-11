"""
LeetCode #1367 - Linked List in Binary Tree
中文题名：二叉树中的链表
https://leetcode.com/problems/linked-list-in-binary-tree/

Given a binary tree `root` and a linked list
with `head` as the first node.

Return True if all the elements in the linked list starting from the
`head` correspond to some downward path connected in the binary
tree otherwise return False.

In this context downward path means a path that starts at some node and goes
downwards.

Example 1:

Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Explanation: Nodes in blue form a subpath in the binary Tree.

Example 2:

Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true

Example 3:

Input: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: false
Explanation: There is no path in the binary tree that contains all the elements of the linked list from `head`.

Constraints:

`1 <= node.val <= 100` for each node in the linked
list and binary tree.

The given linked list will contain between `1` and `100` nodes.

The given binary tree will contain
between `1` and `2500` nodes.

【中文翻译】
给定一棵二叉树 `root` 和一个以 `head` 为第一个节点的链表。

如果链表中从 `head` 开始的所有元素与二叉树中某条向下的路径一一对应，则返回 True；否则返回 False。

此处向下路径是指从某个节点开始向下延伸的路径。

示例 1：
输入：head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
输出：true
解释：树中蓝色的节点构成了与链表对应的子路径。

示例 2：
输入：head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
输出：true

示例 3：
输入：head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
输出：false
解释：二叉树中不存在包含链表中所有元素的路径。
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs_check(list_node: Optional[ListNode], tree_node: Optional[TreeNode]) -> bool:
            """检查从当前树节点开始是否能完全匹配链表"""
            if not list_node:
                return True
            if not tree_node:
                return False
            if list_node.val != tree_node.val:
                return False
            return dfs_check(list_node.next, tree_node.left) or dfs_check(list_node.next, tree_node.right)

        if not root:
            return False
        # 从当前节点开始匹配，或递归检查左右子树
        if dfs_check(head, root):
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 双重 DFS：外层 DFS 遍历二叉树的每个节点作为匹配起点，内层 DFS 从当前树节点开始尝试匹配链表。
# 1. isSubPath: 检查以 root 为起点的向下路径是否包含链表。
#    a. 从当前树节点开始调用 dfs_check 尝试匹配整个链表。
#    b. 如果匹配失败，递归检查左子树和右子树。
# 2. dfs_check(list_node, tree_node): 检查从当前树节点向下的路径是否能完整匹配剩余链表。
#    a. 链表遍历完毕返回 True（匹配成功）。
#    b. 树节点为空或值不相等返回 False。
#    c. 递归尝试左子节点或右子节点继续匹配。
#
# 时间复杂度: O(N * min(L, H))，N 为树节点数，L 为链表长度，H 为树高
# 空间复杂度: O(H + L)，递归栈深度
#
# 关键点:
# - 外层递归枚举所有可能的起点
# - 内层递归严格匹配链表序列
# - 每个树节点都可以作为匹配起点













