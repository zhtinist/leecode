"""
LeetCode #1124 - Longest Well-Performing Interval
中文题名：表现良好的最长时间段
https://leetcode.com/problems/longest-well-performing-interval/

We are given `hours`, a list of the number of hours worked per day for a
given employee.

A day is considered to be a tiring day if and only if the number of hours worked is
(strictly) greater than `8`.

A well-performing interval is an interval of days for which the number of tiring
days is strictly larger than the number of non-tiring days.

Return the length of the longest well-performing interval.

Example 1:

Input: hours = [9,9,6,0,6,6,9]
Output: 3
Explanation: The longest well-performing interval is [9,9,6].

Constraints:

`1 <= hours.length <= 10000`

`0 <= hours[i] <= 16`

【中文翻译】
给定 hours，一个列表，表示某员工每天工作的小时数。

当且仅当一天工作的小时数（严格）大于 8 时，这一天被认为是"劳累的一天"。

表现良好的时间段是一个天数区间，其中劳累的天数严格大于不劳累的天数。

返回表现良好的最长时间段的长度。

示例 1：

输入：hours = [9,9,6,0,6,6,9]
输出：3
解释：表现良好的最长时间段是 [9,9,6]。

约束条件：

`1 <= hours.length <= 10000`

`0 <= hours[i] <= 16`
"""

from typing import List, Optional


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        prefix_sum = 0
        first_occurrence = {}
        ans = 0

        for i, h in enumerate(hours):
            prefix_sum += 1 if h > 8 else -1
            if prefix_sum > 0:
                ans = i + 1
            else:
                if prefix_sum not in first_occurrence:
                    first_occurrence[prefix_sum] = i
                if prefix_sum - 1 in first_occurrence:
                    ans = max(ans, i - first_occurrence[prefix_sum - 1])

        return ans










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 将问题转化为求前缀和数组中最长的和大于 0 的子数组。
# 1. 将 hours 数组转化为得分：劳累天（>8）记 +1，不劳累天（<=8）记 -1。
# 2. 计算前缀和 prefix_sum，问题变为：找到 i < j 使得 prefix_sum[j] - prefix_sum[i] > 0，
#    即 prefix_sum[i] < prefix_sum[j]，且 j - i 最大。
# 3. 遍历数组，维护每个前缀和首次出现的位置（哈希表）。
# 4. 对于当前位置 i：
#    - 若 prefix_sum > 0，说明从开头到 i 的区间满足条件，ans = i + 1。
#    - 否则，查找 prefix_sum - 1 是否在哈希表中。若存在，则区间 [first_occurrence[prefix_sum-1]+1, i] 的和
#      为 prefix_sum - (prefix_sum - 1) = 1 > 0，满足条件，更新 ans。
#    - 仅当 prefix_sum 未出现过时才记录其位置（保留最早出现的位置）。
#
# 时间复杂度: O(n) - 一次遍历
# 空间复杂度: O(n) - 哈希表最坏存储 n 个前缀和
#
# 关键点:
# - 转化为 +1/-1 得分，求最大和 > 0 的子数组
# - 只需要查找 prefix_sum - 1，因为要使得子数组和 >= 1（即 > 0）
