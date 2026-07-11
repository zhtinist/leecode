"""
LeetCode #437 - Path Sum III
中文题名：路径总和 III
https://leetcode.com/problems/path-sum-iii/

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to
1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

【中文翻译】
给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过 1000 个节点，且节点数值范围是 [-1000000, 1000000] 的整数。

示例：

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有：

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""

from typing import List, Optional
from collections import defaultdict


class Solution:
    def pathSum(self, root: Optional['TreeNode'], targetSum: int) -> int:
        def dfs(node: Optional['TreeNode'], current_sum: int) -> int:
            if not node:
                return 0
            current_sum += node.val
            count = prefix_sum[current_sum - targetSum]
            prefix_sum[current_sum] += 1
            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)
            prefix_sum[current_sum] -= 1  # 回溯
            return count

        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1  # 处理从根节点开始的路径
        return dfs(root, 0)










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 前缀和 + 哈希表 + DFS 回溯：
# 问题转化为：在从根到任意节点的路径上，找有多少对节点 (ancestor, node)
# 使得 sum(ancestor..node) = targetSum。
# 即 prefix_sum[node] - prefix_sum[ancestor_parent] = targetSum，
# 即 prefix_sum[ancestor_parent] = prefix_sum[node] - targetSum。
# 1. DFS 从根向下遍历，维护当前路径的前缀和。
# 2. 用哈希表 prefix_sum 记录当前路径上各前缀和出现的次数。
# 3. 在每个节点，查找 prefix_sum[current - targetSum] 的次数，
#    即有多少个祖先节点到当前节点的子路径和等于 targetSum。
# 4. 递归左右子树后需回溯（恢复哈希表状态）。
# 5. prefix_sum[0] = 1 处理从根节点开始的路径。
#
# 时间复杂度: O(n)，每个节点访问一次
# 空间复杂度: O(H)，递归栈深度 + 哈希表（最坏 O(n)）
#
# 关键点:
# - 前缀和之差等于子路径和（与 #560 子数组和为 K 思路一致）
# - 哈希表记录当前路径上的前缀和频率
# - DFS 回溯时需恢复哈希表（只维护当前路径）
# - prefix_sum[0] = 1 处理完整路径
# - 路径必须是向下的，不能横跨左右子树
