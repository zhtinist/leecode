"""
LeetCode #822 - Card Flipping Game
中文题名：翻转卡片游戏
https://leetcode.com/problems/card-flipping-game/

On a table are `N` cards, with a positive integer printed on the front and back of
each card (possibly different).

We flip any number of cards, and after we choose one card.

If the number `X` on the back of the chosen card is not on the front of any
card, then this number X is good.

What is the smallest number that is good?  If no number is good, output `0`.

Here, `fronts[i]` and `backs[i]` represent the number on the front and
back of card `i`.

A flip swaps the front and back numbers, so the value on the front is now on the back
and vice versa.

Example:

Input: fronts = [1,2,4,4,7], backs = [1,3,4,1,3]
Output: `2`
Explanation: If we flip the second card, the fronts are `[1,3,4,4,7]` and the backs are `[1,2,4,1,3]`.
We choose the second card, which has number 2 on the back, and it isn't on the front of any card, so `2` is good.

Note:

`1 <= fronts.length == backs.length <= 1000`.

`1 <= fronts[i] <= 2000`.

`1 <= backs[i] <= 2000`.

【中文翻译】
桌上有 `N` 张卡片，每张卡片的正反面各印有一个正整数（可能不同）。

我们可以翻转任意数量的卡片，然后选择一张卡片。

如果所选卡片背面的数字 `X` 不在任何卡片的正面出现，则这个数字 X 是好的。

返回最小的好数字。如果没有好数字，返回 `0`。

其中，`fronts[i]` 和 `backs[i]` 分别表示第 `i` 张卡片的正面和背面数字。

翻转操作交换正反面数字，即正面上的值现在在背面，反之亦然。

示例：
输入：fronts = [1,2,4,4,7], backs = [1,3,4,1,3]
输出：`2`
解释：翻转第二张卡片后，正面为 `[1,3,4,4,7]`，背面为 `[1,2,4,1,3]`。
选择第二张卡片，其背面数字为 2，且不在任何卡片的正面出现，所以 `2` 是好的。

注意：
`1 <= fronts.length == backs.length <= 1000`。
`1 <= fronts[i] <= 2000`。
`1 <= backs[i] <= 2000`。
"""

from typing import List, Optional


class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        # Numbers that appear on both sides of the SAME card can never be good
        same = {fronts[i] for i in range(len(fronts)) if fronts[i] == backs[i]}

        # Among all numbers not in `same`, find the minimum
        ans = float('inf')
        for x in fronts + backs:
            if x not in same and x < ans:
                ans = x

        return ans if ans != float('inf') else 0



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 关键洞察：正反面相同的卡片上的数字永远无法成为好数字。
# 因为无论是否翻转该卡片，该数字始终在正面出现。
#
# 对于其他数字 X（不出现在任何正反面相同的卡片上）：
# - 对于所有正面为 X 的卡片，翻转它们，使 X 移到背面。
# - 对于所有背面为 X 的卡片，不翻转，X 留在背面。
# - 最终 X 只出现在背面，不在任何正面，因此 X 是好的。
#
# 算法：
# 1. 收集所有 fronts[i] == backs[i] 的数字到集合 `same`。
# 2. 遍历 fronts 和 backs 中所有数字，找到不在 `same` 中的最小值。
# 3. 如果没有这样的数字，返回 0。
#
# 时间复杂度: O(N) - 遍历所有卡片
# 空间复杂度: O(N) - 存储 same 集合
#
# 关键点:
# - fronts[i] == backs[i] 的数字无法被隐藏，永远在正面
# - 其他数字都可以通过选择性翻转变为只在背面出现
# - 目标是找到最小值，只需遍历所有数字即可
