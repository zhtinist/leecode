"""
LeetCode #397 - Integer Replacement
中文题名：整数替换
https://leetcode.com/problems/integer-replacement/

Given a positive integer n and you can do operations as follow:

If n is even, replace n with `n/2`.

If n is odd, you can replace n with either `n + 1` or
`n - 1`.

What is the minimum number of replacements needed for n to become 1?

Example 1:

Input:
8

Output:
3

Explanation:
8 -> 4 -> 2 -> 1

Example 2:

Input:
7

Output:
4

Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1

【中文翻译】
给定一个正整数 n，你可以做如下操作：

如果 n 是偶数，将 n 替换为 n/2。

如果 n 是奇数，你可以将 n 替换为 n + 1 或 n - 1。

问最少需要多少次替换才能使 n 变为 1 ？

示例 1：

输入：
8

输出：
3

解释：
8 -> 4 -> 2 -> 1

示例 2：

输入：
7

输出：
4

解释：
7 -> 8 -> 4 -> 2 -> 1
或
7 -> 6 -> 3 -> 2 -> 1
"""

from typing import List, Optional


class Solution:
    def integerReplacement(self, n: int) -> int:
        steps = 0
        while n > 1:
            if n % 2 == 0:
                n //= 2
            elif n == 3 or n % 4 == 1:
                n -= 1
            else:
                n += 1
            steps += 1
        return steps











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用贪心 + 位运算。核心策略：
# - 偶数直接除以 2（1 步，最优）
# - 奇数时需要选择 +1 或 -1：
#   - 特例 n = 3：应该 -1 → 2 → 1（2 步），如果 +1 则 3→4→2→1（3 步）
#   - n % 4 == 1：n 的二进制以 "01" 结尾，-1 后变为 ...00（偶数），可以连续除 2
#   - n % 4 == 3（且 n != 3）：n 的二进制以 "11" 结尾，+1 后变为 ...00，可以连续除 2
# 策略的本质是让数字尽可能快地变为 4 的倍数，从而能连续做多次除以 2。
#
# 时间复杂度: O(log n) - 每次操作至少减少一位（偶数除 2，奇数操作后变偶数再除 2）
# 空间复杂度: O(1) - 仅使用常数额外空间
#
# 关键点:
# - 贪心规则：尽可能让数字变成 4 的倍数以加速后续操作
# - n = 3 是唯一例外，需要特殊处理（-1 比 +1 更优）
# - 判断 n % 4 等价于看低两位二进制：01 → -1，11 → +1（除 3 外）
# - BFS/递归+记忆化 也可解，但贪心 O(log n) 更优
