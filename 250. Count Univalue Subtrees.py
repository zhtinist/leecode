"""
LeetCode #250 - Count Univalue Subtrees
https://leetcode.com/problems/count-univalue-subtrees/

Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

Example :

Input:  root = [5,1,5,5,5,null,5]

5
/ \
1   5
/ \   \
5   5   5

Output: 4
"""

from typing import List, Optional


class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count = 0

        def dfs(node) -> bool:
            """返回以 node 为根的子树是否为 univalue 子树"""
            if not node:
                return True

            left_uni = dfs(node.left)
            right_uni = dfs(node.right)

            # 左右子树必须是 univalue
            if not left_uni or not right_uni:
                return False

            # 左子节点存在且值不等于当前节点
            if node.left and node.left.val != node.val:
                return False

            # 右子节点存在且值不等于当前节点
            if node.right and node.right.val != node.val:
                return False

            # 当前子树是 univalue
            self.count += 1
            return True

        dfs(root)
        return self.count


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: Yes
#
# 解题思路：
# 自底向上（后序遍历）递归判断。对每个节点，需要其左右子树都是 univalue，
# 且左右子节点（如果存在）的值与当前节点相同，则该子树也是 univalue。
# 用一个全局计数器统计满足条件的子树数量。空节点视为 univalue。
#
# 时间复杂度: O(n) — 每个节点访问一次
# 空间复杂度: O(h) — 递归栈深度，h 为树高，最坏 O(n)
#
# 关键点：
# - 后序遍历：先判断左右子树，再判断当前节点
# - 空节点视为 univalue（递归基础）
# - 检查子节点值是否与当前节点一致
