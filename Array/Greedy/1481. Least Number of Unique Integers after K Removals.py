"""
LeetCode #1481 - Least Number of Unique Integers after K Removals
中文题名：不同整数的最少数目
https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/

Given an array of integers `arr` and an integer `k`. Find
the least number of unique integers after removing
exactly `k` elements.

Example 1:

Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.

Example 2:

Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.

Constraints:

`1 <= arr.length <= 10^5`

`1 <= arr[i] <= 10^9`

`0 <= k <= arr.length`

【中文翻译】

给定一个整数数组 `arr` 和一个整数 `k`。找出恰好移除 `k` 个元素后，数组中不同整数的最少数目。

示例 1：
输入：arr = [5,5,4], k = 1
输出：1
解释：移除单个 4，只剩下 5。

示例 2：
输入：arr = [4,3,1,1,3,3,2], k = 3
输出：2
解释：移除 4、2 以及两个 1 中的一个或三个 3 中的一个。剩余 1 和 3。

约束条件：
1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
0 <= k <= arr.length

"""

from typing import List, Optional


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        from collections import Counter
        freq = Counter(arr)
        # Sort by frequency ascending, remove least frequent elements first
        counts = sorted(freq.values())

        unique = len(counts)
        for c in counts:
            if k >= c:
                k -= c
                unique -= 1
            else:
                break

        return unique



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 统计每个数字出现的频率（使用 Counter）。
# 2. 将频率按升序排序。
# 3. 从频率最小的元素开始移除（贪心策略）：
#    每次尽可能多地移除当前频率的元素。
#    如果 k >= 当前频率，则完全移除该元素（unique--, k -= freq）。
#    如果 k < 当前频率，无法再移除任何完整的元素，停止。
# 4. 返回剩余的 unique 数量。
# 5. 贪心策略正确性：要最小化不同整数的数量，应优先移除出现
#    次数最少的元素，因为这样可以用最少的 k 消除一个不同的整数。
#
# 时间复杂度: O(N log N)
# 空间复杂度: O(N)
#
# 关键点:
# - 贪心策略：优先移除频率低的元素
# - 按频率排序后依次处理
# - Counter 统计频率










