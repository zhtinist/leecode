"""
LeetCode #623 - Add One Row to Tree
中文题名：在二叉树中增加一行
https://leetcode.com/problems/add-one-row-to-tree/

Given the root of a binary tree, then value `v` and depth `d`, you need
to add a row of nodes with value `v` at the given depth `d`. The root
node is at depth 1.

The adding rule is: given a positive integer depth `d`, for each NOT null tree
nodes `N` in depth `d-1`, create two tree nodes with value
`v` as `N's` left subtree root and right subtree root. And
`N's` original left subtree should be the left subtree of the new left
subtree root, its original right subtree should be the right subtree of the new right
subtree root. If depth `d` is 1 that means there is no depth d-1 at all, then
create a tree node with value v as the new root of the whole original tree, and the
original tree is the new root's left subtree.

Example 1:

Input:
A binary tree as following:
4
/   \
2     6
/ \   /
3   1 5

v = 1

d = 2

Output:
4
/ \
1   1
/     \
2       6
/ \     /
3   1   5

Example 2:

Input:
A binary tree as following:
4
/
2
/ \
3   1

v = 1

d = 3

Output:
4
/
2
/ \
1   1
/     \
3       1

Note:

The given d is in range [1, maximum depth of the given tree + 1].

The given binary tree has at least one tree node.

【中文翻译】
给定二叉树的根节点，以及值 `v` 和深度 `d`，
你需要在给定的深度 `d` 处添加一行值为 `v` 的节点。根节点位于深度 1。

添加规则如下：给定一个正整数深度 `d`，对于深度为 `d-1` 的每个非空树节点 `N`，
创建两个值为 `v` 的树节点，作为 `N` 的左子树根和右子树根。
`N` 原来的左子树应该是新左子树根的左子树，
其原来的右子树应该是新右子树根的右子树。
如果深度 `d` 为 1，意味着根本没有深度 d-1 的节点，
则创建一个值为 v 的新根树节点，整个原来的树作为新根的左子树。

示例 1：

输入：
二叉树如下：
       4
     /   \
    2     6
   / \   /
  3   1 5

v = 1
d = 2

输出：
       4
      / \
     1   1
    /     \
   2       6
  / \     /
 3   1   5

示例 2：

输入：
二叉树如下：
       4
      /
     2
    / \
   3   1

v = 1
d = 3

输出：
       4
      /
     2
    / \
   1   1
  /     \
 3       1

注意：

给定的 d 在 [1, 树的最大深度 + 1] 范围内。

给定的二叉树至少有一个节点。
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        def dfs(node: Optional[TreeNode], d: int) -> None:
            if not node:
                return
            if d == depth - 1:
                # Insert new nodes at the target depth
                left_child = TreeNode(val)
                right_child = TreeNode(val)
                left_child.left = node.left
                right_child.right = node.right
                node.left = left_child
                node.right = right_child
                return
            dfs(node.left, d + 1)
            dfs(node.right, d + 1)

        dfs(root, 1)
        return root



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 特殊情况：如果 d == 1，直接创建一个值为 v 的新根节点，将原树作为其左子树。
# 一般情况：使用 DFS 遍历到深度 d-1 的位置：
# 1. 对每个深度为 d-1 的非空节点，创建两个值为 v 的新节点。
# 2. 新左节点的左子树 = 原节点的左子树。
# 3. 新右节点的右子树 = 原节点的右子树。
# 4. 将新创建的节点接入原节点的左右子节点位置。
# 也可使用 BFS 更直观地按层遍历。
#
# 时间复杂度: O(n) - 最坏情况访问所有节点
# 空间复杂度: O(H) - H 为树的高度，递归栈空间
#
# 关键点:
# - d == 1 是特殊情况，需要单独处理
# - 当到达深度 d-1 时，需要保存原左右子树再插入新节点
# - 新节点的左子节点对应原左子树，新节点的右子节点对应原右子树
# - 一旦到达深度 d-1 就不需要再向下递归
