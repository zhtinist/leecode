"""
LeetCode #519 - Random Flip Matrix
中文题名：随机翻转矩阵
https://leetcode.com/problems/random-flip-matrix/

You are given the number of rows `n_rows` and number of columns
`n_cols` of a 2D binary matrix where all values are initially
0. Write a function `flip` which chooses a 0 value uniformly
at random, changes it to 1, and then returns the position `[row.id,
col.id]` of that value. Also, write a function `reset` which sets all
values back to 0. Try to minimize the number of calls to system's
Math.random() and optimize the time and space complexity.

Note:

`1 <= n_rows, n_cols <= 10000`

`0 <= row.id < n_rows` and `0 <= col.id < n_cols`

`flip` will not be called when the matrix has no 0 values left.

the total number of calls to `flip` and `reset` will
not exceed 1000.

Example 1:

Input:
["Solution","flip","flip","flip","flip"]
[[2,3],[],[],[],[]]
Output: [null,[0,1],[1,2],[1,0],[1,1]]

Example 2:

Input:
["Solution","flip","flip","reset","flip"]
[[1,2],[],[],[],[]]
Output: [null,[0,0],[0,1],null,[0,0]]

【中文翻译】
给定一个 2D 二进制矩阵的行数 n_rows 和列数 n_cols，所有值初始为 0。
实现 flip 函数：均匀随机地选择一个值为 0 的位置，将其改为 1，并返回该位置 [row.id, col.id]。
实现 reset 函数：将所有值重置为 0。尽量减少对系统 Math.random() 的调用次数，并优化时间和空间复杂度。

注意：
1 <= n_rows, n_cols <= 10000
0 <= row.id < n_rows，0 <= col.id < n_cols
当矩阵中没有 0 值时，flip 不会被调用。
flip 和 reset 的总调用次数不超过 1000。

示例 1：
    输入：["Solution","flip","flip","flip","flip"]
         [[2,3],[],[],[],[]]
    输出：[null,[0,1],[1,2],[1,0],[1,1]]

示例 2：
    输入：["Solution","flip","flip","reset","flip"]
         [[1,2],[],[],[],[]]
    输出：[null,[0,0],[0,1],null,[0,0]]
"""

import random
from typing import List, Optional


class Solution:
    def __init__(self, n_rows: int, n_cols: int):
        self.rows = n_rows
        self.cols = n_cols
        self.total = n_rows * n_cols
        # 映射已被翻转的索引到当前末尾可用索引
        self.used = {}

    def flip(self) -> List[int]:
        # 从剩余可用位置中随机选一个
        r = random.randint(0, self.total - 1)
        # 获取实际位置（可能已被映射到末尾）
        idx = self.used.get(r, r)
        # 将选中的索引映射到当前可用末尾，避免再次被选中
        self.total -= 1
        self.used[r] = self.used.get(self.total, self.total)
        return [idx // self.cols, idx % self.cols]

    def reset(self) -> None:
        self.total = self.rows * self.cols
        self.used.clear()


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 将二维矩阵压缩为一维数组（索引 0 到 total-1），使用 Fisher-Yates 洗牌算法的变体。
# 维护一个哈希表 `used` 记录已被翻转的索引被映射到了哪个末尾可用位置。
# flip 时：在 [0, total-1] 范围内随机选取 r，通过 used 查找实际位置 idx；
# 然后将 r 映射到当前末尾（total-1），防止重复选中；total 减 1。
# reset 时：恢复 total 并清空 used。
# 这样每次 flip 只需 O(1) 时间和一次随机数调用。
#
# 时间复杂度: flip O(1), reset O(1)
# 空间复杂度: O(F) — F 为 flip 调用次数（最多 1000）
#
# 关键点:
# - Fisher-Yates 洗牌 + 哈希表映射，避免维护整个矩阵
# - used[r] 记录已被选中的 r 实际对应哪个索引
# - 索引转换：一维索引 idx = row * cols + col → row = idx // cols, col = idx % cols
# - total 在 flip 时递减，保证随机范围逐渐缩小
