"""
LeetCode #365 - Water and Jug Problem
中文题名：水壶问题
https://leetcode.com/problems/water-and-jug-problem/

You are given two jugs with capacities x and y litres. There is an infinite
amount of water supply available. You need to determine whether it is possible to measure
exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained
within one or both buckets by the end.

Operations allowed:

Fill any of the jugs completely with water.

Empty any of the jugs.

Pour water from one jug into another till the other jug is completely full or the first
jug itself is empty.

Example 1: (From the famous "Die Hard" example)

Input: x = 3, y = 5, z = 4
Output: True

Example 2:

Input: x = 2, y = 6, z = 5
Output: False

【中文翻译】
有两个容量分别为 x 升和 y 升的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z 升的水？

如果可以，最后请用以上水壶中的一或两个来盛放取得的 z 升水。

你允许：
- 装满任意一个水壶
- 清空任意一个水壶
- 从一个水壶向另外一个水壶倒水，直到装满或者倒空

示例 1：（来自著名的 "Die Hard" 例子）

输入：x = 3, y = 5, z = 4
输出：True

示例 2：

输入：x = 2, y = 6, z = 5
输出：False
"""

from typing import List, Optional


class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        import math
        # 边界情况：目标水量超过两壶容量之和，不可能实现
        if target > x + y:
            return False
        # 目标为 0，始终可以实现（不操作即可）
        if target == 0:
            return True
        # 根据裴蜀定理，可量出的水量必须是 gcd(x, y) 的倍数
        return target % math.gcd(x, y) == 0










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 问题转化为：是否存在整数 a, b 使得 a*x + b*y = target。
# 根据裴蜀定理（Bezout's Identity）：对于非零整数 x, y，ax + by 能表示的所有整数恰好是 gcd(x, y) 的整数倍。
# 因此 target 能被量出的充要条件是：
# 1. target <= x + y（水量不能超过两个水壶的总容量）
# 2. target % gcd(x, y) == 0（target 是最大公约数的倍数）
# 特殊情况：target = 0 始终可以实现。
# 另一种解法是 BFS，模拟所有可能的倒水操作，但数学解法更高效 O(log min(x, y))。
#
# 时间复杂度: O(log min(x, y)) - 计算最大公约数的时间
# 空间复杂度: O(1) - 仅常数变量
#
# 关键点:
# - 裴蜀定理是本题的数学核心：ax + by 的所有整数值恰好是 gcd(x, y) 的整数倍
# - target > x + y 时直接返回 False（容量不足）
# - 自动倒水过程本质上是线性组合的构造
# - BFS 解法也可以 AC，但时间复杂度更高
