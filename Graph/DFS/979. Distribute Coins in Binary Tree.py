"""
LeetCode #979 - Distribute Coins in Binary Tree
中文题名：在二叉树中分配硬币
https://leetcode.com/problems/distribute-coins-in-binary-tree/

给定一个有 N 个节点的二叉树的根节点 root，树中每个节点 node.val 个硬币，并且总共有 N 枚硬币。

在一次移动中，我们可以选择两个相邻的节点，将一枚硬币从一个节点移动到另一个节点。（移动可以是从父节点到子节点，或从子节点到父节点。）

返回使每个节点上都只有一枚硬币所需的最少移动次数。

示例 1：

输入：[3,0,0]
输出：2
解释：从树的根节点开始，我们将一枚硬币移到它的左子节点上，一枚硬币移到它的右子节点上。

示例 2：

输入：[0,3,0]
输出：3
解释：从根节点的左子节点开始，我们将两枚硬币移到根节点上（需要两次移动）。然后，我们将一枚硬币从根节点移到右子节点。

示例 3：

输入：[1,0,2]
输出：2

示例 4：

输入：[1,0,0,null,3]
输出：4

注意：

1 <= N <= 100
0 <= node.val <= N

【中文翻译】
给定一棵二叉树，每个节点上有一定数量的硬币，总硬币数等于节点总数。每次可以沿边移动一枚硬币。问至少需要多少次移动，才能让每个节点都恰好有一枚硬币。

"""

from typing import List, Optional


class Solution:
    def distributeCoins(self, root: Optional['TreeNode']) -> int:
        self.moves = 0

        def dfs(node: Optional['TreeNode']) -> int:
            if node is None:
                return 0
            left_excess = dfs(node.left)
            right_excess = dfs(node.right)
            # Moves needed through this node = abs(excess from left) + abs(excess from right)
            self.moves += abs(left_excess) + abs(right_excess)
            # Excess of this subtree: node.val + left_excess + right_excess - 1
            return node.val + left_excess + right_excess - 1

        dfs(root)
        return self.moves



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 自底向上的 DFS + 后序遍历（DFS 返回每棵子树的过剩/不足硬币数）：
# 1. 定义 dfs(node) 返回该子树需要送给父节点（正数）或从父节点接收（负数）的硬币数。
#    - 如果返回正数 x，表示该子树多出 x 枚硬币需要向上传递。
#    - 如果返回负数 -x，表示该子树缺少 x 枚硬币需要从上面获得。
# 2. 对于每个节点，它的过剩量 = node.val + left_excess + right_excess - 1。
#    - node.val 是当前节点的硬币数。
#    - left_excess 和 right_excess 是子树的过剩量。
#    - 减 1 是因为该节点本身需要保留一枚硬币。
# 3. 移动次数累加：每次穿过当前节点到子节点的硬币移动都需要计算。
#    - 左子树需要向上或向下传递 |left_excess| 枚硬币，每枚硬币走过边需要一次移动。
#    - 右子树同理。
#    - moves += abs(left_excess) + abs(right_excess)。
# 4. 最终返回全局累加的总移动次数。
#
# 时间复杂度: O(N)，每个节点恰好访问一次
# 空间复杂度: O(H)，递归栈深度。H 为树高，最坏 O(N)，平均 O(log N)
#
# 关键点:
# - 后序遍历：先处理子树再处理根节点，计算硬币过剩/不足
# - 过剩量公式：node.val + left_excess + right_excess - 1
# - 移动次数 = 所有子树的过剩量绝对值之和（每枚硬币移动一次穿过一条边）
# - 问题可以归结为：每条边上需要流过多少枚硬币
