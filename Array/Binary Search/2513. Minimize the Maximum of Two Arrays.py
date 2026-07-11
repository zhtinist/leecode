"""
LeetCode #2513 - Minimize the Maximum of Two Arrays
最小化两个数组中的最大值
https://leetcode.cn/problems/minimize-the-maximum-of-two-arrays/

给你两个数组 `arr1` 和 `arr2` ，它们一开始都是空的。你需要往它们中添加正整数，使它们满足以下条件：
`arr1` 包含 `uniqueCnt1` 个 互不相同 的正整数，每个整数都 不能 被 `divisor1` 整除 。
`arr2` 包含 `uniqueCnt2` 个 互不相同 的正整数，每个整数都 不能 被 `divisor2` 整除 。
`arr1` 和 `arr2` 中的元素 互不相同 。
给你 `divisor1` ，`divisor2` ，`uniqueCnt1` 和 `uniqueCnt2` ，请你返回两个数组中 最大元素 的 最小值 。

示例 1：
输入：divisor1 = 2, divisor2 = 7, uniqueCnt1 = 1, uniqueCnt2 = 3 输出：4 解释： 我们可以把前 4 个自然数划分到 arr1 和 arr2 中。 arr1 = [1] 和 arr2 = [2,3,4] 。 可以看出两个数组都满足条件。 最大值是 4 ，所以返回 4 。
示例 2：
输入：divisor1 = 3, divisor2 = 5, uniqueCnt1 = 2, uniqueCnt2 = 1 输出：3 解释： arr1 = [1,2] 和 arr2 = [3] 满足所有条件。 最大值是 3 ，所以返回 3 。
示例 3：
输入：divisor1 = 2, divisor2 = 4, uniqueCnt1 = 8, uniqueCnt2 = 2 输出：15 解释： 最终数组为 arr1 = [1,3,5,7,9,11,13,15] 和 arr2 = [2,6] 。 上述方案是满足所有条件的最优解。

提示：
`2 <= divisor1, divisor2 <= 10^5`
`1 <= uniqueCnt1, uniqueCnt2 < 10^9`
`2 <= uniqueCnt1 + uniqueCnt2 <= 10^9`
"""

from typing import List, Optional


class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        import math
        lcm = divisor1 // math.gcd(divisor1, divisor2) * divisor2

        def can(x: int) -> bool:
            cnt1 = x - x // divisor1
            cnt2 = x - x // divisor2
            cnt_both = x - x // lcm
            return cnt1 >= uniqueCnt1 and cnt2 >= uniqueCnt2 and cnt_both >= uniqueCnt1 + uniqueCnt2

        lo, hi = 1, 2 * (uniqueCnt1 + uniqueCnt2)
        while not can(hi):
            hi *= 2
        while lo < hi:
            mid = (lo + hi) // 2
            if can(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Math, Binary Search, Number Theory
#
# 解题思路:
# 二分查找最小的可能最大值X。检查函数验证：在1到X范围内，不被divisor1整除的数>=uniqueCnt1个，
# 不被divisor2整除的数>=uniqueCnt2个，不被lcm整除的数（两种数组总可用数）>=uniqueCnt1+uniqueCnt2个。
# 三个条件同时满足则该X可行，缩小上界；否则增大下界。
#
# 时间复杂度: O(log M)，其中M为答案上限
# 空间复杂度: O(1)
#
# 关键点:
# - 核心是容斥原理：被LCM整除的数两个数组都不能用
# - 三个条件缺一不可：arr1可用、arr2可用、总可用数足够
# - 二分查找的上界需要足够大，通过倍增确保can(hi)=True
