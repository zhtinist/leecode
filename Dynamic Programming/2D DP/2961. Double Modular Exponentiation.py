"""
LeetCode #2961 - Double Modular Exponentiation
双模幂运算
https://leetcode.cn/problems/double-modular-exponentiation/

给你一个下标从 0 开始的二维数组 `variables` ，其中 `variables[i] = [a_i, b_i, c_i, m_i]`，以及一个整数 `target` 。
如果满足以下公式，则下标 `i` 是 好下标：
`0 <= i < variables.length`
`((a_i^b_i % 10)^c_i) % m_i == target`
返回一个由 好下标 组成的数组，顺序不限 。

示例 1：
输入：variables = [[2,3,3,10],[3,3,3,1],[6,1,1,4]], target = 2 输出：[0,2] 解释：对于 variables 数组中的每个下标 i ： 1) 对于下标 0 ，variables[0] = [2,3,3,10] ，(2^3 % 10)^3 % 10 = 2 。 2) 对于下标 1 ，variables[1] = [3,3,3,1] ，(3^3 % 10)^3 % 1 = 0 。 3) 对于下标 2 ，variables[2] = [6,1,1,4] ，(6^1 % 10)^1 % 4 = 2 。 因此，返回 [0,2] 作为答案。
示例 2：
输入：variables = [[39,3,1000,1000]], target = 17 输出：[] 解释：对于 variables 数组中的每个下标 i ： 1) 对于下标 0 ，variables[0] = [39,3,1000,1000] ，(39^3 % 10)^1000 % 1000 = 1 。 因此，返回 [] 作为答案。

提示：
`1 <= variables.length <= 100`
`variables[i] == [a_i, b_i, c_i, m_i]`
`1 <= a_i, b_i, c_i, m_i <= 10^3`
`0 <= target <= 10^3`
"""

from typing import List, Optional


class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        """
        Use fast modular exponentiation (pow with mod) to compute
        ((a^b % 10)^c) % m efficiently, then collect indices matching target.
        """
        result = []
        for i, (a, b, c, m) in enumerate(variables):
            # First: a^b % 10 using built-in pow with modular exponentiation
            first = pow(a, b, 10)
            # Second: (first)^c % m
            second = pow(first, c, m)
            if second == target:
                result.append(i)
        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Math, Simulation
#
# 解题思路:
# 使用 Python 内置的 pow(base, exp, mod) 函数进行快速模幂运算。
# 先计算 a^b % 10，再计算结果的 c 次方对 m 取模，判断是否等于 target，收集符合条件的下标。
#
# 时间复杂度: O(n)，其中 n 为 variables 长度，每次 pow 计算为 O(log b + log c)
# 空间复杂度: O(1)，除返回结果外仅使用常数空间
#
# 关键点:
# - 使用 pow(a, b, mod) 内置函数进行快速模幂运算，避免大数溢出
# - 题目中第一步模 10 是固定的，第二步模 mi 是变量
# - 由于数据范围小(<=1000)，暴力乘法也可以通过
