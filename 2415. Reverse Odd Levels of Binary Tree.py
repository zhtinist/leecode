"""
LeetCode #2415 - Reverse Odd Levels of Binary Tree
反转二叉树的奇数层
https://leetcode.cn/problems/reverse-odd-levels-of-binary-tree/

给你一棵 完美 二叉树的根节点 `root` ，请你反转这棵树中每个 奇数 层的节点值。
例如，假设第 3 层的节点值是 `[2,1,3,4,7,11,29,18]` ，那么反转后它应该变成 `[18,29,11,7,4,3,1,2]` 。
反转后，返回树的根节点。
完美 二叉树需满足：二叉树的所有父节点都有两个子节点，且所有叶子节点都在同一层。
节点的 层数 等于该节点到根节点之间的边数。

示例 1：
输入：root = [2,3,5,8,13,21,34] 输出：[2,5,3,8,13,21,34] 解释： 这棵树只有一个奇数层。 在第 1 层的节点分别是 3、5 ，反转后为 5、3 。
示例 2：
输入：root = [7,13,11] 输出：[7,11,13] 解释：  在第 1 层的节点分别是 13、11 ，反转后为 11、13 。
示例 3：
输入：root = [0,1,2,0,0,0,0,1,1,1,1,2,2,2,2] 输出：[0,2,1,0,0,0,0,2,2,2,2,1,1,1,1] 解释：奇数层由非零值组成。 在第 1 层的节点分别是 1、2 ，反转后为 2、1 。 在第 3 层的节点分别是 1、1、1、1、2、2、2、2 ，反转后为 2、2、2、2、1、1、1、1 。

提示：
树中的节点数目在范围 `[1, 2^14]` 内
`0 <= Node.val <= 10^5`
`root` 是一棵 完美 二叉树
"""

from typing import List, Optional
from collections import deque


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        queue = deque([root])
        level = 0
        while queue:
            level_size = len(queue)
            nodes = list(queue)
            if level % 2 == 1:
                left, right = 0, level_size - 1
                while left < right:
                    nodes[left].val, nodes[right].val = nodes[right].val, nodes[left].val
                    left += 1
                    right -= 1
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return root



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Tree, Depth-First Search, Breadth-First Search, Binary Tree
#
# 解题思路:
# BFS层序遍历：使用队列进行广度优先搜索，记录当前层号。
# 对于奇数层，收集该层所有节点，使用双指针从两端向中间交换节点值。
# 注意只交换值（val），不改变树的结构。
#
# 时间复杂度: O(n)，每个节点访问一次，n为节点数。
# 空间复杂度: O(w)，w为树的最大宽度（完美二叉树最后一层约n/2个节点）。
#
# 关键点:
# - 完美二叉树的性质保证每层节点数为2^level。
# - 只交换节点值，不修改指针/结构。
# - BFS自然按层处理，适合层相关操作。
