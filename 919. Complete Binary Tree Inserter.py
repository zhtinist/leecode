"""
LeetCode #919 - Complete Binary Tree Inserter
中文题名：完全二叉树插入器
https://leetcode.com/problems/complete-binary-tree-inserter/

A complete binary tree is a binary tree in which every level, except possibly the
last, is completely filled, and all nodes are as far left as possible.

Write a data structure `CBTInserter` that is initialized with a complete
binary tree and supports the following operations:

`CBTInserter(TreeNode root)` initializes the data structure on a given tree with
head node `root`;

`CBTInserter.insert(int v)` will insert a `TreeNode` into the
tree with value `node.val = v` so that the tree remains complete,
and returns the value of the parent of the inserted
`TreeNode`;

`CBTInserter.get_root()` will return the head node of the tree.

Example 1:

Input: inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
Output: [null,1,[1,2]]

Example 2:

Input: inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4,5,6]],[7],[8],[]]
Output: [null,3,4,[1,2,3,4,5,6,7,8]]

【中文翻译】

完全二叉树是每一层（可能除了最后一层）都被完全填满，且所有节点都尽可能靠左的二叉树。
编写一个数据结构 CBTInserter，它用一个完全二叉树初始化，并支持以下操作：
- CBTInserter(TreeNode root)：用给定的头节点 root 初始化数据结构；
- CBTInserter.insert(int v)：插入一个值为 v 的 TreeNode，使树保持完全，
  并返回插入的 TreeNode 的父节点值；
- CBTInserter.get_root()：返回树的头节点。

"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        """
        BFS to build a deque of insertion candidates (nodes missing
        at least one child).
        """
        from collections import deque
        self.root = root
        self.deque = deque()
        # BFS to collect nodes that are not full
        q = deque([root])
        while q:
            node = q.popleft()
            if not node.left or not node.right:
                self.deque.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def insert(self, val: int) -> int:
        """
        Insert a new node with value val. The first node in deque
        is the insertion point. Return its parent's value.
        """
        from collections import deque
        parent = self.deque[0]
        new_node = TreeNode(val)

        if not parent.left:
            parent.left = new_node
        else:
            parent.right = new_node
            self.deque.popleft()  # parent is now full

        self.deque.append(new_node)  # new node needs children
        return parent.val

    def get_root(self) -> Optional[TreeNode]:
        """Return the root of the tree."""
        return self.root


# LeetCode expects class CBTInserter directly for this design problem.
# The Solution alias is provided for local testing convenience.
class Solution:
    def __init__(self, root: Optional[TreeNode]):
        self.inserter = CBTInserter(root)
    def insert(self, val: int) -> int:
        return self.inserter.insert(val)
    def get_root(self) -> Optional[TreeNode]:
        return self.inserter.get_root()



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 利用完全二叉树的性质 —— 节点按层序从左到右填充。
# 1. 初始化：使用 BFS 遍历整棵树，将所有缺少左子节点或右子节点的节点
#    加入一个双端队列 deque 中。
# 2. 插入：取队首节点作为父节点。如果其左子节点为空则插入到左子节点，
#    否则插入到右子节点并将该父节点从队列中移除（因为它已满）。
#    新插入的节点自身缺少两个子节点，将其加入队尾。
# 3. get_root：直接返回保存的根节点。
#
# 时间复杂度: 初始化 O(N)，插入 O(1) 均摊
# 空间复杂度: O(N)
#
# 关键点:
# - 使用队列维护"下一个可以插入的位置"
# - 完全二叉树的层序插入保证了正确性
# - 插入完成后将新节点加入队尾等待后续填充
