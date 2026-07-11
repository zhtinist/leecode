"""
LeetCode #970 - Powerful Integers
中文题名：强整数
https://leetcode.com/problems/powerful-integers/

Given two positive integers `x` and `y`, an integer is
powerful if it is equal to `x^i + y^j` for some integers
`i >= 0` and `j >= 0`.

Return a list of all powerful integers that have value less than or equal to `bound`.

You may return the answer in any order.  In your answer, each value should occur at most
once.

Example 1:

Input: x = 2, y = 3, bound = 10
Output: [2,3,4,5,7,9,10]
Explanation:
2 = 2^0 + 3^0
3 = 2^1 + 3^0
4 = 2^0 + 3^1
5 = 2^1 + 3^1
7 = 2^2 + 3^1
9 = 2^3 + 3^0
10 = 2^0 + 3^2

Example 2:

Input: x = 3, y = 5, bound = 15
Output: [2,4,6,8,10,14]

【中文翻译】
给定两个正整数 `x` 和 `y`，如果一个整数等于 `x^i + y^j`（其中 `i >= 0`，`j >= 0`），
则该整数是强整数。
返回所有值小于或等于 `bound` 的强整数列表。
可以按任意顺序返回答案。答案中每个值最多出现一次。

"""

from typing import List, Optional


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        result = set()

        # 计算 x 的所有幂次（不超过 bound）
        i = 0
        while True:
            val_x = x ** i
            if val_x > bound:
                break

            # 对每个 x^i，计算 y 的所有幂次
            j = 0
            while True:
                val = val_x + y ** j
                if val > bound:
                    break
                result.add(val)
                j += 1
                if y == 1:
                    break

            i += 1
            if x == 1:
                break

        return list(result)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 枚举所有可能的 i 和 j。
# 使用双重循环：外层枚举 x^i（直到超过 bound），内层枚举 y^j（直到 x^i + y^j > bound）。
# 使用集合去重。
# 边界处理：
# - x = 1 时，1^i 始终为 1，外层循环只需执行一次
# - y = 1 时，1^j 始终为 1，内层循环只需执行一次
# 由于 bound 有上限（实际测试中 <= 10^6），幂次 i 和 j 的范围很小（log 级别）。
#
# 时间复杂度: O(log_x(bound) * log_y(bound)) — 幂次数目为对数级别
# 空间复杂度: O(log_x(bound) * log_y(bound)) — 集合存储结果
#
# 关键点:
# - x=1 或 y=1 时需要 break 避免无限循环
# - 使用 set 去重
# - 幂次增长很快，实际枚举量很小
# - 双重循环暴力枚举即可，因为搜索空间是对数级别的
