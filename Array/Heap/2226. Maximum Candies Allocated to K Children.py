"""
LeetCode #2226 - Maximum Candies Allocated to K Children
每个小孩最多能分到多少糖果
https://leetcode.cn/problems/maximum-candies-allocated-to-k-children/

给你一个 下标从 0 开始 的整数数组 `candies` 。数组中的每个元素表示大小为 `candies[i]` 的一堆糖果。你可以将每堆糖果分成任意数量的 子堆 ，但 无法 再将两堆合并到一起。
另给你一个整数 `k` 。你需要将这些糖果分配给 `k` 个小孩，使每个小孩分到 相同 数量的糖果。每个小孩可以拿走 至多一堆 糖果，有些糖果可能会不被分配。
返回每个小孩可以拿走的 最大糖果数目 。

示例 1：
输入：candies = [5,8,6], k = 3 输出：5 解释：可以将 candies[1] 分成大小分别为 5 和 3 的两堆，然后把 candies[2] 分成大小分别为 5 和 1 的两堆。现在就有五堆大小分别为 5、5、3、5 和 1 的糖果。可以把 3 堆大小为 5 的糖果分给 3 个小孩。可以证明无法让每个小孩得到超过 5 颗糖果。
示例 2：
输入：candies = [2,5], k = 11 输出：0 解释：总共有 11 个小孩，但只有 7 颗糖果，但如果要分配糖果的话，必须保证每个小孩至少能得到 1 颗糖果。因此，最后每个小孩都没有得到糖果，答案是 0 。

提示：
`1 <= candies.length <= 10^5`
`1 <= candies[i] <= 10^7`
`1 <= k <= 10^12`
"""

from typing import List, Optional


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # 如果糖果总数不够 k 个小孩每人至少 1 颗，直接返回 0
        if sum(candies) < k:
            return 0

        def can_allocate(c: int) -> bool:
            """判断能否给每个小孩分 c 颗糖果"""
            if c == 0:
                return True
            count = 0
            for pile in candies:
                count += pile // c
                if count >= k:  # 提前终止
                    return True
            return count >= k

        left, right = 1, max(candies)
        while left < right:
            mid = (left + right + 1) // 2  # 上取整，避免死循环
            if can_allocate(mid):
                left = mid  # mid 可行，尝试更大的
            else:
                right = mid - 1

        return left


# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Binary Search
#
# 解题思路:
# 二分搜索答案：每个小孩能分到的最大糖果数 c。
# 判定函数 can_allocate(c)：遍历每堆糖果，每堆可以分出 pile // c 个子堆，
# 累加看是否能达到 k 堆。若能，说明 c 可行，尝试更大的；否则减小 c。
# 边界：如果 sum(candies) < k，无法满足每人至少 1 颗，返回 0。
# 二分搜索使用 (left + right + 1) // 2 的上取整中值防止死循环。
#
# 时间复杂度: O(N log M) 其中 N 为糖果堆数，M 为最大单堆糖果数
# 空间复杂度: O(1) 只使用常量空间
#
# 关键点:
# - 二分搜索的判定函数：每堆可以分出的子堆数 = pile // c
# - can_allocate 中提前终止优化（count >= k 时直接返回）
# - 上取整二分避免 left = mid 时死循环
