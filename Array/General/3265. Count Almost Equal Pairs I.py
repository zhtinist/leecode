"""
LeetCode #3265 - Count Almost Equal Pairs I
统计近似相等数对 I
https://leetcode.cn/problems/count-almost-equal-pairs-i/

给你一个正整数数组 `nums` 。
如果我们执行以下操作 至多一次 可以让两个整数 `x` 和 `y` 相等，那么我们称这个数对是 近似相等 的：
选择 `x` 或者 `y`  之一，将这个数字中的两个数位交换。
请你返回 `nums` 中，下标 `i` 和 `j` 满足 `i < j` 且 `nums[i]` 和 `nums[j]` 近似相等 的数对数目。
注意 ，执行操作后一个整数可以有前导 0 。

示例 1：

输入：nums = [3,12,30,17,21]
输出：2
解释：
近似相等数对包括：
3 和 30 。交换 30 中的数位 3 和 0 ，得到 3 。
12 和 21 。交换12 中的数位 1 和 2 ，得到 21 。
示例 2：

输入：nums = [1,1,1,1,1]
输出：10
解释：
数组中的任意两个元素都是近似相等的。
示例 3：

输入：nums = [123,231]
输出：0
解释：
我们无法通过交换 123 或者 231 中的两个数位得到另一个数。

提示：
`2 <= nums.length <= 100`
`1 <= nums[i] <= 10^6`
"""

from typing import List, Optional


class Solution:
    def countPairs(self, nums: List[int]) -> int:
        from collections import Counter
        n = len(nums)
        cnt = Counter(nums)
        # 完全相同的情况
        ans = sum(v * (v - 1) // 2 for v in cnt.values())

        # 检查通过一次交换可以匹配的对
        # 对于每个数，生成所有可能的交换结果
        checked = set()
        for i in range(n):
            s = list(str(nums[i]))
            m = len(s)
            generated = set()
            generated.add(nums[i])  # 不交换（已经计算过）
            for p in range(m):
                for q in range(p + 1, m):
                    s[p], s[q] = s[q], s[p]
                    val = int(''.join(s))
                    generated.add(val)
                    s[p], s[q] = s[q], s[p]  # 还原
            for val in generated:
                if val != nums[i] and val in cnt:
                    key = tuple(sorted([nums[i], val]))
                    if key not in checked:
                        checked.add(key)
                        ans += cnt[nums[i]] * cnt[val]

        return ans










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Counting, Enumeration, Sorting
#
# 解题思路:
# 近似相等的条件：两个数相等或通过对其中一者交换两个数位后相等。
# 1. 统计相等数对：频率为 v 的数贡献 C(v, 2) 个数对
# 2. 对于每个数，生成所有可能的交换两个数位的结果，
#    检查这些结果是否在数组中存在，统计跨值的数对
# 注意避免重复计算（使用 checked 集合记录已处理的数对）。
#
# 时间复杂度: O(n * d^2) — d 为数位长度（最多 7 位，因为 nums[i] <= 10^6）
# 空间复杂度: O(n)
#
# 关键点:
# - nums 长度 <= 100，暴力枚举所有交换结果可行
# - 避免重复统计已处理的 (a,b) 对
