"""
LeetCode #838 - Push Dominoes
中文题名：推多米诺
https://leetcode.com/problems/push-dominoes/

There are `N` dominoes in a line, and we place
each domino vertically upright.

In the beginning, we simultaneously push some of the dominoes either to the left or to
the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the
left.

Similarly, the dominoes falling to the right push their adjacent dominoes standing on the
right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the
balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no
additional force to a falling or already fallen domino.

Given a string "S" representing the initial state. `S[i] =
'L'`, if the i-th domino has been pushed to the left; `S[i] =
'R'`, if the i-th domino has been pushed to the right; `S[i] = '.'`, if
the `i`-th domino has not been pushed.

Return a string representing the final state.

Example 1:

Input: ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."

Example 2:

Input: "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.

Note:

`0 <= N <= 10^5`

String `dominoes` contains only `'L`', `'R'`
and `'.'`

【中文翻译】
一行中有 `N` 个多米诺骨牌，我们将每个骨牌垂直竖立。

一开始，我们同时将其中一些骨牌向左或向右推。

每过一秒，每个向左倒的骨牌会推动其左侧相邻的骨牌。

类似地，向右倒的骨牌会推动其右侧竖立的相邻骨牌。

当一个垂直的骨牌同时受到来自两侧倒向它的骨牌推动时，由于力的平衡，它会保持竖立。

就本题而言，我们假设正在倒下的骨牌不会对已经倒下或正在倒下的骨牌施加额外的力。

给定一个表示初始状态的字符串 "S"。`S[i] = 'L'` 表示第 i 个骨牌被推向左侧；`S[i] = 'R'` 表示第 i 个骨牌被推向右侧；`S[i] = '.'` 表示第 i 个骨牌没有被推。

返回表示最终状态的字符串。

示例 1：

输入：".L.R...LR..L.."
输出："LL.RR.LLRRLL.."

示例 2：

输入："RR.L"
输出："RR.L"
解释：第一张骨牌不会给第二张骨牌施加额外的力。

注意：

`0 <= N <= 10^5`

字符串 `dominoes` 只包含 `'L'`、`'R'` 和 `'.'`

"""

from typing import List, Optional


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        # Force from left-to-right (R pushes)
        forces = [0] * n
        force = 0
        for i in range(n):
            if dominoes[i] == 'R':
                force = n  # strong force
            elif dominoes[i] == 'L':
                force = 0
            else:  # '.'
                force = max(force - 1, 0)
            forces[i] += force

        # Force from right-to-left (L pushes)
        force = 0
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                force = n
            elif dominoes[i] == 'R':
                force = 0
            else:  # '.'
                force = max(force - 1, 0)
            forces[i] -= force

        # Build result based on net force
        result = []
        for f in forces:
            if f > 0:
                result.append('R')
            elif f < 0:
                result.append('L')
            else:
                result.append('.')

        return ''.join(result)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 两次扫描（力的传播思想）。
# 1. 从左到右扫描：遇到 'R' 时设置正向强推力，向右递减传播。
#    遇到 'L' 时力归零。记录每个位置受到的向右推力。
# 2. 从右到左扫描：遇到 'L' 时设置反向强推力，向左递减传播。
#    遇到 'R' 时力归零。记录每个位置受到的向左推力（用负数表示）。
# 3. 最终状态由净力决定：
#    - 净力 > 0 → 向右倒 'R'
#    - 净力 < 0 → 向左倒 'L'
#    - 净力 = 0 → 保持竖立 '.'
#    当左右力相等时，净力为 0，骨牌保持竖立（力的平衡）。
#
# 时间复杂度: O(n) — 两次线性扫描
# 空间复杂度: O(n) — forces 数组存储每个位置的受力
#
# 关键点:
# - 用递减的力值模拟力的传播：越远离力源，力越弱
# - 当左右力相遇且相等时，净力为 0，骨牌保持竖立
# - 使用足够大的初始力值（如 n）确保传播足够远
# - 两次相反方向的扫描巧妙处理了 R 和 L 的交叉影响
