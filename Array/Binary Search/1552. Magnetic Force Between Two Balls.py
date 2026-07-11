"""
LeetCode #1552 - Magnetic Force Between Two Balls
中文题名：两球之间的磁力
https://leetcode.com/problems/magnetic-force-between-two-balls/


In universe Earth C-137, Rick discovered a special form of magnetic force
between two balls if they are put in his new invented basket. Rick
has `n` empty baskets, the `ith` basket is at
`position[i]`, Morty has `m` balls and needs to distribute the
balls into the baskets such that the minimum magnetic force between
any two balls is maximum.

Rick stated that magnetic force between two different balls at positions
`x` and `y` is `|x - y|`.

Given the integer array `position` and the integer `m`.
Return the required force.

Example 1:

Input: position = [1,2,3,4,7], m = 3
Output: 3
Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.

Example 2:

Input: position = [5,4,3,2,1,1000000000], m = 2
Output: 999999999
Explanation: We can use baskets 1 and 1000000000.

Constraints:

`n == position.length`

`2 <= n <= 10^5`

`1 <= position[i] <= 10^9`

All integers in `position` are distinct.

`2 <= m <= position.length`

【中文翻译】
Rick 有 n 个空篮子，第 i 个篮子在 position[i] 处。Morty 有 m 个球，需要分配到篮子中，
使得任意两球之间的最小磁力最大化。两个分别在位置 x 和 y 的球之间的磁力为 |x - y|。
返回所需的磁力。

示例 1：
输入：position = [1,2,3,4,7], m = 3
输出：3
解释：将球放入篮子 1、4、7，磁力对为 [3,3,6]，最小值为 3。

示例 2：
输入：position = [5,4,3,2,1,1000000000], m = 2
输出：999999999
"""

from typing import List, Optional


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def can_place(min_dist: int) -> bool:
            count = 1
            last_pos = position[0]
            for i in range(1, len(position)):
                if position[i] - last_pos >= min_dist:
                    count += 1
                    last_pos = position[i]
                    if count >= m:
                        return True
            return False

        lo, hi = 1, position[-1] - position[0]
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can_place(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 二分答案。对最小磁力进行二分搜索。对于给定的最小距离 d，
# 贪心检查是否可以放置 m 个球（排序后，尽可能早地放置每个球）。
# 如果 can_place(mid) 为真，说明可以尝试更大的最小距离。
# 使用 upper-bound 二分（mid = (lo+hi+1)//2）。
#
# 时间复杂度: O(N log M) — M 为最大距离
# 空间复杂度: O(1) — 忽略排序空间
#
# 关键点:
# - 最大化最小值问题，典型的二分答案
# - 检查函数贪心放置：每个球放在离上一个球至少 d 的最早位置
# - 排序后贪心是最优的












