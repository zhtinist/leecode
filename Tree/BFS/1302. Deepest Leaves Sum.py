"""
LeetCode #1302 - Deepest Leaves Sum
中文题名：层数最深叶子节点的和
https://leetcode.com/problems/deepest-leaves-sum/

Given a binary tree, return the sum of values of its deepest leaves.

Example 1:

Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15

Constraints:

The number of nodes in the tree is
between `1` and `10^4`.

The value of nodes is between `1` and `100`.

【中文翻译】
给定一棵二叉树，返回其最深叶子节点的值之和。

示例 1：
输入：root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
输出：15

约束条件：
树中节点的数量在 1 到 10^4 之间。
节点的值在 1 到 100 之间。
"""

from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        while queue:
            level_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not queue:
                return level_sum
        return 0



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用层序遍历（BFS）逐层处理二叉树的每一层节点。
# 对于每一层，计算该层所有节点的值之和。当处理完当前层后，
# 如果队列为空（即没有下一层节点），说明当前层就是最深层，
# 直接返回当前层的和。这样只需要一次遍历即可得到结果。
#
# 时间复杂度: O(N)，每个节点访问一次
# 空间复杂度: O(N)，队列最多存储树的最宽层节点数
#
# 关键点:
# - BFS 层序遍历天然适合处理"最深"或"最底层"问题
# - 每次迭代处理一整层，记录当前层和
# - 当下一层为空时，当前层即为最深层
# - 也可以使用 DFS 记录（深度，和），但 BFS 更直观
# - 使用 deque 作为队列，popleft() 为 O(1)










