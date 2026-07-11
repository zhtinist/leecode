"""
LeetCode #846 - Hand of Straights
中文题名：一手顺子
https://leetcode.com/problems/hand-of-straights/

Alice has a `hand` of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size `W`,
and consists of `W` consecutive cards.

Return `true` if and only if she can.

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Alice's `hand` can be rearranged as `[1,2,3],[2,3,4],[6,7,8]`.

Example 2:

Input: hand = [1,2,3,4,5], W = 4
Output: false
Explanation: Alice's `hand` can't be rearranged into groups of `4`.

Note:

`1 <= hand.length <= 10000`

`0 <= hand[i] <= 10^9`

`1 <= W <= hand.length`

【中文翻译】
爱丽丝有一手牌，以一个整数数组 `hand` 表示。

现在她想将这些牌重新排列成若干组，使得每组的大小都是 `W`，且每组由 `W` 张连续的牌组成。

当且仅当可以做到时，返回 `true`。

示例 1：

输入：hand = [1,2,3,6,2,3,4,7,8], W = 3
输出：true
解释：爱丽丝的手牌可以重新排列为 [1,2,3],[2,3,4],[6,7,8]。

示例 2：

输入：hand = [1,2,3,4,5], W = 4
输出：false
解释：爱丽丝的手牌无法重新排列成大小为 4 的组。

注意：

`1 <= hand.length <= 10000`

`0 <= hand[i] <= 10^9`

`1 <= W <= hand.length`

"""

from typing import List, Optional


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        from collections import Counter
        count = Counter(hand)

        # Process cards from smallest to largest
        for card in sorted(count.keys()):
            freq = count[card]
            if freq == 0:
                continue
            # Try to form groups starting with this card
            for next_card in range(card, card + groupSize):
                if count[next_card] < freq:
                    return False
                count[next_card] -= freq

        return True



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 贪心 + 计数。
# 1. 如果总牌数不能被 groupSize 整除，直接返回 False。
# 2. 统计每张牌的数量（使用 Counter）。
# 3. 按牌面值从小到大处理：对于每张牌 card 及其数量 freq，
#    以 card 为起点，需要 freq 组大小为 groupSize 的顺子。
#    即需要 card, card+1, ..., card+groupSize-1 各 freq 张。
# 4. 如果某张所需的牌数量不足，返回 False。
# 5. 由于每次从最小的可用牌开始组顺子，贪心策略是正确的。
#
# 时间复杂度: O(N log N) — 排序牌面值；N 是手牌数量
# 空间复杂度: O(N) — Counter 存储计数
#
# 关键点:
# - 贪心策略：总是从最小的牌开始组顺子
# - 每次消耗 freq 组，确保不会遗漏任何可能的组合
# - 如果一张牌的数量不足，说明无法完成分组
# - 类似的题：1296. Divide Array in Sets of K Consecutive Numbers
