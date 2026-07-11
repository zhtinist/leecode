"""
LeetCode #2476 - Closest Nodes Queries in a Binary Search Tree
二叉搜索树最近节点查询
https://leetcode.cn/problems/closest-nodes-queries-in-a-binary-search-tree/

给你一个 二叉搜索树 的根节点 `root` ，和一个由正整数组成、长度为 `n` 的数组 `queries` 。
请你找出一个长度为 `n` 的 二维 答案数组 `answer` ，其中 `answer[i] = [min_i, max_i]` ：
`min_i` 是树中小于等于 `queries[i]` 的 最大值 。如果不存在这样的值，则使用 `-1` 代替。
`max_i` 是树中大于等于 `queries[i]` 的 最小值 。如果不存在这样的值，则使用 `-1` 代替。
返回数组 `answer` 。

示例 1 ：

输入：root = [6,2,13,1,4,9,15,null,null,null,null,null,null,14], queries = [2,5,16] 输出：[[2,2],[4,6],[15,-1]] 解释：按下面的描述找出并返回查询的答案： - 树中小于等于 2 的最大值是 2 ，且大于等于 2 的最小值也是 2 。所以第一个查询的答案是 [2,2] 。 - 树中小于等于 5 的最大值是 4 ，且大于等于 5 的最小值是 6 。所以第二个查询的答案是 [4,6] 。 - 树中小于等于 16 的最大值是 15 ，且大于等于 16 的最小值不存在。所以第三个查询的答案是 [15,-1] 。
示例 2 ：

输入：root = [4,null,9], queries = [3] 输出：[[-1,4]] 解释：树中不存在小于等于 3 的最大值，且大于等于 3 的最小值是 4 。所以查询的答案是 [-1,4] 。

提示：
树中节点的数目在范围 `[2, 10^5]` 内
`1 <= Node.val <= 10^6`
`n == queries.length`
`1 <= n <= 10^5`
`1 <= queries[i] <= 10^6`
"""

from typing import List, Optional


class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        from bisect import bisect_left

        # Inorder traversal to get sorted array
        sorted_vals = []
        def inorder(node: Optional[TreeNode]) -> None:
            if not node:
                return
            inorder(node.left)
            sorted_vals.append(node.val)
            inorder(node.right)

        inorder(root)

        n = len(sorted_vals)
        ans = []
        for q in queries:
            pos = bisect_left(sorted_vals, q)
            # Floor: max value <= q
            if pos < n and sorted_vals[pos] == q:
                floor_val = q
                ceil_val = q
            else:
                floor_val = sorted_vals[pos - 1] if pos > 0 else -1
                ceil_val = sorted_vals[pos] if pos < n else -1
            ans.append([floor_val, ceil_val])

        return ans

# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Tree, Depth-First Search, Binary Search Tree, Array, Binary Search, Binary Tree
#
# 解题思路:
# 利用二叉搜索树的中序遍历得到一个有序数组。
# 对于每个查询值 q，使用二分查找 (bisect_left) 找到第一个 >= q 的位置 pos。
# 如果 arr[pos] == q，则 floor 和 ceil 都是 q；
# 否则 floor = arr[pos-1]（如果 pos > 0），ceil = arr[pos]（如果 pos < n）。
#
# 时间复杂度: O(n + q * log n)，中序遍历 O(n)，每个查询二分查找 O(log n)
# 空间复杂度: O(n)，存储有序数组
#
# 关键点:
# - BST 中序遍历 = 有序序列
# - 使用 bisect_left 高效定位
# - 边界处理：pos=0 时无 floor，pos=n 时无 ceil
