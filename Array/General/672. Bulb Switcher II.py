"""
LeetCode #672 - Bulb Switcher II
中文题名：灯泡开关 II
https://leetcode.com/problems/bulb-switcher-ii/

There is a room with `n` lights which are turned on initially and 4 buttons on the
wall. After performing exactly `m` unknown operations towards buttons, you need
to return how many different kinds of status of the `n` lights could be.

Suppose `n` lights are labeled as number [1, 2, 3 ..., n], function of these 4
buttons are given below:

Flip all the lights.

Flip lights with even numbers.

Flip lights with odd numbers.

Flip lights with (3k + 1) numbers, k = 0, 1, 2, ...

Example 1:

Input: n = 1, m = 1.
Output: 2
Explanation: Status can be: [on], [off]

Example 2:

Input: n = 2, m = 1.
Output: 3
Explanation: Status can be: [on, off], [off, on], [off, off]

Example 3:

Input: n = 3, m = 1.
Output: 4
Explanation: Status can be: [off, on, off], [on, off, on], [off, off, off], [off, on, on].

Note: `n` and `m` both fit in range [0, 1000].

【中文翻译】
有一个房间，里面有 `n` 盏初始时全部打开的灯，墙上还有 4 个按钮。在执行了恰好 `m` 次未知的按钮操作后，你需要返回这 `n` 盏灯可能有多少种不同的状态。

假设 `n` 盏灯编号为 [1, 2, 3, ..., n]，这 4 个按钮的功能如下：

1. 翻转所有灯的状态。
2. 翻转编号为偶数的灯的状态。
3. 翻转编号为奇数的灯的状态。
4. 翻转编号为 (3k + 1) 的灯的状态，k = 0, 1, 2, ...

示例 1：

输入：n = 1，m = 1
输出：2
解释：可能的状态有：[on]，[off]

示例 2：

输入：n = 2，m = 1
输出：3
解释：可能的状态有：[on, off]，[off, on]，[off, off]

示例 3：

输入：n = 3，m = 1
输出：4
解释：可能的状态有：[off, on, off]，[on, off, on]，[off, off, off]，[off, on, on]。

注意：`n` 和 `m` 均在 [0, 1000] 范围内。
"""

from typing import List, Optional


class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        n = min(n, 3)

        if presses == 0:
            return 1
        if presses == 1:
            return [2, 3, 4][n - 1] if n <= 3 else 4
        if presses == 2:
            return [2, 4, 7][n - 1] if n <= 3 else 7

        return [2, 4, 8][n - 1] if n <= 3 else 8











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 这是一道数学推理题，通过分析4个按钮的作用来枚举所有可能状态。
#
# 关键观察：
# 1. 灯的状态只取决于前3盏灯（n>3 时，后续灯的状态由前3盏确定）
#    因为操作2（偶数）和操作3（奇数）的周期为2，操作4（3k+1）的周期为3
#    任何 n>3 的灯的状态都可由前3盏灯的状态推导出来
# 2. 因此只需考虑 n = min(n, 3)
# 3. 4个操作实际上重复：操作1=操作2+操作3，且每个按钮按两次等于没按
#    所以有效操作次数 m = min(presses, 3)（超过3次后状态会重复）
#
# 枚举所有 (n, m) 组合：
# - n=1: m=0→1, m=1→2, m=2→2, m>=3→2
# - n=2: m=0→1, m=1→3, m=2→4, m>=3→4
# - n=3: m=0→1, m=1→4, m=2→7, m>=3→8
# - n>3: m=0→1, m=1→4, m=2→7, m>=3→8
#
# 时间复杂度: O(1) - 常数时间
# 空间复杂度: O(1) - 常数空间
#
# 关键点:
# - 核心洞察：n>3 的灯的状态由前 3 盏决定（周期性）
# - 按钮操作的对称性：按两次等于没按，所以 m>3 简化为 m=3
# - 手动枚举所有 (n<=3) x (m<=3) 的组合即可得出答案
# - 这是典型找规律题，不是模拟题
