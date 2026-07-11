"""
LeetCode #2616 - Minimize the Maximum Difference of Pairs
最小化数对的最大差值
https://leetcode.cn/problems/minimize-the-maximum-difference-of-pairs/

给你一个下标从 0 开始的整数数组 `nums` 和一个整数 `p` 。请你从 `nums` 中找到 `p` 个下标对，每个下标对对应数值取差值，你需要使得这 `p` 个差值的 最大值 最小。同时，你需要确保每个下标在这 `p` 个下标对中最多出现一次。
对于一个下标对 `i` 和 `j` ，这一对的差值为 `|nums[i] - nums[j]|` ，其中 `|x|` 表示 `x` 的 绝对值 。
请你返回 `p` 个下标对对应数值 最大差值 的 最小值 。我们定义空集的最大值为零。

示例 1：
输入：nums = [10,1,2,7,1,3], p = 2 输出：1 解释：第一个下标对选择 1 和 4 ，第二个下标对选择 2 和 5 。 最大差值为 max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1 。所以我们返回 1 。
示例 2：
输入：nums = [4,2,1,2], p = 1 输出：0 解释：选择下标 1 和 3 构成下标对。差值为 |2 - 2| = 0 ，这是最大差值的最小值。

提示：
`1 <= nums.length <= 10^5`
`0 <= nums[i] <= 10^9`
`0 <= p <= (nums.length)/2`
"""

from typing import List, Optional


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        nums.sort()
        n = len(nums)

        def can_make(max_diff: int) -> bool:
            cnt = 0
            i = 0
            while i < n - 1:
                if nums[i + 1] - nums[i] <= max_diff:
                    cnt += 1
                    i += 2
                else:
                    i += 1
            return cnt >= p

        lo, hi = 0, nums[-1] - nums[0]
        while lo < hi:
            mid = (lo + hi) // 2
            if can_make(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Binary Search, Dynamic Programming, Sorting
#
# 解题思路:
# 排序后二分答案。检查是否能选出p对差值不超过mid的数对：贪心扫描，相邻元素差<=mid就配对并跳过两个元素。
# 这是最大化配对数的最优贪心策略。
#
# 时间复杂度: O(n log M) 其中M是max-min
# 空间复杂度: O(1)
#
# 关键点:
# - 排序是贪心配对的前置条件
# - 二分搜索最小化最大差值
# - 贪心判断函数：相邻配对是最优策略
