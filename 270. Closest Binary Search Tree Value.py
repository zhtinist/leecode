"""
LeetCode #270 - Closest Binary Search Tree Value
https://leetcode.com/problems/closest-binary-search-tree-value/

Given a non-empty binary search tree and a target value, find the value in the BST that is
closest to the target.

Note:

Given target value is a floating point.

You are guaranteed to have only one unique value in the BST that is closest to the
target.

Example:

Input: root = [4,2,5,1,3], target = 3.714286

4
/ \
2   5
/ \
1   3

Output: 4
"""

from typing import List, Optional


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val

        while root:
            # 更新最接近的值
            if abs(root.val - target) < abs(closest - target):
                closest = root.val

            # BST 查找：根据 target 决定向左还是向右
            if target < root.val:
                root = root.left
            else:
                root = root.right

        return closest


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Easy
# Paid Only: Yes
#
# 解题思路：
# 利用 BST 的性质进行二分查找。从根节点开始，不断更新最接近的值。
# 如果 target < 当前节点值，则向左子树移动（因为右子树的值离 target 更远）；
# 如果 target > 当前节点值，则向右子树移动。直到到达叶子节点。
# 这本质上是在 BST 中查找 target，沿途经过的节点包含了最接近的值。
#
# 时间复杂度: O(h) — h 为树高，平均 O(log n)，最坏 O(n)
# 空间复杂度: O(1) — 迭代不用递归栈
#
# 关键点：
# - BST 的二分查找特性
# - 沿途更新最接近值
# - target < node.val → 走左边，否则右边
