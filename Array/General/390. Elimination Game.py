"""
LeetCode #390 - Elimination Game
中文题名：消除游戏
https://leetcode.com/problems/elimination-game/

There is a list of sorted integers from 1 to n. Starting from left to right, remove
the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left, remove the right most
number and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left, until a
single number remains.

Find the last number that remains starting with a list of length n.

Example:

Input:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

Output:
6

【中文翻译】
有一个从 1 到 n 的有序整数列表。从左边到右边，删除第一个数字，然后每隔一个数字删除一个，直到到达列表末尾。

重复上一步，但这次从右到左，从剩余的数字中删除最右边的数字，然后每隔一个数字删除一个。

我们不断重复这些步骤，交替从左到右和从右到左，直到只剩下一个数字。

找出从长度为 n 的列表开始时，最后剩下的数字。

示例：

输入：
n = 9，
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

输出：
6
"""

from typing import List, Optional


class Solution:
    def lastRemaining(self, n: int) -> int:
        head = 1          # 当前轮次的第一个数
        step = 1          # 当前轮次的步长
        left = True       # 是否从左到右
        remaining = n     # 剩余数字个数

        while remaining > 1:
            # 当从左到右，或从右到左且剩余个数为奇数时，head 需要更新
            if left or remaining % 2 == 1:
                head += step
            step *= 2          # 步长翻倍
            remaining //= 2    # 每轮去掉一半
            left = not left    # 方向切换

        return head











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 不需要真的模拟删除过程（那样需要 O(n) 空间），而是追踪"头部数字"的变化。
# 维护四个变量：
# - head: 当前轮次的第一个数字（最终答案就是只剩一个数时的 head）
# - step: 当前轮次相邻数字之间的步长
# - remaining: 当前剩余的数字个数
# - left: 当前是否从左到右消除
# 每轮：
# 1. 如果是从左到右消除，头部一定会被移除，所以 head += step。
# 2. 如果是从右到左消除，只有当剩余数字个数为奇数时，头部才会被移除（因为从右开始，
#    奇数个时头部是"相隔"中被选中的那个），此时 head += step。
# 3. step *= 2（因为每轮之后相邻数字的间隔翻倍）
# 4. remaining //= 2（每次消除一半）
# 5. left = not left（方向切换）
#
# 时间复杂度: O(log n) - 每次 remaining 减半，循环 log n 次
# 空间复杂度: O(1) - 只使用常数个变量
#
# 关键点:
# - 关键洞察：只需追踪头部数字，不需要模拟整个数组
# - 从左到右时 head 必定更新；从右到左时要看剩余个数的奇偶性
# - 步长每轮翻倍（1, 2, 4, 8, ...）
# - 每轮数字个数减半
# - 递归解法：f(n) = 2 * (1 + n/2 - f(n/2)) 当 n>1，也是 O(log n)
