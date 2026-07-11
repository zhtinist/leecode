"""
LeetCode #372 - Super Pow
中文题名：超级次方
https://leetcode.com/problems/super-pow/

Your task is to calculate ab mod 1337 where a is a positive
integer and b is an extremely large positive integer given in the form of an array.

Example 1:

Input: a = 2, b = [3]
Output: 8

Example 2:

Input: a = 2, b = [1,0]
Output: 1024

【中文翻译】
你的任务是计算 a^b mod 1337，其中 a 是一个正整数，b 是一个极其大的正整数，以数组的形式给出。

示例 1：

输入：a = 2, b = [3]
输出：8

示例 2：

输入：a = 2, b = [1,0]
输出：1024
"""

from typing import List, Optional


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        result = 1
        a = a % MOD
        for digit in b:
            result = (pow(result, 10, MOD) * pow(a, digit, MOD)) % MOD
        return result











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 本题要求计算 a^b mod 1337，其中 b 以数组形式给出（可能非常大，无法直接转换为整数）。
# 利用模运算的两个核心性质：
# 1. (x * y) % MOD = ((x % MOD) * (y % MOD)) % MOD
# 2. a^[d1, d2, ..., dn] 可以递推处理，每读取一位新数字，相当于将之前的指数扩大 10 倍再加上新数字
#    即 a^(10 * prev_exp + digit) = (a^prev_exp)^10 * a^digit
# 从左到右遍历数组 b 的每一位数字 digit：
# - 先将当前结果取 10 次方（因为每前进一位，之前的指数要乘以 10）
# - 再乘以 a^digit（加上当前位的贡献）
# - 所有操作均在模 1337 下进行
# 使用 Python 内置的 pow(base, exp, mod) 进行高效模幂运算，避免手动实现快速幂。
#
# 时间复杂度: O(N) - N 是数组 b 的长度，每次迭代调用两次 pow（均摊 O(log mod)，可视为 O(1)）
# 空间复杂度: O(1) - 只使用常数额外空间
#
# 关键点:
# - 指数按位递推公式：result = (result^10 * a^digit) mod MOD
# - pow(base, exp, mod) 是 Python 内置的高效模幂函数，底层使用快速幂算法
# - 提前对 a 取模（a = a % MOD），避免后续大数运算
# - 也可以从右到左递归：a^[d1...dn] = a^dn * (a^[d1...d(n-1)])^10，本质相同
