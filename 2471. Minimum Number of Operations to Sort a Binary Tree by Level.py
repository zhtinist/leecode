"""
LeetCode #2471 - Minimum Number of Operations to Sort a Binary Tree by Level
逐层排序二叉树所需的最少操作数目
https://leetcode.cn/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/

给你一个 值互不相同 的二叉树的根节点 `root` 。
在一步操作中，你可以选择 同一层 上任意两个节点，交换这两个节点的值。
返回每一层按 严格递增顺序 排序所需的最少操作数目。
节点的 层数 是该节点和根节点之间的路径的边数。

示例 1 ：
输入：root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10] 输出：3 解释： - 交换 4 和 3 。第 2 层变为 [3,4] 。 - 交换 7 和 5 。第 3 层变为 [5,6,8,7] 。 - 交换 8 和 7 。第 3 层变为 [5,6,7,8] 。 共计用了 3 步操作，所以返回 3 。 可以证明 3 是需要的最少操作数目。
示例 2 ：
输入：root = [1,3,2,7,6,5,4] 输出：3 解释： - 交换 3 和 2 。第 2 层变为 [2,3] 。  - 交换 7 和 4 。第 3 层变为 [4,6,5,7] 。  - 交换 6 和 5 。第 3 层变为 [4,5,6,7] 。 共计用了 3 步操作，所以返回 3 。  可以证明 3 是需要的最少操作数目。
示例 3 ：
输入：root = [1,2,3,4,5,6] 输出：0 解释：每一层已经按递增顺序排序，所以返回 0 。

提示：
树中节点的数目在范围 `[1, 10^5]` 。
`1 <= Node.val <= 10^5`
树中的所有值 互不相同 。
"""

from typing import List, Optional


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        from collections import deque

        if not root:
            return 0

        total_swaps = 0
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_vals = []
            for _ in range(level_size):
                node = queue.popleft()
                level_vals.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Compute min swaps to sort this level
            n = len(level_vals)
            # Pair (value, original_index) and sort by value
            arr = [(val, idx) for idx, val in enumerate(level_vals)]
            arr.sort(key=lambda x: x[0])

            visited = [False] * n
            swaps = 0
            for i in range(n):
                if visited[i] or arr[i][1] == i:
                    continue
                # Count cycle size
                cycle_size = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = arr[j][1]
                    cycle_size += 1
                swaps += cycle_size - 1

            total_swaps += swaps

        return total_swaps

# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Tree, Breadth-First Search, Binary Tree
#
# 解题思路:
# 使用 BFS 逐层遍历二叉树，将每一层的节点值收集到数组中。
# 对每一层的数组，计算将其排序所需的最少交换次数：将元素与其原始下标配对后按值排序，
# 然后在索引排列中统计循环个数，每个长度为 c 的循环需要 c-1 次交换。
# 总最少交换次数 = sum(每层交换次数)。
#
# 时间复杂度: O(n log n)，其中 n 是节点总数，每层排序的总开销为 O(n log n)
# 空间复杂度: O(n)，BFS 队列和每层数组
#
# 关键点:
# - 最少交换次数 = n - 循环个数
# - 通过图论中的循环分解来计算最小交换次数
# - 节点值互不相同，保证排序结果唯一
