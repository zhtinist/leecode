"""
LeetCode #2265 - Count Nodes Equal to Average of Subtree
统计值等于子树平均值的节点数
https://leetcode.cn/problems/count-nodes-equal-to-average-of-subtree/

给你一棵二叉树的根节点 `root` ，找出并返回满足要求的节点数，要求节点的值等于其 子树 中值的 平均值 。
注意：
`n` 个元素的平均值可以由 `n` 个元素 求和 然后再除以 `n` ，并 向下舍入 到最近的整数。
`root` 的 子树 由 `root` 和它的所有后代组成。

示例 1：
输入：root = [4,8,5,0,1,null,6] 输出：5 解释： 对值为 4 的节点：子树的平均值 (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4 。 对值为 5 的节点：子树的平均值 (5 + 6) / 2 = 11 / 2 = 5 。 对值为 0 的节点：子树的平均值 0 / 1 = 0 。 对值为 1 的节点：子树的平均值 1 / 1 = 1 。 对值为 6 的节点：子树的平均值 6 / 1 = 6 。
示例 2：
输入：root = [1] 输出：1 解释：对值为 1 的节点：子树的平均值 1 / 1 = 1。

提示：
树中节点数目在范围 `[1, 1000]` 内
`0 <= Node.val <= 1000`
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        """
        Return the count of nodes whose value equals the floor average of its subtree.
        Perform a post-order DFS to compute (sum, count) for each subtree.
        At each node, check if node.val == sum // count.
        """
        self.result = 0

        def dfs(node: Optional[TreeNode]) -> tuple[int, int]:
            """Returns (sum_of_subtree, count_of_nodes_in_subtree)."""
            if not node:
                return (0, 0)

            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1

            if node.val == total_sum // total_count:
                self.result += 1

            return (total_sum, total_count)

        dfs(root)
        return self.result


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Tree, Depth-First Search, Binary Tree
#
# 解题思路:
# 使用后序遍历 (Post-order DFS) 自底向上计算每个子树的总和与节点数。
# 对于每个节点，获取其左子树和右子树的 (总和, 节点数)，
# 然后计算当前子树的总和 = 左子树总和 + 右子树总和 + 当前节点值，
# 以及节点总数 = 左子树节点数 + 右子树节点数 + 1。
# 判断当前节点值是否等于 floor(总和 / 节点数)，即 total_sum // total_count。
# 使用一个实例变量 self.result 累计符合条件的节点数。
#
# 时间复杂度: O(n)，其中 n 是树的节点数。每个节点被访问一次。
# 空间复杂度: O(h)，其中 h 是树的高度，为递归调用栈的深度。最坏情况（退化成链表）为 O(n)。
#
# 关键点:
# - 后序遍历确保处理当前节点时，子树的统计信息已经就绪
# - 平均值向下取整即整数除法 //
# - 叶子节点单独构成子树（1 个节点），和等于自身，平均值也等于自身
# - 使用元组返回 (sum, count) 简洁高效
