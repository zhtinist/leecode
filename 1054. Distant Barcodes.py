"""
LeetCode #1054 - Distant Barcodes
中文题名：距离相等的条形码
https://leetcode.com/problems/distant-barcodes/

In a warehouse, there is a row of barcodes, where the `i`-th barcode
is `barcodes[i]`.

Rearrange the barcodes so that no two adjacent barcodes are equal.  You may return any
answer, and it is guaranteed an answer exists.

Example 1:

Input: [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]

Example 2:

Input: [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,2,1,2,1]

【中文翻译】
在一个仓库里，有一排条形码，其中第 i 个条形码为 barcodes[i]。

请你重新排列这些条形码，使其中任意两个相邻的条形码不能相等。你可以返回任何满足要求的答案，此题保证存在答案。

示例 1：

输入：[1,1,1,2,2,2]
输出：[2,1,2,1,2,1]

示例 2：

输入：[1,1,1,1,2,2,3,3]
输出：[1,3,1,3,2,1,2,1]

"""

from typing import List, Optional


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        from collections import Counter
        import heapq

        count = Counter(barcodes)
        max_heap = [(-freq, val) for val, freq in count.items()]
        heapq.heapify(max_heap)

        result = []
        prev_freq, prev_val = 0, 0

        while max_heap:
            freq, val = heapq.heappop(max_heap)
            freq = -freq
            result.append(val)

            if prev_freq > 0:
                heapq.heappush(max_heap, (-prev_freq, prev_val))

            prev_freq = freq - 1
            prev_val = val

        return result










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用贪心 + 最大堆。核心思想：每次放置当前剩余数量最多的条形码，但要避免与上一个放置的相同。
# 1. 统计每个条形码的出现次数，构建最大堆（按频率从大到小）。
# 2. 每次从堆顶取出频率最高的元素，放入结果数组。
# 3. 将上一个放入的元素（频率减一后如果仍大于 0）重新压入堆中。
# 4. 这样保证每次取出的都是当前可选的最大频率元素，且不会与上一个相同。
#
# 时间复杂度: O(n log k) - n 为数组长度，k 为不同元素个数
# 空间复杂度: O(k) - 堆和计数器的空间
#
# 关键点:
# - 贪心策略：优先放置频率最高的元素
# - 使用"冷却"机制：暂存上一个元素，下一轮再入堆
# - 保证每次放置的元素与上一次不同
# - Python 使用负数频率模拟最大堆
