"""
LeetCode #449 - Serialize and Deserialize BST
中文题名：序列化和反序列化二叉搜索树
https://leetcode.com/problems/serialize-and-deserialize-bst/

Serialization is the process of converting a data structure or object into a sequence of bits
so that it can be stored in a file or memory buffer, or transmitted across a network
connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no
restriction on how your serialization/deserialization algorithm should work. You just need
to ensure that a binary search tree can be serialized to a string and this string can be
deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize
and deserialize algorithms should be stateless.

【中文翻译】
序列化是将数据结构或对象转换为比特序列的过程，以便存储在文件或内存缓冲区中，
或通过网络连接链路传输，之后在相同或不同的计算机环境中重建。

设计一个算法来序列化和反序列化二叉搜索树。对序列化/反序列化算法的工作方式没有限制。
只需要确保二叉搜索树可以序列化为字符串，并且该字符串可以反序列化为原始的树结构。
编码字符串应尽可能紧凑。

注意：不要使用类成员/全局/静态变量存储状态。序列化和反序列化算法应是无状态的。
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string using preorder traversal."""
        vals = []

        def preorder(node: Optional[TreeNode]) -> None:
            if not node:
                return
            vals.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return " ".join(vals)


    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        if not data:
            return None

        vals = list(map(int, data.split()))
        self.idx = 0

        def build(lower: int, upper: int) -> Optional[TreeNode]:
            if self.idx >= len(vals):
                return None

            val = vals[self.idx]
            if val < lower or val > upper:
                return None

            self.idx += 1
            node = TreeNode(val)
            node.left = build(lower, val)
            node.right = build(val, upper)
            return node

        return build(float("-inf"), float("inf"))


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 利用 BST 的性质，使用前序遍历进行序列化和反序列化。
#
# 序列化：
# - 前序遍历（根→左→右），将节点值用空格连接成字符串
# - 不需要存储空节点标记（如 #），因为 BST 的性质可以在反序列化时通过上下界恢复结构
# - 例如树 [2,1,3] 序列化为 "2 1 3"
#
# 反序列化：
# - 将字符串解析为数值列表
# - 递归构建：对于每个值，判断是否落在当前允许的 (lower, upper) 范围内
#   - 如果在范围内，创建节点，并分别以 (lower, val) 和 (val, upper) 为界构建左右子树
#   - 如果不在范围内，回溯（上层会尝试将其作为右子树的一部分）
# - 利用 BST 性质：左子树所有值 < 根，右子树所有值 > 根，所以通过上下界可确定每个值的位置
#
# 时间复杂度: O(N) — 每个节点访问一次（序列化和反序列化各 O(N)）
# 空间复杂度: O(N) — 序列化字符串和递归栈
#
# 关键点:
# - 前序遍历序列化，不需要空节点标记（相比普通二叉树的序列化更紧凑）
# - 反序列化时利用 BST 的上下界约束恢复树结构
# - 注意 Codec 类名（不是 Solution）
