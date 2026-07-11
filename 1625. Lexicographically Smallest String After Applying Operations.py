"""
LeetCode #1625 - Lexicographically Smallest String After Applying Operations
中文题名：执行操作后字典序最小的字符串
https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/

You are given a string `s` of even length consisting of
digits from `0` to `9`, and two integers `a` and `b`.

You can apply either of the following two operations any number of times and in any
order on `s`:

Add `a` to all odd indices of `s`
(0-indexed). Digits post `9` are cycled back to
`0`. For example, if `s = "3456"` and `a = 5`,
`s` becomes `"3951"`.

Rotate `s` to the right by `b` positions. For example, if
`s = "3456"` and `b = 1`, `s` becomes `"6345"`.

Return the lexicographically smallest string you can obtain by
applying the above operations any number of times on `s`.

A string `a` is lexicographically smaller than a string `b` (of
the same length) if in the first position where `a` and `b`
differ, string `a` has a letter that appears earlier in the alphabet than
the corresponding letter in `b`. For example, `"0158"` is
lexicographically smaller than `"0190"` because the first position they
differ is at the third letter, and `'5'` comes before `'9'`.

Example 1:

Input: s = "5525", a = 9, b = 2
Output: "2050"
Explanation: We can apply the following operations:
Start:  "5525"
Rotate: "2555"
Add:    "2454"
Add:    "2353"
Rotate: "5323"
Add:    "5222"
​​​​​​​Add:    "5121"
​​​​​​​Rotate: "2151"
​​​​​​​Add:    "2050"​​​​​​​​​​​​
There is no way to obtain a string that is lexicographically smaller then "2050".

Example 2:

Input: s = "74", a = 5, b = 1
Output: "24"
Explanation: We can apply the following operations:
Start:  "74"
Rotate: "47"
​​​​​​​Add:    "42"
​​​​​​​Rotate: "24"​​​​​​​​​​​​
There is no way to obtain a string that is lexicographically smaller then "24".

Example 3:

Input: s = "0011", a = 4, b = 2
Output: "0011"
Explanation: There are no sequence of operations that will give us a lexicographically smaller string than "0011".

Example 4:

Input: s = "43987654", a = 7, b = 3
Output: "00553311"

Constraints:

`2 <= s.length <= 100`

`s.length` is even.

`s` consists of digits from `0` to `9` only.

`1 <= a <= 9`

`1 <= b <= s.length - 1`

【中文翻译】
给定一个长度为偶数的字符串 s，可以执行两种操作任意次：
- 累加操作：将 s 中所有奇数索引（下标从0开始）的字符加上 a（循环：'0'-'9'），若超过 '9' 则回到 '0'
- 轮转操作：将 s 向右轮转 b 位
返回可以得到的字典序最小的字符串。

示例 1：
输入: s = "5525", a = 9, b = 2
输出: "2050"
解释: 轮转2位→"2555"，累加(所有奇数位+a=9)→"2454"（'5'+9='4'循环），再累加→"2050"（'4'+9='3'...不是）。经过一系列操作得到"2050"。
"""

from typing import List, Optional
from collections import deque


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        seen = set()
        queue = deque([s])
        seen.add(s)
        ans = s

        while queue:
            cur = queue.popleft()
            if cur < ans:
                ans = cur

            # 轮转操作：向右轮转 b 位
            rotated = cur[n - b:] + cur[:n - b]
            if rotated not in seen:
                seen.add(rotated)
                queue.append(rotated)

            # 累加操作：奇数索引位置加 a
            chars = list(cur)
            for i in range(1, n, 2):
                chars[i] = str((int(chars[i]) + a) % 10)
            added = ''.join(chars)
            if added not in seen:
                seen.add(added)
                queue.append(added)

        return ans
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# BFS 搜索所有可能的状态。从初始字符串开始，每次尝试两种操作（轮转和累加），
# 将新状态加入队列。用集合记录访问过的状态避免重复。
# 在所有访问过的状态中取字典序最小的。
#
# 时间复杂度: O(N * D) — N 为字符串长度，D 为不同状态数（每种轮转位置 × 每种累加组合）
# 空间复杂度: O(N * D) — 存储访问集合
#
# 关键点:
# - 轮转只改变偶数位的位置，累加只改变奇数位的值 → 两个操作影响不同部分
# - BFS 保证能找到所有可达状态
# - 注意轮转 b 位：s[n-b:] + s[:n-b]
