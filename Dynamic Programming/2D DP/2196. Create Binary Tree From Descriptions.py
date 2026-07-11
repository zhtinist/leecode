"""
LeetCode #2196 - Create Binary Tree From Descriptions
根据描述创建二叉树
https://leetcode.cn/problems/create-binary-tree-from-descriptions/

给你一个二维整数数组 `descriptions` ，其中 `descriptions[i] = [parent_i, child_i, isLeft_i]` 表示 `parent_i` 是 `child_i` 在 二叉树 中的 父节点，二叉树中各节点的值 互不相同 。此外：
如果 `isLeft_i == 1` ，那么 `child_i` 就是 `parent_i` 的左子节点。
如果 `isLeft_i == 0` ，那么 `child_i` 就是 `parent_i` 的右子节点。
请你根据 `descriptions` 的描述来构造二叉树并返回其 根节点 。
测试用例会保证可以构造出 有效 的二叉树。

示例 1：

输入：descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]] 输出：[50,20,80,15,17,19] 解释：根节点是值为 50 的节点，因为它没有父节点。 结果二叉树如上图所示。
示例 2：

输入：descriptions = [[1,2,1],[2,3,0],[3,4,1]] 输出：[1,2,null,null,3,4] 解释：根节点是值为 1 的节点，因为它没有父节点。  结果二叉树如上图所示。

提示：
`1 <= descriptions.length <= 10^4`
`descriptions[i].length == 3`
`1 <= parent_i, child_i <= 10^5`
`0 <= isLeft_i <= 1`
`descriptions` 所描述的二叉树是一棵有效二叉树
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes: dict[int, TreeNode] = {}
        children: set[int] = set()

        for parent, child, isLeft in descriptions:
            # Get or create parent node
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            # Get or create child node
            if child not in nodes:
                nodes[child] = TreeNode(child)

            # Link child to parent
            if isLeft == 1:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]

            # Record that child has a parent
            children.add(child)

        # Root is the only node that never appears as a child
        for val, node in nodes.items():
            if val not in children:
                return node

        return None


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Tree, Array, Hash Table, Binary Tree
#
# 解题思路:
# 1. 使用哈希表 nodes 存储所有已创建的节点（键为节点值，值为 TreeNode 对象）。
# 2. 使用集合 children 记录所有作为子节点出现过节点值。
# 3. 遍历 descriptions 数组，对于每条描述 [parent, child, isLeft]：
#    - 确保 parent 和 child 对应的节点都已创建（若不存在则新建）。
#    - 根据 isLeft 的值，将 child 节点设为 parent 的左子节点或右子节点。
#    - 将 child 值加入 children 集合。
# 4. 遍历所有节点，不在 children 集合中的节点即为根节点（没有父节点），返回该节点。
#
# 时间复杂度: O(N)，其中 N 为 descriptions 的长度。只需一次遍历即可构建整棵树和找到根节点。
# 空间复杂度: O(N)，哈希表存储所有的树节点。
#
# 关键点:
# - 利用"二叉树中各节点的值互不相同"的特性，用哈希表快速查找/创建节点。
# - 利用"子节点集合"来定位根节点：根节点永远不会作为子节点出现。
# - 题目保证可以构造出有效的二叉树，所以一定能找到唯一的根节点。
