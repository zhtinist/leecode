"""
LeetCode #2860 - Happy Students
让所有学生保持开心的分组方法数
https://leetcode.cn/problems/happy-students/

给你一个下标从 0 开始、长度为 `n` 的整数数组 `nums` ，其中 `n` 是班级中学生的总数。班主任希望能够在让所有学生保持开心的情况下选出一组学生：
如果能够满足下述两个条件之一，则认为第 `i` 位学生将会保持开心：
这位学生被选中，并且被选中的学生人数 严格大于 `nums[i]` 。
这位学生没有被选中，并且被选中的学生人数 严格小于 `nums[i]` 。
返回能够满足让所有学生保持开心的分组方法的数目。

示例 1：
输入：nums = [1,1] 输出：2 解释： 有两种可行的方法： 班主任没有选中学生。 班主任选中所有学生形成一组。  如果班主任仅选中一个学生来完成分组，那么两个学生都无法保持开心。因此，仅存在两种可行的方法。
示例 2：
输入：nums = [6,0,3,3,6,7,2,7] 输出：3 解释： 存在三种可行的方法： 班主任选中下标为 1 的学生形成一组。 班主任选中下标为 1、2、3、6 的学生形成一组。 班主任选中所有学生形成一组。

提示：
`1 <= nums.length <= 10^5`
`0 <= nums[i] < nums.length`
"""

from typing import List, Optional


class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        # Case: select 0 students
        if nums[0] > 0:
            ans += 1
        # Case: select k students (1 <= k < n)
        for k in range(1, n):
            if nums[k - 1] < k < nums[k]:
                ans += 1
        # Case: select all n students
        if nums[-1] < n:
            ans += 1
        return ans



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Array, Enumeration, Sorting
#
# 解题思路:
# 排序后，枚举选中的学生数量 k（0 到 n）。选中 k 个学生时，需要 k > 所有选中学生的 nums 值且 k < 所有未选中学生的 nums 值。
# 由于数组已排序，选中前 k 个最小的，条件变为 nums[k-1] < k < nums[k]（边界情况单独处理）。
#
# 时间复杂度: O(n log n)
# 空间复杂度: O(1)
#
# 关键点:
# - 排序后最优策略是选中 nums 值最小的 k 个学生
# - 验证条件：选中人数 k 必须严格介于选中组的最大值和未选中组的最小值之间
# - 边界：k=0 只需 0 < nums[0]；k=n 只需 nums[n-1] < n
