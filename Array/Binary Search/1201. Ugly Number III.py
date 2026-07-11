"""
LeetCode #1201 - Ugly Number III
中文题名：丑数 III
https://leetcode.com/problems/ugly-number-iii/

Write a program to find the `n`-th ugly number.

Ugly numbers are positive integers which are divisible
by `a` or `b` or
`c`.

Example 1:

Input: n = 3, a = 2, b = 3, c = 5
Output: 4
Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.

Example 2:

Input: n = 4, a = 2, b = 3, c = 4
Output: 6
Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 10, 12... The 4th is 6.

Example 3:

Input: n = 5, a = 2, b = 11, c = 13
Output: 10
Explanation: The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is 10.

Example 4:

Input: n = 1000000000, a = 2, b = 217983653, c = 336916467
Output: 1999999984

Constraints:

`1 <= n, a, b, c <= 10^9`

`1 <= a * b * c <= 10^18`

It's guaranteed that the result will be in range `[1, 2 *
10^9]`

【中文翻译】
编写一个程序找出第 n 个丑数。

丑数是可以被 a 或 b 或 c 整除的正整数。

示例 1：

输入：n = 3, a = 2, b = 3, c = 5
输出：4
解释：丑数序列为 2, 3, 4, 5, 6, 8, 9, 10... 第 3 个是 4。

示例 2：

输入：n = 4, a = 2, b = 3, c = 4
输出：6
解释：丑数序列为 2, 3, 4, 6, 8, 9, 10, 12... 第 4 个是 6。

示例 3：

输入：n = 5, a = 2, b = 11, c = 13
输出：10
解释：丑数序列为 2, 4, 6, 8, 10, 11, 12, 13... 第 5 个是 10。

示例 4：

输入：n = 1000000000, a = 2, b = 217983653, c = 336916467
输出：1999999984

约束条件：

1 <= n, a, b, c <= 10^9
1 <= a * b * c <= 10^18
保证结果在 [1, 2 * 10^9] 范围内

"""

from typing import List, Optional


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        import math

        def lcm(x: int, y: int) -> int:
            return x // math.gcd(x, y) * y

        ab = lcm(a, b)
        ac = lcm(a, c)
        bc = lcm(b, c)
        abc = lcm(ab, c)

        def count(x: int) -> int:
            return (x // a + x // b + x // c
                    - x // ab - x // ac - x // bc
                    + x // abc)

        left, right = 1, 2 * 10 ** 9
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= n:
                right = mid
            else:
                left = mid + 1
        return left










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用二分查找 + 容斥原理（Inclusion-Exclusion Principle）。
#
# 定义函数 count(x) = 在 [1, x] 范围内有多少个丑数（能被 a 或 b 或 c 整除的数）。
# 根据容斥原理：
# count(x) = floor(x/a) + floor(x/b) + floor(x/c)
#           - floor(x/lcm(a,b)) - floor(x/lcm(a,c)) - floor(x/lcm(b,c))
#           + floor(x/lcm(a,b,c))
#
# 然后对答案进行二分查找：
# - 搜索范围 [1, 2*10^9]（题目保证答案在此区间内）
# - 找到最小的 x 使得 count(x) >= n
# - 当 count(mid) >= n 时，收缩右边界；否则收缩左边界
#
# 时间复杂度: O(log(2*10^9)) ≈ O(31) - 二分查找需要约 31 次迭代，每次 count 计算 O(1)
# 空间复杂度: O(1) - 仅使用常数个变量
#
# 关键点:
# - 容斥原理公式：|A ∪ B ∪ C| = |A| + |B| + |C| - |A∩B| - |A∩C| - |B∩C| + |A∩B∩C|
# - 交集的计算：能被 a 和 b 同时整除 = 能被 lcm(a, b) 整除
# - LCM 计算：lcm(x, y) = x / gcd(x, y) * y（先除后乘防止溢出）
# - 二分查找模板：left < right, mid 下取整，根据 count(mid) >= n 来移动边界
