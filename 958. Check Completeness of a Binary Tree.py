"""
LeetCode #958 - Check Completeness of a Binary Tree
中文题名：二叉树的完全性检验
https://leetcode.com/problems/check-completeness-of-a-binary-tree/

Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:

In a complete binary tree every level, except possibly the last, is completely filled, and
all nodes in the last level are as far left as possible. It can have between 1 and
2h nodes inclusive at the last level h.

Example 1:

Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.

Example 2:

Input: [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.

【中文翻译】
给定一个二叉树，判断它是否是完全二叉树。
根据维基百科的定义：在完全二叉树中，除了最后一层外，每一层都被完全填满，
并且最后一层的所有节点都尽可能靠左。最后一层 h 可以包含 1 到 2^h 个节点（含两端）。

"""

from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque([root])
        seen_null = False

        while queue:
            node = queue.popleft()

            if node is None:
                seen_null = True
            else:
                if seen_null:
                    # 在遇到空节点后又遇到了非空节点
                    return False
                queue.append(node.left)
                queue.append(node.right)

        return True



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用 BFS 层序遍历。关键观察：在完全二叉树中，如果按层序遍历（包括空节点），
# 一旦遇到第一个空节点，之后的所有节点都必须为空节点。
# 因此，在 BFS 过程中维护一个标志 seen_null：
# - 遇到空节点时，设置 seen_null = True
# - 之后如果再遇到非空节点，则不是完全二叉树
# BFS 需要将左右子节点（包括 None）都加入队列。
#
# 时间复杂度: O(N) — 遍历所有节点
# 空间复杂度: O(N) — 队列最多存储一层节点
#
# 关键点:
# - 层序遍历时也要将 None 子节点入队
# - 一旦看到 null 后不能再看到非 null 节点
# - 完全二叉树的定义：除了最后一层，每层都填满；最后一层节点靠左
