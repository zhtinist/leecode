"""
LeetCode #513 - Find Bottom Left Tree Value
中文题名：找树左下角的值
https://leetcode.com/problems/find-bottom-left-tree-value/

Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:

Input:

2
/ \
1   3

Output:
1

Example 2:

Input:

1
/ \
2   3
/   / \
4   5   6
/
7

Output:
7

Note:
You may assume the tree (i.e., the given root node) is not NULL.

【中文翻译】
给定一个二叉树，在树的最后一行找到最左边的值。

示例 1：
    输入：
        2
       / \
      1   3
    输出：1

示例 2：
    输入：
        1
       / \
      2   3
     /   / \
    4   5   6
   /
  7
    输出：7

注意：你可以假设树（即给定的根节点）不为 NULL。
"""

from typing import List, Optional
from collections import deque


class Solution:
    def findBottomLeftValue(self, root: Optional['TreeNode']) -> int:
        queue = deque([root])
        while queue:
            node = queue.popleft()
            # 先加右子节点，再加左子节点 —— 最后弹出的节点就是最底层最左边的节点
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return node.val


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用 BFS 层序遍历，但改变入队顺序：先将右子节点入队，再将左子节点入队。
# 这样 BFS 遍历的最后一个节点（即最后被 popleft 的节点）就是最后一层最左边的节点。
# 因为每层从左到右，右子节点先入队确保了左子节点后入队，最终指向左下角的值。
#
# 时间复杂度: O(N) — 每个节点访问一次
# 空间复杂度: O(W) — 队列最大宽度，最坏情况 O(N)
#
# 关键点:
# - BFS 右先左后的入队顺序，使得最后弹出的节点即为左下角节点
# - 也可以标准 BFS 按层遍历，记录每层第一个节点值，最后返回最后一层的第一个值
# - DFS 记录深度也可解决，但 BFS 更直观
