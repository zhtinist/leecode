"""
LeetCode #2641 - Cousins in Binary Tree II
二叉树的堂兄弟节点 II
https://leetcode.cn/problems/cousins-in-binary-tree-ii/

给你一棵二叉树的根 `root` ，请你将每个节点的值替换成该节点的所有 堂兄弟节点值的和 。
如果两个节点在树中有相同的深度且它们的父节点不同，那么它们互为 堂兄弟 。
请你返回修改值之后，树的根 `root` 。
注意，一个节点的深度指的是从树根节点到这个节点经过的边数。

示例 1：

输入：root = [5,4,9,1,10,null,7] 输出：[0,0,0,7,7,null,11] 解释：上图展示了初始的二叉树和修改每个节点的值之后的二叉树。 - 值为 5 的节点没有堂兄弟，所以值修改为 0 。 - 值为 4 的节点没有堂兄弟，所以值修改为 0 。 - 值为 9 的节点没有堂兄弟，所以值修改为 0 。 - 值为 1 的节点有一个堂兄弟，值为 7 ，所以值修改为 7 。 - 值为 10 的节点有一个堂兄弟，值为 7 ，所以值修改为 7 。 - 值为 7 的节点有两个堂兄弟，值分别为 1 和 10 ，所以值修改为 11 。
示例 2：

输入：root = [3,1,2] 输出：[0,0,0] 解释：上图展示了初始的二叉树和修改每个节点的值之后的二叉树。 - 值为 3 的节点没有堂兄弟，所以值修改为 0 。 - 值为 1 的节点没有堂兄弟，所以值修改为 0 。 - 值为 2 的节点没有堂兄弟，所以值修改为 0 。

提示：
树中节点数目的范围是 `[1, 10^5]` 。
`1 <= Node.val <= 10^4`
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        # BFS: compute level sums
        from collections import deque
        level_sum = []
        q = deque([root])
        while q:
            s = 0
            for _ in range(len(q)):
                node = q.popleft()
                s += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level_sum.append(s)

        # Second BFS: replace values
        q = deque([root])
        root.val = 0  # root has no cousins
        level = 0
        while q:
            level += 1
            for _ in range(len(q)):
                node = q.popleft()
                # sum of children's values (siblings)
                sibling_sum = 0
                if node.left:
                    sibling_sum += node.left.val
                if node.right:
                    sibling_sum += node.right.val

                if node.left:
                    node.left.val = level_sum[level] - sibling_sum
                    q.append(node.left)
                if node.right:
                    node.right.val = level_sum[level] - sibling_sum
                    q.append(node.right)

        return root



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Tree, Depth-First Search, Breadth-First Search, Hash Table, Binary Tree
#
# 解题思路:
# 两次BFS。第一次计算每层所有节点的值总和(level_sum)。第二次遍历时，
# 计算每个节点的两个子节点值的和(sibling_sum)，然后用level_sum[level] - sibling_sum
# 作为堂兄弟节点值的和来替换子节点的值。根节点没有堂兄弟，值为0。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 堂兄弟 = 同层但不同父节点的节点
# - 节点新值 = 该层总和 - 该节点及其兄弟节点的和
# - 两次BFS：先计算每层总和，再更新每个节点的值
