"""
LeetCode #1041 - Robot Bounded In Circle
中文题名：困于环中的机器人
https://leetcode.com/problems/robot-bounded-in-circle/

On an infinite plane, a robot initially stands at `(0, 0)` and faces north.  The
robot can receive one of three instructions:

`"G"`: go straight 1 unit;

`"L"`: turn 90 degrees to the left;

`"R"`: turn 90 degress to the right.

The robot performs the `instructions` given in order, and repeats them forever.

Return `true` if and only if there exists a circle in the plane such that the
robot never leaves the circle.

Example 1:

Input: "GGLLGG"
Output: true
Explanation:
The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.

Example 2:

Input: "GG"
Output: false
Explanation:
The robot moves north indefinitely.

Example 3:

Input: "GL"
Output: true
Explanation:
The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...

Note:

`1 <= instructions.length <= 100`

`instructions[i]` is in `{'G', 'L', 'R'}`

【中文翻译】
在无限平面上，一个机器人最初位于 (0, 0)，面朝北方。机器人可以接受以下三种指令之一：

"G"：直线前进 1 个单位；
"L"：向左转 90 度；
"R"：向右转 90 度。

机器人按顺序执行给定的指令，并永远重复执行。

当且仅当平面上存在一个圆使得机器人永远不会离开该圆时，返回 true。

示例 1：

输入："GGLLGG"
输出：true
解释：
机器人从 (0,0) 移动到 (0,2)，转 180 度，然后返回 (0,0)。
当重复这些指令时，机器人保持在以原点为中心、半径为 2 的圆内。

示例 2：

输入："GG"
输出：false
解释：
机器人无限地向北移动。

示例 3：

输入："GL"
输出：true
解释：
机器人从 (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...

注意：

1 <= instructions.length <= 100
instructions[i] 属于 {'G', 'L', 'R'}
"""

from typing import List, Optional


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # Directions: 0=north, 1=east, 2=south, 3=west
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x = y = 0
        d = 0  # facing north

        for ch in instructions:
            if ch == 'G':
                x += dirs[d][0]
                y += dirs[d][1]
            elif ch == 'L':
                d = (d + 3) % 4  # turn left (equivalent to -1 mod 4)
            elif ch == 'R':
                d = (d + 1) % 4  # turn right

        # Robot is bounded in a circle if:
        # 1. It returns to (0,0) after one cycle, OR
        # 2. It does NOT face north after one cycle
        return (x == 0 and y == 0) or d != 0










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 模拟机器人执行一轮指令。关键在于：如果一轮指令执行完毕后：
# 1. 机器人回到原点 (0,0)：无论面朝何方，都会循环回到原点，形成环。
# 2. 机器人不在原点但面朝方向不再是北方（初始方向）：经过最多4轮指令后，
#    机器人一定会回到原点。因为方向变化可以分解为旋转，每轮都旋转一定角度，
#    经过有限轮后方向向量总和为零。
# 3. 如果机器人不在原点且面朝北方：意味着每轮都在同一方向上移动，无法形成环。
# 因此返回条件为：(x==0 and y==0) or d != 0。
#
# 时间复杂度: O(N) - 遍历一次指令
# 空间复杂度: O(1) - 常量空间
#
# 关键点:
# - 核心逻辑：一轮后要么回到原点，要么方向改变
# - 如果方向改变，最多4轮必然回到原点
# - 使用 (dx, dy) 数组表示四个方向
