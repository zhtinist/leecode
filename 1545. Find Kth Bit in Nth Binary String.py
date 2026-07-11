"""
LeetCode #1545 - Find Kth Bit in Nth Binary String
中文题名：找出第 N 个二进制字符串中的第 K 位
https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/


Given two positive integers `n` and `k`, the
binary string  `Sn` is formed as follows:

`S1 = "0"`

`Si = Si-1 + "1" + reverse(invert(Si-1))` for `i
> 1`

Where `+` denotes the concatenation operation, `reverse(x)` returns
the reversed string x, and `invert(x)` inverts
all the bits in x (0 changes to 1 and 1 changes to 0).

For example, the first 4 strings in the above sequence are:

`S1 = "0"`

`S2 = "011"`

`S3 = "0111001"`

`S4 = "011100110110001"`

Return the `kth` bit in `Sn`.
It is guaranteed that `k` is valid for the
given `n`.

Example 1:

Input: n = 3, k = 1
Output: "0"
Explanation: S3 is "0111001". The first bit is "0".

Example 2:

Input: n = 4, k = 11
Output: "1"
Explanation: S4 is "011100110110001". The 11th bit is "1".

Example 3:

Input: n = 1, k = 1
Output: "0"

Example 4:

Input: n = 2, k = 3
Output: "1"

Constraints:

`1 <= n <= 20`

`1 <= k <= 2n - 1`

【中文翻译】
给定两个正整数 n 和 k，二进制字符串 Sn 按以下方式构造：
S1 = "0"
Si = Si-1 + "1" + reverse(invert(Si-1))，其中 + 表示拼接，reverse 表示反转，invert 表示按位取反。
返回 Sn 的第 k 位字符。

示例 1：
输入：n = 3, k = 1
输出："0"
解释：S3 = "0111001"，第 1 位是 "0"。

示例 2：
输入：n = 4, k = 11
输出："1"
解释：S4 = "011100110110001"，第 11 位是 "1"。

示例 3：
输入：n = 1, k = 1
输出："0"

示例 4：
输入：n = 2, k = 3
输出："1"
"""

from typing import List, Optional


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'
        length = (1 << n) - 1  # 2^n - 1
        mid = length // 2 + 1
        if k == mid:
            return '1'
        elif k < mid:
            return self.findKthBit(n - 1, k)
        else:
            # k > mid: mirrored position in right half
            mirrored_k = length - k + 1
            bit = self.findKthBit(n - 1, mirrored_k)
            return '0' if bit == '1' else '1'



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 利用递归和字符串的构造规律。Sn 的长度为 2^n - 1，中间位置（第 mid 位）始终是 '1'。
# 如果 k == mid，返回 '1'。如果 k < mid，在左半部分递归（即 Sn-1）。
# 如果 k > mid，映射到右半部分的对称位置 mirrored_k = length - k + 1，
# 递归得到结果后取反（0 变 1，1 变 0）。
#
# 时间复杂度: O(N) — 每次递归 n 减 1
# 空间复杂度: O(N) — 递归栈深度
#
# 关键点:
# - 利用对称性和取反性质递归求解
# - 中间位置始终是 '1'
# - 右半部分 = 左半部分的逆序取反












