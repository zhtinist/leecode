"""
LeetCode #2145 - Count the Hidden Sequences
统计隐藏数组数目
https://leetcode.cn/problems/count-the-hidden-sequences/

给你一个下标从 0 开始且长度为 `n` 的整数数组 `differences` ，它表示一个长度为 `n + 1` 的 隐藏 数组 相邻 元素之间的 差值 。更正式的表述为：我们将隐藏数组记作 `hidden` ，那么 `differences[i] = hidden[i + 1] - hidden[i]` 。
同时给你两个整数 `lower` 和 `upper` ，它们表示隐藏数组中所有数字的值都在 闭 区间 `[lower, upper]` 之间。
比方说，`differences = [1, -3, 4]` ，`lower = 1` ，`upper = 6` ，那么隐藏数组是一个长度为 `4` 且所有值都在 `1` 和 `6` （包含两者）之间的数组。
`[3, 4, 1, 5]` 和 `[4, 5, 2, 6]` 都是符合要求的隐藏数组。
`[5, 6, 3, 7]` 不符合要求，因为它包含大于 `6` 的元素。
`[1, 2, 3, 4]` 不符合要求，因为相邻元素的差值不符合给定数据。
请你返回 符合 要求的隐藏数组的数目。如果没有符合要求的隐藏数组，请返回 `0` 。

示例 1：
输入：differences = [1,-3,4], lower = 1, upper = 6 输出：2 解释：符合要求的隐藏数组为： - [3, 4, 1, 5] - [4, 5, 2, 6] 所以返回 2 。
示例 2：
输入：differences = [3,-4,5,1,-2], lower = -4, upper = 5 输出：4 解释：符合要求的隐藏数组为： - [-3, 0, -4, 1, 2, 0] - [-2, 1, -3, 2, 3, 1] - [-1, 2, -2, 3, 4, 2] - [0, 3, -1, 4, 5, 3] 所以返回 4 。
示例 3：
输入：differences = [4,-7,2], lower = 3, upper = 6 输出：0 解释：没有符合要求的隐藏数组，所以返回 0 。

提示：
`n == differences.length`
`1 <= n <= 10^5`
`-10^5 <= differences[i] <= 10^5`
`-10^5 <= lower <= upper <= 10^5`
"""

from typing import List, Optional


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # Let hidden[0] = x, then hidden[i] = x + prefix[i]
        min_val = 0
        max_val = 0
        cur = 0
        for d in differences:
            cur += d
            min_val = min(min_val, cur)
            max_val = max(max_val, cur)

        # x + min_val >= lower and x + max_val <= upper
        # lower - min_val <= x <= upper - max_val
        low_bound = lower - min_val
        high_bound = upper - max_val

        if low_bound > high_bound:
            return 0
        return high_bound - low_bound + 1



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Prefix Sum
#
# 解题思路:
# 设 hidden[0] = x（未知），则 hidden[i] = x + prefix[i]，其中 prefix[i] 是 differences
# 前 i 项的和。遍历 differences 计算前缀和的动态范围：最小值 min_val 和最大值 max_val。
# 要使 hidden 所有元素都在 [lower, upper] 内，x 必须同时满足：
#   x + min_val >= lower  =>  x >= lower - min_val
#   x + max_val <= upper  =>  x <= upper - max_val
# 因此 x 的取值范围为 [lower - min_val, upper - max_val]，合法 x 的个数即为答案。
#
# 时间复杂度: O(N)，一次遍历计算前缀和的极值。
# 空间复杂度: O(1)，只使用常数级别的变量。
#
# 关键点:
# - 将 hidden 数组表示为 x + prefix 的形式，问题转化为求 x 的取值范围
# - 只需前缀和的最小值和最大值，不需要存储整个前缀数组
