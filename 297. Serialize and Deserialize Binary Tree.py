"""
LeetCode #297 - Serialize and Deserialize Binary Tree
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Serialization is the process of converting a data structure or object into a sequence of bits
so that it can be stored in a file or memory buffer, or transmitted across a network
connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on
how your serialization/deserialization algorithm should work. You just need to ensure that a
binary tree can be serialized to a string and this string can be deserialized to the
original tree structure.

Example:

You may serialize the following tree:

1
/ \
2   3
/ \
4   5

as `"[1,2,3,null,null,4,5]"`

Clarification: The above format is the same as how LeetCode serializes a binary tree.
You do not necessarily need to follow this format, so please be creative and come up with
different approaches yourself.

Note: Do not use class member/global/static variables to store states.
Your serialize and deserialize algorithms should be stateless.
"""

from typing import List, Optional


from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    """Serialize and deserialize a binary tree using BFS level-order traversal.

    Serialized format: comma-separated values with "null" for null nodes.
    Example: "1,2,3,null,null,4,5"
    """

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string using BFS."""
        if not root:
            return ""

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")

        # Remove trailing nulls
        while result and result[-1] == "null":
            result.pop()

        return ",".join(result)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes a string back to a tree using BFS."""
        if not data:
            return None

        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = deque([root])
        i = 1

        while queue and i < len(values):
            node = queue.popleft()

            # Left child
            if i < len(values) and values[i] != "null":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1

            # Right child
            if i < len(values) and values[i] != "null":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1

        return root


class Solution:
    """
    This problem uses Codec class, not Solution.
    The Codec implementation above is the complete solution.
    """
    pass


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Hard
# Paid Only: No
#
# 解题思路:
# 使用 BFS 层序遍历进行序列化和反序列化。
# 序列化（serialize）：使用队列进行 BFS，遇到 null 节点也加入队列（其子节点不再加入）。
# 输出格式为逗号分隔的字符串，如 "1,2,3,null,null,4,5"。
# 最后去掉尾部的 "null" 减少冗余。
# 反序列化（deserialize）：将字符串按逗号分割，第一个是根节点。
# 使用队列按 BFS 顺序重建树：每次从队列取出一个节点，连续读取两个值作为其
# 左右子节点（如果是 "null" 则跳过）。
#
# 时间复杂度: O(N) - 序列化和反序列化各遍历所有节点一次
# 空间复杂度: O(N) - 序列化字符串和 BFS 队列
#
# 关键点:
# - BFS 序列化自然地保持了树的层级结构
# - 序列化时 null 节点也需要入队以保持正确的结构对应
# - 反序列化时用队列维护 BFS 顺序
# - 去掉尾部 null 可以减少字符串大小
# - 也可以使用 DFS 先序遍历（需要两个遍历结果或用标记区分 null）
