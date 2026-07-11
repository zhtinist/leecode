"""
LeetCode #3319 - K-th Largest Perfect Subtree Size in Binary Tree
第 K 大的完美二叉子树的大小
https://leetcode.cn/problems/k-th-largest-perfect-subtree-size-in-binary-tree/

给你一棵 二叉树 的根节点 `root` 和一个整数`k`。
返回第 `k` 大的 完美二叉子树 的大小，如果不存在则返回 `-1`。
完美二叉树 是指所有叶子节点都在同一层级的树，且每个父节点恰有两个子节点。

示例 1：

输入： root = [5,3,6,5,2,5,7,1,8,null,null,6,8], k = 2
输出： 3
解释：

完美二叉子树的根节点在图中以黑色突出显示。它们的大小按非递增顺序排列为 `[3, 3, 1, 1, 1, 1, 1, 1]`。
第 `2` 大的完美二叉子树的大小是 3。
示例 2：

输入： root = [1,2,3,4,5,6,7], k = 1
输出： 7
解释：

完美二叉子树的大小按非递增顺序排列为 `[7, 3, 3, 1, 1, 1, 1]`。最大的完美二叉子树的大小是 7。
示例 3：

输入： root = [1,2,3,null,4], k = 3
输出： -1
解释：

完美二叉子树的大小按非递增顺序排列为 `[1, 1]`。完美二叉子树的数量少于 3。

提示：
树中的节点数目在 `[1, 2000]` 范围内。
`1 <= Node.val <= 2000`
`1 <= k <= 1024`
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        sizes = []

        def dfs(node) -> int:
            """Return size if perfect subtree, else -1."""
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if left == -1 or right == -1 or left != right:
                return -1
            size = 1 + left + right
            sizes.append(size)
            return size

        dfs(root)
        sizes.sort(reverse=True)
        return sizes[k - 1] if k <= len(sizes) else -1



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Tree, Depth-First Search, Binary Tree, Sorting
#
# 解题思路:
# 使用DFS自底向上遍历二叉树。对于每个节点，递归计算左右子树是否为完美二叉树及其大小。
# 完美二叉树的条件：左右子树都是完美二叉树且大小相等。如果满足，则该子树大小 = 1 + 左子树大小 + 右子树大小。
# 收集所有完美子树的大小到列表中，排序后取第k大的值。如果不足k个则返回-1。
#
# 时间复杂度: O(n + m log m)，其中n为节点数，m为完美子树数量
# 空间复杂度: O(h + m)，h为树高（递归栈），m为完美子树数量
#
# 关键点:
# - 完美二叉树的判定条件：左右子树都是完美且大小相同
# - 空节点视为大小为0的完美子树（递归基）
# - 自底向上收集所有完美子树大小，排序取第k大
