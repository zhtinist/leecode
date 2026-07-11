"""
LeetCode #2337 - Move Pieces to Obtain a String
移动片段得到字符串
https://leetcode.cn/problems/move-pieces-to-obtain-a-string/

给你两个字符串 `start` 和 `target` ，长度均为 `n` 。每个字符串 仅 由字符 `'L'`、`'R'` 和 `'_'` 组成，其中：
字符 `'L'` 和 `'R'` 表示片段，其中片段 `'L'` 只有在其左侧直接存在一个 空位 时才能向 左 移动，而片段 `'R'` 只有在其右侧直接存在一个 空位 时才能向 右 移动。
字符 `'_'` 表示可以被 任意 `'L'` 或 `'R'` 片段占据的空位。
如果在移动字符串 `start` 中的片段任意次之后可以得到字符串 `target` ，返回 `true` ；否则，返回 `false` 。

示例 1：
输入：start = "_L__R__R_", target = "L______RR" 输出：true 解释：可以从字符串 start 获得 target ，需要进行下面的移动： - 将第一个片段向左移动一步，字符串现在变为 "L___R__R_" 。 - 将最后一个片段向右移动一步，字符串现在变为 "L___R___R" 。 - 将第二个片段向右移动三步，字符串现在变为 "L______RR" 。 可以从字符串 start 得到 target ，所以返回 true 。
示例 2：
输入：start = "R_L_", target = "__LR" 输出：false 解释：字符串 start 中的 'R' 片段可以向右移动一步得到 "_RL_" 。 但是，在这一步之后，不存在可以移动的片段，所以无法从字符串 start 得到 target 。
示例 3：
输入：start = "_R", target = "R_" 输出：false 解释：字符串 start 中的片段只能向右移动，所以无法从字符串 start 得到 target 。

提示：
`n == start.length == target.length`
`1 <= n <= 10^5`
`start` 和 `target` 由字符 `'L'`、`'R'` 和 `'_'` 组成
"""

from typing import List, Optional


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        """
        Key observations:
        1. 'L' can only move LEFT into empty spaces '_'.
        2. 'R' can only move RIGHT into empty spaces '_'.
        3. Pieces cannot cross each other — the relative order of L and R
           must be identical in start and target (ignoring underscores).

        Approach: two pointers scan both strings skipping underscores.
        For each matched piece, verify the movement direction constraint.
        """
        n = len(start)
        i = 0  # pointer for start
        j = 0  # pointer for target

        while i < n or j < n:
            # Skip leading underscores
            while i < n and start[i] == '_':
                i += 1
            while j < n and target[j] == '_':
                j += 1

            # If both exhausted, success
            if i == n and j == n:
                return True
            # If only one exhausted, mismatch
            if i == n or j == n:
                return False

            # Characters must match (both 'L' or both 'R')
            if start[i] != target[j]:
                return False

            # 'L' can only move left: start position must be >= target position
            if start[i] == 'L' and i < j:
                return False

            # 'R' can only move right: start position must be <= target position
            if start[i] == 'R' and i > j:
                return False

            i += 1
            j += 1

        return True



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Two Pointers, String
#
# 解题思路:
# 1. 关键约束分析：
#    - 'L' 只能向左移动（移动到空位 '_'）
#    - 'R' 只能向右移动
#    - 'L' 和 'R' 不能互相穿越，因此去掉所有 '_' 后两者的相对顺序必须相同
# 2. 使用双指针分别遍历 start 和 target，跳过 '_'：
#    - 比较当前非 '_' 字符是否相同，不同则无法转换
#    - 对于 'L'：start 中的位置必须 >= target 中的位置（因为只能左移）
#    - 对于 'R'：start 中的位置必须 <= target 中的位置（因为只能右移）
#    - 若任一条件不满足则返回 False
# 3. 两个指针都到达末尾则转换成功。
#
# 时间复杂度: O(n) — 每个字符最多被访问一次
# 空间复杂度: O(1) — 仅使用常数额外空间
#
# 关键点:
# - 忽略 '_' 后，start 和 target 中 'L'/'R' 的相对顺序必须完全一致
# - L 的最终位置不能比初始位置更靠右；R 不能更靠左
# - 空位 '_' 只是移动的媒介，片段本身不改变类型
