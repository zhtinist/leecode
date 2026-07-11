"""
LeetCode #473 - Matchsticks to Square
中文题名：火柴拼正方形
https://leetcode.com/problems/matchsticks-to-square/

Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little
match girl has, please find out a way you can make one square by using up all those
matchsticks. You should not break any stick, but you can link them up, and each matchstick
must be used exactly one time.

Your input will be several matchsticks the girl has, represented with their stick length.
Your output will either be true or false, to represent whether you could make one square
using all the matchsticks the little match girl has.

Example 1:

Input: [1,1,2,2,2]
Output: true

Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.

Example 2:

Input: [3,3,3,3,4]
Output: false

Explanation: You cannot find a way to form a square with all the matchsticks.

Note:

The length sum of the given matchsticks is in the range of `0` to
`10^9`.

The length of the given matchstick array will not exceed `15`.

【中文翻译】
还记得卖火柴的小女孩的故事吗？现在你已知小女孩拥有的所有火柴，请判断能否用所有火柴拼成一个
正方形。不能折断火柴，但可以首尾相连，每根火柴必须恰好使用一次。

输入为火柴长度组成的数组，输出为布尔值，表示能否用所有火柴拼成一个正方形。

示例 1：
    输入：[1,1,2,2,2]
    输出：true
    解释：可以拼成边长为 2 的正方形，其中一条边由两根长度为 1 的火柴组成。

示例 2：
    输入：[3,3,3,3,4]
    输出：false
    解释：无法用所有火柴拼成正方形。

注意：
- 火柴长度总和范围为 0 到 10^9。
- 火柴数组长度不超过 15。
"""

from typing import List, Optional


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        """
        Backtracking approach: partition matchsticks into 4 subsets
        with equal sum (each subset = one side of the square).
        Sort descending to fail faster with pruning.
        """
        if not matchsticks:
            return False

        total = sum(matchsticks)
        if total % 4 != 0:
            return False

        side = total // 4
        matchsticks.sort(reverse=True)  # try longer sticks first for better pruning

        if matchsticks[0] > side:
            return False

        sides = [0] * 4

        def backtrack(index: int) -> bool:
            if index == len(matchsticks):
                return all(s == side for s in sides)

            stick = matchsticks[index]
            for i in range(4):
                if sides[i] + stick <= side:
                    # Optimization: skip duplicate side lengths
                    if i > 0 and sides[i] == sides[i - 1]:
                        continue
                    sides[i] += stick
                    if backtrack(index + 1):
                        return True
                    sides[i] -= stick
            return False

        return backtrack(0)



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 使用回溯算法将火柴分配到正方形的四条边，等同于"将数组划分为 4 个等和子集"问题。
# 首先计算总和，若不能整除 4 或最大火柴超过边长，直接返回 False。将火柴降序排列
# 以便尽早发现失败（长火柴约束更强，减少搜索分支）。回溯时，尝试将每根火柴放入四条
# 边之一，若放入后不超过目标边长则继续递归。剪枝优化：跳过与前一条边等长的重复尝试。
#
# 时间复杂度: O(4^N) 理论上限，剪枝使实际运行远低于此（N ≤ 15）
# 空间复杂度: O(N) — 递归栈深度（火柴数量）
#
# 关键点:
# - 降序排列加速剪枝（先放长火柴快速排除不可行方案）
# - 跳过相同边长的重复分支是关键剪枝
# - 等价于经典的"划分为 K 个等和子集"问题（K=4）
# - 总和不能整除 4 则必然不可能
