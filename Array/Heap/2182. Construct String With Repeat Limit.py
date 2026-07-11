"""
LeetCode #2182 - Construct String With Repeat Limit
构造限制重复的字符串
https://leetcode.cn/problems/construct-string-with-repeat-limit/

给你一个字符串 `s` 和一个整数 `repeatLimit` ，用 `s` 中的字符构造一个新字符串 `repeatLimitedString` ，使任何字母 连续 出现的次数都不超过 `repeatLimit` 次。你不必使用 `s` 中的全部字符。
返回 字典序最大的 `repeatLimitedString` 。
如果在字符串 `a` 和 `b` 不同的第一个位置，字符串 `a` 中的字母在字母表中出现时间比字符串 `b` 对应的字母晚，则认为字符串 `a` 比字符串 `b` 字典序更大 。如果字符串中前 `min(a.length, b.length)` 个字符都相同，那么较长的字符串字典序更大。

示例 1：
输入：s = "cczazcc", repeatLimit = 3 输出："zzcccac" 解释：使用 s 中的所有字符来构造 repeatLimitedString "zzcccac"。 字母 'a' 连续出现至多 1 次。 字母 'c' 连续出现至多 3 次。 字母 'z' 连续出现至多 2 次。 因此，没有字母连续出现超过 repeatLimit 次，字符串是一个有效的 repeatLimitedString 。 该字符串是字典序最大的 repeatLimitedString ，所以返回 "zzcccac" 。 注意，尽管 "zzcccca" 字典序更大，但字母 'c' 连续出现超过 3 次，所以它不是一个有效的 repeatLimitedString 。
示例 2：
输入：s = "aababab", repeatLimit = 2 输出："bbabaa" 解释： 使用 s 中的一些字符来构造 repeatLimitedString "bbabaa"。  字母 'a' 连续出现至多 2 次。  字母 'b' 连续出现至多 2 次。  因此，没有字母连续出现超过 repeatLimit 次，字符串是一个有效的 repeatLimitedString 。  该字符串是字典序最大的 repeatLimitedString ，所以返回 "bbabaa" 。  注意，尽管 "bbabaaa" 字典序更大，但字母 'a' 连续出现超过 2 次，所以它不是一个有效的 repeatLimitedString 。

提示：
`1 <= repeatLimit <= s.length <= 10^5`
`s` 由小写英文字母组成
"""

from typing import List, Optional


import heapq
from collections import Counter


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        """
        贪心 + 最大堆: 统计每个字符的出现次数。
        每次从最大堆中取出字典序最大的字符，最多连续放 repeatLimit 个。
        如果该字符还有剩余，则需要从次大的字符中取一个作为 "分隔符"，
        然后再继续使用最大的字符。这样保证相同字符不会连续超过 repeatLimit 次。
        """
        freq = Counter(s)
        # 最大堆：用负数模拟 (Python 默认最小堆)
        max_heap = [(-ord(ch), ch, cnt) for ch, cnt in freq.items()]
        heapq.heapify(max_heap)

        result = []
        while max_heap:
            neg_ord, ch, cnt = heapq.heappop(max_heap)
            # 最多连续使用 repeatLimit 个当前最大字符
            use = min(cnt, repeatLimit)
            result.append(ch * use)
            cnt -= use

            if cnt > 0:
                if not max_heap:
                    # 没有次大字符可作分隔符，结束
                    break
                # 从次大字符中取一个作为分隔符
                neg_ord2, ch2, cnt2 = heapq.heappop(max_heap)
                result.append(ch2)
                cnt2 -= 1
                if cnt2 > 0:
                    heapq.heappush(max_heap, (neg_ord2, ch2, cnt2))
                # 最大字符还有剩余，放回堆中继续使用
                heapq.heappush(max_heap, (neg_ord, ch, cnt))

        return ''.join(result)


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Hash Table, String, Counting, Heap (Priority Queue)
#
# 解题思路:
# 1. 统计 s 中每个字符的频率，放入最大堆（按字典序降序排列）。
# 2. 循环从堆顶取最大字符：
#    a. 最多连续放 repeatLimit 个该字符。
#    b. 如果该字符还有剩余：
#       - 检查堆中是否还有次大字符。如果没有，结束（无法再构造）。
#       - 取一个次大字符作为"分隔符"，放到结果中。
#       - 将最大字符（仍有剩余）和次大字符（如果还有剩余）放回堆中。
# 3. 重复直到堆为空或无法继续。
# 4. 返回拼接的字符串。
#
# 时间复杂度: O(n + k * log 26) ≈ O(n)
# - 统计频率 O(n)，堆操作 O(26 log 26)，n 远大于 26。
#
# 空间复杂度: O(1)
# - 堆和频率表大小均为常数（最多 26 个小写字母，不计结果字符串）。
#
# 关键点:
# - 使用最大堆保证每次取字典序最大的可用字符。
# - 当最大字符用满 repeatLimit 后仍有剩余时，必须用一个次大字符隔开。
# - 如果堆中只剩一个字符且已用了 repeatLimit 次，直接结束。
