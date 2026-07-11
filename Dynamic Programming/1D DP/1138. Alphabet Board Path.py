"""
LeetCode #1138 - Alphabet Board Path
中文题名：字母板上的路径
https://leetcode.com/problems/alphabet-board-path/

On an alphabet board, we start at position `(0, 0)`, corresponding to character `board[0][0]`.

Here, `board = ["abcde", "fghij", "klmno", "pqrst",
"uvwxy", "z"]`, as shown in the diagram below.

We may make the following moves:

`'U'` moves our position up one row, if the position exists on the
board;

`'D'` moves our position down one row, if the position exists on the
board;

`'L'` moves our position left one column, if the position exists on
the board;

`'R'` moves our position right one column, if the position exists on
the board;

`'!'` adds the character `board[r][c]` at our current
position `(r, c)` to the answer.

(Here, the only positions that exist on the board are positions with letters on them.)

Return a sequence of moves that makes our answer equal to `target` in the
minimum number of moves.  You may return any path that does so.

Example 1:

Input: target = "leet"
Output: "DDR!UURRR!!DDD!"

Example 2:

Input: target = "code"
Output: "RR!DDRR!UUL!R!"

Constraints:

`1 <= target.length <= 100`

`target` consists only of English lowercase letters.

【中文翻译】
在一块字母板上，我们从位置 (0, 0) 开始，对应字符 board[0][0]。

这里 board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]，如下图所示。

我们可以进行以下移动：

'U' 将我们的位置向上移动一行，如果该位置在板上存在；
'D' 将我们的位置向下移动一行，如果该位置在板上存在；
'L' 将我们的位置向左移动一列，如果该位置在板上存在；
'R' 将我们的位置向右移动一列，如果该位置在板上存在；
'!' 将我们当前位置 (r, c) 上的字符 board[r][c] 添加到答案中。

（这里，板上存在的位置是那些有字母的位置。）

返回一个移动序列，使得我们的答案等于 target，且移动次数最少。你可以返回任意满足条件的路径。

示例 1：

输入：target = "leet"
输出："DDR!UURRR!!DDD!"

示例 2：

输入：target = "code"
输出："RR!DDRR!UUL!R!"

约束条件：

`1 <= target.length <= 100`

target 只包含英文小写字母。
"""

from typing import List, Optional


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        result = []
        cur_r, cur_c = 0, 0

        for ch in target:
            idx = ord(ch) - ord('a')
            target_r, target_c = idx // 5, idx % 5

            # Key: move left/up BEFORE right/down to avoid the hole at 'z' position
            while cur_c > target_c:
                result.append('L')
                cur_c -= 1
            while cur_r > target_r:
                result.append('U')
                cur_r -= 1
            while cur_c < target_c:
                result.append('R')
                cur_c += 1
            while cur_r < target_r:
                result.append('D')
                cur_r += 1

            result.append('!')

        return ''.join(result)










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 模拟在字母板上的移动过程。字母板是一个 5x5 的网格加上一个单独的 'z'（位置 (5, 0)）。
# 1. 将每个字母映射到坐标 (row, col)：row = index // 5, col = index % 5。
# 2. 从当前位置 (cur_r, cur_c) 移动到目标位置 (target_r, target_c)。
# 3. 关键陷阱：字母 'z' 位于 (5, 0)，即第 5 行第 0 列。第 5 行的 1-4 列是空的。
#    如果从 'z' 出发直接向右移动，会进入非法区域。
#    因此，移动顺序必须是：先左/上，再右/下。
#    具体来说：先处理 L 和 U（向左和向上），再处理 R 和 D（向右和向下）。
#    这样可以确保不会经过非法位置。
# 4. 到达目标后添加 '!' 表示选择该字母。
#
# 时间复杂度: O(n) - n 为目标字符串长度，每个字符最多进行 10 步移动
# 空间复杂度: O(1) - 不计返回值，只用了常数空间
#
# 关键点:
# - 字母板第 6 行只有 'z' 一个字母，移动时需注意避开空位
# - 移动顺序：必须 L/U 优先于 R/D，避免走到不存在的格子
