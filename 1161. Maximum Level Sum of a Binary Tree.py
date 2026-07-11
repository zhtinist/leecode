"""
LeetCode #1161 - Maximum Level Sum of a Binary Tree
中文题名：最大层内元素和
https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

Given the `root` of a binary tree, the level of its root is `1`, the
level of its children is `2`, and so on.

Return the smallest level `X` such that the sum of all the values
of nodes at level `X` is maximal.

Example 1:

Input: [1,7,0,7,-8,null,null]
Output: 2
Explanation:
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

Note:

The number of nodes in the given tree is between `1` and `10^4`.

`-10^5 <= node.val <= 10^5`

【中文翻译】
给定二叉树的根节点 root，其根节点的层数为 1，子节点的层数为 2，以此类推。

返回层内元素之和最大的那一层的层号 X。如果有多个层的和相同，返回最小的层号。

示例 1：

输入：[1,7,0,7,-8,null,null]
输出：2
解释：
第 1 层元素之和 = 1。
第 2 层元素之和 = 7 + 0 = 7。
第 3 层元素之和 = 7 + (-8) = -1。
所以我们返回和第 2 层，该层的和最大。

注意：

树中的节点数在 1 到 10^4 之间。

`-10^5 <= node.val <= 10^5`
"""

from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return 0

        max_sum = float('-inf')
        max_level = 1
        level = 1

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

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level

            level += 1

        return max_level










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 标准的层序遍历（BFS）问题：
# 1. 使用队列（deque）进行广度优先搜索，按层遍历二叉树。
# 2. 对于每一层，累加该层所有节点的值得到 level_sum。
# 3. 维护全局最大和 max_sum 和对应的层级 max_level。
# 4. 当某层的和严格大于 max_sum 时更新（使用 > 确保返回最小的层级号）。
# 5. 层号从 1 开始递增。
#
# 时间复杂度: O(n) - 每个节点访问一次
# 空间复杂度: O(w) - 队列长度不超过树的最大宽度，最坏 O(n)
#
# 关键点:
# - BFS 按层遍历天然适合统计每层信息
# - 使用 for _ in range(len(queue)) 精确控制每层的遍历范围
# - 使用严格大于（>）而不是 >= 来确保返回最小的层级号
# - 节点值可能为负，max_sum 初始化为负无穷
