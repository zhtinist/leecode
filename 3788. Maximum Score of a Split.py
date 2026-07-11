"""
LeetCode #3788 - Maximum Score of a Split
分割的最大得分
https://leetcode.cn/problems/maximum-score-of-a-split/

给你一个长度为 `n` 的整数数组 `nums`。
请你选出一个下标 `i` 以分割数组，该下标满足 `0 <= i < n - 1`。
对于选择的分割下标 `i`：
令 `prefixSum(i)` 表示数组前缀的和，即 `nums[0] + nums[1] + ... + nums[i]`。
令 `suffixMin(i)` 表示数组后缀的最小值，即 `nums[i + 1], nums[i + 2], ..., nums[n - 1]` 中的最小值。
在下标 `i` 的 分割得分 定义为：
`score(i) = prefixSum(i) - suffixMin(i)`
返回所有有效分割下标中 最大 的分割得分。

示例 1：

输入： nums = [10,-1,3,-4,-5]
输出： 17
解释：
最优的分割下标是 `i = 2`，`score(2) = prefixSum(2) - suffixMin(2) = (10 + (-1) + 3) - (-5) = 17`。
示例 2：

输入： nums = [-7,-5,3]
输出： -2
解释：
最优的分割下标是 `i = 0`，`score(0) = prefixSum(0) - suffixMin(0) = (-7) - (-5) = -2`。
示例 3：

输入： nums = [1,1]
输出： 0
解释：
唯一有效分割下标是 `i = 0`，`score(0) = prefixSum(0) - suffixMin(0) = 1 - 1 = 0`。

提示：
`2 <= nums.length <= 10^5`
`-10^9​​​​​​​ <= nums[i] <= 10^9`
"""

from typing import List, Optional


class Solution:
    def maxScoreSplit(self, nums: List[int]) -> int:
        n = len(nums)

        # Prefix sums
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        # Suffix minimums
        suff_min = [0] * n
        suff_min[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suff_min[i] = min(nums[i], suff_min[i + 1])

        ans = -float('inf')
        for i in range(n - 1):
            score = pref[i + 1] - suff_min[i + 1]
            ans = max(ans, score)

        return ans










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Prefix Sum
#
# 解题思路:
# 预处理前缀和数组 pref，其中 pref[i+1] = sum(nums[0..i])。
# 预处理后缀最小值数组 suff_min，其中 suff_min[i] = min(nums[i..n-1])。
# 对于每个分割点 i（0 <= i < n-1）：
#   score = pref[i+1] - suff_min[i+1]
# 取最大值即可。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)
#
# 关键点:
# - 前缀和和后缀最小值预处理后 O(1) 计算每个分割点得分
