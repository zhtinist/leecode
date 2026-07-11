"""
LeetCode #2274 - Maximum Consecutive Floors Without Special Floors
不含特殊楼层的最大连续楼层数
https://leetcode.cn/problems/maximum-consecutive-floors-without-special-floors/

Alice 管理着一家公司，并租用大楼的部分楼层作为办公空间。Alice 决定将一些楼层作为 特殊楼层 ，仅用于放松。
给你两个整数 `bottom` 和 `top` ，表示 Alice 租用了从 `bottom` 到 `top`（含 `bottom` 和 `top` 在内）的所有楼层。另给你一个整数数组 `special` ，其中 `special[i]` 表示  Alice 指定用于放松的特殊楼层。
返回不含特殊楼层的 最大 连续楼层数。

示例 1：
输入：bottom = 2, top = 9, special = [4,6] 输出：3 解释：下面列出的是不含特殊楼层的连续楼层范围： - (2, 3) ，楼层数为 2 。 - (5, 5) ，楼层数为 1 。 - (7, 9) ，楼层数为 3 。 因此，返回最大连续楼层数 3 。
示例 2：
输入：bottom = 6, top = 8, special = [7,6,8] 输出：0 解释：每层楼都被规划为特殊楼层，所以返回 0 。

提示
`1 <= special.length <= 10^5`
`1 <= bottom <= special[i] <= top <= 10^9`
`special` 中的所有值 互不相同
"""

from typing import List, Optional


class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        """
        Return the maximum number of consecutive floors without special floors.
        """
        special.sort()
        ans = 0

        # gap before the first special floor
        ans = max(ans, special[0] - bottom)

        # gaps between consecutive special floors
        for i in range(1, len(special)):
            # Number of non-special floors between special[i-1] and special[i]
            # is special[i] - special[i-1] - 1
            ans = max(ans, special[i] - special[i-1] - 1)

        # gap after the last special floor
        ans = max(ans, top - special[-1])

        return ans


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Sorting
#
# 解题思路:
# 将特殊楼层排序后，不含特殊楼层的连续段即为排序后相邻特殊楼层之间的区间。
# 计算三个部分的连续楼层数：(1) bottom 到第一个特殊楼层之间的楼层数，
# (2) 相邻特殊楼层之间的楼层数（间隔 - 1），(3) 最后一个特殊楼层到 top
# 之间的楼层数。取这三部分的最大值即可。例如 special[i-1]=4, special[i]=6,
# 中间只有楼层 5 是非特殊楼层，数量为 6-4-1=1。
#
# 时间复杂度: O(N log N)，N 为 special 数组长度。排序占据主要时间。
# 空间复杂度: O(1)，仅使用常数额外空间（排序可能使用 O(log N) 递归栈空间）。
#
# 关键点:
# - 先排序特殊楼层，使它们按楼层号从小到大排列
# - 相邻特殊楼层之间的间隙 = special[i] - special[i-1] - 1
# - 不要忘记边界情况：bottom 到第一个特殊楼层、最后一个特殊楼层到 top
# - 如果 bottom 紧挨第一个特殊楼层或 top 紧挨最后一个特殊楼层，间隙为 0
