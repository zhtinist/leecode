"""
LeetCode #1222 - Queens That Can Attack the King
中文题名：可以攻击国王的皇后
https://leetcode.com/problems/queens-that-can-attack-the-king/

On an 8x8 chessboard, there can be multiple Black Queens and one White King.

Given an array of integer coordinates `queens` that represents the positions of
the Black Queens, and a pair of coordinates `king` that represent the position of
the White King, return the coordinates of all the queens (in any order) that can attack the
King.

Example 1:

Input: queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]
Output: [[0,1],[1,0],[3,3]]
Explanation:
The queen at [0,1] can attack the king cause they're in the same row.
The queen at [1,0] can attack the king cause they're in the same column.
The queen at [3,3] can attack the king cause they're in the same diagnal.
The queen at [0,4] can't attack the king cause it's blocked by the queen at [0,1].
The queen at [4,0] can't attack the king cause it's blocked by the queen at [1,0].
The queen at [2,4] can't attack the king cause it's not in the same row/column/diagnal as the king.

Example 2:

Input: queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]
Output: [[2,2],[3,4],[4,4]]

Example 3:

Input: queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], king = [3,4]
Output: [[2,3],[1,4],[1,6],[3,7],[4,3],[5,4],[4,5]]

Constraints:

`1 <= queens.length <= 63`

`queens[0].length == 2`

`0 <= queens[i][j] < 8`

`king.length == 2`

`0 <= king[0], king[1] < 8`

At most one piece is allowed in a cell.

【中文翻译】
在一个 8x8 的棋盘上，放置着任意数量的黑皇后和一个白国王。

给定一个由整数坐标组成的数组 queens，表示所有黑皇后的位置，以及一对坐标 king，表示白国王的位置。返回所有可以攻击国王的皇后的坐标（任意顺序）。

示例 1：

输入：queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]
输出：[[0,1],[1,0],[3,3]]
解释：
[0,1] 的皇后可以攻击国王，因为他们在同一行。
[1,0] 的皇后可以攻击国王，因为他们在同一列。
[3,3] 的皇后可以攻击国王，因为他们在同一对角线。
[0,4] 的皇后不能攻击国王，因为她被 [0,1] 的皇后挡住了。
[4,0] 的皇后不能攻击国王，因为她被 [1,0] 的皇后挡住了。
[2,4] 的皇后不能攻击国王，因为她和国王不在同一行/列/对角线。

示例 2：

输入：queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]
输出：[[2,2],[3,4],[4,4]]

示例 3：

输入：queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], king = [3,4]
输出：[[2,3],[1,4],[1,6],[3,7],[4,3],[5,4],[4,5]]

约束条件：

1 <= queens.length <= 63
queens[0].length == 2
0 <= queens[i][j] < 8
king.length == 2
0 <= king[0], king[1] < 8
一个单元格上最多放置一个棋子。

"""

from typing import List, Optional


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queen_set = set(tuple(q) for q in queens)
        dirs = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1),           (0, 1),
                (1, -1),  (1, 0),  (1, 1)]

        res = []
        kx, ky = king

        for dx, dy in dirs:
            x, y = kx + dx, ky + dy
            while 0 <= x < 8 and 0 <= y < 8:
                if (x, y) in queen_set:
                    res.append([x, y])
                    break
                x += dx
                y += dy

        return res










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 从国王的位置出发，向 8 个方向（上、下、左、右及其四个对角线）依次搜索。
# 每个方向上遇到的第一个皇后就是该方向上可以攻击国王的皇后（因为后面的皇后会被前面这个挡住）。
# 使用哈希集合存储所有皇后的位置，便于 O(1) 判断某个坐标是否有皇后。
#
# 具体步骤：
# 1. 将所有皇后的坐标存入 set 以便快速查找。
# 2. 定义 8 个方向的方向向量。
# 3. 对每个方向：从国王位置出发，沿方向逐步移动，检查当前坐标是否有皇后。
#    - 如果有，将其加入结果并停止该方向的搜索（break）。
#    - 如果超出棋盘边界（0 <= x, y < 8），也停止搜索。
# 4. 返回所有找到的皇后坐标。
#
# 时间复杂度: O(1) - 棋盘固定 8x8，每个方向最多走 7 步，总操作数为常数
# 空间复杂度: O(1) - 皇后数量最多 63，但棋盘固定大小
#
# 关键点:
# - 从国王出发向外搜索而非遍历所有皇后，利用"挡住"特性（第一个遇到的就是答案）
# - 使用 set 存储皇后位置实现 O(1) 查找
# - 8 个方向向量可以用 range(-1, 2) 的嵌套循环生成，去除 (0, 0) 即可
