"""
LeetCode #272 - Closest Binary Search Tree Value II
中文题名：最接近的二叉搜索树值 II
https://leetcode.com/problems/closest-binary-search-tree-value-ii/

Given a non-empty binary search tree and a target value, find *k* values in the BST that
are closest to the target.

Note:

Given target value is a floating point.

You may assume *k* is always valid, that is: *k* <= total nodes.

You are guaranteed to have only one unique set of *k* values in the BST that are
closest to the target.

Example:

Input: root = [4,2,5,1,3], target = 3.714286, and *k* = 2

4
/ \
2   5
/ \
1   3

Output: [4,3]

Follow up:

Assume that the BST is balanced, could you solve it in less than *O*(*n*) runtime
(where *n* = total nodes)?

【中文翻译】
给定一个非空二叉搜索树和一个目标值，在 BST 中找到 *k* 个最接近目标值的值。

注意：

给定的目标值是一个浮点数。

你可以假设 *k* 始终有效，即：*k* <= 总节点数。

你可以保证 BST 中只有唯一一组 *k* 个值最接近目标值。

示例：

输入：root = [4,2,5,1,3], target = 3.714286，且 *k* = 2

4
/ \
2   5
/ \
1   3

输出：[4,3]

进阶：

假设 BST 是平衡的，你能否在小于 *O*(*n*) 的时间复杂度内解决此题（其中 *n* = 总节点数）？
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        """Find k values in BST closest to target.

        Approach: Use two stacks for predecessors and successors.
        First, find the closest element path and initialize both stacks.
        Then pop the closer one and replenish from the appropriate stack.
        O(log n + k) average time for balanced BST.
        """
        res = []
        pred_stack = []  # stores nodes for predecessor (smaller values)
        succ_stack = []  # stores nodes for successor (larger values)

        # Initialize both stacks by walking to the target
        cur = root
        while cur:
            if cur.val <= target:
                pred_stack.append(cur)
                cur = cur.right
            else:
                succ_stack.append(cur)
                cur = cur.left

        def get_next_pred():
            """Get next smaller value from predecessor stack."""
            if not pred_stack:
                return
            node = pred_stack.pop()
            # Go to the rightmost node of the left subtree
            cur = node.left
            while cur:
                pred_stack.append(cur)
                cur = cur.right
            return node

        def get_next_succ():
            """Get next larger value from successor stack."""
            if not succ_stack:
                return
            node = succ_stack.pop()
            # Go to the leftmost node of the right subtree
            cur = node.right
            while cur:
                succ_stack.append(cur)
                cur = cur.left
            return node

        # Initial peek
        pred_node = pred_stack[-1] if pred_stack else None
        succ_node = succ_stack[-1] if succ_stack else None

        while k > 0:
            if pred_node and succ_node:
                diff_pred = abs(pred_node.val - target)
                diff_succ = abs(succ_node.val - target)
                if diff_pred < diff_succ:
                    res.append(pred_node.val)
                    pred_node = get_next_pred()
                else:
                    res.append(succ_node.val)
                    succ_node = get_next_succ()
            elif pred_node:
                res.append(pred_node.val)
                pred_node = get_next_pred()
            elif succ_node:
                res.append(succ_node.val)
                succ_node = get_next_succ()
            k -= 1

        return res


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Hard
# Paid Only: Yes
#
# 解题思路:
# 使用两个栈分别维护前驱（predecessor，小于target的值）和后继（successor，
# 大于等于target的值）。首先从根节点走向target，将路径上的节点分别推入
# 对应的栈中。然后像合并两个有序列表一样，每次比较前驱栈顶和后继栈顶哪个
# 离target更近，取出较近的一个加入结果，并将该节点的对应方向子树压入栈中。
# 对于平衡BST，时间复杂度为 O(log N + k)，空间复杂度为 O(log N)。
#
# 时间复杂度: O(log N + k) 平衡BST / O(N + k) 最坏情况
# 空间复杂度: O(log N) 平衡BST / O(N) 最坏情况
#
# 关键点:
# - 利用BST性质，通过两个栈分别管理小于和大于target的值
# - 初始遍历路径同时填充两个栈
# - get_next_pred: 弹出栈顶后，将左子树的右链压入栈
# - get_next_succ: 弹出栈顶后，将右子树的左链压入栈
