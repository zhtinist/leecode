"""
LeetCode #1447 - Simplified Fractions
中文题名：最简分数
https://leetcode.com/problems/simplified-fractions/

Given an integer `n`, return a list of all simplified
fractions between 0 and 1 (exclusive) such that the denominator is less-than-or-equal-to
`n`. The fractions can be in any order.

Example 1:

Input: n = 2
Output: ["1/2"]
Explanation: "1/2" is the only unique fraction with a denominator less-than-or-equal-to 2.

Example 2:

Input: n = 3
Output: ["1/2","1/3","2/3"]

Example 3:

Input: n = 4
Output: ["1/2","1/3","1/4","2/3","3/4"]
Explanation: "2/4" is not a simplified fraction because it can be simplified to "1/2".

Example 4:

Input: n = 1
Output: []

Constraints:

`1 <= n <= 100`

【中文翻译】
给定一个整数 `n`，返回所有介于 0 和 1 之间（不包括 0 和 1）且分母小于或等于 `n` 的最简分数的列表。
分数可以按任意顺序排列。

示例 1：

输入：n = 2
输出：["1/2"]
解释："1/2" 是唯一分母小于或等于 2 的最简分数。

示例 2：

输入：n = 3
输出：["1/2","1/3","2/3"]

示例 3：

输入：n = 4
输出：["1/2","1/3","1/4","2/3","3/4"]
解释："2/4" 不是最简分数，因为它可以化简为 "1/2"。

示例 4：

输入：n = 1
输出：[]

约束条件：

`1 <= n <= 100`
"""

from typing import List, Optional


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        import math
        ans = []
        for denom in range(2, n + 1):
            for numer in range(1, denom):
                if math.gcd(numer, denom) == 1:
                    ans.append(f"{numer}/{denom}")
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 遍历分母 denom 从 2 到 n：
# 对于每个分母，遍历分子 numer 从 1 到 denom-1。
# 使用 math.gcd 判断 numer 和 denom 的最大公约数是否为 1。
# 如果互质（gcd == 1），则该分数是最简分数，添加到结果列表中。
#
# 时间复杂度: O(N^2 log N)  -- 外层 O(N^2) 对分子分母，gcd 操作为 O(log N)
# 空间复杂度: O(1)  -- 不计结果列表，仅用常数额外空间
#
# 关键点:
# - 最简分数的充要条件是分子分母互质（gcd == 1）
# - 分母从 2 开始，n=1 时返回空列表
# - 分数格式为 f"{numer}/{denom}"









