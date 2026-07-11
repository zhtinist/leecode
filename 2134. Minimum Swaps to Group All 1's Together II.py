"""
LeetCode #2134 - Minimum Swaps to Group All 1's Together II
最少交换次数来组合所有的 1 II
https://leetcode.cn/problems/minimum-swaps-to-group-all-1s-together-ii/

交换 定义为选中一个数组中的两个 互不相同 的位置并交换二者的值。
环形 数组是一个数组，可以认为 第一个 元素和 最后一个 元素 相邻 。
给你一个 二进制环形 数组 `nums` ，返回在 任意位置 将数组中的所有 `1` 聚集在一起需要的最少交换次数。

示例 1：
输入：nums = [0,1,0,1,1,0,0] 输出：1 解释：这里列出一些能够将所有 1 聚集在一起的方案： [0,0,1,1,1,0,0] 交换 1 次。 [0,1,1,1,0,0,0] 交换 1 次。 [1,1,0,0,0,0,1] 交换 2 次（利用数组的环形特性）。 无法在交换 0 次的情况下将数组中的所有 1 聚集在一起。 因此，需要的最少交换次数为 1 。
示例 2：
输入：nums = [0,1,1,1,0,0,1,1,0] 输出：2 解释：这里列出一些能够将所有 1 聚集在一起的方案： [1,1,1,0,0,0,0,1,1] 交换 2 次（利用数组的环形特性）。 [1,1,1,1,1,0,0,0,0] 交换 2 次。 无法在交换 0 次或 1 次的情况下将数组中的所有 1 聚集在一起。 因此，需要的最少交换次数为 2 。
示例 3：
输入：nums = [1,1,0,0,1] 输出：0 解释：得益于数组的环形特性，所有的 1 已经聚集在一起。 因此，需要的最少交换次数为 0 。

提示：
`1 <= nums.length <= 10^5`
`nums[i]` 为 `0` 或者 `1`
"""

from typing import List, Optional


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total_ones = sum(nums)
        n = len(nums)

        if total_ones == 0 or total_ones == n:
            return 0

        # Sliding window on doubled array
        extended = nums + nums
        ones_in_window = sum(extended[:total_ones])
        max_ones = ones_in_window

        for i in range(total_ones, n + total_ones):
            ones_in_window += extended[i] - extended[i - total_ones]
            max_ones = max(max_ones, ones_in_window)

        return total_ones - max_ones



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Sliding Window
#
# 解题思路:
# 问题转化为：在环形数组中找一个长度为 total_ones 的窗口，使得窗口内包含最多的 1。
# 最少交换次数 = total_ones - 窗口内最大 1 的数量（即需要把窗口外的 1 换进来）。
# 处理环形：将数组复制一份拼接到末尾（extended = nums + nums）。
# 滑动窗口：
# - 初始窗口取前 total_ones 个元素，统计 1 的数量。
# - 向右滑动窗口，每次加入一个新元素、移除最左元素，更新窗口内 1 的数量。
# - 记录窗口内 1 的最大值 max_ones。
# 最终结果 = total_ones - max_ones。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)（用于拼接数组，可优化为 O(1) 但 O(n) 更清晰）
#
# 关键点:
# - 最少交换次数 = 总数 - 窗口内已有 1 的最大数
# - 环形处理：数组拼接自身
# - 滑动窗口大小固定为 total_ones
