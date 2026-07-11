"""
LeetCode #255 - Verify Preorder Sequence in Binary Search Tree
中文题名：验证二叉搜索树的前序遍历序列
https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/

Given an array of numbers, verify whether it is the correct preorder traversal sequence of a
binary search tree.

You may assume each number in the sequence is unique.

Consider the following binary search tree:

5
/ \
2   6
/ \
1   3

Example 1:

Input: [5,2,6,1,3]
Output: false

Example 2:

Input: [5,2,1,3,6]
Output: true

Follow up:

Could you do it using only constant space complexity?

【中文翻译】
给定一个整数数组，验证它是否是二叉搜索树（BST）的正确前序遍历序列。

你可以假设数组中的数字是唯一的。

考虑以下二叉搜索树：

5
/ \
2   6
/ \
1   3

示例 1：

输入：[5,2,6,1,3]
输出：false

示例 2：

输入：[5,2,1,3,6]
输出：true

进阶：

你能否使用常数空间复杂度完成此题？
"""

from typing import List, Optional


class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        # 模拟构建 BST 的过程
        stack = []
        lower_bound = float('-inf')

        for val in preorder:
            # 当前值必须大于 lower_bound
            if val < lower_bound:
                return False

            # 如果当前值大于栈顶，说明进入了右子树
            # 弹出所有小于当前值的节点，更新 lower_bound
            while stack and val > stack[-1]:
                lower_bound = stack.pop()

            stack.append(val)

        return True


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: Yes
#
# 解题思路：
# 使用单调栈模拟 BST 的前序遍历构建过程。维护一个 lower_bound（下界），
# 代表当前节点必须大于该值（因为 BST 右子树所有节点都大于根）。
# 遍历数组，如果当前值小于 lower_bound，则不是合法的 BST 前序。
# 当遇到比栈顶大的值时，说明进入了某个节点的右子树，弹出栈中比它小的值，
# 最后一个弹出的值成为新的 lower_bound。
#
# 时间复杂度: O(n) — 每个元素入栈出栈各一次
# 空间复杂度: O(n) — 栈空间，最坏情况（完全左斜树）
#
# 关键点：
# - lower_bound 跟踪当前节点必须大于的最小值
# - 遇到更大值时弹出栈并更新 lower_bound
# - Follow up 的 O(1) 空间可以原地利用输入数组作为栈
