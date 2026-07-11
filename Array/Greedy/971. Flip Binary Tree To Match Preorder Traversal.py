"""
LeetCode #971 - Flip Binary Tree To Match Preorder Traversal
中文题名：翻转二叉树以匹配先序遍历
https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/

给定一个有 N 个节点的二叉树，每个节点都有一个从 {1, ..., N} 中取值且互不相同的值。

可以通过交换该节点的左右子节点来翻转二叉树中的节点。

考虑从根节点开始的先序遍历所报告的 N 个值的序列。将这一 N 个值的序列称为树的航行序列。

（回想一下，节点的先序遍历意味着我们先报告当前节点的值，然后先序遍历左子节点，再先序遍历右子节点。）

我们的目标是翻转树中最少数量的节点，使得树的航行序列与给定的 voyage 相匹配。

如果可以做到，则返回所有被翻转节点的值的列表。你可以按任意顺序返回答案。

如果无法做到，则返回列表 [-1]。

示例 1：

输入：root = [1,2], voyage = [2,1]
输出：[-1]

示例 2：

输入：root = [1,2,3], voyage = [1,3,2]
输出：[1]

示例 3：

输入：root = [1,2,3], voyage = [1,2,3]
输出：[]

注意：

1 <= N <= 100

【中文翻译】
给定一个有 N 个节点的二叉树，每个节点的值互不相同，取值范围为 {1, ..., N}。可以翻转任意节点的左右子树。请问最少翻转多少个节点，可以使树的先序遍历结果与给定的 voyage 数组一致？如果可以，返回所有被翻转的节点值的列表（顺序任意）；否则返回 [-1]。

"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        self.idx = 0
        self.result = []

        def dfs(node: Optional[TreeNode]) -> bool:
            if node is None:
                return True
            if node.val != voyage[self.idx]:
                return False
            self.idx += 1
            if node.left and node.left.val != voyage[self.idx]:
                # Need to flip: swap left and right
                self.result.append(node.val)
                return dfs(node.right) and dfs(node.left)
            return dfs(node.left) and dfs(node.right)

        if dfs(root):
            return self.result
        return [-1]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用贪心 DFS 进行先序遍历匹配：
# 1. 维护一个全局索引 idx 指向 voyage 数组当前应匹配的位置。
# 2. 对树进行先序遍历（DFS），每次访问节点时检查当前节点值是否等于 voyage[idx]：
#    - 如果不相等，说明无法匹配，返回 False。
#    - 如果相等，idx 加 1。
# 3. 关键判断：如果当前节点有左子节点，且左子节点的值不等于 voyage[idx]
#    （即下一个期望值），则说明需要翻转当前节点。
#    - 翻转操作：交换左右子树的遍历顺序，即先遍历右子树再遍历左子树。
#    - 将当前节点值加入结果列表。
# 4. 如果 voyage 数组中还有未被匹配的元素但树已遍历完，说明无法匹配。
# 5. 最终，如果整棵树成功匹配，返回翻转列表；否则返回 [-1]。
#
# 时间复杂度: O(N)，每个节点恰好访问一次
# 空间复杂度: O(H)，H 为树的高度，递归栈空间。最坏情况 O(N)（链状树），平均 O(log N)
#
# 关键点:
# - 利用先序遍历的顺序特性，贪心判断是否需要翻转
# - 当左子节点值不等于下一个期望值时，必须翻转当前节点
# - 翻转后交换左右子树的遍历顺序
# - 使用闭包中的 self.idx 追踪 voyage 索引
