"""
LeetCode #3587 - Minimum Adjacent Swaps to Alternate Parity
最小相邻交换至奇偶交替
https://leetcode.cn/problems/minimum-adjacent-swaps-to-alternate-parity/

给你一个由互不相同的整数组成的数组 `nums` 。
在一次操作中，你可以交换任意两个 相邻 元素。
在一个排列中，当所有相邻元素的奇偶性交替出现，我们认为该排列是 有效排列。这意味着每对相邻元素中一个是偶数，一个是奇数。
请返回将 `nums` 变成任意一种 有效排列 所需的最小相邻交换次数。
如果无法重排 `nums` 来获得有效排列，则返回 `-1`。

示例 1：

输入： nums = [2,4,6,5,7]
输出：3
解释：
将 5 和 6 交换，数组变成  `[2,4,5,6,7]`
将 5 和 4 交换，数组变成  `[2,5,4,6,7]`
将 6 和 7 交换，数组变成  `[2,5,4,7,6]`。此时是一个有效排列。因此答案是 3。
示例 2：

输入： nums = [2,4,5,7]
输出： 1
解释：
将 4 和 5 交换，数组变成 `[2,5,4,7]`。此时是一个有效排列。因此答案是 1。
示例 3：

输入： nums = [1,2,3]
输出： 0
解释：
数组已经是有效排列，因此不需要任何操作。
示例 4：

输入： nums = [4,5,6,8]
输出：-1
解释：
没有任何一种排列可以满足奇偶交替的要求，因此返回 -1。

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^9`
`nums` 中的所有元素都是 唯一 的
"""

from typing import List, Optional


class Solution:
    def minAdjacentSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        odd_count = sum(1 for x in nums if x % 2 == 1)
        even_count = n - odd_count

        # Check if any valid arrangement is possible
        # For alternating starting with odd: need odd_count == ceil(n/2)
        # For alternating starting with even: need even_count == ceil(n/2)
        odd_first_possible = (odd_count == (n + 1) // 2)
        even_first_possible = (even_count == (n + 1) // 2)

        if not odd_first_possible and not even_first_possible:
            return -1

        def count_swaps(start_with_odd: bool) -> int:
            """Count min adjacent swaps to achieve arrangement
            where target parity at position i is determined by start_with_odd."""
            # target[i] = (start_with_odd and i%2==0) or (not start_with_odd and i%2==1)
            # i.e., odd positions when start_with_odd, odd at even indices
            odd_idx = 0  # which odd number we're assigning
            even_idx = 0  # which even number we're assigning
            swaps = 0

            for i in range(n):
                if start_with_odd:
                    # odd target positions: 0, 2, 4, ...
                    # even target positions: 1, 3, 5, ...
                    if nums[i] % 2 == 1:
                        # This odd number should go to position odd_idx * 2
                        swaps += abs(i - odd_idx * 2)
                        odd_idx += 1
                    else:
                        swaps += abs(i - (even_idx * 2 + 1))
                        even_idx += 1
                else:
                    # even target positions: 0, 2, 4, ...
                    # odd target positions: 1, 3, 5, ...
                    if nums[i] % 2 == 1:
                        swaps += abs(i - (odd_idx * 2 + 1))
                        odd_idx += 1
                    else:
                        swaps += abs(i - even_idx * 2)
                        even_idx += 1

            # Each adjacent swap moves an element 1 position.
            # The sum of absolute distances counts each movement,
            # but each swap fixes the position of two elements.
            # So total swaps = sum of distances / 2.
            return swaps // 2

        ans = float('inf')
        if odd_first_possible:
            ans = min(ans, count_swaps(True))
        if even_first_possible:
            ans = min(ans, count_swaps(False))

        return ans if ans != float('inf') else -1











# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array
#
# 解题思路:
# 1. 统计奇数和偶数的数量。有效排列要求相邻元素奇偶交替。
#    - 如果从奇数开始：位置 0,2,4,... 放奇数（共 ceil(n/2) 个），位置 1,3,5,... 放偶数（共 floor(n/2) 个）
#    - 如果从偶数开始：位置 0,2,4,... 放偶数（共 ceil(n/2) 个），位置 1,3,5,... 放奇数（共 floor(n/2) 个）
#    - 如果两种模式都无法满足计数要求，返回 -1。
# 2. 对于每种可能的模式，计算最小相邻交换次数：
#    a. 从左到右扫描，为每个元素分配目标位置。
#       第 k 个奇数分配到第 k 个奇数目标位置，第 k 个偶数分配到第 k 个偶数目标位置（保持同类元素的相对顺序）。
#    b. 累计每个元素的当前位置与目标位置的距离之和。
#    c. 每次相邻交换会同时移动两个元素各 1 个单位，所以交换次数 = 总距离 / 2。
# 3. 返回两种模式中的最小值。
#
# 时间复杂度: O(N)，只需一次扫描
# 空间复杂度: O(1)，只使用常数额外空间
#
# 关键点:
# - 保持奇数和偶数各自内部的相对顺序不变可以获得最小交换次数
# - 每次相邻交换使两个元素向目标方向各移动一步，因此交换次数 = 总移动距离 / 2
# - 需检查两种起始奇偶性模式，取其中的最小值
