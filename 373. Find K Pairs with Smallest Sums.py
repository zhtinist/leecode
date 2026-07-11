"""
LeetCode #373 - Find K Pairs with Smallest Sums
中文题名：查找和最小的K对数字
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

You are given two integer arrays nums1 and nums2 sorted in ascending order and
an integer k.

Define a pair (u,v) which consists of one element from the first array and one element
from the second array.

Find the k pairs (u1,v1),(u2,v2)
...(uk,vk) with the smallest sums.

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence:
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [1,1],[1,1]
Explanation: The first 2 pairs are returned from the sequence:
[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [1,3],[2,3]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]

【中文翻译】
给定两个按升序排列的整数数组 nums1 和 nums2，以及一个整数 k。

定义一个数对 (u,v)，其中 u 来自第一个数组，v 来自第二个数组。

找到和最小的 k 个数对 (u1,v1),(u2,v2)...(uk,vk)。

示例 1：

输入：nums1 = [1,7,11], nums2 = [2,4,6], k = 3
输出：[[1,2],[1,4],[1,6]]
解释：返回序列中的前 3 个数对：
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

示例 2：

输入：nums1 = [1,1,2], nums2 = [1,2,3], k = 2
输出：[1,1],[1,1]
解释：返回序列中的前 2 个数对：
[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

示例 3：

输入：nums1 = [1,2], nums2 = [3], k = 3
输出：[1,3],[2,3]
解释：返回序列中的所有可能数对：[1,3],[2,3]
"""

import heapq
from typing import List, Optional


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []

        heap = []
        # 将 nums1 的前 k 个元素分别与 nums2[0] 组成初始数对放入堆中
        for i in range(min(len(nums1), k)):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        result = []
        while heap and len(result) < k:
            _, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            # 将当前 nums1[i] 与 nums2 的下一个元素配对，放入堆中
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return result











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 本题要求从两个有序数组中找出和最小的 k 个数对。如果直接生成所有可能的数对（共 m*n 个）
# 再排序，时间复杂度过高。最优解法是使用最小堆（优先队列）。
#
# 核心思想类似于"多路归并"：
# 1. 先将所有 (nums1[i], nums2[0]) 的数对（最多 min(m, k) 个）放入最小堆中，
#    堆中存储三元组 (两数之和, nums1索引i, nums2索引j)
# 2. 每次从堆中弹出和最小的数对加入结果
# 3. 然后将该数对中 nums2 的索引向后移动一位，形成新的数对 (nums1[i], nums2[j+1]) 放入堆中
#    这样保证了 nums1[i] 配对所有 nums2[j] 是按和从小到大产生的
# 4. 重复上述过程直到结果集满 k 个或堆为空
#
# 时间复杂度: O(k * log min(m, k)) - 每次堆操作为 O(log min(m, k))，最多执行 k 次
# 空间复杂度: O(min(m, k)) - 堆的大小不超过 min(m, k)
#
# 关键点:
# - 不需要生成所有数对，利用最小堆动态找出前 k 个最小和
# - 初始只放入 (nums1[i], nums2[0])，后续通过递增 nums2 的索引来扩展
# - 堆中存储索引而非数对本身，方便定位下一个配对元素
# - 注意边界：k 可能大于 m*n，此时返回所有可能的数对即可
