"""
LeetCode #858 - Mirror Reflection
中文题名：镜面反射
https://leetcode.com/problems/mirror-reflection/

There is a special square room with mirrors on each of the four walls.  Except
for the southwest corner, there are receptors on each of the remaining corners,
numbered `0`, `1`, and `2`.

The square room has walls of length `p`, and a laser ray from the southwest corner first
meets the east wall at a distance `q` from the `0`th receptor.

Return the number of the receptor that the ray meets first.  (It is guaranteed that the
ray will meet a receptor eventually.)

Example 1:

Input: p = 2, q = 1
Output: 2
Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.

Note:

`1 <= p <= 1000`

`0 <= q <= p`

【中文翻译】
有一个特殊的正方形房间，四面墙上都有镜子。除了西南角外，其他三个角上各有一个接收器，编号为 0、1 和 2。

正方形房间的墙壁长度为 p，一束激光从西南角射出，首先碰到东墙，距离 0 号接收器 q 处。

返回激光首先遇到的接收器的编号。（保证激光最终一定会遇到一个接收器。）

"""

from typing import List, Optional


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        import math

        g = math.gcd(p, q)
        # Number of horizontal reflections = p/g, vertical = q/g
        # Reduced to the smallest integer ratio
        m = p // g  # number of room lengths traveled vertically
        n = q // g  # number of room lengths traveled horizontally

        # Determine receptor based on parity
        if m % 2 == 0:
            return 2  # m even -> receptor 2 (right wall, bottom corner)
        if n % 2 == 0:
            return 0  # m odd, n even -> receptor 0 (left wall, top corner)
        return 1  # m odd, n odd -> receptor 1 (right wall, top corner)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 将房间展开（镜像反射等价于直线在无限扩展的网格中传播）。
# 光线的路径等价于从 (0,0) 出发，每次横坐标增加 p（到达对面墙），
# 纵坐标增加 q（到达对面墙的反方向位置）。
# 我们需要找到最小的整数 m, n 使得 m*p = n*q（到达某个角落）。
# 即到达角落时，m = q/gcd(p,q)，n = p/gcd(p,q)。
# m 表示垂直方向经过的房间数，n 表示水平方向经过的房间数。
# 奇偶性决定到达哪个接收器：
# - m 为偶数：到达右侧墙壁（接收器 2，因为是下方的右角）
# - m 为奇数且 n 为偶数：到达左侧墙壁上方（接收器 0）
# - m 为奇数且 n 为奇数：到达右侧墙壁上方（接收器 1）
#
# 时间复杂度: O(log(min(p,q))) GCD 计算
# 空间复杂度: O(1)
#
# 关键点:
# - 将镜面反射展开为直线在扩展网格中的传播（折叠房间法）
# - LCM 原理：第一次到达角落时 m*p = n*q = lcm(p,q)
# - 关键是 p/gcd 和 q/gcd 的奇偶性决定了哪个接收器
# - 不需要模拟反射过程，纯数学推导
