"""
LeetCode #2583 - Kth Largest Sum in a Binary Tree
二叉树中的第 K 大层和
https://leetcode.cn/problems/kth-largest-sum-in-a-binary-tree/

给你一棵二叉树的根节点 `root` 和一个正整数 `k` 。
树中的 层和 是指 同一层 上节点值的总和。
返回树中第 `k` 大的层和（不一定不同）。如果树少于 `k` 层，则返回 `-1` 。
注意，如果两个节点与根节点的距离相同，则认为它们在同一层。

示例 1：

输入：root = [5,8,9,2,1,3,7,4,6], k = 2 输出：13 解释：树中每一层的层和分别是： - Level 1: 5 - Level 2: 8 + 9 = 17 - Level 3: 2 + 1 + 3 + 7 = 13 - Level 4: 4 + 6 = 10 第 2 大的层和等于 13 。
示例 2：

输入：root = [1,2,null,3], k = 1 输出：3 解释：最大的层和是 3 。

提示：
树中的节点数为 `n`
`2 <= n <= 10^5`
`1 <= Node.val <= 10^6`
`1 <= k <= n`
"""

from typing import List, Optional


class Solution:
    def kthLargestLevelSum(self, root: Optional['TreeNode'], k: int) -> int:
        from collections import deque
        if not root:
            return -1
        level_sums = []
        q = deque([root])
        while q:
            level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level_sums.append(level_sum)
        if len(level_sums) < k:
            return -1
        level_sums.sort(reverse=True)
        return level_sums[k - 1]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Tree, Breadth-First Search, Binary Tree, Sorting
#
# 解题思路:
# 使用BFS层序遍历二叉树，计算每层节点值的总和，存入列表。
# 将层和列表降序排序，返回第k个元素。若层数少于k则返回-1。
#
# 时间复杂度: O(N log N)，N为节点数
# 空间复杂度: O(N)
#
# 关键点:
# - BFS用队列实现层序遍历
# - 每层处理len(q)个节点确保同一层
# - 排序后取第k-1个（索引从0开始）
