"""
LeetCode #866 - Prime Palindrome
中文题名：回文素数
https://leetcode.com/problems/prime-palindrome/

Find the smallest prime palindrome greater than or equal to `N`.

Recall that a number is prime if it's only divisors are 1 and itself, and
it is greater than 1.

For example, 2,3,5,7,11 and 13 are primes.

Recall that a number is a palindrome if it reads the same from left to right as it
does from right to left.

For example, 12321 is a palindrome.

Example 1:

Input: 6
Output: 7

Example 2:

Input: 8
Output: 11

Example 3:

Input: 13
Output: 101

【中文翻译】
找到大于或等于 N 的最小回文素数。

回想一下，如果一个数只有 1 和自身两个约数，并且大于 1，则它是素数。例如，2, 3, 5, 7, 11 和 13 都是素数。

回想一下，如果一个数从左到右读和从右到左读一样，则它是回文数。例如，12321 是一个回文数。

"""

from typing import List, Optional


class Solution:
    def primePalindrome(self, n: int) -> int:
        # Helper: check if a number is prime
        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            if x == 2:
                return True
            if x % 2 == 0:
                return False
            i = 3
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 2
            return True

        # Helper: generate the next palindrome >= n
        # All even-length palindromes > 11 are divisible by 11, so skip them
        def next_palindrome(x: int) -> int:
            s = str(x)
            length = len(s)

            # Check candidates of current length and increasing lengths
            for L in range(length, 10):  # up to 10-digit numbers
                # Only check odd-length palindromes (except handle 11 specially)
                if L % 2 == 0 and L > 2:
                    continue

                half_len = (L + 1) // 2
                start = int(s[:half_len]) if L == length else 10 ** (half_len - 1)

                for half in range(start, 10 ** half_len):
                    prefix = str(half)
                    if L % 2 == 1:
                        # Odd length: e.g., "123" -> "12321"
                        pal = int(prefix + prefix[-2::-1])
                    else:
                        # Even length: e.g., "12" -> "1221"
                        pal = int(prefix + prefix[::-1])

                    if pal >= n:
                        return pal

        # Special case: handle n <= 11
        if n <= 2:
            return 2
        if n <= 3:
            return 3
        if n <= 5:
            return 5
        if n <= 7:
            return 7
        if n <= 11:
            return 11

        # Generate palindromes and check primality
        pal = next_palindrome(n)
        while True:
            if is_prime(pal):
                return pal
            pal = next_palindrome(pal + 1)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 关键数学事实：所有偶数长度的回文数（除了 11）都能被 11 整除，所以不可能是素数。
# 因此我们只需要检查奇数长度的回文数（以及手动处理 11）。
#
# 算法步骤：
# 1. 手动处理 n <= 11 的特殊情况（直接返回对应的最小素数回文）。
# 2. 生成大于等于 n 的下一个回文数（只生成奇数长度的，跳过偶数长度 > 2 的）。
# 3. 使用试除法检查回文数是否为素数。
# 4. 如果不是素数，继续生成下一个回文数。
#
# 生成回文数的方法：取前半部分作为前缀，然后镜像拼接。
# 例如：前缀 "123" -> "12321"，前缀 "12" -> "1221"。
# 从 n 的长度开始尝试，逐步增加长度（实际最多到 10 位数足够，因为题目范围合理）。
#
# 时间复杂度: 每次检验素数 O(sqrt(N))，需要检验的回文数数量有限（素数密度约为 1/log(N)）
# 空间复杂度: O(1)
#
# 关键点:
# - 偶数长度的回文数（除 11 外）都能被 11 整除，永远不可能是素数
# - 只需要检查奇数长度的回文数
# - 生成回文数：取前半部分镜像拼接，无需遍历所有数字
# - 素数检验用试除法 O(sqrt(N)) 即可，因为回文数密度低且 N 范围有限
