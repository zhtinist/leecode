"""
LeetCode #1609 - Even Odd Tree
中文题名：奇偶树
https://leetcode.com/problems/even-odd-tree/

A binary tree is named Even-Odd if it meets the following
conditions:

The root of the binary tree is at level index `0`, its children are
at level index `1`, their children are at level index `2`,
etc.

For every even-indexed level, all nodes at the level have
odd integer values in strictly increasing
order (from left to right).

For every odd-indexed level, all nodes at the level have even
integer values in strictly decreasing order (from left to
right).

Given the `root` of a binary tree, return `true`
if the binary tree is Even-Odd, otherwise return
`false`.

Example 1:

Input: root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
Output: true
Explanation: The node values on each level are:
Level 0: [1]
Level 1: [10,4]
Level 2: [3,7,9]
Level 3: [12,8,6,2]
Since levels 0 and 2 are all odd and increasing, and levels 1 and 3 are all even and decreasing, the tree is Even-Odd.

Example 2:

Input: root = [5,4,2,3,3,7]
Output: false
Explanation: The node values on each level are:
Level 0: [5]
Level 1: [4,2]
Level 2: [3,3,7]
Node values in the level 2 must be in strictly increasing order, so the tree is not Even-Odd.

Example 3:

Input: root = [5,9,1,3,5,7]
Output: false
Explanation: Node values in the level 1 should be even integers.

Example 4:

Input: root = [1]
Output: true

Example 5:

Input: root = [11,8,6,1,3,9,11,30,20,18,16,12,10,4,2,17]
Output: true

Constraints:

The number of nodes in the tree is in the range `[1, 105]`.

`1 <= Node.val <= 106`

【中文翻译】
如果一棵二叉树满足以下条件，则称为奇偶树：
- 偶数索引层（根为第0层）：所有节点值为奇数，且从左到右严格递增
- 奇数索引层：所有节点值为偶数，且从左到右严格递减
给定根节点 root，判断二叉树是否为奇偶树。

示例 1：root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
第0层: [1] (奇数，递增)
第1层: [10,4] (偶数，递减)
第2层: [3,7,9] (奇数，递增)
第3层: [12,8,6,2] (偶数，递减)
输出: true

示例 2：root = [5,4,2,3,3,7]
第2层: [3,3,7] — 不是严格递增
输出: false

示例 3：root = [5,9,1,3,5,7]
第1层: [9,1] — 9是奇数，不满足偶数层条件
输出: false
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
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque([root])
        level = 0

        while queue:
            size = len(queue)
            prev_val = float('-inf') if level % 2 == 0 else float('inf')

            for _ in range(size):
                node = queue.popleft()

                # 检查奇偶性
                if level % 2 == 0:  # 偶数层：必须为奇数，严格递增
                    if node.val % 2 == 0 or node.val <= prev_val:
                        return False
                else:  # 奇数层：必须为偶数，严格递减
                    if node.val % 2 == 1 or node.val >= prev_val:
                        return False

                prev_val = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        return True



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用 BFS 层序遍历二叉树。维护当前层级 level 和前一个节点的值 prev_val。
# - 偶数层（level % 2 == 0）：当前值必须为奇数且大于 prev_val（严格递增）
# - 奇数层（level % 2 == 1）：当前值必须为偶数且小于 prev_val（严格递减）
# 若任何条件不满足则返回 False。
#
# 时间复杂度: O(N) — 每个节点访问一次
# 空间复杂度: O(W) — 队列最大宽度，最坏情况 O(N)
#
# 关键点:
# - 层级从0开始，root在第0层（偶数层）
# - 偶数层要求奇数+递增，奇数层要求偶数+递减
# - 初始化 prev_val 为 -inf（偶数层）或 inf（奇数层）简化边界判断
