"""
LeetCode #2086 - Minimum Number of Food Buckets to Feed the Hamsters
喂食仓鼠的最小食物桶数
https://leetcode.cn/problems/minimum-number-of-food-buckets-to-feed-the-hamsters/

给你一个下标从 0 开始的字符串 `hamsters` ，其中 `hamsters[i]`  要么是：
`'H'` 表示有一个仓鼠在下标 `i` ，或者
`'.'` 表示下标 `i` 是空的。
你将要在空的位置上添加一定数量的食物桶来喂养仓鼠。如果仓鼠的左边或右边至少有一个食物桶，就可以喂食它。更正式地说，如果你在位置 `i - 1` 或者 `i + 1` 放置一个食物桶，就可以喂养位置为 `i` 处的仓鼠。
在 空的位置 放置食物桶以喂养所有仓鼠的前提下，请你返回需要的 最少 食物桶数。如果无解请返回 `-1` 。

示例 1：

输入：hamsters = "H..H" 输出：2 解释： 我们可以在下标为 1 和 2 处放食物桶。 可以发现如果我们只放置 1 个食物桶，其中一只仓鼠将得不到喂养。
示例 2：

输入：street = ".H.H." 输出：1 解释： 我们可以在下标为 2 处放置一个食物桶。
示例 3：
输入：street = ".HHH." 输出：-1 解释： 如果我们如图那样在每个空位放置食物桶，下标 2 处的仓鼠将吃不到食物。

提示：
`1 <= hamsters.length <= 10^5`
`hamsters[i]` 要么是 `'H'` ，要么是 `'.'` 。
"""

from typing import List, Optional


class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        n = len(hamsters)
        s = list(hamsters)
        buckets = 0

        for i in range(n):
            if s[i] == 'H':
                # First check if already fed by a bucket on left or right
                if (i - 1 >= 0 and s[i - 1] == 'B') or (i + 1 < n and s[i + 1] == 'B'):
                    continue
                # Prefer to place bucket on the right (can potentially feed next hamster too)
                if i + 1 < n and s[i + 1] == '.':
                    buckets += 1
                    s[i + 1] = 'B'
                elif i - 1 >= 0 and s[i - 1] == '.':
                    buckets += 1
                    s[i - 1] = 'B'
                else:
                    return -1
        return buckets



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, String, Dynamic Programming
#
# 解题思路:
# 贪心策略：从左到右遍历，遇到仓鼠'H'时，优先将食物桶放在右边（因为放在右边
# 还可能喂养右边的下一只仓鼠，更优）。如果右边不能放则放左边。
# 如果两边都不能放且左右也没有已有的食物桶，则返回-1（无解）。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n) 或 O(1)（可直接在字符串上修改）
#
# 关键点:
# - 贪心：优先放右边
# - 右边可能同时喂养当前仓鼠和下一只
# - 无解：两个相邻仓鼠且中间没有空位
