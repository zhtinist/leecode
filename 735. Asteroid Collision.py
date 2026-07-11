"""
LeetCode #735 - Asteroid Collision
中文题名：行星碰撞
https://leetcode.com/problems/asteroid-collision/

We are given an array `asteroids` of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its
direction (positive meaning right, negative meaning left). Each asteroid moves at the same
speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller
one will explode. If both are the same size, both will explode. Two asteroids moving in the
same direction will never meet.

Example 1:

Input:
asteroids = [5, 10, -5]
Output: [5, 10]
Explanation:
The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.

Example 2:

Input:
asteroids = [8, -8]
Output: []
Explanation:
The 8 and -8 collide exploding each other.

Example 3:

Input:
asteroids = [10, 2, -5]
Output: [10]
Explanation:
The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.

Example 4:

Input:
asteroids = [-2, -1, 1, 2]
Output: [-2, -1, 1, 2]
Explanation:
The -2 and -1 are moving left, while the 1 and 2 are moving right.
Asteroids moving the same direction never meet, so no asteroids will meet each other.

Note:

The length of `asteroids` will be at most `10000`.

Each asteroid will be a non-zero integer in the range `[-1000, 1000].`.

【中文翻译】
给定一个整数数组 asteroids，表示在同一行的行星。

对于数组中的每一个元素，其绝对值表示行星的大小，正负表示行星的移动方向（正表示向右移动，负表示向左移动）。每一颗行星以相同的速度移动。

找出碰撞后剩下的所有行星。碰撞规则：两个行星相互碰撞，较小的行星会爆炸。如果两颗行星大小相同，则两颗行星都会爆炸。两颗移动方向相同的行星，永远不会发生碰撞。

示例 1：

输入：
asteroids = [5, 10, -5]
输出：[5, 10]
解释：
10 和 -5 碰撞后只剩下 10。5 和 10 永远不会发生碰撞。

示例 2：

输入：
asteroids = [8, -8]
输出：[]
解释：
8 和 -8 碰撞后，两者都发生爆炸。

示例 3：

输入：
asteroids = [10, 2, -5]
输出：[10]
解释：
2 和 -5 碰撞后剩下 -5。10 和 -5 碰撞剩下 10。

示例 4：

输入：
asteroids = [-2, -1, 1, 2]
输出：[-2, -1, 1, 2]
解释：
-2 和 -1 向左移动，而 1 和 2 向右移动。
由于移动方向相同的行星永远不会发生碰撞，所以不会有行星碰撞。

注意：

数组 asteroids 的长度不超过 10000。

每一颗行星都是非零整数，范围是 [-1000, 1000]。
"""

from typing import List, Optional


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                if stack[-1] < -a:
                    stack.pop()
                    continue
                elif stack[-1] == -a:
                    stack.pop()
                break
            else:
                stack.append(a)
        return stack










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 栈模拟碰撞过程：
# 1. 使用栈存储存活的行星，遍历每个行星。
# 2. 碰撞仅发生在：当前行星向左（a < 0）且栈顶向右（stack[-1] > 0）。
#    - 若栈顶较小（stack[-1] < -a）：栈顶爆炸，继续循环。
#    - 若栈顶相等（stack[-1] == -a）：两者都爆炸（弹出栈顶，break）。
#    - 若栈顶较大（stack[-1] > -a）：当前行星爆炸（break，不入栈）。
# 3. 若未触发碰撞（同向或空栈），将当前行星入栈。
# 4. 最终栈中剩余行星即为结果。
# 利用 Python 的 for...else 语法：当 while 循环未被 break 中断时执行 else。
#
# 时间复杂度: O(n)，每个元素最多入栈和出栈一次
# 空间复杂度: O(n)，栈存储最终结果
#
# 关键点:
# - 碰撞条件：栈顶 > 0 且当前 < 0（方向相对）
# - 同向不碰撞：正正、负负、负正均安全
# - 当前行星可能连续撞爆多个栈顶行星
# - 使用 for...else 优雅处理"碰撞后不入栈 vs 正常入栈"
