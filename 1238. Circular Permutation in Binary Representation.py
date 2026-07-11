"""
LeetCode #1238 - Circular Permutation in Binary Representation
中文题名：循环码排列
https://leetcode.com/problems/circular-permutation-in-binary-representation/

Given 2 integers `n` and `start`. Your task is return
any permutation `p` of `(0,1,2.....,2^n -1) `such
that :

`p[0] = start`

`p[i]` and `p[i+1]` differ by only one bit in their binary
representation.

`p[0]` and `p[2^n -1]` must also differ by only one bit in
their binary representation.

Example 1:

Input: n = 2, start = 3
Output: [3,2,0,1]
Explanation: The binary representation of the permutation is (11,10,00,01).
All the adjacent element differ by one bit. Another valid permutation is [3,1,0,2]

Example 2:

Input: n = 3, start = 2
Output: [2,6,7,5,4,0,1,3]
Explanation: The binary representation of the permutation is (010,110,111,101,100,000,001,011).

Constraints:

`1 <= n <= 16`

`0 <= start < 2 ^ n`

【中文翻译】
给你两个整数 `n` 和 `start`。你的任务是返回任意一个排列 `p`，其中 `p` 是 `(0,1,2,...,2^n - 1)` 的一个排列，满足：

- `p[0] = start`
- `p[i]` 和 `p[i+1]` 的二进制表示形式只有一位不同
- `p[0]` 和 `p[2^n - 1]` 的二进制表示形式也只有一位不同

示例 1：

输入：n = 2, start = 3
输出：[3,2,0,1]
解释：该排列的二进制表示是 (11,10,00,01)。所有相邻元素都只有一位不同。另一个有效排列是 [3,1,0,2]。

示例 2：

输入：n = 3, start = 2
输出：[2,6,7,5,4,0,1,3]
解释：该排列的二进制表示是 (010,110,111,101,100,000,001,011)。

约束条件：

`1 <= n <= 16`

`0 <= start < 2 ^ n`
"""

from typing import List, Optional


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        # Generate Gray code sequence of length 2^n
        gray = [i ^ (i >> 1) for i in range(1 << n)]

        # Find the index of `start` in the Gray code sequence
        idx = gray.index(start)

        # Rotate to start from `start`
        return gray[idx:] + gray[:idx]










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 格雷码（Gray Code）。题目要求相邻数字二进制只有一位不同，且首尾循环也只有一位不同，
# 这正是格雷码的定义。n 位格雷码序列恰好包含 2^n 个数字（0 到 2^n - 1），且满足相邻只有一位不同的特性。
# 1. 生成 n 位格雷码序列：gray[i] = i ^ (i >> 1)，其中 i 从 0 到 2^n - 1。
# 2. 找到 `start` 在格雷码序列中的位置 idx。
# 3. 将序列从 idx 处"旋转"，即 gray[idx:] + gray[:idx]，使得序列以 `start` 开头。
# 格雷码的首尾也只有一位不同（0 和 2^n - 1 的格雷码），所以循环排列后首尾条件仍然满足。
#
# 时间复杂度: O(2^n)，需要生成完整的格雷码序列
# 空间复杂度: O(2^n)，存储完整的格雷码序列
#
# 关键点:
# - 格雷码公式：G(i) = i ^ (i >> 1)
# - n 位格雷码天然满足相邻一位不同且首尾一位不同
# - 只需生成标准格雷码序列后旋转到以 `start` 开头即可
# - 也可以直接用 `start ^ (i ^ (i >> 1))` 的技巧从 start 开始生成
