"""
LeetCode #1953 - Maximum Number of Weeks for Which You Can Work
你可以工作的最大周数
https://leetcode.cn/problems/maximum-number-of-weeks-for-which-you-can-work/

给你 `n` 个项目，编号从 `0` 到 `n - 1` 。同时给你一个整数数组 `milestones` ，其中每个 `milestones[i]` 表示第 `i` 个项目中的阶段任务数量。
你可以按下面两个规则参与项目中的工作：
每周，你将会完成 某一个 项目中的 恰好一个 阶段任务。你每周都 必须 工作。
在 连续的 两周中，你 不能 参与并完成同一个项目中的两个阶段任务。
一旦所有项目中的全部阶段任务都完成，或者执行仅剩的一个阶段任务将会导致你违反上面的规则，你将 停止工作。注意，由于这些条件的限制，你可能无法完成所有阶段任务。
返回在不违反上面规则的情况下你 最多 能工作多少周。

示例 1：
输入：milestones = [1,2,3] 输出：6 解释：一种可能的情形是： ​​​​- 第 1 周，你参与并完成项目 0 中的一个阶段任务。 - 第 2 周，你参与并完成项目 2 中的一个阶段任务。 - 第 3 周，你参与并完成项目 1 中的一个阶段任务。 - 第 4 周，你参与并完成项目 2 中的一个阶段任务。 - 第 5 周，你参与并完成项目 1 中的一个阶段任务。 - 第 6 周，你参与并完成项目 2 中的一个阶段任务。 总周数是 6 。
示例 2：
输入：milestones = [5,2,1] 输出：7 解释：一种可能的情形是： - 第 1 周，你参与并完成项目 0 中的一个阶段任务。 - 第 2 周，你参与并完成项目 1 中的一个阶段任务。 - 第 3 周，你参与并完成项目 0 中的一个阶段任务。 - 第 4 周，你参与并完成项目 1 中的一个阶段任务。 - 第 5 周，你参与并完成项目 0 中的一个阶段任务。 - 第 6 周，你参与并完成项目 2 中的一个阶段任务。 - 第 7 周，你参与并完成项目 0 中的一个阶段任务。 总周数是 7 。 注意，你不能在第 8 周参与完成项目 0 中的最后一个阶段任务，因为这会违反规则。 因此，项目 0 中会有一个阶段任务维持未完成状态。

提示：
`n == milestones.length`
`1 <= n <= 10^5`
`1 <= milestones[i] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        """
        If the largest milestone count > sum of all others + 1,
        we can't finish it all because we need gaps between same-project weeks.
        Otherwise, we can finish all milestones.
        """
        total = sum(milestones)
        max_val = max(milestones)
        rest = total - max_val

        if max_val > rest + 1:
            return 2 * rest + 1
        else:
            return total



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array
#
# 解题思路:
# 核心观察：如果某个项目的任务数超过其他所有项目任务数之和 + 1，
# 则无法完成该项目的所有任务（因为相邻周不能做同一项目）。
# 设最大值为 M，其余总和为 S。
# - 若 M <= S + 1：可以把所有任务穿插完成，返回 total
# - 若 M > S + 1：最多做 2*S + 1 周（S 个其他任务作为间隔 + M 中的 S+1 个）
#
# 可以理解为：把最大的项目当成"隔板"，其他项目的任务插入其间。
#
# 时间复杂度: O(N)，一次遍历求和并找最大值
# 空间复杂度: O(1)
#
# 关键点:
# - 贪心的本质是"插空"：最大项目的任务作为主体，其他任务填入空隙
# - M <= S + 1 时能全部完成
# - 返回值和 sum 可能超过 32 位整数范围，Python 自动支持大整数
