"""
LeetCode #478 - Generate Random Point in a Circle
中文题名：在圆内随机生成点
https://leetcode.com/problems/generate-random-point-in-a-circle/

Given the radius and x-y positions of the center of a circle, write a function `randPoint` which generates
a uniform random point in the circle.

Note:

input and output values are in floating-point.

radius and x-y position of the center of the circle is passed into the class
constructor.

a point on the circumference of the circle is considered to be in the circle.

`randPoint` returns a size 2 array containing x-position and
y-position of the random point, in that order.

Example 1:

Input:
["Solution","randPoint","randPoint","randPoint"]
[[1,0,0],[],[],[]]
Output: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]

Example 2:

Input:
["Solution","randPoint","randPoint","randPoint"]
[[10,5,-7.5],[],[],[]]
Output: [null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]

【中文翻译】
给定圆的半径和圆心坐标 (x, y)，编写一个函数 randPoint，在圆内均匀随机生成一个点。

注意：
    输入和输出值均为浮点数。
    圆的半径和圆心坐标通过类构造函数传入。
    圆周上的点也被认为在圆内。
    randPoint 返回一个长度为 2 的数组，按顺序包含随机点的 x 坐标和 y 坐标。

示例 1：
    输入：["Solution","randPoint","randPoint","randPoint"]
         [[1,0,0],[],[],[]]
    输出：[null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]

示例 2：
    输入：["Solution","randPoint","randPoint","randPoint"]
         [[10,5,-7.5],[],[],[]]
    输出：[null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]
"""

from typing import List, Optional
import random
import math


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        # Uniform distribution in a circle:
        # - Angle theta: uniform in [0, 2*pi)
        # - Radius r: use sqrt(random()) to account for area scaling
        #   (area grows with r^2, so larger r should be more likely)
        theta = random.uniform(0, 2 * math.pi)
        r = self.radius * math.sqrt(random.uniform(0, 1))

        x = self.x_center + r * math.cos(theta)
        y = self.y_center + r * math.sin(theta)
        return [x, y]



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 要在圆内生成均匀分布的点，不能简单地均匀取半径 r 和角度 theta，因为面积与 r^2 成正比——
# 如果 r 均匀分布，靠近圆心的点会过多。正确做法：角度 theta 在 [0, 2π) 内均匀分布，
# 而半径 r = radius * sqrt(random())，利用平方根变换使得面积上的分布均匀。
# 最终 x = x_center + r * cos(theta)，y = y_center + r * sin(theta)。
#
# 时间复杂度: O(1) — 每次调用 randPoint 执行常数次运算
# 空间复杂度: O(1) — 仅使用常数额外空间
#
# 关键点:
# - 拒绝采样法也可行（在正方形内随机取点，检查是否在圆内），但效率较低
# - 正确做法必须对半径取平方根：r = radius * sqrt(random())
# - 角度 theta 直接用 uniform(0, 2π) 即可，因圆的旋转对称性
