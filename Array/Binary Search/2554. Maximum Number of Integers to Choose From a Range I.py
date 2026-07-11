"""
LeetCode #2554 - Maximum Number of Integers to Choose From a Range I
从一个范围内选择最多整数 I
https://leetcode.cn/problems/maximum-number-of-integers-to-choose-from-a-range-i/

给你一个整数数组 `banned` 和两个整数 `n` 和 `maxSum` 。你需要按照以下规则选择一些整数：
被选择整数的范围是 `[1, n]` 。
每个整数 至多 选择 一次 。
被选择整数不能在数组 `banned` 中。
被选择整数的和不超过 `maxSum` 。
请你返回按照上述规则 最多 可以选择的整数数目。

示例 1：
输入：banned = [1,6,5], n = 5, maxSum = 6 输出：2 解释：你可以选择整数 2 和 4 。 2 和 4 在范围 [1, 5] 内，且它们都不在 banned 中，它们的和是 6 ，没有超过 maxSum 。
示例 2：
输入：banned = [1,2,3,4,5,6,7], n = 8, maxSum = 1 输出：0 解释：按照上述规则无法选择任何整数。
示例 3：
输入：banned = [11], n = 7, maxSum = 50 输出：7 解释：你可以选择整数 1, 2, 3, 4, 5, 6 和 7 。 它们都在范围 [1, 7] 中，且都没出现在 banned 中，它们的和是 28 ，没有超过 maxSum 。

提示：
`1 <= banned.length <= 10^4`
`1 <= banned[i], n <= 10^4`
`1 <= maxSum <= 10^9`
"""

from typing import List, Optional


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ban_set = set(banned)
        cur_sum = 0
        count = 0
        for i in range(1, n + 1):
            if i in ban_set:
                continue
            if cur_sum + i > maxSum:
                break
            cur_sum += i
            count += 1
        return count



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Hash Table, Binary Search, Sorting
#
# 解题思路:
# 贪心选择最小的可用整数。将banned转为集合以便O(1)查找。从1到n遍历，
# 跳过被禁止的数，累加当前和。一旦超过maxSum就停止。因为选择最小的数能得到最多数量。
#
# 时间复杂度: O(N + B)，B为banned长度
# 空间复杂度: O(B)
#
# 关键点:
# - 贪心选最小数可以最大化数量（和一定时，选小数个数多）
# - 使用set存储banned实现O(1)检查
# - 无需排序，直接从小到大遍历1到n
