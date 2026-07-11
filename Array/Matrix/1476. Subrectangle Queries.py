"""
LeetCode #1476 - Subrectangle Queries
中文题名：子矩形查询
https://leetcode.com/problems/subrectangle-queries/

Implement the class `SubrectangleQueries` which receives a `rows
x cols` rectangle as a matrix of integers in the constructor and supports two
methods:

1.` updateSubrectangle(int row1, int col1, int row2, int col2, int
newValue)`

Updates all values with `newValue` in the subrectangle whose upper
left coordinate is `(row1,col1)` and bottom right coordinate is
`(row2,col2)`.

2.` getValue(int row, int col)`

Returns the current value of the coordinate `(row,col)` from the
rectangle.

Example 1:

Input
["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue","getValue"]
[[[[1,2,1],[4,3,4],[3,2,1],[1,1,1]]],[0,2],[0,0,3,2,5],[0,2],[3,1],[3,0,3,2,10],[3,1],[0,2]]
Output
[null,1,null,5,5,null,10,5]
Explanation
SubrectangleQueries subrectangleQueries = new SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]]);
// The initial rectangle (4x3) looks like:
// 1 2 1
// 4 3 4
// 3 2 1
// 1 1 1
subrectangleQueries.getValue(0, 2); // return 1
subrectangleQueries.updateSubrectangle(0, 0, 3, 2, 5);
// After this update the rectangle looks like:
// 5 5 5
// 5 5 5
// 5 5 5
// 5 5 5
subrectangleQueries.getValue(0, 2); // return 5
subrectangleQueries.getValue(3, 1); // return 5
subrectangleQueries.updateSubrectangle(3, 0, 3, 2, 10);
// After this update the rectangle looks like:
// 5   5   5
// 5   5   5
// 5   5   5
// 10  10  10
subrectangleQueries.getValue(3, 1); // return 10
subrectangleQueries.getValue(0, 2); // return 5

Example 2:

Input
["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue"]
[[[[1,1,1],[2,2,2],[3,3,3]]],[0,0],[0,0,2,2,100],[0,0],[2,2],[1,1,2,2,20],[2,2]]
Output
[null,1,null,100,100,null,20]
Explanation
SubrectangleQueries subrectangleQueries = new SubrectangleQueries([[1,1,1],[2,2,2],[3,3,3]]);
subrectangleQueries.getValue(0, 0); // return 1
subrectangleQueries.updateSubrectangle(0, 0, 2, 2, 100);
subrectangleQueries.getValue(0, 0); // return 100
subrectangleQueries.getValue(2, 2); // return 100
subrectangleQueries.updateSubrectangle(1, 1, 2, 2, 20);
subrectangleQueries.getValue(2, 2); // return 20

Constraints:

There will be at most `500` operations
considering both methods: `updateSubrectangle` and `getValue`.

`1 <= rows, cols <= 100`

`rows == rectangle.length`

`cols == rectangle[i].length`

`0 <= row1 <= row2 < rows`

`0 <= col1 <= col2 < cols`

`1 <= newValue, rectangle[i][j] <= 10^9`

`0 <= row < rows`

`0 <= col < cols`

【中文翻译】

实现类 `SubrectangleQueries`，它在构造函数中接收一个 `rows x cols` 的矩形（整数矩阵），并支持两个方法：

1. `updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)`
将左上角坐标为 `(row1,col1)`、右下角坐标为 `(row2,col2)` 的子矩形中的所有值更新为 `newValue`。

2. `getValue(int row, int col)`
返回矩形中坐标 `(row,col)` 的当前值。

示例 1：
输入：
["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue","getValue"]
[[[[1,2,1],[4,3,4],[3,2,1],[1,1,1]]],[0,2],[0,0,3,2,5],[0,2],[3,1],[3,0,3,2,10],[3,1],[0,2]]
输出：[null,1,null,5,5,null,10,5]
解释：
SubrectangleQueries subrectangleQueries = new SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]]);
// 初始矩形 (4x3) 如下：
// 1 2 1
// 4 3 4
// 3 2 1
// 1 1 1
subrectangleQueries.getValue(0, 2); // 返回 1
subrectangleQueries.updateSubrectangle(0, 0, 3, 2, 5);
// 此次更新后矩形变为：
// 5 5 5
// 5 5 5
// 5 5 5
// 5 5 5
subrectangleQueries.getValue(0, 2); // 返回 5
subrectangleQueries.getValue(3, 1); // 返回 5
subrectangleQueries.updateSubrectangle(3, 0, 3, 2, 10);
// 此次更新后矩形变为：
// 5   5   5
// 5   5   5
// 5   5   5
// 10  10  10
subrectangleQueries.getValue(3, 1); // 返回 10
subrectangleQueries.getValue(0, 2); // 返回 5

示例 2：
输入：
["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue"]
[[[[1,1,1],[2,2,2],[3,3,3]]],[0,0],[0,0,2,2,100],[0,0],[2,2],[1,1,2,2,20],[2,2]]
输出：[null,1,null,100,100,null,20]
解释：
SubrectangleQueries subrectangleQueries = new SubrectangleQueries([[1,1,1],[2,2,2],[3,3,3]]);
subrectangleQueries.getValue(0, 0); // 返回 1
subrectangleQueries.updateSubrectangle(0, 0, 2, 2, 100);
subrectangleQueries.getValue(0, 0); // 返回 100
subrectangleQueries.getValue(2, 2); // 返回 100
subrectangleQueries.updateSubrectangle(1, 1, 2, 2, 20);
subrectangleQueries.getValue(2, 2); // 返回 20

约束条件：
最多进行 500 次操作（包括 updateSubrectangle 和 getValue）。
1 <= rows, cols <= 100
0 <= row1 <= row2 < rows
0 <= col1 <= col2 < cols
1 <= newValue, rectangle[i][j] <= 10^9

"""

from typing import List, Optional


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rect = rectangle
        self.updates = []  # list of (row1, col1, row2, col2, newValue)

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.updates.append((row1, col1, row2, col2, newValue))

    def getValue(self, row: int, col: int) -> int:
        # Check updates from last to first for the latest covering update
        for i in range(len(self.updates) - 1, -1, -1):
            r1, c1, r2, c2, val = self.updates[i]
            if r1 <= row <= r2 and c1 <= col <= c2:
                return val
        return self.rect[row][col]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 保存原始矩形作为初始值。
# 2. 将每次 updateSubrectangle 操作记录到一个列表中，
#    存储 (row1, col1, row2, col2, newValue)。
# 3. getValue(row, col)：从更新列表的末尾向前遍历，
#    找到第一个覆盖 (row, col) 的更新，返回其 newValue。
#    如果没有任何更新覆盖该位置，返回原始矩形中的值。
# 4. 这种"惰性更新"方法的优势在于 updateSubrectangle 是 O(1)，
#    不需要实际修改整个子矩形。
#
# 时间复杂度: update O(1), getValue O(U)（U 为更新次数）
# 空间复杂度: O(U) 用于存储更新历史
#
# 关键点:
# - update 只需记录操作，不需要实际修改矩阵
# - getValue 从后向前遍历更新列表，找到最新的覆盖该位置的更新
# - 适用于更新操作频繁但查询较少的场景
# - 也可以直接修改矩形（update O(rows*cols)），取决于操作频率










