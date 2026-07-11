"""
LeetCode #1503 - Last Moment Before All Ants Fall Out of a Plank
中文题名：所有蚂蚁掉下来前的最后一刻
https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/

We have a wooden plank of the length `n` units.
Some ants are walking on the plank, each ant moves with speed 1 unit per
second. Some of the ants move to the left, the other move
to the right.

When two ants moving in two different directions meet at some point,
they change their directions and continue moving again. Assume changing directions
doesn't take any additional time.

When an ant reaches one end of the plank at a time `t`,
it falls out of the plank imediately.

Given an integer `n` and two integer arrays `left` and `right`,
the positions of the ants moving to the left and the right. Return the moment
when the last ant(s) fall out of the plank.

Example 1:

Input: n = 4, left = [4,3], right = [0,1]
Output: 4
Explanation: In the image above:
-The ant at index 0 is named A and going to the right.
-The ant at index 1 is named B and going to the right.
-The ant at index 3 is named C and going to the left.
-The ant at index 4 is named D and going to the left.
Note that the last moment when an ant was on the plank is t = 4 second, after that it falls imediately out of the plank. (i.e. We can say that at t = 4.0000000001, there is no ants on the plank).

Example 2:

Input: n = 7, left = [], right = [0,1,2,3,4,5,6,7]
Output: 7
Explanation: All ants are going to the right, the ant at index 0 needs 7 seconds to fall.

Example 3:

Input: n = 7, left = [0,1,2,3,4,5,6,7], right = []
Output: 7
Explanation: All ants are going to the left, the ant at index 7 needs 7 seconds to fall.

Example 4:

Input: n = 9, left = [5], right = [4]
Output: 5
Explanation: At t = 1 second, both ants will be at the same intial position but with different direction.

Example 5:

Input: n = 6, left = [6], right = [0]
Output: 6

Constraints:

`1 <= n <= 10^4`

`0 <= left.length <= n + 1`

`0 <= left[i] <= n`

`0 <= right.length <= n + 1`

`0 <= right[i] <= n`

`1 <= left.length + right.length <= n + 1`

All values of `left` and `right` are unique, and each
value can appear only in one of the two arrays.

【中文翻译】
有一块长度为 n 个单位的木板。一些蚂蚁在木板上移动，每只蚂蚁以每秒 1 个单位的速度移动。
有些蚂蚁向左移动，其他蚂蚁向右移动。

当两只向不同方向移动的蚂蚁在某点相遇时，它们会改变方向并继续移动。
假设改变方向不需要任何额外时间。

当蚂蚁在时间 t 到达木板的一端时，它会立即从木板上掉下来。

给定整数 n 和两个整数数组 left 和 right，分别表示向左和向右移动的蚂蚁的位置。
返回最后一只蚂蚁从木板上掉下来的时刻。

示例 1：

输入：n = 4, left = [4,3], right = [0,1]
输出：4
解释：最后一只蚂蚁在木板上的时刻是 t=4 秒，之后立即掉下。

示例 2：

输入：n = 7, left = [], right = [0,1,2,3,4,5,6,7]
输出：7
解释：所有蚂蚁向右移动，索引 0 处的蚂蚁需要 7 秒才能掉下来。

示例 3：

输入：n = 7, left = [0,1,2,3,4,5,6,7], right = []
输出：7
解释：所有蚂蚁向左移动，索引 7 处的蚂蚁需要 7 秒才能掉下来。

示例 4：

输入：n = 9, left = [5], right = [4]
输出：5

示例 5：

输入：n = 6, left = [6], right = [0]
输出：6
"""

from typing import List, Optional


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        # Ants meeting and changing direction = ants passing through each other
        # Left-moving ants fall after 'pos' seconds
        # Right-moving ants fall after 'n - pos' seconds
        max_time = 0
        for pos in left:
            max_time = max(max_time, pos)
        for pos in right:
            max_time = max(max_time, n - pos)
        return max_time



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 关键洞察：两只蚂蚁相遇后改变方向，等价于两只蚂蚁互相穿过对方继续前进。
# 因此每只蚂蚁只需按原方向走到尽头。向左走的蚂蚁需要 pos 秒到达左端，
# 向右走的蚂蚁需要 n-pos 秒到达右端。答案即为所有蚂蚁所需时间的最大值。
#
# 时间复杂度: O(L + R) — 遍历 left 和 right 数组
# 空间复杂度: O(1)
#
# 关键点:
# - 核心等价转换：相遇掉头 = 互相穿过
# - 无需模拟蚂蚁运动，直接计算每只蚂蚁到边缘的距离
# - 最后一只掉落的蚂蚁 = 距离边缘最远的蚂蚁
