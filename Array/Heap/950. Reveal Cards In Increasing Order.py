"""
LeetCode #950 - Reveal Cards In Increasing Order
中文题名：按递增顺序显示卡牌
https://leetcode.com/problems/reveal-cards-in-increasing-order/

In a deck of cards, every card has a unique integer.  You can order the deck in any
order you want.

Initially, all the cards start face down (unrevealed) in one deck.

Now, you do the following steps repeatedly, until all cards are revealed:

Take the top card of the deck, reveal it, and take it out of the deck.

If there are still cards in the deck, put the next top card of the deck at the
bottom of the deck.

If there are still unrevealed cards, go back to step 1.  Otherwise, stop.

Return an ordering of the deck that would reveal the cards in increasing
order.

The first entry in the answer is considered to be the top of the deck.

Example 1:

Input: [17,13,11,2,3,5,7]
Output: [2,13,3,11,5,17,7]
Explanation:
We get the deck in the order [17,13,11,2,3,5,7] (this order doesn't matter), and reorder it.
After reordering, the deck starts as [2,13,3,11,5,17,7], where 2 is the top of the deck.
We reveal 2, and move 13 to the bottom.  The deck is now [3,11,5,17,7,13].
We reveal 3, and move 11 to the bottom.  The deck is now [5,17,7,13,11].
We reveal 5, and move 17 to the bottom.  The deck is now [7,13,11,17].
We reveal 7, and move 13 to the bottom.  The deck is now [11,17,13].
We reveal 11, and move 17 to the bottom.  The deck is now [13,17].
We reveal 13, and move 17 to the bottom.  The deck is now [17].
We reveal 17.
Since all the cards revealed are in increasing order, the answer is correct.

Note:

`1 <= A.length <= 1000`

`1 <= A[i] <= 10^6`

`A[i] != A[j]` for all `i != j`

【中文翻译】
在一副牌中，每张牌都有一个唯一的整数。你可以按任意顺序排列这副牌。

最初，所有牌都朝下（未揭示）放在一副牌中。

现在，你反复执行以下步骤，直到所有牌都被揭示：
1. 取牌堆顶部的牌，揭示它，并将其移出牌堆。
2. 如果牌堆中仍有牌，则将牌堆顶部的下一张牌移动到牌堆的底部。
3. 如果仍有未揭示的牌，返回步骤 1。否则停止。

返回一种牌的排列顺序，使得揭示的牌按递增顺序排列。
答案中的第一个元素被视为牌堆的顶部。

"""

from typing import List, Optional
from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort()
        result = [0] * n
        indices = deque(range(n))

        for card in deck:
            # Reveal the card at the next available index
            result[indices.popleft()] = card
            # Move the next index to the bottom
            if indices:
                indices.append(indices.popleft())

        return result



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 1. 模拟索引过程：使用双端队列 indices 来模拟牌的揭示过程，初始存入所有
#    索引位置 0 到 n-1。
# 2. 模拟揭示规则：
#    - 每次从队首取出一个索引（模拟"揭示"），将排序后的最小牌放入该位置
#    - 然后将队首的下一个索引移到队尾（模拟"将下一张牌移到底部"）
# 3. 核心思想：先确定"哪个位置在第几步被揭示"，再按递增顺序将牌填入那些位置。
#    排序后的 deck 按顺序分配，保证揭示顺序递增。
# 4. 返回结果数组。
#
# 时间复杂度: O(N * log N) — 排序的开销，队列模拟为 O(N)。
# 空间复杂度: O(N) — 结果数组和双端队列。
#
# 关键点:
# - 反向思维：不直接排序牌面，而是确定揭示次序与索引位置的映射
# - 队列模拟揭示过程决定每张牌应该放在哪个位置
# - 将排序后的牌按揭示顺序填入对应索引即可
