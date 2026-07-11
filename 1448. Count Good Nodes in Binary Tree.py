"""
LeetCode #1448 - Count Good Nodes in Binary Tree
中文题名：统计二叉树中好节点的数目
https://leetcode.com/problems/count-good-nodes-in-binary-tree/

Given a binary tree `root`, a node X in the tree is
named good if in the path from root to X there are no
nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Example 1:

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:

Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.

Constraints:

The number of nodes in the binary tree is in the range `[1,
10^5]`.

Each node's value is between `[-10^4, 10^4]`.

【中文翻译】
给定一棵二叉树 `root`，如果从根节点到节点 X 的路径中没有节点的值大于 X 的值，
则称该节点 X 为"好节点"。

返回二叉树中好节点的数量。

示例 1：

输入：root = [3,1,4,3,null,1,5]
输出：4
解释：蓝色节点为好节点。
根节点 (3) 始终是好节点。
节点 4 -> (3,4) 是从根节点出发的路径中的最大值。
节点 5 -> (3,4,5) 是路径中的最大值。
节点 3 -> (3,1,3) 是路径中的最大值。

示例 2：

输入：root = [3,3,null,4,2]
输出：3
解释：节点 2 -> (3, 3, 2) 不是好节点，因为 "3" 比它大。

示例 3：

输入：root = [1]
输出：1
解释：根节点被视为好节点。

约束条件：

二叉树中节点的数量在 `[1, 10^5]` 范围内。

每个节点的值在 `[-10^4, 10^4]` 之间。
"""

from typing import List, Optional


class Solution:
    def goodNodes(self, root: Optional['TreeNode']) -> int:
        def dfs(node: Optional['TreeNode'], max_val: int) -> int:
            if not node:
                return 0
            count = 0
            if node.val >= max_val:
                count = 1
                max_val = node.val
            count += dfs(node.left, max_val)
            count += dfs(node.right, max_val)
            return count

        return dfs(root, root.val)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用 DFS 递归遍历二叉树，同时维护从根到当前节点的路径上的最大值 max_val。
# 对于每个节点，如果其值 >= max_val，则该节点是好节点（计数 +1），并更新 max_val。
# 将更新后的 max_val 传递给左右子树继续递归。
# 根节点始终是好节点（根节点值 >= 自身）。
#
# 时间复杂度: O(N)  -- 每个节点访问一次
# 空间复杂度: O(H)  -- 递归栈深度，H 为树的高度，最坏 O(N)，平均 O(log N)
#
# 关键点:
# - 维护路径最大值，而非全局最大值
# - 当节点值大于等于路径最大值时是好节点，并更新最大值
# - 根节点始终是好节点，因为 val >= val 始终成立









