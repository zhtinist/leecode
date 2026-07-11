"""
LeetCode #894 - All Possible Full Binary Trees
中文题名：所有可能的满二叉树
https://leetcode.com/problems/all-possible-full-binary-trees/

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Return a list of all possible full binary trees with `N` nodes.  Each element
of the answer is the root node of one possible tree.

Each `node` of each tree in the answer must have `node.val
= 0`.

You may return the final list of trees in any order.

Example 1:

Input: 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
Explanation:

Note:

`1 <= N <= 20`

【中文翻译】

满二叉树是一棵每个节点恰好有 0 个或 2 个子节点的二叉树。

返回包含 `N` 个节点的所有可能满二叉树的列表。答案中的每个元素都是一棵可能的树的根节点。

答案中每棵树的每个 `节点` 的 `node.val = 0`。

你可以按任意顺序返回最终的树列表。

"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, N: int) -> List[Optional[TreeNode]]:
        # 满二叉树节点数必须为奇数
        if N % 2 == 0:
            return []

        memo = {}  # 记忆化：节点数 -> 所有可能的满二叉树列表

        def build(n: int) -> List[Optional[TreeNode]]:
            if n in memo:
                return memo[n]
            if n == 1:
                memo[n] = [TreeNode(0)]
                return memo[n]

            result = []
            # 左子树节点数 i 从 1 到 n-2，步长为 2（左右子树节点数都必须是奇数）
            for left_nodes in range(1, n - 1, 2):
                right_nodes = n - 1 - left_nodes
                for left_tree in build(left_nodes):
                    for right_tree in build(right_nodes):
                        root = TreeNode(0)
                        root.left = left_tree
                        root.right = right_tree
                        result.append(root)

            memo[n] = result
            return result

        return build(N)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 递归 + 记忆化。满二叉树的节点数必须是奇数（根 + 偶数的左右子树节点和）。
# 如果 N 为偶数，直接返回空列表。
# 递归构建：左子树节点数 i 从 1 到 N-2（步长2保证奇数），
# 右子树节点数为 N-1-i。
# 对所有左子树组合和右子树组合做笛卡尔积，组合成新的树。
# 使用 memo 字典记忆化每种节点数对应的满二叉树列表，避免重复计算。
#
# 时间复杂度: O(2^N) — Catalan数的量级，所有可能的满二叉树数量
# 空间复杂度: O(2^N) — 存储所有生成的树
#
# 关键点:
# - N 必须为奇数，偶数直接返回 []
# - 左右子树节点数都是奇数，步长为2枚举
# - 记忆化递归避免指数级重复计算
# - 题目要求 node.val = 0
