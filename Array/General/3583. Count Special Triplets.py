"""
LeetCode #3583 - Count Special Triplets
统计特殊三元组
https://leetcode.cn/problems/count-special-triplets/

给你一个整数数组 `nums`。
特殊三元组 定义为满足以下条件的下标三元组 `(i, j, k)`：
`0 <= i < j < k < n`，其中 `n = nums.length`
`nums[i] == nums[j] * 2`
`nums[k] == nums[j] * 2`
返回数组中 特殊三元组 的总数。
由于答案可能非常大，请返回结果对 `10^9 + 7` 取余数后的值。

示例 1：

输入： nums = [6,3,6]
输出： 1
解释：
唯一的特殊三元组是 `(i, j, k) = (0, 1, 2)`，其中：
`nums[0] = 6`, `nums[1] = 3`, `nums[2] = 6`
`nums[0] = nums[1] * 2 = 3 * 2 = 6`
`nums[2] = nums[1] * 2 = 3 * 2 = 6`
示例 2：

输入： nums = [0,1,0,0]
输出： 1
解释：
唯一的特殊三元组是 `(i, j, k) = (0, 2, 3)`，其中：
`nums[0] = 0`, `nums[2] = 0`, `nums[3] = 0`
`nums[0] = nums[2] * 2 = 0 * 2 = 0`
`nums[3] = nums[2] * 2 = 0 * 2 = 0`
示例 3：

输入： nums = [8,4,2,8,4]
输出： 2
解释：
共有两个特殊三元组：
`(i, j, k) = (0, 1, 3)`
`nums[0] = 8`, `nums[1] = 4`, `nums[3] = 8`
`nums[0] = nums[1] * 2 = 4 * 2 = 8`
`nums[3] = nums[1] * 2 = 4 * 2 = 8`
`(i, j, k) = (1, 2, 4)`
`nums[1] = 4`, `nums[2] = 2`, `nums[4] = 4`
`nums[1] = nums[2] * 2 = 2 * 2 = 4`
`nums[4] = nums[2] * 2 = 2 * 2 = 4`

提示：
`3 <= n == nums.length <= 10^5`
`0 <= nums[i] <= 10^5`
"""

from typing import List, Optional
from collections import defaultdict

MOD = 10 ** 9 + 7


class Solution:
    def countSpecialTriplets(self, nums: List[int]) -> int:
        n = len(nums)

        # left_count[j] = 在 j 左侧有多少 i 满足 nums[i] == nums[j] * 2
        left_freq = defaultdict(int)
        left_count = [0] * n
        for j in range(n):
            target = nums[j] * 2
            left_count[j] = left_freq.get(target, 0)
            left_freq[nums[j]] = left_freq.get(nums[j], 0) + 1

        # right_count[j] = 在 j 右侧有多少 k 满足 nums[k] == nums[j] * 2
        right_freq = defaultdict(int)
        right_count = [0] * n
        for j in range(n - 1, -1, -1):
            target = nums[j] * 2
            right_count[j] = right_freq.get(target, 0)
            right_freq[nums[j]] = right_freq.get(nums[j], 0) + 1

        # 每个 j 位置的贡献 = left_count[j] * right_count[j]
        ans = 0
        for j in range(n):
            ans = (ans + left_count[j] * right_count[j]) % MOD

        return ans










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Counting
#
# 解题思路:
# 对于每个中间位置 j，需要统计：
# - 左侧有多少 i < j 满足 nums[i] == nums[j] * 2（记为 left_count[j]）
# - 右侧有多少 k > j 满足 nums[k] == nums[j] * 2（记为 right_count[j]）
# 则 j 位置对答案的贡献 = left_count[j] * right_count[j]。
#
# 算法分三步：
# 1. 从左到右遍历，用哈希表记录已见过的元素频率，计算每个 j 的 left_count
# 2. 从右到左遍历，用哈希表记录已见过的元素频率，计算每个 j 的 right_count
# 3. 累加每个 j 的贡献
#
# 时间复杂度: O(n)
# 空间复杂度: O(n) — 存储 left_count 和 right_count 数组，以及两个哈希表
#
# 关键点:
# - 以 j 为中心分开统计左右匹配数
# - 利用乘法原理：左边有 a 种选择，右边有 b 种选择，则有 a*b 个三元组
# - 注意结果要取模 10^9+7
