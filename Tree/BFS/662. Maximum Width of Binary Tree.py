"""
LeetCode #662 - Maximum Width of Binary Tree
中文题名：二叉树最大宽度
https://leetcode.com/problems/maximum-width-of-binary-tree/

Given a binary tree, write a function to get the maximum width of the given tree. The width
of a tree is the maximum width among all levels. The binary tree has the same structure as a
full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right
most non-null nodes in the level, where the `null` nodes between the end-nodes
are also counted into the length calculation.

Example 1:

Input:

1
/   \
3     2
/ \     \
5   3     9

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).

Example 2:

Input:

1
/
3
/ \
5   3

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).

Example 3:

Input:

1
/ \
3   2
/
5

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).

Example 4:

Input:

1
/ \
3   2
/     \
5       9
/         \
6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).

Note: Answer will in the range of 32-bit signed integer.

【中文翻译】
给定一棵二叉树，编写一个函数来获取这棵树的最大宽度。树的宽度是所有层中的最大宽度。该二叉树与满二叉树（full binary tree）具有相同的结构，但某些节点为空。

每一层的宽度定义为该层两端节点之间的长度（该层中最左和最右的非空节点），其中两端之间的 `null` 节点也要计入长度计算。

示例 1：

输入：

           1
         /   \
        3     2
       / \     \
      5   3     9

输出：4
解释：第三层存在最大宽度，长度为 4（5,3,null,9）。

示例 2：

输入：

          1
         /
        3
       / \
      5   3

输出：2
解释：第三层存在最大宽度，长度为 2（5,3）。

示例 3：

输入：

          1
         / \
        3   2
       /
      5

输出：2
解释：第二层存在最大宽度，长度为 2（3,2）。

示例 4：

输入：

          1
         / \
        3   2
       /     \
      5       9
     /         \
    6           7

输出：8
解释：第四层存在最大宽度，长度为 8（6,null,null,null,null,null,null,7）。

注意：答案在 32 位有符号整数的范围内。
"""

from collections import deque
from typing import List, Optional


class Solution:
    def widthOfBinaryTree(self, root: Optional['TreeNode']) -> int:
        if not root:
            return 0

        max_width = 0
        queue: deque[tuple['TreeNode', int]] = deque()
        queue.append((root, 1))

        while queue:
            level_size = len(queue)
            _, first_idx = queue[0]
            _, last_idx = queue[-1]
            max_width = max(max_width, last_idx - first_idx + 1)

            for _ in range(level_size):
                node, idx = queue.popleft()
                if node.left:
                    queue.append((node.left, 2 * idx))
                if node.right:
                    queue.append((node.right, 2 * idx + 1))

        return max_width











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用 BFS 层序遍历，同时为每个节点分配一个索引值：
# - 根节点索引为 1
# - 左子节点索引 = 父节点索引 * 2
# - 右子节点索引 = 父节点索引 * 2 + 1
# 对于每一层，宽度 = 该层最右节点的索引 - 该层最左节点的索引 + 1。
# 维护全局最大宽度即可。
# 这个索引方案相当于满二叉树的层序编号，因此能正确计算包含空节点的宽度。
#
# 时间复杂度: O(n) - 每个节点访问一次
# 空间复杂度: O(w) - 队列大小，最坏情况为 O(n)，w 为树的最大宽度
#
# 关键点:
# - 利用满二叉树的索引编号方案来间接计算宽度
# - 每一层的宽度 = last_idx - first_idx + 1
# - 不需要实际存储空节点，索引会自动考虑空位
# - 注意大索引可能溢出 32 位整型（Python 自动处理大整数）
# - DFS 方案也可实现，记录每一层第一个节点的索引
