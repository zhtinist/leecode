"""
LeetCode #3092 - Most Frequent IDs
最高频率的 ID
https://leetcode.cn/problems/most-frequent-ids/

你需要在一个集合里动态记录 ID 的出现频率。给你两个长度都为 `n` 的整数数组 `nums` 和 `freq` ，`nums` 中每一个元素表示一个 ID ，对应的 `freq` 中的元素表示这个 ID 在集合中此次操作后需要增加或者减少的数目。
增加 ID 的数目：如果 `freq[i]` 是正数，那么 `freq[i]` 个 ID 为 `nums[i]` 的元素在第 `i` 步操作后会添加到集合中。
减少 ID 的数目：如果 `freq[i]` 是负数，那么 `-freq[i]` 个 ID 为 `nums[i]` 的元素在第 `i` 步操作后会从集合中删除。
请你返回一个长度为 `n` 的数组 `ans` ，其中 `ans[i]` 表示第 `i` 步操作后出现频率最高的 ID 数目 ，如果在某次操作后集合为空，那么 `ans[i]` 为 0 。

示例 1：

输入：nums = [2,3,2,1], freq = [3,2,-3,1]
输出：[3,3,2,2]
解释：
第 0 步操作后，有 3 个 ID 为 2 的元素，所以 `ans[0] = 3` 。
第 1 步操作后，有 3 个 ID 为 2 的元素和 2 个 ID 为 3 的元素，所以 `ans[1] = 3` 。
第 2 步操作后，有 2 个 ID 为 3 的元素，所以 `ans[2] = 2` 。
第 3 步操作后，有 2 个 ID 为 3 的元素和 1 个 ID 为 1 的元素，所以 `ans[3] = 2` 。
示例 2：

输入：nums = [5,5,3], freq = [2,-2,1]
输出：[2,0,1]
解释：
第 0 步操作后，有 2 个 ID 为 5 的元素，所以 `ans[0] = 2` 。
第 1 步操作后，集合中没有任何元素，所以 `ans[1] = 0` 。
第 2 步操作后，有 1 个 ID 为 3 的元素，所以 `ans[2] = 1` 。

提示：
`1 <= nums.length == freq.length <= 10^5`
`1 <= nums[i] <= 10^5`
`-10^5 <= freq[i] <= 10^5`
`freq[i] != 0`
输入保证任何操作后，集合中的元素出现次数不会为负数。
"""

from typing import List, Optional


class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        import heapq
        n = len(nums)
        cnt = {}  # ID -> 当前频率
        ans = []
        # 最大堆，存储 (-freq, id)，用于快速获取最大频率
        # 但堆中可能存在过期的频率记录，需要惰性删除
        max_heap = []  # (-freq, id)

        for i in range(n):
            num = nums[i]
            f = freq[i]
            cnt[num] = cnt.get(num, 0) + f
            heapq.heappush(max_heap, (-cnt[num], num))

            # 弹出堆顶直到找到正确的频率
            while max_heap:
                neg_freq, id_val = max_heap[0]
                if cnt.get(id_val, 0) == -neg_freq:
                    break
                heapq.heappop(max_heap)

            if max_heap:
                ans.append(-max_heap[0][0])
            else:
                ans.append(0)

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Ordered Set, Heap (Priority Queue)
#
# 解题思路:
# 使用哈希表记录每个ID的当前频率，使用最大堆维护当前的最大频率。
# 每次更新后，将新的频率推入堆中。堆中可能有过期记录（频率被后续更新改变），
# 因此需要惰性删除：查看堆顶，如果堆顶记录的频率与哈希表中的当前频率不一致，则弹出。
# 这样可以在O(log n)时间内维护最大频率。
#
# 时间复杂度: O(n log n)
# 空间复杂度: O(n)
#
# 关键点:
# - 使用堆+惰性删除处理动态频率更新
# - 哈希表记录每个ID的当前真实频率
# - 堆顶频率与哈希表不一致时弹出（过期记录）
