"""
LeetCode #875 - Koko Eating Bananas
中文题名：爱吃香蕉的珂珂
https://leetcode.com/problems/koko-eating-bananas/

Koko loves to eat bananas.  There are `N` piles of bananas, the
`i`-th pile has `piles[i]` bananas.  The guards have gone
and will come back in `H` hours.

Koko can decide her bananas-per-hour eating speed of `K`.  Each hour, she
chooses some pile of bananas, and eats K bananas from that pile.  If the pile has less
than `K` bananas, she eats all of them instead, and won't eat any more
bananas during this hour.

Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards
come back.

Return the minimum integer `K` such that she can eat all the bananas within `H`
hours.

Example 1:

Input: piles = [3,6,7,11], H = 8
Output: 4

Example 2:

Input: piles = [30,11,23,4,20], H = 5
Output: 30

Example 3:

Input: piles = [30,11,23,4,20], H = 6
Output: 23

Note:

`1 <= piles.length <= 10^4`

`piles.length <= H <= 10^9`

`1 <= piles[i] <= 10^9`

【中文翻译】
珂珂喜欢吃香蕉。这里有 N 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，
将在 H 小时后回来。珂珂可以决定她吃香蕉的速度 K（单位：根/小时）。每个小时，
她将会选择一堆香蕉，从中吃掉 K 根。如果这堆香蕉少于 K 根，她将吃掉这堆的所有香蕉，
然后这一小时内不会再吃更多的香蕉。珂珂喜欢慢慢吃，但仍然想在警卫回来前吃完所有的香蕉。
返回她可以在 H 小时内吃完所有香蕉的最小速度 K。

"""

from typing import List, Optional
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 速度的下界是 1，上界是最大堆的香蕉数
        left, right = 1, max(piles)

        def can_finish(k: int) -> bool:
            """判断以速度 k 是否能在 h 小时内吃完所有香蕉"""
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
                if hours > h:
                    return False
            return hours <= h

        # 二分查找最小的满足条件的 K
        while left < right:
            mid = (left + right) // 2
            if can_finish(mid):
                right = mid  # 可以吃完，尝试更小的速度
            else:
                left = mid + 1  # 吃不完，需要加快速度

        return left



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 二分查找。K 的取值范围是 [1, max(piles)]。对于给定的速度 K，我们可以在 O(N) 时间内
# 计算出吃完所有香蕉所需的总时间：对每堆香蕉，需要 ceil(piles[i] / K) 小时。
# 然后进行二分搜索：如果以速度 mid 可以在 H 小时内吃完，则尝试更小的速度（right = mid）；
# 否则需要提高速度（left = mid + 1）。由于 can_finish 是单调的（速度越快越容易完成），
# 二分查找保证找到最小的可行速度。
#
# 时间复杂度: O(N log M)，其中 N = piles.length，M = max(piles)
# 空间复杂度: O(1)
#
# 关键点:
# - 单调性：速度越快越容易在 H 小时内完成，因此可以用二分查找
# - 计算每堆香蕉所需时间用 ceil(pile / k) = (pile + k - 1) // k
# - 上界是 max(piles) 而非 sum(piles)，因为每小时只能吃一堆
