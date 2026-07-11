"""
LeetCode #1145 - Binary Tree Coloring Game
中文题名：二叉树着色游戏
https://leetcode.com/problems/binary-tree-coloring-game/

Two players play a turn based game on a binary tree.  We are given the
`root` of this binary tree, and the number of nodes `n` in the
tree.  `n` is odd, and each node has a distinct value from
`1` to `n`.

Initially, the first player names a value `x` with `1 <= x <= n`,
and the second player names a value `y` with `1 <= y <= n` and
`y != x`.  The first player colors the node with value `x` red,
and the second player colors the node with value `y` blue.

Then, the players take turns starting with the first player.  In each turn, that player
chooses a node of their color (red if player 1, blue if player 2) and colors an uncolored
neighbor of the chosen node (either the left child, right child, or parent of the chosen
node.)

If (and only if) a player cannot choose such a node in this way, they must pass their
turn.  If both players pass their turn, the game ends, and the winner is the player
that colored more nodes.

You are the second player.  If it is possible to choose such a `y` to
ensure you win the game, return `true`.  If it is not possible, return
`false`.

Example 1:

Input: root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3
Output: true
Explanation: The second player can choose the node with value 2.

Constraints:

`root` is the root of a binary tree with `n` nodes and distinct
node values from `1` to `n`.

`n` is odd.

`1 <= x <= n <= 100`

【中文翻译】
两个玩家在二叉树上玩一个回合制游戏。给定这棵二叉树的根节点 root，以及树中的节点数 n。n 是奇数，每个节点的值从 1 到 n 各不相同。

最初，第一个玩家指定一个值 x（1 <= x <= n），第二个玩家指定一个值 y（1 <= y <= n 且 y != x）。第一个玩家将值为 x 的节点染成红色，第二个玩家将值为 y 的节点染成蓝色。

然后，玩家轮流进行，由第一个玩家开始。在每个回合中，该玩家选择一个自己颜色的节点（玩家 1 为红色，玩家 2 为蓝色），并为所选节点的一个未染色的邻居染色（可以是所选节点的左子节点、右子节点或父节点）。

当（且仅当）一个玩家无法以这种方式选择节点时，该玩家必须跳过回合。如果两个玩家都跳过回合，游戏结束，染色节点更多的玩家获胜。

你是第二个玩家。如果可以选择这样的 y 来确保你赢得游戏，返回 true。如果不可能，返回 false。

示例 1：

输入：root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3
输出：true
解释：第二个玩家可以选择值为 2 的节点。

约束条件：

root 是具有 n 个节点的二叉树的根节点，节点值从 1 到 n 各不相同。

n 是奇数。

`1 <= x <= n <= 100`
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        # Find the node with value x and count sizes of its left subtree,
        # right subtree, and the rest of the tree
        self.left_count = 0
        self.right_count = 0

        def count_nodes(node: TreeNode) -> int:
            if not node:
                return 0
            left = count_nodes(node.left)
            right = count_nodes(node.right)
            if node.val == x:
                self.left_count = left
                self.right_count = right
            return left + right + 1

        count_nodes(root)

        # The three regions the second player can choose from:
        # 1. Left subtree of node x
        # 2. Right subtree of node x
        # 3. The rest of the tree: n - left_count - right_count - 1
        parent_side = n - self.left_count - self.right_count - 1

        # Second player wins if any region has more than half the nodes
        half = n // 2
        return (self.left_count > half or
                self.right_count > half or
                parent_side > half)










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 这是一道博弈策略题。第一个玩家选择了节点 x 后，树被分成三个区域：
# 1. x 的左子树
# 2. x 的右子树
# 3. 其余部分（x 的父节点及兄弟子树部分）
#
# 第二个玩家选择 y 后，第一个玩家的红色节点 x 会"阻塞" y 扩展到 x 所在方向。
# 因此，第二个玩家选择的 y 应该位于三个区域中节点数最多的那个区域，
# 这样才能在竞争中占据优势。
#
# 具体步骤：
# 1. 找到值为 x 的节点，统计其左子树大小 left_count 和右子树大小 right_count。
# 2. 计算第三个区域的大小：parent_side = n - left_count - right_count - 1。
# 3. 如果三个区域中任意一个的大小 > n/2，则第二个玩家选择该区域中的节点作为 y，
#    即可获得超过一半的节点，从而获胜。
# 4. 如果没有任何区域大于 n/2，则第一个玩家选择 x 后占据了最优位置，第二个玩家无法获胜。
#
# 时间复杂度: O(n) - 需要遍历整棵树来统计节点数
# 空间复杂度: O(h) - 递归栈深度，h 为树的高度，最坏 O(n)
#
# 关键点:
# - 第一个玩家选的节点 x 将树分为三个独立区域
# - 第二个玩家只能控制其中一个区域（被 x 阻塞）
# - 只要存在一个区域大小超过 n/2，第二个玩家就能赢
# - y 应该选在 x 的左孩子、右孩子或父节点，即紧邻 x 的位置
