"""
LeetCode #874 - Walking Robot Simulation
中文题名：模拟行走机器人
https://leetcode.com/problems/walking-robot-simulation/

A robot on an infinite grid starts at point (0, 0) and faces north.  The robot can
receive one of three possible types of commands:

`-2`: turn left 90 degrees

`-1`: turn right 90 degrees

`1 <= x <= 9`: move forward `x` units

Some of the grid squares are obstacles.

The `i`-th obstacle is at grid point `(obstacles[i][0],
obstacles[i][1])`

If the robot would try to move onto them, the robot stays on the previous grid square instead
(but still continues following the rest of the route.)

Return the square of the maximum Euclidean distance that the robot will be
from the origin.

Example 1:

Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: robot will go to (3, 4)

Example 2:

Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation: robot will be stuck at (1, 4) before turning left and going to (1, 8)

【中文翻译】
机器人在一个无限大小的网格上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令：
-2：向左转 90 度；
-1：向右转 90 度；
1 <= x <= 9：向前移动 x 个单位长度。
网格上有一些格子被视为障碍物。第 i 个障碍物位于网格点 (obstacles[i][0], obstacles[i][1])。
如果机器人试图走到障碍物上方，它将停留在该障碍物前一个网格方块上（但仍会继续遵循路线的其余部分）。
返回机器人到原点的最大欧氏距离的平方。

"""

from typing import List, Optional


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # 方向数组：北、东、南、西 (按顺时针)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # 初始方向索引：0 = 北
        dir_idx = 0
        x, y = 0, 0
        max_dist_sq = 0

        # 将障碍物转为 set of tuples 以便 O(1) 查找
        obstacle_set = set(map(tuple, obstacles))

        for cmd in commands:
            if cmd == -2:
                # 左转 90 度 = 逆时针
                dir_idx = (dir_idx - 1) % 4
            elif cmd == -1:
                # 右转 90 度 = 顺时针
                dir_idx = (dir_idx + 1) % 4
            else:
                # 向前移动 cmd 步，每次一步检测障碍物
                dx, dy = directions[dir_idx]
                for _ in range(cmd):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in obstacle_set:
                        break  # 遇到障碍物，停止前进
                    x, y = nx, ny
                    max_dist_sq = max(max_dist_sq, x * x + y * y)

        return max_dist_sq



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 模拟题。用方向数组表示北(0,1)、东(1,0)、南(0,-1)、西(-1,0) 四个方向，
# 用一个索引 dir_idx 追踪当前朝向。遇到 -2 时逆时针旋转（索引 -1 模 4），
# 遇到 -1 时顺时针旋转（索引 +1 模 4）。遇到前进命令时，一步一步移动，
# 每步检查是否会撞上障碍物——如果会，则停止该命令的剩余步数。
# 每移动一步后更新最大距离平方。
#
# 时间复杂度: O(N + K)，其中 N 是命令数，K 是障碍物总数。每个障碍物存入 set O(K)，
# 所有命令的总前进步数为 O(9N) = O(N)
# 空间复杂度: O(K)，存储障碍物集合
#
# 关键点:
# - 方向数组 + 索引法处理转向，避免 if-elif 分支
# - 障碍物用 set 存储，O(1) 查找
# - 必须每步检测障碍物，不能一次跳 cmd 步
