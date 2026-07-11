"""
LeetCode #1894 - Find the Student that Will Replace the Chalk
找到需要补充粉笔的学生编号
https://leetcode.cn/problems/find-the-student-that-will-replace-the-chalk/

一个班级里有 `n` 个学生，编号为 `0` 到 `n - 1` 。每个学生会依次回答问题，编号为 `0` 的学生先回答，然后是编号为 `1` 的学生，以此类推，直到编号为 `n - 1` 的学生，然后老师会重复这个过程，重新从编号为 `0` 的学生开始回答问题。
给你一个长度为 `n` 且下标从 `0` 开始的整数数组 `chalk` 和一个整数 `k` 。一开始粉笔盒里总共有 `k` 支粉笔。当编号为 `i` 的学生回答问题时，他会消耗 `chalk[i]` 支粉笔。如果剩余粉笔数量 严格小于 `chalk[i]` ，那么学生 `i` 需要 补充 粉笔。
请你返回需要 补充 粉笔的学生 编号 。

示例 1：
输入：chalk = [5,1,5], k = 22 输出：0 解释：学生消耗粉笔情况如下： - 编号为 0 的学生使用 5 支粉笔，然后 k = 17 。 - 编号为 1 的学生使用 1 支粉笔，然后 k = 16 。 - 编号为 2 的学生使用 5 支粉笔，然后 k = 11 。 - 编号为 0 的学生使用 5 支粉笔，然后 k = 6 。 - 编号为 1 的学生使用 1 支粉笔，然后 k = 5 。 - 编号为 2 的学生使用 5 支粉笔，然后 k = 0 。 编号为 0 的学生没有足够的粉笔，所以他需要补充粉笔。
示例 2：
输入：chalk = [3,4,1,2], k = 25 输出：1 解释：学生消耗粉笔情况如下： - 编号为 0 的学生使用 3 支粉笔，然后 k = 22 。 - 编号为 1 的学生使用 4 支粉笔，然后 k = 18 。 - 编号为 2 的学生使用 1 支粉笔，然后 k = 17 。 - 编号为 3 的学生使用 2 支粉笔，然后 k = 15 。 - 编号为 0 的学生使用 3 支粉笔，然后 k = 12 。 - 编号为 1 的学生使用 4 支粉笔，然后 k = 8 。 - 编号为 2 的学生使用 1 支粉笔，然后 k = 7 。 - 编号为 3 的学生使用 2 支粉笔，然后 k = 5 。 - 编号为 0 的学生使用 3 支粉笔，然后 k = 2 。 编号为 1 的学生没有足够的粉笔，所以他需要补充粉笔。

提示：
`chalk.length == n`
`1 <= n <= 10^5`
`1 <= chalk[i] <= 10^5`
`1 <= k <= 10^9`
"""

from typing import List, Optional


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        k %= total  # Remove complete cycles

        for i, usage in enumerate(chalk):
            if k < usage:
                return i
            k -= usage

        return 0  # Should never reach here given constraints



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Binary Search, Prefix Sum, Simulation
#
# 解题思路:
# 1. 计算一轮所有学生消耗粉笔的总和 total。
# 2. 用 k % total 去除完整的循环，只关注最后一轮。
# 3. 在最后一轮中遍历学生，当剩余粉笔 k 严格小于当前学生
#    需要的 chalk[i] 时，该学生需要补充粉笔。
#
# 时间复杂度: O(n) — 一次求和和一次遍历
# 空间复杂度: O(1) — 常数变量
#
# 关键点:
# - 使用模运算跳过完整轮次，避免模拟 O(k) 次操作
# - 条件是 k < chalk[i]（严格小于），不是 <=
# - k 可能很大（10^9），total 可能也很大，但 Python 可以处理
