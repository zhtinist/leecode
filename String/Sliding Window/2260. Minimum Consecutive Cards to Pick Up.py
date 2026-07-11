"""
LeetCode #2260 - Minimum Consecutive Cards to Pick Up
必须拿起的最小连续卡牌数
https://leetcode.cn/problems/minimum-consecutive-cards-to-pick-up/

给你一个整数数组 `cards` ，其中 `cards[i]` 表示第 `i` 张卡牌的 值 。如果两张卡牌的值相同，则认为这一对卡牌 匹配 。
返回你必须拿起的最小连续卡牌数，以使在拿起的卡牌中有一对匹配的卡牌。如果无法得到一对匹配的卡牌，返回 `-1` 。

示例 1：
输入：cards = [3,4,2,3,4,7] 输出：4 解释：拿起卡牌 [3,4,2,3] 将会包含一对值为 3 的匹配卡牌。注意，拿起 [4,2,3,4] 也是最优方案。
示例 2：
输入：cards = [1,0,5,3] 输出：-1 解释：无法找出含一对匹配卡牌的一组连续卡牌。

提示：
`1 <= cards.length <= 10^5`
`0 <= cards[i] <= 10^6`
"""

from typing import List, Optional


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        """
        Find the minimum length of a contiguous subarray that contains at least one duplicate.
        Use a hash map to track the most recent index of each card value.
        For each card, if we've seen it before, the subarray length from the last occurrence
        to the current index is a candidate answer.
        """
        last_seen: dict[int, int] = {}
        min_len = float('inf')

        for i, card in enumerate(cards):
            if card in last_seen:
                min_len = min(min_len, i - last_seen[card] + 1)
            last_seen[card] = i

        return min_len if min_len != float('inf') else -1


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Sliding Window
#
# 解题思路:
# 题目要求找出包含一对相同卡牌的最短连续子数组。核心思路是：对于每个卡牌值，
# 如果它之前出现过，那么从上次出现位置到当前位置之间的子数组就包含一对匹配卡牌。
# 使用一个哈希表 last_seen 记录每个卡牌值最后出现的位置。遍历数组时，若当前卡牌
# 值已存在于哈希表中，则计算当前下标与上次出现下标之间的距离（子数组长度），
# 并更新全局最小值。最终返回最小长度，若不存在匹配则返回 -1。
#
# 时间复杂度: O(n)，其中 n 是数组长度。只需一次遍历。
# 空间复杂度: O(n)，用于哈希表存储每个卡牌值的最近出现位置。
#
# 关键点:
# - 使用哈希表记录每个值最后出现的位置，一次遍历即可解决
# - 子数组长度为 i - last_seen[card] + 1（包含两端点）
# - 注意边界条件：无匹配时返回 -1
