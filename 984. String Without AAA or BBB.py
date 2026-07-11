"""
LeetCode #984 - String Without AAA or BBB
中文题名：不含 AAA 或 BBB 的字符串
https://leetcode.com/problems/string-without-aaa-or-bbb/

给定两个整数 A 和 B，返回任意一个字符串 S，要求满足：

S 的长度为 A + B，且正好包含 A 个 'a' 字母与 B 个 'b' 字母；
子串 'aaa' 不会出现在 S 中；
子串 'bbb' 不会出现在 S 中。

示例 1：

输入：A = 1, B = 2
输出："abb"
解释："abb"、"bab" 和 "bba" 都是正确的答案。

示例 2：

输入：A = 4, B = 1
输出："aabaa"

【中文翻译】
给定整数 A 和 B，构造一个由 A 个 'a' 和 B 个 'b' 组成的字符串，要求不能出现三个连续相同的字符（即 "aaa" 和 "bbb" 不能出现）。返回任意一个合法结果。

"""

from typing import List, Optional


class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        result = []
        while a > 0 or b > 0:
            if a > b:
                if len(result) >= 2 and result[-1] == 'a' and result[-2] == 'a':
                    result.append('b')
                    b -= 1
                else:
                    result.append('a')
                    a -= 1
            elif b > a:
                if len(result) >= 2 and result[-1] == 'b' and result[-2] == 'b':
                    result.append('a')
                    a -= 1
                else:
                    result.append('b')
                    b -= 1
            else:
                # a == b, alternate
                if result and result[-1] == 'a':
                    result.append('b')
                    b -= 1
                else:
                    result.append('a')
                    a -= 1
        return ''.join(result)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心法：
# 1. 核心思想：每次尝试放置剩余数量更多的字母。
# 2. 维护两个计数 a 和 b（剩余可用的字母数）和一个结果列表。
# 3. 每次循环判断：
#    - 如果 a > b：优先放 'a'。但如果前两个字符已经都是 'a'（即将产生 "aaa"），则必须放 'b'。
#    - 如果 b > a：优先放 'b'。但如果前两个字符已经都是 'b'（即将产生 "bbb"），则必须放 'a'。
#    - 如果 a == b：交替放置，与上一个字符不同即可。
# 4. 这个贪心策略总是可行的，因为只要满足 max(a, b) <= 2 * min(a, b) + 2 即可构造。
#    题目输入保证始终有解。
#
# 时间复杂度: O(A + B)，每次循环放置一个字符，共 A + B 次迭代
# 空间复杂度: O(A + B) 或 O(1)，不计算输出字符串的大小则为 O(1)
#
# 关键点:
# - 贪心策略：总是优先使用剩余数量多的字母
# - 检查前两个字符避免出现三个连续相同字符
# - 当两个字母数量相等时，交替放置
# - 题目保证输入一定有解（max(A, B) <= 2 * min(A, B) + 2）
