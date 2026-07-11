"""
LeetCode #786 - K-th Smallest Prime Fraction
中文题名：第 K 个最小的素数分数
https://leetcode.com/problems/k-th-smallest-prime-fraction/

A sorted list `A` contains 1, plus some number of primes.  Then, for every p
< q in the list, we consider the fraction p/q.

What is the `K`-th smallest fraction considered?  Return your answer as an
array of ints, where `answer[0] = p` and `answer[1] = q`.

Examples:
Input: A = [1, 2, 3, 5], K = 3
Output: [2, 5]
Explanation:
The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, 2/3.
The third fraction is 2/5.

Input: A = [1, 7], K = 1
Output: [1, 7]

Note:

`A` will have length between `2` and `2000`.

Each `A[i]` will be between `1` and `30000`.

`K` will be between `1` and `A.length * (A.length - 1) /
2`.

【中文翻译】
一个已排序的列表 `A` 包含 1 和一些素数。然后，对于列表中的每一对 p < q，我们考虑分数 p/q。

第 `K` 小的分数是哪个？以整数数组的形式返回答案，其中 `answer[0] = p`，`answer[1] = q`。

示例：
输入：A = [1, 2, 3, 5], K = 3
输出：[2, 5]
解释：
按排序顺序考虑的分数有：
1/5, 1/3, 2/5, 1/2, 3/5, 2/3。
第三个分数是 2/5。

输入：A = [1, 7], K = 1
输出：[1, 7]

注意：

`A` 的长度在 `2` 到 `2000` 之间。

每个 `A[i]` 在 `1` 到 `30000` 之间。

`K` 在 `1` 到 `A.length * (A.length - 1) / 2` 之间。
"""

from typing import List, Optional


class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        import heapq
        n = len(A)
        # Min-heap: (fraction_value, numerator_index, denominator_index)
        heap = [(A[0] / A[i], 0, i) for i in range(1, n)]
        heapq.heapify(heap)

        for _ in range(K - 1):
            _, i, j = heapq.heappop(heap)
            if i + 1 < j:
                heapq.heappush(heap, (A[i + 1] / A[j], i + 1, j))

        _, i, j = heap[0]
        return [A[i], A[j]]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 最小堆 / 多路归并。
# 类似于合并 K 个有序链表。
# 对于每个分母 j（从 1 到 n-1），以分子 i = 0 开始（A[0]/A[j]）是最小的分数。
# 1. 将所有 (A[0]/A[j], 0, j) 放入最小堆。
# 2. 重复 K-1 次：弹出堆顶 (A[i]/A[j], i, j)，然后将下一个分子 i+1 的分数 (A[i+1]/A[j], i+1, j) 入堆（如果 i+1 < j）。
# 3. 第 K 次堆顶即为答案。
# 也可以使用二分查找：在 [0, 1] 上二分猜值，统计 <= mid 的分数数量。
#
# 时间复杂度: O(K log N + N log N) 其中使用堆方法，K 最大为 O(N^2)，实际 O(N^2 log N)
# 空间复杂度: O(N) - 堆中最多 N 个元素
#
# 关键点:
# - 多路归并：每路是固定分母、递增分子的有序序列
# - 初始堆包含每个分母对应的最小分子分数
# - 弹出后推入同分母下一个分子
# - 也可用二分查找优化到 O(N log N)
