"""
LeetCode #2588 - Count the Number of Beautiful Subarrays
统计美丽子数组数目
https://leetcode.cn/problems/count-the-number-of-beautiful-subarrays/

给你一个下标从 0 开始的整数数组`nums` 。每次操作中，你可以：
选择两个满足 `0 <= i, j < nums.length` 的不同下标 `i` 和 `j` 。
选择一个非负整数 `k` ，满足 `nums[i]` 和 `nums[j]` 在二进制下的第 `k` 位（下标编号从 0 开始）是 `1` 。
将 `nums[i]` 和 `nums[j]` 都减去 `2^k` 。
如果一个子数组内执行上述操作若干次（包括 0 次）后，该子数组可以变成一个全为 `0` 的数组，那么我们称它是一个 美丽 的子数组。
请你返回数组 `nums` 中 美丽子数组 的数目。
子数组是一个数组中一段连续 非空 的元素序列。
注意：所有元素最初都是 0 的子数组被认为是美丽的，因为不需要进行任何操作。

示例 1：
输入：nums = [4,3,1,2,4] 输出：2 解释：nums 中有 2 个美丽子数组：[4,3,1,2,4] 和 [4,3,1,2,4] 。 - 按照下述步骤，我们可以将子数组 [3,1,2] 中所有元素变成 0 ：   - 选择 [3, 1, 2] 和 k = 1 。将 2 个数字都减去 2^1 ，子数组变成 [1, 1, 0] 。   - 选择 [1, 1, 0] 和 k = 0 。将 2 个数字都减去 2^0 ，子数组变成 [0, 0, 0] 。 - 按照下述步骤，我们可以将子数组 [4,3,1,2,4] 中所有元素变成 0 ：   - 选择 [4, 3, 1, 2, 4] 和 k = 2 。将 2 个数字都减去 2^2 ，子数组变成 [0, 3, 1, 2, 0] 。   - 选择 [0, 3, 1, 2, 0] 和 k = 0 。将 2 个数字都减去 2^0 ，子数组变成 [0, 2, 0, 2, 0] 。   - 选择 [0, 2, 0, 2, 0] 和 k = 1 。将 2 个数字都减去 2^1 ，子数组变成 [0, 0, 0, 0, 0] 。
示例 2：
输入：nums = [1,10,4] 输出：0 解释：nums 中没有任何美丽子数组。

提示：
`1 <= nums.length <= 10^5`
`0 <= nums[i] <= 10^6`
"""

from typing import List, Optional


class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        from collections import defaultdict
        prefix = 0
        cnt = defaultdict(int)
        cnt[0] = 1
        ans = 0
        for x in nums:
            prefix ^= x
            ans += cnt[prefix]
            cnt[prefix] += 1
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Bit Manipulation, Array, Hash Table, Prefix Sum
#
# 解题思路:
# 关键转化：每次操作消除两个同位的1，等价于子数组的异或和必须为0。
# 因此问题变为统计异或和为0的子数组数量。使用前缀异或+哈希表：
# prefix[i]表示前i个元素的异或和，子数组[l,r]异或和为0当且仅当prefix[l]==prefix[r+1]。
# 遍历时计数prefix值出现的次数，每次累加之前的出现次数。
#
# 时间复杂度: O(N)
# 空间复杂度: O(N)
#
# 关键点:
# - 核心洞察：操作等价于异或，子数组可清零=异或和为0
# - 前缀异或经典模式：prefix[l]==prefix[r+1]时子数组异或和为0
# - 初始化cnt[0]=1处理从头开始的子数组
