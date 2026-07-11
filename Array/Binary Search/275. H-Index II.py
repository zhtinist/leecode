"""
LeetCode #275 - H-Index II
中文题名：H 指数 II
https://leetcode.com/problems/h-index-ii/

Given an array of citations sorted in ascending order (each citation is
a non-negative integer) of a researcher, write a function to compute the researcher's
h-index.

According to the definition
of h-index on Wikipedia: "A scientist has index *h* if *h* of
his/her *N* papers have at least *h* citations
each, and the other *N &minus; h* papers have no more
than *h *citations each."

Example:

Input: `citations = [0,1,3,5,6]`
Output: 3
Explanation: `[0,1,3,5,6] `means the researcher has `5` papers in total and each of them had
received 0`, 1, 3, 5, 6` citations respectively.
Since the researcher has `3` papers with at least `3` citations each and the remaining
two with no more than `3` citations each, her h-index is `3`.

Note:

If there are several possible values for *h*, the maximum one is taken as the
h-index.

Follow up:

This is a follow up problem to H-Index, where `citations`
is now guaranteed to be sorted in ascending order.

Could you solve it in logarithmic time complexity?

【中文翻译】
给定一位研究者论文被引用次数的数组（每个元素是非负整数），数组已经按照升序排列，编写一个函数计算该研究者的 h 指数。

根据维基百科上 h 指数的定义：「h 指数」是指一位科研人员的 h 指数是指他/她至少有 h 篇论文分别被引用了至少 h 次，且其余的 *N − h* 篇论文每篇被引用次数不超过 h 次。

示例：

输入：`citations = [0,1,3,5,6]`
输出：3
解释：`[0,1,3,5,6]` 表示该研究者有 `5` 篇论文，每篇分别被引用 `0, 1, 3, 5, 6` 次。
由于该研究者有 `3` 篇论文至少被引用 `3` 次，其余两篇论文被引用次数不超过 `3` 次，所以其 h 指数为 `3`。

注意：

如果 h 有多种可能的值，h 指数取其中最大的作为 h 指数。

进阶：

这是 H 指数 的后续问题，其中 `citations` 现在保证按升序排列。

你能否在对数时间复杂度内解决此题？
"""

from typing import List, Optional


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """Compute h-index using binary search (array is sorted).

        For a sorted ascending array, at index i (0-based), there are (n - i)
        papers with citations >= citations[i]. We want the largest h such that
        citations[n - h] >= h (i.e., the h-th paper from the right has >= h citations).

        Binary search for the first position where citations[mid] >= n - mid.
        """
        n = len(citations)
        left, right = 0, n - 1

        while left <= right:
            mid = left + (right - left) // 2
            papers_with_at_least = n - mid  # papers with citations >= citations[mid]
            if citations[mid] >= papers_with_at_least:
                right = mid - 1  # try for a larger h (smaller mid)
            else:
                left = mid + 1

        # left is the first index where citations[left] >= n - left
        # h-index = n - left
        return n - left


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 由于数组已按升序排列，可以使用二分查找。关键观察：对于索引 i，有 (n - i)
# 篇论文的引用次数 >= citations[i]。我们寻找满足 citations[i] >= n - i
# 的第一个位置 i，那么 H-Index = n - i。
# 二分查找：如果 citations[mid] >= n - mid，说明 mid 及其右侧可能都是
# 候选位置，缩小右边界；否则缩小左边界。最终 left 指向第一个满足条件的位置。
#
# 时间复杂度: O(log N) - 二分查找
# 空间复杂度: O(1) - 只使用常数个变量
#
# 关键点:
# - 利用已排序的特性，O(log N) 时间解决问题
# - 核心不等式: citations[i] >= n - i
# - H-Index = n - left（left 是第一个满足条件的位置）
# - 与 #274 对比：排序数组可以用二分查找优化到对数时间
