"""
LeetCode #1405 - Longest Happy String
中文题名：最长快乐字符串
https://leetcode.com/problems/longest-happy-string/

A string is called happy if it does not have any of the strings `'aaa'`,
`'bbb'` or `'ccc'` as a substring.

Given three integers `a`, `b` and `c`, return
any string `s`, which satisfies following
conditions:

`s` is happy and longest possible.

`s` contains at most `a` occurrences
of the letter `'a'`, at most `b` occurrences
of the letter `'b'` and at most `c`
occurrences of the letter `'c'`.

`s `will only contain `'a'`, `'b'` and
`'c'` letters.

If there is no such string `s` return the empty string
`""`.

Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.

Example 2:

Input: a = 2, b = 2, c = 1
Output: "aabbc"

Example 3:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It's the only correct answer in this case.

Constraints:

`0 <= a, b, c <= 100`

`a + b + c > 0`

【中文翻译】

如果一个字符串不包含子串 'aaa'、'bbb' 或 'ccc'，则称其为"快乐"字符串。

给定三个整数 a、b 和 c，返回满足以下条件的任意字符串 s：

s 是快乐字符串且尽可能长。
s 最多包含 a 个 'a'、b 个 'b' 和 c 个 'c'。
s 只包含字母 'a'、'b' 和 'c'。

如果不存在这样的字符串 s，返回空字符串 ""。

示例 1：
输入：a = 1, b = 1, c = 7
输出："ccaccbcc"
解释："ccbccacc" 也是正确答案。

示例 2：
输入：a = 2, b = 2, c = 1
输出："aabbc"

示例 3：
输入：a = 7, b = 1, c = 0
输出："aabaa"
解释：这是这种情况下的唯一正确答案。

约束条件：
0 <= a, b, c <= 100
a + b + c > 0
"""

from typing import List, Optional
import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # 最大堆（Python 只有最小堆，用负数模拟）
        heap = []
        if a > 0:
            heap.append((-a, 'a'))
        if b > 0:
            heap.append((-b, 'b'))
        if c > 0:
            heap.append((-c, 'c'))
        heapq.heapify(heap)

        result = []

        while heap:
            count1, char1 = heapq.heappop(heap)
            count1 = -count1

            # 如果结果末尾已经有两个相同的字符，不能再加这个字符
            if len(result) >= 2 and result[-1] == result[-2] == char1:
                if not heap:
                    break
                # 取第二多的字符
                count2, char2 = heapq.heappop(heap)
                count2 = -count2
                result.append(char2)
                count2 -= 1
                if count2 > 0:
                    heapq.heappush(heap, (-count2, char2))
                heapq.heappush(heap, (-count1, char1))
            else:
                # 正常添加最多的字符（添加 1 个，如果数量多可以加 2 个）
                add_count = min(count1, 2)
                result.append(char1 * add_count)
                count1 -= add_count
                if count1 > 0:
                    heapq.heappush(heap, (-count1, char1))

        return ''.join(result)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心策略：每次选择剩余数量最多且不会导致三个连续相同字符的字母。
# 使用最大堆来高效获取当前数量最多的字母。
# 算法：
# 1. 将所有 (count, char) 放入最大堆。
# 2. 弹出数量最多的字符：
#    a. 如果结果末尾已有该字符的两个连续，则取第二多的字符（放一个）。
#    b. 否则正常添加当前最多的字符（最多两个）。
# 3. 将剩余数量大于 0 的字符放回堆中继续。
#
# 时间复杂度: O(a + b + c)  每个字符被处理一次
# 空间复杂度: O(1)  堆中最多 3 个元素
#
# 关键点:
# - 贪心：优先使用剩余数量最多的字母
# - 避免三个连续相同字符的关键是检查末尾两个
# - 当最多字母被阻止时，必须取第二多的字母
# - 每次添加 1 个比添加 2 个更安全（保守策略），但添加 2 个也是安全的且可能更优










