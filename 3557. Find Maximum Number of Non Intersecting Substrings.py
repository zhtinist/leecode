"""
LeetCode #3557 - Find Maximum Number of Non Intersecting Substrings
不相交子字符串的最大数量
https://leetcode.cn/problems/find-maximum-number-of-non-intersecting-substrings/

给你一个字符串 `word`。
返回以 首尾字母相同 且 长度至少为 4 的 不相交子字符串 的最大数量。
子字符串 是字符串中连续的 非空 字符序列。

示例 1：

输入： word = "abcdeafdef"
输出： 2
解释：
两个子字符串是 `"abcdea"` 和 `"fdef"`。
示例 2：

输入： word = "bcdaaaab"
输出： 1
解释：
唯一的子字符串是 `"aaaa"`。注意我们 不能 同时选择 `"bcdaaaab"`，因为它和另一个子字符串有重叠。

提示：
`1 <= word.length <= 2 * 10^5`
`word` 仅由小写英文字母组成。
"""

from typing import List, Optional


class Solution:
    def maxSubstrings(self, word: str) -> int:
        n = len(word)
        # For each character, store all its occurrence positions
        from collections import defaultdict
        positions = defaultdict(list)
        for i, ch in enumerate(word):
            positions[ch].append(i)

        intervals = []
        for i in range(n):
            ch = word[i]
            # Binary search for the first position of same char at distance >= 3
            # We need j >= i+3 such that word[j] == ch
            lst = positions[ch]
            import bisect
            idx = bisect.bisect_left(lst, i + 3)
            if idx < len(lst):
                j = lst[idx]
                intervals.append((i, j))

        # Greedy interval scheduling: sort by end, pick non-overlapping
        intervals.sort(key=lambda x: x[1])
        count = 0
        last_end = -1
        for start, end in intervals:
            if start > last_end:
                count += 1
                last_end = end

        return count










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Hash Table, String, Dynamic Programming
#
# 解题思路:
# 这是一个经典的区间调度问题。对于每个起始位置 i，我们需要找到以相同字母结尾的最短有效子字符串
# （即找到 j >= i+3 且 word[j] == word[i] 的最小 j）。每个这样的子字符串形成一个区间 [i, j]。
# 区间越短，留给其他子字符串的空间越多，因此对于每个起点只需要最短的区间。
# 预处理：用哈希表记录每个字母出现的所有位置，然后用二分查找快速定位每个起点的最短有效区间。
# 最后对所有区间按结束位置排序，贪心选择不重叠的区间即可得到最大数量。
#
# 时间复杂度: O(n log n)，其中 n 为字符串长度。预处理 O(n)，每个位置二分查找 O(log n)，
#   排序 O(n log n)，贪心选择 O(n)。总 O(n log n)。
# 空间复杂度: O(n)，存储位置哈希表和区间列表。
#
# 关键点:
# - 对于每个起点只需最短区间（最早结束），因为长区间不会比短区间更优。
# - 经典贪心区间调度：按结束时间升序排序，每次选不重叠的区间，能得到最大区间数。
# - 二分查找加速找到每个起点的目标位置，避免 O(n^2) 暴力扫描。
