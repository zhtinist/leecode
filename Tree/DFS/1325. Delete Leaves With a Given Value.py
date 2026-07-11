"""
LeetCode #1325 - Delete Leaves With a Given Value
中文题名：删除给定值的叶子节点
https://leetcode.com/problems/delete-leaves-with-a-given-value/

Given a binary tree `root` and an integer `target`,
delete all the leaf nodes with value `target`.

Note that once you delete a leaf node with value
`target`, if it's parent node becomes a leaf node and
has the value `target`, it should also be
deleted (you need to continue doing that until you can't).

Example 1:

Input: root = [1,2,3,2,null,2,4], target = 2
Output: [1,null,3,null,4]
Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left).
After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).

Example 2:

Input: root = [1,3,3,3,2], target = 3
Output: [1,3,null,null,2]

Example 3:

Input: root = [1,2,null,2,null,2], target = 2
Output: [1]
Explanation: Leaf nodes in green with value (target = 2) are removed at each step.

Example 4:

Input: root = [1,1,1], target = 1
Output: []

Example 5:

Input: root = [1,2,3], target = 1
Output: [1,2,3]

Constraints:

`1 <= target <= 1000`

Each tree has at most `3000` nodes.

Each node's value is between `[1, 1000]`.

【中文翻译】
给定一棵二叉树 root 和一个整数 target，删除所有值为 target 的叶子节点。
注意，一旦删除了一个值为 target 的叶子节点，如果它的父节点变成了叶子节点且值也为 target，
那么该父节点也应被删除（需要持续执行直到无法继续删除）。

示例 1：

输入：root = [1,2,3,2,null,2,4], target = 2
输出：[1,null,3,null,4]
解释：值为 target=2 的叶子节点（绿色）被删除。
删除后，新的节点变成值为 target=2 的叶子节点，继续被删除。

示例 2：

输入：root = [1,3,3,3,2], target = 3
输出：[1,3,null,null,2]

示例 3：

输入：root = [1,2,null,2,null,2], target = 2
输出：[1]
解释：每一步中值为 target=2 的叶子节点都被删除。

示例 4：

输入：root = [1,1,1], target = 1
输出：[]

示例 5：

输入：root = [1,2,3], target = 1
输出：[1,2,3]
"""

from typing import List, Optional


class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        # After processing children, check if current node became a leaf with target value
        if not root.left and not root.right and root.val == target:
            return None
        return root



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用后序遍历（自底向上）。先递归处理左右子树，然后检查当前节点：
# 如果左右子树都为空（是叶子节点）且值等于 target，则返回 None（删除该节点）。
# 由于是后序遍历，子节点的删除会在父节点判断之前完成，自然实现了级联删除。
#
# 时间复杂度: O(N) — 每个节点访问一次
# 空间复杂度: O(H) — 递归栈深度，H 为树高
#
# 关键点:
# - 必须使用后序遍历（左右根），确保子节点先被处理
# - 删除操作通过返回 None 实现
# - 级联删除自然发生：子节点删除后，父节点可能变成新的叶子节点
