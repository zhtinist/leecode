"""
LeetCode #274 - H-Index
https://leetcode.com/problems/h-index/

Given an array of citations (each citation is a non-negative integer) of a researcher, write
a function to compute the researcher's h-index.

According to the definition
of h-index on Wikipedia: "A scientist has index *h* if *h* of his/her *N*
papers have at least *h* citations each, and the other *N &minus; h* papers
have no more than *h* citations each."

Example:

Input: `citations = [3,0,6,1,5]`
Output: 3
Explanation: `[3,0,6,1,5] `means the researcher has `5` papers in total and each of them had
received `3, 0, 6, 1, 5` citations respectively.
Since the researcher has `3` papers with at least `3` citations each and the remaining
two with no more than `3` citations each, her h-index is `3`.

Note: If there are several possible values for *h*, the maximum
one is taken as the h-index.
"""

from typing import List, Optional


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """Compute the h-index using counting sort approach.

        The h-index is the largest h such that at least h papers have >= h citations.
        Counting sort: for each citation count, increment bucket[min(c, n)].
        Then scan from high to low, accumulating counts until accumulated >= i.
        """
        n = len(citations)
        # buckets[i] = number of papers with exactly i citations
        # bucket[n] accumulates papers with >= n citations
        buckets = [0] * (n + 1)

        for c in citations:
            if c >= n:
                buckets[n] += 1
            else:
                buckets[c] += 1

        # Scan from high to low
        count = 0
        for i in range(n, -1, -1):
            count += buckets[i]
            if count >= i:
                return i

        return 0


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用计数排序（Counting Sort）的思想。H-Index 定义为最大的 h，使得至少有
# h 篇论文被引用了至少 h 次。创建一个大小为 n+1 的桶数组，其中 bucket[i]
# 表示被引用了恰好 i 次的论文数量（bucket[n] 存引用次数 >= n 的论文）。
# 然后从大到小遍历，累加论文数量。当累加数量 >= 当前索引 i 时，i 就是 H-Index。
#
# 时间复杂度: O(N) - 一次遍历计数 + 一次从大到小扫描
# 空间复杂度: O(N) - 桶数组大小为 N+1
#
# 关键点:
# - 引用次数超过 N 的论文统一放入 bucket[N]，因为 H-Index 不可能超过 N
# - 从大到小扫描累加，第一个满足 count >= i 的 i 就是答案
# - 比排序方法 O(N log N) 更优
