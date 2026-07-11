"""
LeetCode #1305 - All Elements in Two Binary Search Trees
中文题名：两棵二叉搜索树中的所有元素
https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

Given two binary search trees `root1` and `root2`.

Return a list containing all the integers from both trees sorted in
ascending order.

Example 1:

Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]

Example 2:

Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]

Example 3:

Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]

Example 4:

Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]

Example 5:

Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]

Constraints:

Each tree has at most `5000` nodes.

Each node's value is between `[-10^5, 10^5]`.

【中文翻译】
给定两个二叉搜索树 root1 和 root2。

返回一个列表，包含两棵树中的所有整数，并按升序排序。

示例 1：
输入：root1 = [2,1,4], root2 = [1,0,3]
输出：[0,1,1,2,3,4]

示例 2：
输入：root1 = [0,-10,10], root2 = [5,1,7,0,2]
输出：[-10,0,0,1,2,5,7,10]

示例 3：
输入：root1 = [], root2 = [5,1,7,0,2]
输出：[0,1,2,5,7]

示例 4：
输入：root1 = [0,-10,10], root2 = []
输出：[-10,0,10]

示例 5：
输入：root1 = [1,null,8], root2 = [8,1]
输出：[1,1,8,8]

约束条件：
每棵树最多有 5000 个节点。
每个节点的值在 [-10^5, 10^5] 之间。
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        def inorder(root: Optional[TreeNode], result: List[int]) -> None:
            if not root:
                return
            inorder(root.left, result)
            result.append(root.val)
            inorder(root.right, result)

        list1, list2 = [], []
        inorder(root1, list1)
        inorder(root2, list2)

        # Merge two sorted lists
        result = []
        i = j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1
        # Append remaining elements
        result.extend(list1[i:])
        result.extend(list2[j:])
        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 对两棵二叉搜索树分别进行中序遍历 (inorder traversal)，
#    因为 BST 的中序遍历天然得到升序序列。
# 2. 得到两个已排序的列表后，使用双指针法将它们合并为一个有序列表。
# 3. 合并过程类似归并排序的 merge 操作：
#    比较两个列表的当前元素，取较小者放入结果列表。
# 4. 最后将剩余元素追加到结果末尾。
#
# 时间复杂度: O(N1 + N2)，N1 和 N2 分别为两棵树的节点数。
#  中序遍历每棵树 O(N)，合并两个有序列表 O(N1+N2)。
# 空间复杂度: O(N1 + N2)，存储两个有序列表和最终结果。
#
# 关键点:
# - BST 中序遍历得到有序序列是核心性质
# - 双指针合并两个有序列表是经典归并操作
# - 可以直接在一次遍历中不使用额外列表？可以使用迭代器/生成器，但实现复杂度较高
# - 注意处理树为空的情况（空树的中序遍历结果为空列表）










