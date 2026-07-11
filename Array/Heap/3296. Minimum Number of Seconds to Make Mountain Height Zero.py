"""
LeetCode #3296 - Minimum Number of Seconds to Make Mountain Height Zero
移山所需的最少秒数
https://leetcode.cn/problems/minimum-number-of-seconds-to-make-mountain-height-zero/

给你一个整数 `mountainHeight` 表示山的高度。
同时给你一个整数数组 `workerTimes`，表示工人们的工作时间（单位：秒）。
工人们需要 同时 进行工作以 降低 山的高度。对于工人 `i` :
山的高度降低 1，需要 `workerTimes[i]` 秒。
山的高度降低 2，需要 `workerTimes[i] * 2` 秒。
...
山的高度降低 `x`，需要 `workerTimes[i] * x` 秒。
工人 `i` 所花费的总时间是所有 `x` 单位所需时间的总和。由于所有工人同时操作，所需的总时间是任何工人花费的 最大 时间。
返回一个整数，表示工人们使山的高度降低到 0 所需的 最少 秒数。

示例 1：

输入： mountainHeight = 4, workerTimes = [2,1,1]
输出： 3
解释：
将山的高度降低到 0 的一种方式是：
工人 0 将高度降低 1，花费 `workerTimes[0] = 2` 秒。
工人 1 将高度降低 2，花费 `workerTimes[1] + workerTimes[1] * 2 = 3` 秒。
工人 2 将高度降低 1，花费 `workerTimes[2] = 1` 秒。
因为工人同时工作，所需的最少时间为 `max(2, 3, 1) = 3` 秒。
示例 2：

输入： mountainHeight = 10, workerTimes = [3,2,2,4]
输出： 12
解释：
工人 0 将高度降低 2，花费 `workerTimes[0] + workerTimes[0] * 2 = 9` 秒。
工人 1 将高度降低 3，花费 `workerTimes[1] + workerTimes[1] * 2 + workerTimes[1] * 3 = 12` 秒。
工人 2 将高度降低 3，花费 `workerTimes[2] + workerTimes[2] * 2 + workerTimes[2] * 3 = 12` 秒。
工人 3 将高度降低 2，花费 `workerTimes[3] + workerTimes[3] * 2 = 12` 秒。
所需的最少时间为 `max(9, 12, 12, 12) = 12` 秒。
示例 3：

输入： mountainHeight = 5, workerTimes = [1]
输出： 15
解释：
这个示例中只有一个工人，所以答案是 `workerTimes[0] + workerTimes[0] * 2 + workerTimes[0] * 3 + workerTimes[0] * 4 + workerTimes[0] * 5 = 15` 秒。

提示：
`1 <= mountainHeight <= 10^5`
`1 <= workerTimes.length <= 10^4`
`1 <= workerTimes[i] <= 10^6`
"""

from typing import List, Optional


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        import math

        def check(t: int) -> bool:
            # 在 t 秒内所有工人能降低的总高度
            total = 0
            for w in workerTimes:
                # 工人 w 能在 t 秒内降低的高度 x 满足 w * (1+2+...+x) <= t
                # w * x * (x+1) / 2 <= t
                # x^2 + x - 2t/w <= 0
                # x = floor((-1 + sqrt(1 + 8t/w)) / 2)
                x = int((-1 + math.isqrt(1 + 8 * t // w)) // 2)
                total += x
                if total >= mountainHeight:
                    return True
            return total >= mountainHeight

        lo, hi = 1, workerTimes[0] * mountainHeight * (mountainHeight + 1) // 2
        ans = hi
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Math, Binary Search, Heap (Priority Queue)
#
# 解题思路:
# 二分答案 —— 最少秒数。
# check(t): 判断在 t 秒内能否降低 mountainHeight 的高度。
# 对于每个工人 i，其降低高度 x 所需时间为 workerTimes[i] * (1+2+...+x) = workerTimes[i] * x * (x+1) / 2。
# 解不等式求 x 的最大整数解：x = floor((-1 + sqrt(1 + 8*t/w)) / 2)
# 所有工人的 x 之和 >= mountainHeight 即表示可行。
#
# 时间复杂度: O(n * log(ans))
# 空间复杂度: O(1)
#
# 关键点:
# - 二分答案框架
# - 对每个工人，解一元二次不等式求最大可降低高度
# - 注意整数溢出，使用整数运算
