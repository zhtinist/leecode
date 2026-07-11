"""
LeetCode #1026 - Maximum Difference Between Node and Ancestor
中文题名：节点与其祖先之间的最大差值
https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

Given the `root` of a binary tree, find the maximum value `V` for which
there exists different nodes `A` and `B` where `V
= |A.val - B.val|` and `A` is an ancestor of `B`.

(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is
an ancestor of B.)

Example 1:

Input: [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation:
We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

Note:

The number of nodes in the tree is between `2` and `5000`.

Each node will have value between `0` and `100000`.

【中文翻译】
给定一棵二叉树的根节点 root，找出满足以下条件的最大值 V：存在不同的节点 A 和 B，使得 V = |A.val - B.val|，且 A 是 B 的祖先。

（如果 A 的任何子节点等于 B，或者 A 的任何子节点是 B 的祖先，那么节点 A 是 B 的祖先。）

示例 1：

输入：[8,3,10,1,6,null,14,null,null,4,7,13]
输出：7
解释：
我们有各种祖先-节点差值，部分如下：
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
在所有可能的差值中，最大值 7 由 |8 - 1| = 7 得到。

注意：

树中节点的数量在 2 到 5000 之间。
每个节点的值在 0 到 100000 之间。
"""

from typing import List, Optional


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, cur_min: int, cur_max: int) -> int:
            if not node:
                return cur_max - cur_min
            cur_min = min(cur_min, node.val)
            cur_max = max(cur_max, node.val)
            left = dfs(node.left, cur_min, cur_max)
            right = dfs(node.right, cur_min, cur_max)
            return max(left, right)

        return dfs(root, root.val, root.val)










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用深度优先搜索(DFS)遍历二叉树。在从根到叶子的路径上，维护路径上的最小值和最大值。
# 对于每个叶子节点，路径上的最大差值就是 max - min。由于祖先-后代关系要求祖先
# 必须在后代的路径上方，我们只需在整条根到叶子的路径上计算最大绝对值差值即可。
# 递归地计算左右子树中的最大差值，取全局最大值。
#
# 时间复杂度: O(N) - 每个节点访问一次
# 空间复杂度: O(H) - 递归栈深度，H为树高，最坏O(N)，平均O(logN)
#
# 关键点:
# - 维护路径上的最小值和最大值，差值即为路径上的最大祖先-后代差值
# - 叶子节点的 cur_max - cur_min 即为该路径的最大差值
# - 不需要考虑绝对值，因为 max >= min 恒成立
