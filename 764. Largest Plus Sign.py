"""
LeetCode #764 - Largest Plus Sign
中文题名：最大加号标志
https://leetcode.com/problems/largest-plus-sign/

In a 2D `grid` from (0, 0) to (N-1, N-1), every cell contains a `1`,
except those cells in the given list `mines` which are `0`. What is
the largest axis-aligned plus sign of `1`s contained in the grid? Return the
order of the plus sign. If there is none, return 0.

An "axis-aligned plus sign of `1`s of order k" has some center
`grid[x][y] = 1` along with 4 arms of length `k-1` going up, down,
left, and right, and made of `1`s. This is demonstrated in the diagrams below.
Note that there could be `0`s or `1`s beyond the arms of the plus
sign, only the relevant area of the plus sign is checked for 1s.

Examples of Axis-Aligned Plus Signs of Order k:

Order 1:
000
010
000

Order 2:
00000
00100
01110
00100
00000

Order 3:
0000000
0001000
0001000
0111110
0001000
0001000
0000000

Example 1:

Input: N = 5, mines = [[4, 2]]
Output: 2
Explanation:
11111
11111
11111
11111
11011
In the above grid, the largest plus sign can only be order 2.  One of them is marked in bold.

Example 2:

Input: N = 2, mines = []
Output: 1
Explanation:
There is no plus sign of order 2, but there is of order 1.

Example 3:

Input: N = 1, mines = [[0, 0]]
Output: 0
Explanation:
There is no plus sign, so return 0.

Note:

`N` will be an integer in the range `[1, 500]`.

`mines` will have length at most `5000`.

`mines[i]` will be length 2 and consist of integers in the range `[0,
N-1]`.

(Additionally, programs submitted in C, C++, or C# will be judged with a slightly
smaller time limit.)

【中文翻译】
在一个从 (0, 0) 到 (N-1, N-1) 的二维网格 `grid` 中，除了给定列表 `mines` 中的单元格为 `0` 之外，每个单元格都包含一个 `1`。网格中包含的由 `1` 组成的最大轴对齐加号标志的阶数是多少？返回加号标志的阶数。如果不存在，返回 0。

一个"轴对齐的由 `1` 组成的 k 阶加号标志"具有一个中心 `grid[x][y] = 1`，以及向上、向下、向左和向右延伸的长度为 `k-1` 的 4 个臂，全部由 `1` 组成。注意加号标志的臂之外可能存在 `0` 或 `1`，只有加号标志的相关区域才被检查是否为 1。

示例 1：

输入：N = 5, mines = [[4, 2]]
输出：2
解释：最大的加号标志只能是 2 阶。

示例 2：

输入：N = 2, mines = []
输出：1
解释：不存在 2 阶的加号标志，但存在 1 阶的。

示例 3：

输入：N = 1, mines = [[0, 0]]
输出：0
解释：没有加号标志，因此返回 0。

注意：

`N` 是范围在 `[1, 500]` 内的整数。

`mines` 的长度最多为 `5000`。

（此外，使用 C、C++ 或 C# 提交的程序将以稍小的时间限制进行评判。）
"""

from typing import List, Optional


class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        banned = {tuple(m) for m in mines}
        dp = [[0] * N for _ in range(N)]
        ans = 0

        # left to right
        for r in range(N):
            count = 0
            for c in range(N):
                count = 0 if (r, c) in banned else count + 1
                dp[r][c] = count

        # right to left
        for r in range(N):
            count = 0
            for c in range(N - 1, -1, -1):
                count = 0 if (r, c) in banned else count + 1
                dp[r][c] = min(dp[r][c], count)

        # top to bottom
        for c in range(N):
            count = 0
            for r in range(N):
                count = 0 if (r, c) in banned else count + 1
                dp[r][c] = min(dp[r][c], count)

        # bottom to top
        for c in range(N):
            count = 0
            for r in range(N - 1, -1, -1):
                count = 0 if (r, c) in banned else count + 1
                dp[r][c] = min(dp[r][c], count)
                ans = max(ans, dp[r][c])

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 动态规划（四次扫描）。
# 对于每个单元格，我们需要知道从该单元格出发向上、下、左、右四个方向能延伸多少个连续的 1。
# 加号标志的阶数等于四个方向长度的最小值。
# 1. 使用一个 N×N 的 dp 数组，初始化为 0。
# 2. 第一次从左到右扫描每行，计算每个格子向左延伸的连续 1 个数，存入 dp。
# 3. 第二次从右到左扫描，计算向右延伸数，与 dp 中已有值取 min。
# 4. 第三次从上到下扫描，计算向上延伸数，取 min。
# 5. 第四次从下到上扫描，计算向下延伸数，取 min，同时更新全局最大值 ans。
# 6. 遇到地雷格子时，连续计数重置为 0。
# 使用集合 banned 存储地雷位置，O(1) 判断。
#
# 时间复杂度: O(N^2) - 四次遍历整个网格
# 空间复杂度: O(N^2) - dp 数组存储每个格子的中间结果
#
# 关键点:
# - 四次扫描分别计算四个方向的连续 1 长度
# - 每个格子的加号阶数 = min(左, 右, 上, 下)
# - 用地雷集合而非矩阵判断，节省空间和时间
# - 最终答案在第四次扫描中更新
