"""
LeetCode #3556 - Sum of Largest Prime Substrings
最大质数子字符串之和
https://leetcode.cn/problems/sum-of-largest-prime-substrings/

给定一个字符串 `s`，找出可以由其 子字符串 组成的 3个最大的不同质数 的和。
返回这些质数的 总和 ，如果少于 3 个不同的质数，则返回 所有 不同质数的和。
质数是大于 1 且只有两个因数的自然数：1和它本身。
子字符串 是字符串中的一个连续字符序列。
注意：每个质数即使出现在 多个 子字符串中，也只能计算 一次 。此外，将子字符串转换为整数时，忽略任何前导零。

示例 1：

输入： s = "12234"
输出： 1469
解释：
由 `"12234"` 的子字符串形成的不同质数为 2 ，3 ，23 ，223 和 1223。
最大的 3 个质数是 1223、223 和 23。它们的和是 1469。
示例 2：

输入： s = "111"
输出： 11
解释：
由 `"111"` 的子字符串形成的不同质数是 11。
由于只有一个质数，所以结果是 11。

提示：
`1 <= s.length <= 10`
`s` 仅由数字组成。
"""

from typing import List, Optional


class Solution:
    def sumOfLargestPrimeSubstrings(self, s: str) -> int:
        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            if x < 4:
                return True
            if x % 2 == 0 or x % 3 == 0:
                return False
            i = 5
            while i * i <= x:
                if x % i == 0 or x % (i + 2) == 0:
                    return False
                i += 6
            return True

        primes = set()
        n = len(s)

        for i in range(n):
            if s[i] == '0':
                continue  # skip leading zero, treat as 0 (not prime)
            num = 0
            for j in range(i, n):
                num = num * 10 + int(s[j])
                if is_prime(num):
                    primes.add(num)

        sorted_primes = sorted(primes, reverse=True)
        return sum(sorted_primes[:3])










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Hash Table, Math, String, Number Theory, Sorting
#
# 解题思路:
# 由于 s 长度最多为 10，子字符串总数不超过 55 个，可以暴力枚举所有子字符串。
# 枚举每个起始位置 i 和结束位置 j，通过数值累加（num = num * 10 + digit）构造整数。
# 注意跳过前导零（以 '0' 开头的子字符串值为 0，不是质数）。
# 对每个子字符串对应的整数判断是否为质数，是则加入集合以去重。
# 最后将集合中的质数降序排序，取前 3 个（不足则全取）求和。
#
# 时间复杂度: O(n^2 * sqrt(M))，其中 n 为字符串长度（<=10），M 为子字符串数值上限（<=10^10）。
#   实际规模很小，完全可以暴力。
# 空间复杂度: O(n^2)，用于存储所有不同质数（最坏情况每个子字符串都是质数）。
#
# 关键点:
# - 字符串长度极小（<=10），暴力枚举完全可行。
# - 使用集合去重，确保每个质数只计算一次。
# - 质数判断使用 6k±1 优化（检查 2,3 后每次跳 6）。
