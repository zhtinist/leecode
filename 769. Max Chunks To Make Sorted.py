"""
LeetCode #769 - Max Chunks To Make Sorted
中文题名：最多能完成排序的块
https://leetcode.com/problems/max-chunks-to-make-sorted/

Given an array `arr` that is a permutation of `[0, 1, ..., arr.length -
1]`, we split the array into some number of "chunks" (partitions), and
individually sort each chunk.  After concatenating them, the result equals the
sorted array.

What is the most number of chunks we could have made?

Example 1:

Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.

Example 2:

Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.

Note:

`arr` will have length in range `[1, 10]`.

`arr[i]` will be a permutation of `[0, 1, ..., arr.length - 1]`.

【中文翻译】
给定一个数组 `arr`，它是 `[0, 1, ..., arr.length - 1]` 的一个排列，我们将数组分割成若干"块"（分区），并对每个块分别进行排序。将它们连接起来后，结果等于排序后的数组。

我们最多能分成多少块？

示例 1：

输入：arr = [4,3,2,1,0]
输出：1
解释：分成两块或更多块将不会返回所需的结果。例如，分成 [4, 3], [2, 1, 0] 的结果是 [3, 4, 0, 1, 2]，这不是有序的。

示例 2：

输入：arr = [1,0,2,3,4]
输出：4
解释：我们可以分成两块，如 [1, 0], [2, 3, 4]。然而，分成 [1, 0], [2], [3], [4] 可以得到最多的块数。

注意：

`arr` 的长度范围在 `[1, 10]`。

`arr[i]` 是 `[0, 1, ..., arr.length - 1]` 的一个排列。
"""

from typing import List, Optional


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        cur_max = 0
        for i, val in enumerate(arr):
            cur_max = max(cur_max, val)
            if cur_max == i:
                chunks += 1
        return chunks



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心。
# 由于 arr 是 [0, 1, ..., N-1] 的排列，排序后的数组中 arr[i] 应该等于 i。
# 遍历数组时维护当前遇到的最大值 cur_max。
# 当 cur_max == i 时，说明区间 [0, i] 中的所有元素都已经出现过（最大值刚好等于下标），
# 当前区间内的元素排序后正好对应 [0, i]，可以形成一个独立的块。
# 每当满足该条件，块数加一。
#
# 时间复杂度: O(N) - 一次遍历
# 空间复杂度: O(1) - 只使用常数额外空间
#
# 关键点:
# - 核心洞察：对于排序后的数组 arr[i] = i
# - 当前最大值 == 当前下标时即可切分
# - 利用了 arr 是完整排列的性质
# - 与 #768 的区别：#768 中 arr 是任意元素（可能有重复），需要更复杂的方法
