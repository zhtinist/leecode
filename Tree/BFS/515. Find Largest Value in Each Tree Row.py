"""
LeetCode #515 - Find Largest Value in Each Tree Row
中文题名：在每个树行中找最大值
https://leetcode.com/problems/find-largest-value-in-each-tree-row/

You need to find the largest value in each row of a binary tree.

Example:

Input:

1
/ \
3   2
/ \   \
5   3   9

Output: [1, 3, 9]

【中文翻译】
给定一棵二叉树，找出每一行中的最大值。

示例：
    输入：
          1
         / \
        3   2
       / \   \
      5   3   9
    输出：[1, 3, 9]
"""

from typing import List, Optional
from collections import deque


class Solution:
    def largestValues(self, root: Optional['TreeNode']) -> List[int]:
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            level_max = float('-inf')
            for _ in range(len(queue)):
                node = queue.popleft()
                level_max = max(level_max, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_max)
        return result


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用 BFS 层序遍历二叉树。对每一层，遍历该层的所有节点并记录最大值。
# 每层处理完后将最大值加入结果列表。通过 `for _ in range(len(queue))` 控制
# 每层只处理当前层的节点数，确保层与层之间不混淆。
#
# 时间复杂度: O(N) — 每个节点访问一次
# 空间复杂度: O(W) — 队列最大宽度，最坏情况 O(N/2) = O(N)
#
# 关键点:
# - 层序遍历的标准写法：先记录当前队列长度，再循环该次数
# - 空树需特殊处理，返回空列表
# - 每层用 float('-inf') 初始化最大值
