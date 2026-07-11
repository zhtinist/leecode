"""
LeetCode #1296 - Divide Array in Sets of K Consecutive Numbers
中文题名：划分数组为连续数字的集合
https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

Given an array of integers `nums` and a positive
integer `k`, find whether it's possible to divide this array into sets
of `k` consecutive numbers

Return `True` if its possible otherwise return `False`.

Example 1:

Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].

Example 2:

Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
Output: true
Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].

Example 3:

Input: nums = [3,3,2,2,1,1], k = 3
Output: true

Example 4:

Input: nums = [1,2,3,4], k = 3
Output: false
Explanation: Each array should be divided in subarrays of size 3.

Constraints:

`1 <= nums.length <= 10^5`

`1 <= nums[i] <= 10^9`

`1 <= k <= nums.length`

【中文翻译】
给定一个整数数组 nums 和一个正整数 k，判断是否可以将该数组划分为若干组，每组包含 k 个连续数字。

如果可能则返回 True，否则返回 False。

示例 1：

输入：nums = [1,2,3,3,4,4,5,6], k = 4
输出：true
解释：数组可以划分为 [1,2,3,4] 和 [3,4,5,6]。

示例 2：

输入：nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
输出：true
解释：数组可以划分为 [1,2,3]、[2,3,4]、[3,4,5] 和 [9,10,11]。

示例 3：

输入：nums = [3,3,2,2,1,1], k = 3
输出：true

示例 4：

输入：nums = [1,2,3,4], k = 3
输出：false
解释：每个数组应该被划分为大小为 3 的子数组。

约束条件：

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= k <= nums.length
"""

from typing import List, Optional


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        from collections import Counter

        if len(nums) % k != 0:
            return False

        count = Counter(nums)
        # Sort unique keys to process from smallest
        for num in sorted(count.keys()):
            freq = count[num]
            if freq == 0:
                continue
            # Try to form groups starting with num
            for i in range(1, k):
                next_num = num + i
                if count[next_num] < freq:
                    return False
                count[next_num] -= freq
            # count[num] implicitly becomes 0 (consumed as the start of groups)
            # Actually we don't need to set it explicitly since we won't visit it again

        return True










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心算法，类似"一手顺子"(#846 Hand of Straights)。
# 1. 首先检查数组长度是否能被 k 整除，不能则直接返回 False。
# 2. 使用 Counter 统计每个数字的出现次数。
# 3. 将不重复的数字按键排序，从小到大处理。
# 4. 对于每个数字 num，如果有剩余次数 freq > 0，
#    则必须以 num 为起点组成 freq 个连续 k 元组。
#    检查 num+1 到 num+k-1 每个数字的剩余次数是否 >= freq，
#    若不足则返回 False；若足够则减去 freq 表示已被消耗。
# 5. 若所有数字都成功处理，返回 True。
#
# 时间复杂度: O(n log n) - 排序主导，n 为数组中不同数字的个数
# 空间复杂度: O(n) - Counter 存储每个数字的频次
#
# 关键点:
# - 贪心策略：从小到大处理，每个最小数字必须作为某个组的起点
# - Counter 充当哈希表，查询和更新 O(1)
# - 长度不整除 k 时快速剪枝
