"""
LeetCode #2391 - Minimum Amount of Time to Collect Garbage
收集垃圾的最少总时间
https://leetcode.cn/problems/minimum-amount-of-time-to-collect-garbage/

给你一个下标从 0 开始的字符串数组 `garbage` ，其中 `garbage[i]` 表示第 `i` 个房子的垃圾集合。`garbage[i]` 只包含字符 `'M'` ，`'P'` 和 `'G'` ，但可能包含多个相同字符，每个字符分别表示一单位的金属、纸和玻璃。垃圾车收拾 一 单位的任何一种垃圾都需要花费 `1` 分钟。
同时给你一个下标从 0 开始的整数数组 `travel` ，其中 `travel[i]` 是垃圾车从房子 `i` 行驶到房子 `i + 1` 需要的分钟数。
城市里总共有三辆垃圾车，分别收拾三种垃圾。每辆垃圾车都从房子 `0` 出发，按顺序 到达每一栋房子。但它们 不是必须 到达所有的房子。
任何时刻只有 一辆 垃圾车处在使用状态。当一辆垃圾车在行驶或者收拾垃圾的时候，另外两辆车 不能 做任何事情。
请你返回收拾完所有垃圾需要花费的 最少 总分钟数。

示例 1：
输入：garbage = ["G","P","GP","GG"], travel = [2,4,3] 输出：21 解释： 收拾纸的垃圾车： 1. 从房子 0 行驶到房子 1 2. 收拾房子 1 的纸垃圾 3. 从房子 1 行驶到房子 2 4. 收拾房子 2 的纸垃圾 收拾纸的垃圾车总共花费 8 分钟收拾完所有的纸垃圾。 收拾玻璃的垃圾车： 1. 收拾房子 0 的玻璃垃圾 2. 从房子 0 行驶到房子 1 3. 从房子 1 行驶到房子 2 4. 收拾房子 2 的玻璃垃圾 5. 从房子 2 行驶到房子 3 6. 收拾房子 3 的玻璃垃圾 收拾玻璃的垃圾车总共花费 13 分钟收拾完所有的玻璃垃圾。 由于没有金属垃圾，收拾金属的垃圾车不需要花费任何时间。 所以总共花费 8 + 13 = 21 分钟收拾完所有垃圾。
示例 2：
输入：garbage = ["MMM","PGM","GP"], travel = [3,10] 输出：37 解释： 收拾金属的垃圾车花费 7 分钟收拾完所有的金属垃圾。 收拾纸的垃圾车花费 15 分钟收拾完所有的纸垃圾。 收拾玻璃的垃圾车花费 15 分钟收拾完所有的玻璃垃圾。 总共花费 7 + 15 + 15 = 37 分钟收拾完所有的垃圾。

提示：
`2 <= garbage.length <= 10^5`
`garbage[i]` 只包含字母 `'M'` ，`'P'` 和 `'G'` 。
`1 <= garbage[i].length <= 10`
`travel.length == garbage.length - 1`
`1 <= travel[i] <= 100`
"""

from typing import List, Optional


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        """
        For each garbage type ('M', 'P', 'G'):
        - Count total units of that type across all houses.
        - Find the last house index that contains this type.
        - Add travel time (prefix sum of travel up to that last house).
        Return the sum for all three types.
        """
        # Precompute prefix sum of travel for quick lookup
        n = len(garbage)
        prefix = [0] * n  # prefix[i] = total travel time from house 0 to house i
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + travel[i - 1]

        total = 0
        for gtype in ('M', 'P', 'G'):
            pick_time = 0
            last_house = -1
            for i, g in enumerate(garbage):
                cnt = g.count(gtype)
                if cnt > 0:
                    pick_time += cnt
                    last_house = i
            if last_house >= 0:
                total += pick_time + prefix[last_house]

        return total



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, String, Prefix Sum
#
# 解题思路:
# 1. 三种垃圾车(M、P、G)独立运行，总时间 = 每种垃圾车花费的时间之和。
# 2. 对于每种垃圾类型，遍历所有房子统计该类型的总数量（收集时间）。
# 3. 同时记录该类型最后一次出现的房子索引（行驶时间只需到那栋房子）。
# 4. 使用 travel 的前缀和快速计算行驶到第 i 栋房子所需的时间。
# 5. 收集时间 + 行驶时间 = 该垃圾车的总时间。
#
# 时间复杂度: O(n) — 每种垃圾类型遍历一次所有房子（3 * n，常数级别）
# 空间复杂度: O(n) — 前缀和数组
#
# 关键点:
# - 垃圾车不需要到达所有房子，只需要到达该类型垃圾最后一次出现的房子
# - 三种垃圾车独立计算，相互之间不干扰（因为任何时刻只有一辆车工作，总时间可以直接相加）
# - 使用前缀和优化行驶时间的计算
