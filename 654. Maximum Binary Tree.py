"""
LeetCode #654 - Maximum Binary Tree
中文题名：最大二叉树
https://leetcode.com/problems/maximum-binary-tree/

Given an integer array with no duplicates. A maximum tree building on this array is defined
as follow:

The root is the maximum number in the array.

The left subtree is the maximum tree constructed from left part subarray divided by the
maximum number.

The right subtree is the maximum tree constructed from right part subarray divided by
the maximum number.

Construct the maximum tree by the given array and output the root node of this tree.

Example 1:

Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

6
/   \
3     5
\    /
2  0
\
1

Note:

The size of the given array will be in the range [1,1000].

【中文翻译】
给定一个不含重复元素的整数数组。基于此数组构建的最大二叉树定义如下：

根节点是数组中的最大值。

左子树是通过数组中最大值左边部分构造的最大二叉树。

右子树是通过数组中最大值右边部分构造的最大二叉树。

通过给定的数组构建最大二叉树，并输出这棵树的根节点。

示例 1：

输入：[3,2,1,6,0,5]
输出：返回表示以下树的根节点：

      6
    /   \
   3     5
    \    /
     2  0
      \
       1

注意：

给定数组的大小在 [1, 1000] 范围内。
"""

from typing import List, Optional


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional['TreeNode']:
        if not nums:
            return None

        max_idx = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[max_idx]:
                max_idx = i

        root = TreeNode(nums[max_idx])
        root.left = self.constructMaximumBinaryTree(nums[:max_idx])
        root.right = self.constructMaximumBinaryTree(nums[max_idx + 1:])

        return root











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 递归构建。对于当前数组区间，执行以下步骤：
# 1. 找到区间内最大值及其索引
# 2. 以最大值为根节点
# 3. 用最大值左侧子数组递归构建左子树
# 4. 用最大值右侧子数组递归构建右子树
# 5. 返回根节点
# 递归终止条件：数组为空时返回 None。
#
# 时间复杂度: O(n^2) - 每层递归都要扫描区间找最大值，最坏情况（升序/降序数组）退化到 O(n^2)。
#           平均情况下为 O(n log n)（类似快速排序）
# 空间复杂度: O(n) - 递归栈的深度，最坏情况（斜树）为 O(n)
#
# 关键点:
# - 递归定义与分治思想：问题天然是递归的
# - 可以用单调栈优化到 O(n)：
#   遍历数组，维护递减栈，对于新元素 nums[i]，
#   如果小于栈顶，则作为栈顶的右子节点；
#   如果大于栈顶，则弹出直到栈顶更大（弹出的最后一个作为左子节点）
# - 递归解法简单直观，足够应对 n <= 1000 的约束
