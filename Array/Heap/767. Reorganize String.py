"""
LeetCode #767 - Reorganize String
中文题名：重构字符串
https://leetcode.com/problems/reorganize-string/

Given a string `S`, check if the letters can be rearranged so that two characters
that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"

Example 2:

Input: S = "aaab"
Output: ""

Note:

`S` will consist of lowercase letters and have length in range `[1,
500]`.

【中文翻译】
给定一个字符串 `S`，检查是否能重新排列其中的字母，使得两相邻的字符不相同。

如果可能，输出任意一个可能的结果。如果不可能，返回空字符串。

示例 1：

输入：S = "aab"
输出："aba"

示例 2：

输入：S = "aaab"
输出：""

注意：

`S` 由小写字母组成，长度范围在 `[1, 500]`。
"""

from typing import List, Optional


class Solution:
    def reorganizeString(self, S: str) -> str:
        from collections import Counter
        import heapq

        cnt = Counter(S)
        max_freq = max(cnt.values())
        if max_freq > (len(S) + 1) // 2:
            return ""

        heap = [(-freq, ch) for ch, freq in cnt.items()]
        heapq.heapify(heap)

        res = []
        while len(heap) >= 2:
            freq1, ch1 = heapq.heappop(heap)
            freq2, ch2 = heapq.heappop(heap)
            res.append(ch1)
            res.append(ch2)
            if freq1 + 1 < 0:
                heapq.heappush(heap, (freq1 + 1, ch1))
            if freq2 + 1 < 0:
                heapq.heappush(heap, (freq2 + 1, ch2))

        if heap:
            res.append(heap[0][1])

        return "".join(res)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心算法 + 最大堆。
# 1. 首先统计每个字符的出现频率。如果某个字符的频率超过 (N+1)/2，则不可能满足相邻不同，返回空字符串。
# 2. 使用最大堆（Python 中为负数最小堆），每次取出频率最高和次高的两个字符，交替放入结果。
# 3. 将剩余次数大于 0 的字符重新压入堆中。
# 4. 最后如果堆中还剩一个字符（此时频率一定为 1），直接追加到末尾即可。
#
# 时间复杂度: O(N log K)，其中 N 是字符串长度，K = 26（不同字符数），实际为 O(N)
# 空间复杂度: O(K) = O(1)
#
# 关键点:
# - 可行性判断：max_freq > (N+1)//2 时无法构造
# - 贪心策略：每次优先放置剩余最多的字符
# - 使用最大堆维护频率顺序
# - 交替放置最多和次多的字符能最大化间隔
