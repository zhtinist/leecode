"""
LeetCode #2211 - Count Collisions on a Road
统计道路上的碰撞次数
https://leetcode.cn/problems/count-collisions-on-a-road/

在一条无限长的公路上有 `n` 辆汽车正在行驶。汽车按从左到右的顺序按从 `0` 到 `n - 1` 编号，每辆车都在一个 独特的 位置。
给你一个下标从 0 开始的字符串 `directions` ，长度为 `n` 。`directions[i]` 可以是 `'L'`、`'R'` 或 `'S'` 分别表示第 `i` 辆车是向 左 、向 右 或者 停留 在当前位置。每辆车移动时 速度相同 。
碰撞次数可以按下述方式计算：
当两辆移动方向 相反 的车相撞时，碰撞次数加 `2` 。
当一辆移动的车和一辆静止的车相撞时，碰撞次数加 `1` 。
碰撞发生后，涉及的车辆将无法继续移动并停留在碰撞位置。除此之外，汽车不能改变它们的状态或移动方向。
返回在这条道路上发生的 碰撞总次数 。

示例 1：
输入：directions = "RLRSLL" 输出：5 解释： 将会在道路上发生的碰撞列出如下： - 车 0 和车 1 会互相碰撞。由于它们按相反方向移动，碰撞数量变为 0 + 2 = 2 。 - 车 2 和车 3 会互相碰撞。由于 3 是静止的，碰撞数量变为 2 + 1 = 3 。 - 车 3 和车 4 会互相碰撞。由于 3 是静止的，碰撞数量变为 3 + 1 = 4 。 - 车 4 和车 5 会互相碰撞。在车 4 和车 3 碰撞之后，车 4 会待在碰撞位置，接着和车 5 碰撞。碰撞数量变为 4 + 1 = 5 。 因此，将会在道路上发生的碰撞总次数是 5 。
示例 2：
输入：directions = "LLRR" 输出：0 解释： 不存在会发生碰撞的车辆。因此，将会在道路上发生的碰撞总次数是 0 。

提示：
`1 <= directions.length <= 10^5`
`directions[i]` 的值为 `'L'`、`'R'` 或 `'S'`
"""

from typing import List, Optional


class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)
        s = list(directions)

        left = 0
        right = n - 1

        # Remove prefix 'L' cars: they drive left and have nothing
        # to their left to collide with, so they never collide
        while left < n and s[left] == 'L':
            left += 1

        # Remove suffix 'R' cars: they drive right and have nothing
        # to their right to collide with, so they never collide
        while right >= 0 and s[right] == 'R':
            right -= 1

        # All remaining cars in [left, right] must collide.
        # Count cars that are not stationary ('S') — each contributes
        # 1 collision (either a moving-vs-stationary hit = 1, or half
        # of a moving-vs-moving hit = 1 out of the 2 counted).
        collisions = 0
        for i in range(left, right + 1):
            if s[i] != 'S':
                collisions += 1

        return collisions


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Stack, String, Simulation
#
# 解题思路:
# 1. 关键观察：最左侧连续向左行驶的车（'L'）永远不会发生碰撞，
#    因为它们的左侧没有任何车辆。同样，最右侧连续向右行驶的车（'R'）
#    也永远不会发生碰撞，因为它们的右侧没有任何车辆。
# 2. 去掉这些"安全"的车之后，剩余的中间部分中的所有非静止车辆必然会发生碰撞：
#    - 向右的车（'R'）迟早会遇到右侧的向左的车或静止的车。
#    - 向左的车（'L'）迟早会遇到左侧的向右的车或静止的车。
#    - 每次碰撞后，参与的车辆都变为静止（'S'），继续作为障碍物。
# 3. 每辆非静止的车都会贡献恰好 1 次碰撞计数：
#    - R 撞 L：两车各计 1 次（共 2 次）。
#    - R/L 撞 S：移动的车计 1 次。
#    因此，中间部分非 'S' 的车的数量就是碰撞总次数。
#
# 时间复杂度: O(N)，其中 N 为 directions 的长度。只需三次线性扫描（去前缀、去后缀、计数）。
# 空间复杂度: O(N) 或 O(1)。此处 O(N) 是因为转换为了列表，
#             也可以直接用字符串索引实现 O(1) 额外空间。
#
# 关键点:
# - 核心洞察：只有中间段的车会碰撞，头和尾的安全车可以直接忽略。
# - 每辆非静止的车恰好贡献一次碰撞（无论与移动车还是静止车相撞）。
# - 不需要模拟整个碰撞过程，直接统计即可。
