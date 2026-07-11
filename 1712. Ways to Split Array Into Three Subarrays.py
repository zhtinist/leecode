"""
LeetCode #1712 - Ways to Split Array Into Three Subarrays
中文题名：将数组分成三个子数组的方案数
https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/

A split of an integer array is good if:

The array is split into three non-empty contiguous subarrays -
named `left`, `mid`, `right` respectively from
left to right.

The sum of the elements in `left` is less than or equal to the sum of
the elements in `mid`, and the sum of the elements in
`mid` is less than or equal to the sum of the elements in
`right`.

Given `nums`, an array of non-negative integers, return
the number of good ways to split `nums`. As the
number may be too large, return it modulo `109 + 7`.

Example 1:

Input: nums = [1,1,1]
Output: 1
Explanation: The only good way to split nums is [1] [1] [1].

Example 2:

Input: nums = [1,2,2,2,5,0]
Output: 3
Explanation: There are three good ways of splitting nums:
[1] [2] [2,2,5,0]
[1] [2,2] [2,5,0]
[1,2] [2,2] [5,0]

Example 3:

Input: nums = [3,2,1]
Output: 0
Explanation: There is no good way to split nums.

Constraints:

`3 <= nums.length <= 105`

`0 <= nums[i] <= 104`

【中文翻译】
如果一个整数数组满足以下条件，则称其划分是好的：

将数组分成三个非空连续子数组——从左到右分别称为 `left`、`mid` 和 `right`。
`left` 的元素之和小于等于 `mid` 的元素之和，且 `mid` 的元素之和小于等于 `right` 的元素之和。

给定一个非负整数数组 `nums`，返回好的划分方案数。由于答案可能很大，
请返回其对 `10^9 + 7` 取模的结果。

示例 1：

输入: nums = [1,1,1]
输出: 1
解释: 唯一好的划分方式是 [1] [1] [1]

示例 2：

输入: nums = [1,2,2,2,5,0]
输出: 3
解释: 有三种好的划分方式：
[1] [2] [2,2,5,0]
[1] [2,2] [2,5,0]
[1,2] [2,2] [5,0]

示例 3：

输入: nums = [3,2,1]
输出: 0
解释: 没有好的划分方式

约束条件：

`3 <= nums.length <= 10^5`
`0 <= nums[i] <= 10^4`
"""

from typing import List, Optional
import bisect


class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        """
        前缀和 + 二分查找 / 双指针：
        前缀和 pre[i] = sum(nums[0..i))

        枚举左分割点 i（left 为 [0..i-1]）：
        - 需要找到 mid 的右端点 j，使得：
          1) sum(left) <= sum(mid)  =>  pre[i+1] - pre[i] >= pre[i]
          2) sum(mid) <= sum(right) =>  pre[n] - pre[j] >= pre[j] - pre[i]

        实际上，对于固定的 i，合法的 j 满足：
        - j >= 第一个使 sum(mid) >= sum(left) 的位置（用二分查找 pre 中 >= 2*pre[i] 的位置）
        - j <= 最后一个使 sum(mid) <= sum(right) 的位置（即 pre[j] - pre[i] <= pre[n] - pre[j]
          => 2*pre[j] <= pre[n] + pre[i] => pre[j] <= (pre[n]+pre[i])//2）

        合法 j 的范围是 [left_bound, right_bound]，如果 left_bound <= right_bound，
        则有效方案数 += right_bound - left_bound + 1。
        注意 j 不能为 n-1（right 必须非空）。
        """
        MOD = 10 ** 9 + 7
        n = len(nums)
        # 前缀和 pre[i] = sum(nums[0..i))
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]

        total_sum = pre[n]
        result = 0

        # 枚举 left 的右边界 i（left = nums[0..i]）
        for i in range(1, n - 1):  # i 从 1 开始，留至少一个给 mid 和 right
            left_sum = pre[i]

            # 找到最小的 j 使得 mid_sum >= left_sum
            # mid_sum = pre[j] - pre[i] >= left_sum  =>  pre[j] >= left_sum + pre[i] = 2 * left_sum
            min_j = bisect.bisect_left(pre, 2 * left_sum, lo=i + 1, hi=n)

            # 找到最大的 j 使得 mid_sum <= right_sum
            # right_sum = total_sum - pre[j] >= pre[j] - pre[i] = mid_sum
            # => total_sum - pre[j] >= pre[j] - pre[i]
            # => total_sum + pre[i] >= 2 * pre[j]
            # => pre[j] <= (total_sum + pre[i]) // 2
            max_j = bisect.bisect_right(pre, (total_sum + pre[i]) // 2, lo=i + 1, hi=n) - 1

            if min_j <= max_j and max_j < n:
                result = (result + max_j - min_j + 1) % MOD

        return result










# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 前缀和 + 二分查找。枚举左分割点 i（left = nums[0..i]），
# 然后二分查找中间子数组的合法右端点 j 的范围。
#
# 设前缀和 pre[k] = sum(nums[0..k))，总数组和 total = pre[n]。
# 对于固定的左分割点 i：
# - left_sum = pre[i]
# - mid_sum = pre[j] - pre[i]（其中 j 是 mid 的右端点）
# - right_sum = pre[n] - pre[j]
#
# 条件转换：
# 1) mid_sum >= left_sum => pre[j] - pre[i] >= pre[i] => pre[j] >= 2 * pre[i]
#    用 bisect_left 找到最小的 j
# 2) right_sum >= mid_sum => pre[n] - pre[j] >= pre[j] - pre[i]
#    => pre[n] + pre[i] >= 2 * pre[j] => pre[j] <= (pre[n] + pre[i]) // 2
#    用 bisect_right 找到最大的 j
#
# 合法 j 的范围为 [min_j, max_j]，贡献 max_j - min_j + 1 种方案。
# 同时需确保 max_j < n（right 非空，所以 j 不能等于 n-1，但这已由 min_j <= i+1 保证）。
#
# 时间复杂度: O(n log n)，遍历 n 次，每次二分 O(log n)。
#   也可用双指针优化到 O(n)，但 O(n log n) 已足够。
# 空间复杂度: O(n)，前缀和数组
#
# 关键点:
# - 前缀和将区间和转化为 O(1) 查询
# - 两个条件分别对应 j 的下界和上界
# - 使用 bisect_left 找下界，bisect_right 找上界
# - 注意数组元素非负，前缀和单调递增，所以二分有效
# - j 不能等于 n（right 非空）
