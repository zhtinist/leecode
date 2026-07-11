"""
LeetCode #1734 - Decode XORed Permutation
中文题名：解码异或后的排列
https://leetcode.com/problems/decode-xored-permutation/

There is an integer array `perm` that is a permutation of the first
`n` positive integers, where `n` is always odd.

It was encoded into another integer array `encoded` of length `n -
1`, such that `encoded[i] = perm[i] XOR perm[i + 1]`. For example,
if `perm = [1,3,2]`, then `encoded = [2,1]`.

Given the `encoded` array, return the original array
`perm`. It is guaranteed that the answer exists and is unique.

Example 1:

Input: encoded = [3,1]
Output: [1,2,3]
Explanation: If perm = [1,2,3], then encoded = [1 XOR 2,2 XOR 3] = [3,1]

Example 2:

Input: encoded = [6,5,4,6]
Output: [2,4,1,5,3]

Constraints:

`3 <= n < 105`

`n` is odd.

`encoded.length == n - 1`

【中文翻译】
给定一个整数数组 encoded，它是从长度为 n 的排列 perm（奇数 n）通过以下方式得到的：
encoded[i] = perm[i] XOR perm[i+1]。例如 perm = [1,3,2] → encoded = [1 XOR 3, 3 XOR 2] = [2, 1]。
给定 encoded，返回原始排列 perm。

示例 1：
输入: encoded = [3,1]
输出: [1,2,3]
解释: perm = [1,2,3]（n=3是奇数）。1 XOR 2 = 3，2 XOR 3 = 1。
"""

from typing import List, Optional


class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1

        # 计算 total = 1 ^ 2 ^ 3 ^ ... ^ n
        total = 0
        for i in range(1, n + 1):
            total ^= i

        # 计算 odd_xor = perm[1] ^ perm[2] ^ ... ^ perm[n-1]
        #         = encoded[0] ^ encoded[2] ^ encoded[4] ^ ...
        odd_xor = 0
        for i in range(0, n - 1, 2):
            odd_xor ^= encoded[i]

        # perm[0] = total ^ odd_xor
        perm = [0] * n
        perm[0] = total ^ odd_xor

        for i in range(n - 1):
            perm[i + 1] = perm[i] ^ encoded[i]

        return perm
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 已知 n 为奇数，排列 perm 是 1 到 n 的排列。
# 设 total = 1 ^ 2 ^ ... ^ n（1到n所有数的异或）。
# 设 odd_xor = perm[1] ^ perm[2] ^ ... ^ perm[n-1] = encoded[0] ^ encoded[2] ^ ...（所有奇数索引 encoded）。
# 则 total ^ odd_xor = perm[0]（因为 total 包含 perm[0]，而 odd_xor 包含其他所有元素）。
# 求出 perm[0] 后，利用 encoded 逐个恢复：perm[i+1] = perm[i] ^ encoded[i]。
#
# 时间复杂度: O(N)
# 空间复杂度: O(N)
#
# 关键点:
# - 利用 n 为奇数的特性：total 和 odd_xor 的关系
# - 所有奇数索引的 encoded 异或等于除了 perm[0] 之外所有元素的异或
# - 已知 perm[0] 后可以线性重建整个排列
