"""
LeetCode #754 - Reach a Number
中文题名：到达终点数字
https://leetcode.com/problems/reach-a-number/

You are standing at position `0` on an infinite number line. There is a goal at
position `target`.

On each move, you can either go left or right. During the n-th move (starting from
1), you take n steps.

Return the minimum number of steps required to reach the destination.

Example 1:

Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.

Example 2:

Input: target = 2
Output: 3
Explanation:
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.

Note:

`target` will be a non-zero integer in the range `[-10^9, 10^9]`.

【中文翻译】
在一根无限长的数轴上，你站在 0 的位置。在位置 target 上有一个目标点。

在每一次移动中，你可以向左或向右移动。在第 n 次移动（从 1 开始），你走了 n 步。

返回到达目的地所需的最小移动次数。

示例 1：

输入：target = 3
输出：2
解释：
第一次移动，从 0 到 1。
第二次移动，从 1 到 3。

示例 2：

输入：target = 2
输出：3
解释：
第一次移动，从 0 到 1。
第二次移动，从 1 到 -1。
第三次移动，从 -1 到 2。

注意：

target 是在 [-10^9, 10^9] 范围中的非零整数。
"""

from typing import List, Optional


class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        k = 0
        total = 0
        while total < target:
            k += 1
            total += k
        while (total - target) % 2 != 0:
            k += 1
            total += k
        return k



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 数学解法。由于数轴是对称的，target 的正负不影响步数，先取绝对值。
# 1. 不断累加 k（第 k 步走 k 步），直到总和 total >= target。
# 2. 如果 total == target，直接返回 k。
# 3. 如果 total > target，计算差值 delta = total - target。
#    - 如果 delta 是偶数，说明可以通过将其中某些步反向来抵消差值。
#      例如：target=2, 1+2+3=6, delta=4(偶数), 可以将第1步反向(走-1+2+3=4→不对)
#      实际上需要继续增加步数。
#    - 正确做法：当 total >= target 且 delta 为偶数时，返回 k。
#    - 如果不满足，继续 k += 1, total += k，直到 delta 为偶数。
#
# 时间复杂度: O(sqrt(|target|)) - k 约等于 sqrt(2*target)
# 空间复杂度: O(1)
#
# 关键点:
# - 对称性：正负 target 答案相同，取绝对值
# - 核心数学洞察：溢出的距离 delta 必须为偶数，才能通过翻转某步的方向来抵消
# - 每翻转第 i 步的方向，总和减少 2*i（是偶数）
# - 如果 delta 是奇数，就继续加步数直到 delta 变为偶数
