"""
LeetCode #526 - Beautiful Arrangement
中文题名：优美的排列
https://leetcode.com/problems/beautiful-arrangement/

Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array
that is constructed by these N numbers successfully if one of the following is true
for the ith position (1 <= i <= N) in this array:

The number at the ith position is divisible by i.

i is divisible by the number at the ith position.

Now given N, how many beautiful arrangements can you construct?

Example 1:

Input: 2
Output: 2
Explanation:

The first beautiful arrangement is [1, 2]:

Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

The second beautiful arrangement is [2, 1]:

Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.

Note:

N is a positive integer and will not exceed 15.

【中文翻译】
假设有从 1 到 N 的 N 个整数。如果对于数组中的第 i 个位置（1 <= i <= N）满足以下
任一条件，则称为"优美的排列"：
- 第 i 个位置的数字能被 i 整除
- i 能被第 i 个位置的数字整除

给定 N，可以构造多少个优美的排列？

示例 1：
    输入：2
    输出：2
    解释：
    第一个优美排列是 [1, 2]：
        第 1 个位置 (i=1) 的数字是 1，1 能被 i (i=1) 整除
        第 2 个位置 (i=2) 的数字是 2，2 能被 i (i=2) 整除
    第二个优美排列是 [2, 1]：
        第 1 个位置 (i=1) 的数字是 2，2 能被 i (i=1) 整除
        第 2 个位置 (i=2) 的数字是 1，i (i=2) 能被 1 整除

说明：N 是一个正整数且不超过 15。
"""

from typing import List, Optional


class Solution:
    def countArrangement(self, n: int) -> int:
        self.count = 0
        visited = [False] * (n + 1)

        def backtrack(pos: int) -> None:
            if pos > n:
                self.count += 1
                return

            for num in range(1, n + 1):
                if not visited[num] and (num % pos == 0 or pos % num == 0):
                    visited[num] = True
                    backtrack(pos + 1)
                    visited[num] = False

        backtrack(1)
        return self.count


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用回溯法（DFS）遍历所有可能的排列。从位置 1 开始，尝试将每个未使用的数字放入当前位置。
# 只有满足"数字能被位置整除"或"位置能被数字整除"的数字才可以选择。当所有位置都填满时
# （pos > n），找到一个有效排列，计数加一。通过 visited 数组记录已使用的数字，回溯时撤销标记。
# 由于 N <= 15，回溯法完全可行。
#
# 时间复杂度: O(k) — 其中 k 为有效排列的数量，最坏情况约为 N!
# 空间复杂度: O(N) — 递归栈深度和 visited 数组
#
# 关键点:
# - 回溯时枚举每个位置（而非枚举数字），天然剪枝减少搜索空间
# - 每个位置只放满足整除条件的数字
# - 可用位运算优化 visited 标记，但 N <= 15 时数组已足够
