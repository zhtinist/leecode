"""
LeetCode #3034 - Number of Subarrays That Match a Pattern I
匹配模式数组的子数组数目 I
https://leetcode.cn/problems/number-of-subarrays-that-match-a-pattern-i/

给你一个下标从 0 开始长度为 `n` 的整数数组 `nums` ，和一个下标从 `0` 开始长度为 `m` 的整数数组 `pattern` ，`pattern` 数组只包含整数 `-1` ，`0` 和 `1` 。
大小为 `m + 1` 的子数组 `nums[i..j]` 如果对于每个元素 `pattern[k]` 都满足以下条件，那么我们说这个子数组匹配模式数组 `pattern` ：
如果 `pattern[k] == 1` ，那么 `nums[i + k + 1] > nums[i + k]`
如果 `pattern[k] == 0` ，那么 `nums[i + k + 1] == nums[i + k]`
如果 `pattern[k] == -1` ，那么 `nums[i + k + 1] < nums[i + k]`
请你返回匹配 `pattern` 的 `nums` 子数组的 数目 。

示例 1：
输入：nums = [1,2,3,4,5,6], pattern = [1,1] 输出：4 解释：模式 [1,1] 说明我们要找的子数组是长度为 3 且严格上升的。在数组 nums 中，子数组 [1,2,3] ，[2,3,4] ，[3,4,5] 和 [4,5,6] 都匹配这个模式。 所以 nums 中总共有 4 个子数组匹配这个模式。
示例 2：
输入：nums = [1,4,4,1,3,5,5,3], pattern = [1,0,-1] 输出：2 解释：这里，模式数组 [1,0,-1] 说明我们需要找的子数组中，第一个元素小于第二个元素，第二个元素等于第三个元素，第三个元素大于第四个元素。在 nums 中，子数组 [1,4,4,1] 和 [3,5,5,3] 都匹配这个模式。 所以 nums 中总共有 2 个子数组匹配这个模式。

提示：
`2 <= n == nums.length <= 100`
`1 <= nums[i] <= 10^9`
`1 <= m == pattern.length < n`
`-1 <= pattern[i] <= 1`
"""

from typing import List, Optional


class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        """
        Brute force for n <= 100. For each starting position i,
        check if the subarray nums[i..i+m] matches the pattern.
        """
        n = len(nums)
        m = len(pattern)
        ans = 0

        for i in range(n - m):
            match = True
            for k in range(m):
                if pattern[k] == 1 and not (nums[i + k + 1] > nums[i + k]):
                    match = False
                    break
                if pattern[k] == 0 and not (nums[i + k + 1] == nums[i + k]):
                    match = False
                    break
                if pattern[k] == -1 and not (nums[i + k + 1] < nums[i + k]):
                    match = False
                    break
            if match:
                ans += 1

        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, String Matching, Hash Function, Rolling Hash
#
# 解题思路:
# n <= 100，直接暴力枚举所有可能的起始位置 i。对于每个起始位置，
# 检查长度为 m+1 的子数组是否与 pattern 匹配。pattern[k] 定义了相邻元素的比较关系：
# 1 表示递增，0 表示相等，-1 表示递减。全部匹配则计数加一。
#
# 时间复杂度: O(n * m)，n、m 均不超过 100
# 空间复杂度: O(1)
#
# 关键点:
# - pattern 长度 m 对应子数组长度 m+1，因为有 m 个相邻比较关系
# - 小数据范围（n <= 100）允许暴力枚举
# - 使用三个 if 条件分别处理 pattern[k] == 1/0/-1 的情况
