"""
LeetCode #779 - K-th Symbol in Grammar
中文题名：第K个语法符号
https://leetcode.com/problems/k-th-symbol-in-grammar/

On the first row, we write a `0`. Now in every subsequent row, we look at the
previous row and replace each occurrence of `0` with `01`, and each
occurrence of `1` with `10`.

Given row `N` and index `K`, return the `K`-th indexed
symbol in row `N`. (The values of `K` are 1-indexed.) (1 indexed).

Examples:
Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001

Note:

`N` will be an integer in the range `[1, 30]`.

`K` will be an integer in the range `[1, 2^(N-1)]`.

【中文翻译】
在第一行我们写上一个 `0`。接下来的每一行，将上一行中的 `0` 替换为 `01`，将 `1` 替换为 `10`。

给定行号 `N` 和索引 `K`，返回第 `N` 行中第 `K` 个字符。（`K` 的值从 1 开始索引。）

示例：
输入：N = 1, K = 1
输出：0

输入：N = 2, K = 1
输出：0

输入：N = 2, K = 2
输出：1

输入：N = 4, K = 5
输出：1

解释：
第 1 行：0
第 2 行：01
第 3 行：0110
第 4 行：01101001

注意：

`N` 是范围在 `[1, 30]` 内的整数。

`K` 是范围在 `[1, 2^(N-1)]` 内的整数。
"""

from typing import List, Optional


class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        # The K-th symbol is determined by the parity of 1-bits in (K-1)
        # row N is just the sequence where bit i = popcount(i) % 2
        return bin(K - 1).count('1') % 2



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 位运算 / 递归。
# 观察规律：
# 第 N 行就是 Thue-Morse 序列：t[i] = popcount(i) % 2，其中 i 从 0 开始。
# 因此第 K 个元素（1-indexed）等于 (K-1) 的二进制表示中 1 的个数的奇偶性。
# 也可以使用递归：
# - 如果 K 是奇数，结果与上一行的 (K+1)//2 位置相同
# - 如果 K 是偶数，结果与上一行的 K//2 位置相反
# 递归基：N=1 时返回 0。
# 位运算法更简洁：直接统计 (K-1) 二进制中 1 的个数。
#
# 时间复杂度: O(log K) - bin(K-1).count('1') 或递归深度
# 空间复杂度: O(1)
#
# 关键点:
# - 本质是 Thue-Morse 序列
# - K-1 的二进制中 1 的个数取模 2
# - 也可以递归：根据 K 的奇偶性决定是否翻转父节点的值
# - N 只是层数，不影响结果（只影响范围）
