"""
LeetCode #2780 - Minimum Index of a Valid Split
合法分割的最小下标
https://leetcode.cn/problems/minimum-index-of-a-valid-split/

如果在长度为 `m` 的整数数组 `arr` 中 超过一半 的元素值为 `x`，那么我们称 `x` 是 支配元素 。
给你一个下标从 0 开始长度为 `n` 的整数数组 `nums` ，数据保证它含有一个 支配 元素。
你需要在下标 `i` 处将 `nums` 分割成两个数组 `nums[0, ..., i]` 和 `nums[i + 1, ..., n - 1]` ，如果一个分割满足以下条件，我们称它是 合法 的：
`0 <= i < n - 1`
`nums[0, ..., i]` 和 `nums[i + 1, ..., n - 1]` 的支配元素相同。
这里， `nums[i, ..., j]` 表示 `nums` 的一个子数组，它开始于下标 `i` ，结束于下标 `j` ，两个端点都包含在子数组内。特别地，如果 `j < i` ，那么 `nums[i, ..., j]` 表示一个空数组。
请你返回一个 合法分割 的 最小 下标。如果合法分割不存在，返回 `-1` 。

示例 1：
输入：nums = [1,2,2,2] 输出：2 解释：我们将数组在下标 2 处分割，得到 [1,2,2] 和 [2] 。 数组 [1,2,2] 中，元素 2 是支配元素，因为它在数组中出现了 2 次，且 2 * 2 > 3 。 数组 [2] 中，元素 2 是支配元素，因为它在数组中出现了 1 次，且 1 * 2 > 1 。 两个数组 [1,2,2] 和 [2] 都有与 nums 一样的支配元素，所以这是一个合法分割。 下标 2 是合法分割中的最小下标。
示例 2：
输入：nums = [2,1,3,1,1,1,7,1,2,1] 输出：4 解释：我们将数组在下标 4 处分割，得到 [2,1,3,1,1] 和 [1,7,1,2,1] 。 数组 [2,1,3,1,1] 中，元素 1 是支配元素，因为它在数组中出现了 3 次，且 3 * 2 > 5 。 数组 [1,7,1,2,1] 中，元素 1 是支配元素，因为它在数组中出现了 3 次，且 3 * 2 > 5 。 两个数组 [2,1,3,1,1] 和 [1,7,1,2,1] 都有与 nums 一样的支配元素，所以这是一个合法分割。 下标 4 是所有合法分割中的最小下标。
示例 3：
输入：nums = [3,3,3,3,7,2,2] 输出：-1 解释：没有合法分割。

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^9`
`nums` 有且只有一个支配元素。
"""

from typing import List, Optional


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        candidate = nums[0]
        count = 0
        for x in nums:
            if count == 0:
                candidate = x
            count += 1 if x == candidate else -1

        total = sum(1 for x in nums if x == candidate)
        left_cnt = 0
        for i in range(n - 1):
            if nums[i] == candidate:
                left_cnt += 1
            right_cnt = total - left_cnt
            if left_cnt * 2 > (i + 1) and right_cnt * 2 > (n - i - 1):
                return i
        return -1



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Sorting
#
# 解题思路:
# 首先用摩尔投票法找出整个数组的支配元素（众数）。
# 然后统计支配元素的总出现次数 total。从左到右遍历分割点 i，维护左侧支配元素计数 left_cnt。
# 检查左右两侧是否都满足支配条件：left_cnt*2 > i+1 且 (total-left_cnt)*2 > n-i-1。
# 返回第一个满足条件的分割点。
#
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 关键点:
# - 摩尔投票法 O(n) 时间 O(1) 空间找到支配元素
# - 整个数组的支配元素必须是两个子数组的支配元素（否则无法同时满足）
# - 前缀计数：从左到右维护左侧支配元素的出现次数
