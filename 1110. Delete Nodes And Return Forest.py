"""
LeetCode #1110 - Delete Nodes And Return Forest
中文题名：删点成林
https://leetcode.com/problems/delete-nodes-and-return-forest/

Given the `root` of a binary tree, each node in the tree has a distinct
value.

After deleting all nodes with a value in `to_delete`, we are left with a
forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any
order.

Example 1:

Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]

Constraints:

The number of nodes in the given tree is at most `1000`.

Each node has a distinct value between `1` and `1000`.

`to_delete.length <= 1000`

`to_delete` contains distinct values between `1` and
`1000`.

【中文翻译】
给定二叉树的根节点 root，树上的每个节点都具有不同的值。

删除所有值在 to_delete 中的节点后，我们会得到一个森林（一些不相交的树构成的集合）。

返回森林中每棵树的根节点。你可以按任意顺序返回结果。

示例 1：

输入：root = [1,2,3,4,5,6,7], to_delete = [3,5]
输出：[[1,2,null,4],[6],[7]]

约束条件：

树中的节点数最多为 1000。

每个节点有一个介于 1 到 1000 之间的不同值。

`to_delete.length <= 1000`

to_delete 包含介于 1 到 1000 之间的不同值。
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        result = []

        def dfs(node, is_root):
            if not node:
                return None
            deleted = node.val in to_delete_set
            if is_root and not deleted:
                result.append(node)
            node.left = dfs(node.left, deleted)
            node.right = dfs(node.right, deleted)
            return None if deleted else node

        dfs(root, True)
        return result










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用后序遍历（DFS）递归处理每个节点。核心思路：
# 1. 将 to_delete 转为集合以便 O(1) 查找。
# 2. 定义递归函数 dfs(node, is_root)：
#    - is_root 表示当前节点是否应该成为新树的根。
#    - 如果节点值为空则返回 None。
#    - 判断当前节点是否需要删除。
#    - 如果 is_root 为 True 且不需要删除，将其加入结果列表。
#    - 递归处理左右子节点。注意：如果当前节点被删除，其子节点将成为新根（is_root=True）。
#    - 返回 None（如果被删除）或 node（如果保留）。
# 3. 从根节点开始调用 dfs(root, True)。
#
# 时间复杂度: O(n) - 每个节点访问一次
# 空间复杂度: O(h) - 递归调用栈深度，h 为树的高度，最坏 O(n)
#
# 关键点:
# - 后序遍历：先处理子节点再处理父节点，确保子节点在父节点处理前已确定去留
# - is_root 参数传递：父节点被删除时子节点成为新根
# - 使用 set 存储 to_delete 以获得 O(1) 查找
