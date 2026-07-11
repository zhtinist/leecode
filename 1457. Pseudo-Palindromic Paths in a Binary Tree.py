"""
LeetCode #1457 - Pseudo-Palindromic Paths in a Binary Tree
中文题名：二叉树中的伪回文路径
https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/

Given a binary tree where node values are digits from 1 to 9. A path in the binary
tree is said to be pseudo-palindromic if at least one permutation of
the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the
root node to leaf nodes.

Example 1:

Input: root = [2,3,1,3,1,null,1]
Output: 2
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 2:

Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).

Example 3:

Input: root = [9]
Output: 1

Constraints:

The given binary tree will have between `1` and
`10^5` nodes.

Node values are digits from `1` to `9`.

【中文翻译】
给定一棵二叉树，其中节点值为 1 到 9 的数字。如果从根节点到叶节点的路径中，
节点值的至少一种排列是回文，则称该路径为伪回文路径。

返回从根节点到叶节点的伪回文路径的数量。

示例 1：

输入：root = [2,3,1,3,1,null,1]
输出：2
解释：上图表示了给定的二叉树。从根节点到叶节点有三条路径：红色路径 [2,3,3]、
绿色路径 [2,1,1] 和路径 [2,3,1]。在这些路径中，只有红色路径和绿色路径是伪回文路径，
因为红色路径 [2,3,3] 可以重新排列为 [3,2,3]（回文），
绿色路径 [2,1,1] 可以重新排列为 [1,2,1]（回文）。

示例 2：

输入：root = [2,1,1,1,3,null,null,null,null,null,1]
输出：1
解释：上图表示了给定的二叉树。从根节点到叶节点有三条路径：绿色路径 [2,1,1]、
路径 [2,1,3,1] 和路径 [2,1]。在这些路径中，只有绿色路径是伪回文路径，
因为 [2,1,1] 可以重新排列为 [1,2,1]（回文）。

示例 3：

输入：root = [9]
输出：1

约束条件：

给定的二叉树节点数在 `1` 到 `10^5` 之间。

节点值为 `1` 到 `9` 的数字。
"""

from typing import List, Optional


class Solution:
    def pseudoPalindromicPaths(self, root: Optional['TreeNode']) -> int:
        def dfs(node: Optional['TreeNode'], mask: int) -> int:
            if not node:
                return 0
            mask ^= (1 << node.val)
            if not node.left and not node.right:
                return 1 if (mask & (mask - 1)) == 0 else 0
            return dfs(node.left, mask) + dfs(node.right, mask)

        return dfs(root, 0)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用位掩码（bitmask）记录路径上每个数字（1-9）出现次数的奇偶性。
# 对于节点值为 val，将掩码的第 val 位取反（toggle）：mask ^= (1 << val)。
# 到达叶节点时，检查掩码中至多只有一位为 1，即 mask & (mask - 1) == 0
# （这意味着路径上至多只有一个数字出现奇数次，其余均为偶数次，可以排列成回文）。
# 递归累加左右子树的伪回文路径数量。
#
# 时间复杂度: O(N)  -- 每个节点访问一次
# 空间复杂度: O(H)  -- 递归栈深度，H 为树高
#
# 关键点:
# - 回文的充要条件是至多一个字符出现奇数次
# - 位掩码优雅地跟踪 1-9 数字的频率奇偶性
# - mask & (mask - 1) == 0 判断二进制中是否至多只有 1 个 1









