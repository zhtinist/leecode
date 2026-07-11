"""
LeetCode #3153 - Sum of Digit Differences of All Pairs
所有数对中数位差之和
https://leetcode.cn/problems/sum-of-digit-differences-of-all-pairs/

你有一个数组 `nums` ，它只包含 正 整数，所有正整数的数位长度都 相同 。
两个整数的 数位差 指的是两个整数 相同 位置上不同数字的数目。
请你返回 `nums` 中 所有 整数对里，数位差之和。

示例 1：

输入：nums = [13,23,12]
输出：4
解释：
计算过程如下：
- 13 和 23 的数位差为 1 。
- 13 和 12 的数位差为 1 。
- 23 和 12 的数位差为 2 。
所以所有整数数对的数位差之和为 `1 + 1 + 2 = 4` 。
示例 2：

输入：nums = [10,10,10,10]
输出：0
解释：
数组中所有整数都相同，所以所有整数数对的数位不同之和为 0 。

提示：
`2 <= nums.length <= 10^5`
`1 <= nums[i] < 10^9`
`nums` 中的整数都有相同的数位长度。
"""

from typing import List, Optional


class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        n = len(nums)
        length = len(str(nums[0]))
        ans = 0
        total_pairs = n * (n - 1) // 2

        for pos in range(length):
            cnt = [0] * 10
            for x in nums:
                d = (x // (10 ** pos)) % 10
                cnt[d] += 1
            # 计算该位上相同数字的对数
            same = sum(c * (c - 1) // 2 for c in cnt)
            ans += total_pairs - same

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Math, Counting
#
# 解题思路:
# 所有数字数位长度相同，数位差即对应位置数字不同的对数。逐位独立计算：
# 对于每个数位，统计0-9的频率，该位数字相同的对数 = sum(C(cnt, 2))，
# 数字不同的对数 = 总对数 - 相同对数。将所有位的不同对数累加。
#
# 时间复杂度: O(n * L)，L为数字位数（最多9）
# 空间复杂度: O(10) = O(1)
#
# 关键点:
# - 数位独立，每位单独统计
# - 用补集思想：总对数 - 相同对数 = 不同对数
# - 组合数C(n,2)=n*(n-1)/2
