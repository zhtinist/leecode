"""
LeetCode #2096 - Step-By-Step Directions From a Binary Tree Node to Another
从二叉树一个节点到另一个节点每一步的方向
https://leetcode.cn/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

给你一棵 二叉树 的根节点 `root` ，这棵二叉树总共有 `n` 个节点。每个节点的值为 `1` 到 `n` 中的一个整数，且互不相同。给你一个整数 `startValue` ，表示起点节点 `s` 的值，和另一个不同的整数 `destValue` ，表示终点节点 `t` 的值。
请找到从节点 `s` 到节点 `t` 的 最短路径 ，并以字符串的形式返回每一步的方向。每一步用 大写 字母 `'L'` ，`'R'` 和 `'U'` 分别表示一种方向：
`'L'` 表示从一个节点前往它的 左孩子 节点。
`'R'` 表示从一个节点前往它的 右孩子 节点。
`'U'` 表示从一个节点前往它的 父 节点。
请你返回从 `s` 到 `t` 最短路径 每一步的方向。

示例 1：

输入：root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6 输出："UURL" 解释：最短路径为：3 → 1 → 5 → 2 → 6 。
示例 2：

输入：root = [2,1], startValue = 2, destValue = 1 输出："L" 解释：最短路径为：2 → 1 。

提示：
树中节点数目为 `n` 。
`2 <= n <= 10^5`
`1 <= Node.val <= n`
树中所有节点的值 互不相同 。
`1 <= startValue, destValue <= n`
`startValue != destValue`
"""

from typing import List, Optional


class Solution:
    def getDirections(self, root: Optional['TreeNode'], startValue: int, destValue: int) -> str:
        def find_path(node, target, path):
            if not node:
                return False
            if node.val == target:
                return True
            path.append('L')
            if find_path(node.left, target, path):
                return True
            path.pop()
            path.append('R')
            if find_path(node.right, target, path):
                return True
            path.pop()
            return False

        path_to_start = []
        path_to_dest = []
        find_path(root, startValue, path_to_start)
        find_path(root, destValue, path_to_dest)

        i = 0
        while i < len(path_to_start) and i < len(path_to_dest) and path_to_start[i] == path_to_dest[i]:
            i += 1

        result = 'U' * (len(path_to_start) - i) + ''.join(path_to_dest[i:])
        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Tree, Depth-First Search, String, Binary Tree
#
# 解题思路:
# 使用DFS分别找到从根节点到startValue和destValue的路径（用'L'和'R'表示方向）。
# 找到两条路径的公共前缀——这部分对应从根到最近公共祖先(LCA)的路径。
# 从start到LCA需要向上回溯，每一步用'U'表示；从LCA到dest沿用dest路径中剩余的部分。
# 最终结果 = 'U' * (start路径长度 - 公共前缀长度) + dest路径的剩余部分（从公共前缀之后开始）。
#
# 时间复杂度: O(N)，其中N为树的节点数。DFS遍历每个节点最多一次。
# 空间复杂度: O(H)，其中H为树的高度。递归调用栈和路径列表的空间开销。
#
# 关键点:
# - DFS回溯记录路径：左子树搜'L'，右子树搜'R'，搜不到则pop回溯。
# - 两条路径的公共前缀即对应LCA，公共部分之后第一个不同的位置就是分叉点。
# - start到LCA的距离 = len(path_to_start) - i，每一步都是'U'（向上）。
