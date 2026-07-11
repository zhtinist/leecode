"""
LeetCode #3371 - Identify the Largest Outlier in an Array
识别数组中的最大异常值
https://leetcode.cn/problems/identify-the-largest-outlier-in-an-array/

给你一个整数数组 `nums`。该数组包含 `n` 个元素，其中 恰好 有 `n - 2` 个元素是 特殊数字 。剩下的 两个 元素中，一个是所有 特殊数字 的 和 ，另一个是 异常值 。
异常值 的定义是：既不是原始特殊数字之一，也不是表示元素和的那个数。
注意，特殊数字、和 以及 异常值 的下标必须 不同 ，但可以共享 相同 的值。
返回 `nums` 中可能的 最大异常值。

示例 1：

输入： nums = [2,3,5,10]
输出： 10
解释：
特殊数字可以是 2 和 3，因此和为 5，异常值为 10。
示例 2：

输入： nums = [-2,-1,-3,-6,4]
输出： 4
解释：
特殊数字可以是 -2、-1 和 -3，因此和为 -6，异常值为 4。
示例 3：

输入： nums = [1,1,1,1,1,5,5]
输出： 5
解释：
特殊数字可以是 1、1、1、1 和 1，因此和为 5，另一个 5 为异常值。

提示：
`3 <= nums.length <= 10^5`
`-1000 <= nums[i] <= 1000`
输入保证 `nums` 中至少存在 一个 可能的异常值。
"""

from typing import List, Optional


class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        from collections import Counter
        total = sum(nums)
        cnt = Counter(nums)
        ans = -10 ** 9
        for x in nums:
            remaining = total - x
            if remaining % 2 != 0:
                continue
            special_sum = remaining // 2
            need = cnt[special_sum]
            if special_sum == x:
                need -= 1
            if need > 0:
                ans = max(ans, x)
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Hash Table, Counting, Enumeration
#
# 解题思路:
# 设总元素和为S，n-2个特殊数字的和为sum_special。则数组中有一个元素值=sum_special，另一个是异常值x。
# 所以 S = sum_special + sum_special + x = 2*sum_special + x，即 sum_special = (S - x) / 2。
# 遍历每个元素作为候选异常值x，检查(S-x)/2是否为整数且存在于数组中（处理重复值），更新最大异常值。
#
# 时间复杂度: O(n)
# 空间复杂度: O(n)，Counter存储频率
#
# 关键点:
# - 公式推导: S = 2*sum_special + outlier
# - 注意处理sum_special和outlier可能是相同值的情况（通过计数判断）
