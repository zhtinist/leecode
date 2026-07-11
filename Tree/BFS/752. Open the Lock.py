"""
LeetCode #752 - Open the Lock
中文题名：打开转盘锁
https://leetcode.com/problems/open-the-lock/

You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: `'0',
'1', '2', '3', '4', '5', '6', '7', '8', '9'`. The wheels can rotate freely and wrap
around: for example we can turn `'9'` to be `'0'`, or `'0'`
to be `'9'`. Each move consists of turning one wheel one slot.

The lock initially starts at `'0000'`, a string representing the state of the 4
wheels.

You are given a list of `deadends` dead ends, meaning if the lock displays any of
these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a `target` representing the value of the wheels that will unlock the lock,
return the minimum total number of turns required to open the lock, or -1 if it is
impossible.

Example 1:

Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".

Example 2:

Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation:
We can turn the last wheel in reverse to move from "0000" -> "0009".

Example 3:

Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation:
We can't reach the target without getting stuck.

Example 4:

Input: deadends = ["0000"], target = "8888"
Output: -1

Note:

The length of `deadends` will be in the range `[1, 500]`.

`target` will not be in the list `deadends`.

Every string in `deadends` and the string `target` will be a
string of 4 digits from the 10,000 possibilities `'0000'` to
`'9999'`.

【中文翻译】
你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字：'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'。每个拨轮可以自由旋转：例如把 '9' 变为 '0'，'0' 变为 '9'。每次旋转都只能旋转一个拨轮的一位数字。

锁的初始数字为 '0000'，一个代表四个拨轮的数字的字符串。

列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。

字符串 target 代表可以解锁的数字，你需要给出最小的旋转次数，如果无论如何不能解锁，返回 -1。

示例 1：

输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
输出：6
解释：
可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，因为当拨动到 "0102" 时这个锁就会被锁定。

示例 2：

输入：deadends = ["8888"], target = "0009"
输出：1
解释：
我们可以把最后一位反向旋转，从 "0000" -> "0009"。

示例 3：

输入：deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
输出：-1
解释：
我们无法旋转到目标数字而不被锁定。

示例 4：

输入：deadends = ["0000"], target = "8888"
输出：-1

注意：

死亡列表 deadends 的长度范围为 [1, 500]。

目标数字 target 不会在 deadends 之中。

每个 deadends 和 target 中的字符串都是 4 位数字，在 10,000 种可能 '0000' 到 '9999' 之中。
"""

from typing import List, Optional


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        from collections import deque
        dead = set(deadends)
        if "0000" in dead:
            return -1
        if target == "0000":
            return 0

        queue = deque([("0000", 0)])
        visited = set(["0000"])

        while queue:
            state, steps = queue.popleft()
            for i in range(4):
                for d in (1, -1):
                    digit = (int(state[i]) + d) % 10
                    next_state = state[:i] + str(digit) + state[i + 1:]
                    if next_state == target:
                        return steps + 1
                    if next_state not in visited and next_state not in dead:
                        visited.add(next_state)
                        queue.append((next_state, steps + 1))
        return -1



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# BFS 最短路径问题。将每个 4 位数字组合看作图中的一个节点。
# 每个节点有 8 个邻居（4 个位置，每个位置可以向上或向下旋转一位）。
# 从 "0000" 开始 BFS 搜索，避开 deadends 中的节点。
# 关键：旋转是循环的（9 → 0 和 0 → 9），使用模运算 (digit + d) % 10。
# BFS 保证首次到达 target 时的步数就是最短步数。
# 提前处理特殊情况：起点 "0000" 在 deadends 中，或 target 就是 "0000"。
#
# 时间复杂度: O(10000 * 8) = O(1) - 状态空间固定为 10000 种可能
# 空间复杂度: O(10000) - visited 集合和队列最多存储所有状态
#
# 关键点:
# - BFS 天然适合无权图的最短路径问题
# - 每个状态的 8 个邻居通过模运算生成，巧妙处理循环
# - visited 集合避免重复访问和死循环
# - deadends 相当于障碍物，遇到时跳过
# - 状态空间固定（0000-9999），所以复杂度为常数级别
