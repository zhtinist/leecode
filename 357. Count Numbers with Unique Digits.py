"""
LeetCode #357 - Count Numbers with Unique Digits
中文题名：计算各个位数不同的数字个数
https://leetcode.com/problems/count-numbers-with-unique-digits/

Given a non-negative integer n, count all numbers with unique digits, x, where 0 <=
x < 10^n.

Example:

Input: 2
Output: 91
Explanation: The answer should be the total numbers in the range of 0 <= x < 100,
excluding `11,22,33,44,55,66,77,88,99`

【中文翻译】
给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10^n。

示例：

输入：2
输出：91
解释：答案应为 0 ≤ x < 100 范围内排除 `11,22,33,44,55,66,77,88,99` 后的所有数字个数。
"""

from typing import List, Optional


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1  # 只有数字 0
        if n == 1:
            return 10  # 0-9 共 10 个
        # 初始包含 n=1 的结果
        total = 10
        # 计算 2 位到 n 位的唯一数字个数并累加
        for k in range(2, n + 1):
            # 第一位有 9 种选择（1-9）
            # 后续 k-1 位依次从剩余数字中选择：9 × 8 × 7 × ... × (11-k)
            choices = 9
            available = 9
            for i in range(k - 1):
                choices *= available
                available -= 1
            total += choices
        return total










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用组合数学（排列）计算各位数字唯一的数字个数，避免穷举。
# - n = 0：只有数字 0，共 1 个。
# - n = 1：0-9 共 10 个（0 算作 1 位数，虽然没有前导零，但其本身合法）。
# - n >= 2：对于 k 位数（2 <= k <= n），
#   第一位不能为 0，有 9 种选择（1-9）。
#   第二位可以从 0-9 中选一个与第一位不同的数字，也是 9 种选择。
#   第三位有 8 种选择（排除前两位已用的数字），依此类推。
#   第 k 位有 (11-k) 种选择。
#   所以 k 位数的唯一数字个数 = 9 × 9 × 8 × 7 × ... × (11-k)。
#   将 1 位数到 n 位数的结果累加即可。
#
# 时间复杂度: O(n^2) - 外层循环 n 次，内层循环 k-1 次；或 O(n) 用乘法累积
# 空间复杂度: O(1) - 仅常数变量
#
# 关键点:
# - 核心是排列组合公式，而非暴力枚举
# - 第一位不能为 0，所以有 9 种选择
# - 后续每位从剩余未用的数字中选，形成 9×8×7... 的排列模式
# - n 较大时（n > 10），由鸽巢原理，11 位数以上必重复，但题目约束 n 不会太大
