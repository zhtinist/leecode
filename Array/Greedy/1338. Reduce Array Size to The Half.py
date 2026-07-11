"""
LeetCode #1338 - Reduce Array Size to The Half
中文题名：数组大小减半
https://leetcode.com/problems/reduce-array-size-to-the-half/

Given an array `arr`.  You can choose a set of integers and remove
all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of
the integers of the array are removed.

Example 1:

Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has size greater than half of the size of the old array.

Example 2:

Input: arr = [7,7,7,7,7,7]
Output: 1
Explanation: The only possible set you can choose is {7}. This will make the new array empty.

Example 3:

Input: arr = [1,9]
Output: 1

Example 4:

Input: arr = [1000,1000,3,7]
Output: 1

Example 5:

Input: arr = [1,2,3,4,5,6,7,8,9,10]
Output: 5

Constraints:

`1 <= arr.length <= 10^5`

`arr.length` is even.

`1 <= arr[i] <= 10^5`

【中文翻译】
给定一个数组 `arr`。你可以选择一个整数集合，并移除数组中这些整数的所有出现。

返回使得至少一半的数组元素被移除所需的最小集合大小。

示例 1：

输入: arr = [3,3,3,3,5,5,5,2,2,7]
输出: 2
解释: 选择 {3,7} 将使新数组变为 [5,5,5,2,2]，大小为 5（等于原数组大小的一半）。
可选的大小为 2 的集合有 {3,5}、{3,2}、{5,2}。
不能选择 {2,7}，因为它会使新数组变为 [3,3,3,3,5,5,5]，大小超过原数组的一半。

示例 2：

输入: arr = [7,7,7,7,7,7]
输出: 1
解释: 唯一可选的集合是 {7}，这会使新数组变为空。

示例 3：

输入: arr = [1,9]
输出: 1

示例 4：

输入: arr = [1000,1000,3,7]
输出: 1

示例 5：

输入: arr = [1,2,3,4,5,6,7,8,9,10]
输出: 5
解释: 由于每个元素只出现一次，需要移除一半的元素（5 个）才能达到目标。

约束条件：

`1 <= arr.length <= 10^5`

`arr.length` 为偶数。

`1 <= arr[i] <= 10^5`
"""

from typing import List, Optional


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        from collections import Counter

        n = len(arr)
        target = n // 2

        # 统计每个元素的出现次数
        freq = Counter(arr)

        # 按出现次数降序排序
        counts = sorted(freq.values(), reverse=True)

        # 贪心选择出现次数最多的元素，直到移除数量达到目标
        removed = 0
        set_size = 0
        for count in counts:
            removed += count
            set_size += 1
            if removed >= target:
                return set_size

        return set_size



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 统计数组中每个整数的出现频率（使用 Counter）。
# 2. 将频率按从大到小排序。
# 3. 贪心地从频率最高的元素开始选择，累计已移除的元素数量。
# 4. 当累计移除数量达到或超过 n/2 时，返回已选择的元素个数（即集合大小）。
#
# 贪心策略的正确性：要最小化集合大小，每次应该选择出现次数最多的元素，
# 因为这样可以最快地达到移除目标。
#
# 时间复杂度: O(N log N) — 统计频率 O(N)，排序 O(M log M) 其中 M ≤ N 为不同元素个数
# 空间复杂度: O(N) — Counter 存储频率
#
# 关键点:
# - 贪心策略：总是移除频率最高的元素
# - 目标值是 n/2（整数除法），因为数组长度恒为偶数
# - Counter 可以方便地统计频率










