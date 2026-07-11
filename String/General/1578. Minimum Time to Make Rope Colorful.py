"""
LeetCode #1578 - Minimum Time to Make Rope Colorful
中文题名：使绳子变成彩色的最短时间
https://leetcode.com/problems/minimum-time-to-make-rope-colorful/


Given a string `s` and an array of integers `cost` where
`cost[i]` is the cost of deleting the character `i` in
`s`.

Return the minimum cost of deletions such that there are no two identical
letters next to each other.

Notice that you will delete the chosen characters at the same time, in other words,
after deleting a character, the costs of deleting other characters will not
change.

Example 1:

Input: s = "abaac", cost = [1,2,3,4,5]
Output: 3
Explanation: Delete the letter "a" with cost 3 to get "abac" (String without two identical letters next to each other).

Example 2:

Input: s = "abc", cost = [1,2,3]
Output: 0
Explanation: You don't need to delete any character because there are no identical letters next to each other.

Example 3:

Input: s = "aabaa", cost = [1,2,3,4,1]
Output: 2
Explanation: Delete the first and the last character, getting the string ("aba").

Constraints:

`s.length == cost.length`

`1 <= s.length, cost.length <= 10^5`

`1 <= cost[i] <= 10^4`

`s` contains only lowercase English letters.

【中文翻译】
Alice 有 n 个气球排列在一根绳子上，每个气球的颜色为 colors[i]，移除气球 i 需要 neededTime[i] 秒。
要求移除一些气球后，绳子上没有两个相邻的气球颜色相同。返回所需的最少时间。

示例 1：
输入：colors = "abaac", neededTime = [1,2,3,4,5]
输出：3
解释：移除索引 0（1 秒）和 3（4 秒），但移除 0 和 3 用 5 秒。更好的方案：移除 2（3 秒）。

示例 2：
输入：colors = "abc", neededTime = [1,2,3]
输出：0

示例 3：
输入：colors = "aabaa", neededTime = [1,2,3,4,1]
输出：2
"""

from typing import List, Optional


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        result = 0
        i = 0
        n = len(colors)
        while i < n:
            j = i
            max_time = 0
            total_time = 0
            # Find all consecutive same-color balloons
            while j < n and colors[j] == colors[i]:
                total_time += neededTime[j]
                max_time = max(max_time, neededTime[j])
                j += 1
            # Keep the most expensive one, remove the rest
            result += total_time - max_time
            i = j
        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 对于每段连续相同颜色的气球，我们需要保留其中一个，移除其余所有。
# 为了使总时间最小，应该保留移除时间最大的那个（即花钱最多的），移除其余的。
# 所以每段的代价 = 该段所有 neededTime 之和 - 该段最大的 neededTime。
# 遍历所有连续段，累加代价即可。
#
# 时间复杂度: O(N) — 一次遍历
# 空间复杂度: O(1)
#
# 关键点:
# - 每组连续相同颜色保留耗时最大的气球
# - 其他全部移除
# - 代价 = sum - max












