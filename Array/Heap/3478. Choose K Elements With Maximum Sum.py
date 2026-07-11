"""
LeetCode #3478 - Choose K Elements With Maximum Sum
选出和最大的 K 个元素
https://leetcode.cn/problems/choose-k-elements-with-maximum-sum/

给你两个整数数组，`nums1` 和 `nums2`，长度均为 `n`，以及一个正整数 `k` 。
对从 `0` 到 `n - 1` 每个下标 `i` ，执行下述操作：
找出所有满足 `nums1[j]` 小于 `nums1[i]` 的下标 `j` 。
从这些下标对应的 `nums2[j]` 中选出 至多 `k` 个，并 最大化 这些值的总和作为结果。
返回一个长度为 `n` 的数组 `answer` ，其中 `answer[i]` 表示对应下标 `i` 的结果。

示例 1：

输入：nums1 = [4,2,1,5,3], nums2 = [10,20,30,40,50], k = 2
输出：[80,30,0,80,50]
解释：
对于 `i = 0` ：满足 `nums1[j] < nums1[0]` 的下标为 `[1, 2, 4]` ，选出其中值最大的两个，结果为 `50 + 30 = 80` 。
对于 `i = 1` ：满足 `nums1[j] < nums1[1]` 的下标为 `[2]` ，只能选择这个值，结果为 `30` 。
对于 `i = 2` ：不存在满足 `nums1[j] < nums1[2]` 的下标，结果为 `0` 。
对于 `i = 3` ：满足 `nums1[j] < nums1[3]` 的下标为 `[0, 1, 2, 4]` ，选出其中值最大的两个，结果为 `50 + 30 = 80` 。
对于 `i = 4` ：满足 `nums1[j] < nums1[4]` 的下标为 `[1, 2]` ，选出其中值最大的两个，结果为 `30 + 20 = 50` 。
示例 2：

输入：nums1 = [2,2,2,2], nums2 = [3,1,2,3], k = 1
输出：[0,0,0,0]
解释：由于 `nums1` 中的所有元素相等，不存在满足条件 `nums1[j] < nums1[i]`，所有位置的结果都是 0 。

提示：
`n == nums1.length == nums2.length`
`1 <= n <= 10^5`
`1 <= nums1[i], nums2[i] <= 10^6`
`1 <= k <= n`
"""

from typing import List, Optional


class Solution:
    def findAnswer(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        import heapq

        n = len(nums1)
        # Group by nums1 value: same value can't use each other
        # Sort by nums1, process in ascending order
        pairs = [(nums1[i], nums2[i], i) for i in range(n)]
        pairs.sort(key=lambda x: x[0])

        ans = [0] * n
        heap = []       # min-heap of top k nums2 values from strictly smaller nums1
        heap_sum = 0

        i = 0
        while i < n:
            # Find all elements with same nums1 value
            j = i
            while j < n and pairs[j][0] == pairs[i][0]:
                j += 1

            # Answer for this group: use current heap (only strictly smaller nums1)
            for t in range(i, j):
                idx = pairs[t][2]
                ans[idx] = heap_sum

            # Add this group's nums2 values to heap
            for t in range(i, j):
                val = pairs[t][1]
                heapq.heappush(heap, val)
                heap_sum += val
                if len(heap) > k:
                    removed = heapq.heappop(heap)
                    heap_sum -= removed

            i = j

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Sorting, Heap (Priority Queue)
#
# 解题思路:
# 1. 按 nums1 升序排列 (nums1[i], nums2[i], i) 三元组
# 2. 顺序遍历，维护一个小顶堆保存已见过的 nums2 的最多 k 个最大值及其总和
# 3. 相同 nums1 值的元素分组处理：
#    - 先计算当前组所有元素的答案（使用堆中的值，这些来自严格更小的 nums1）
#    - 再将当前组的 nums2 值加入堆中
# 4. 堆大小超过 k 时弹出最小值，保持堆中为最大的 k 个
#
# 时间复杂度: O(n log k)
# 空间复杂度: O(n)
#
# 关键点:
# - 严格小于：相同 nums1 的元素不能互相引用，需分组处理
# - 小顶堆维护最大的 k 个值，堆顶是第 k 大的值
