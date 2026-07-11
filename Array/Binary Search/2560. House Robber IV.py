"""
LeetCode #2560 - House Robber IV
打家劫舍 IV
https://leetcode.cn/problems/house-robber-iv/

沿街有一排连续的房屋。每间房屋内都藏有一定的现金。现在有一位小偷计划从这些房屋中窃取现金。
由于相邻的房屋装有相互连通的防盗系统，所以小偷 不会窃取相邻的房屋 。
小偷的 窃取能力 定义为他在窃取过程中能从单间房屋中窃取的 最大金额 。
给你一个整数数组 `nums` 表示每间房屋存放的现金金额。形式上，从左起第 `i` 间房屋中放有 `nums[i]` 美元。
另给你一个整数 `k` ，表示窃贼将会窃取的 最少 房屋数。小偷总能窃取至少 `k` 间房屋。
返回小偷的 最小 窃取能力。

示例 1：
输入：nums = [2,3,5,9], k = 2 输出：5 解释： 小偷窃取至少 2 间房屋，共有 3 种方式： - 窃取下标 0 和 2 处的房屋，窃取能力为 max(nums[0], nums[2]) = 5 。 - 窃取下标 0 和 3 处的房屋，窃取能力为 max(nums[0], nums[3]) = 9 。 - 窃取下标 1 和 3 处的房屋，窃取能力为 max(nums[1], nums[3]) = 9 。 因此，返回 min(5, 9, 9) = 5 。
示例 2：
输入：nums = [2,7,9,3,1], k = 2 输出：2 解释：共有 7 种窃取方式。窃取能力最小的情况所对应的方式是窃取下标 0 和 4 处的房屋。返回 max(nums[0], nums[4]) = 2 。

提示：
`1 <= nums.length <= 10^5`
`1 <= nums[i] <= 10^9`
`1 <= k <= (nums.length + 1)/2`
"""

from typing import List, Optional


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def can(cap: int) -> bool:
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= cap:
                    count += 1
                    i += 2  # skip next (adjacent)
                else:
                    i += 1
            return count >= k

        lo, hi = min(nums), max(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if can(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Array, Binary Search, Dynamic Programming
#
# 解题思路:
# 二分查找最小窃取能力。检查函数判断能力为cap时能否偷至少k间房屋：
# 遍历房屋，若金额<=cap则偷并跳过相邻（i+=2），否则跳过当前（i+=1）。
# 使用二分搜索在[min(nums), max(nums)]范围内找到最小的可行cap。
#
# 时间复杂度: O(N log M)，M为金额范围
# 空间复杂度: O(1)
#
# 关键点:
# - 二分答案+贪心检查
# - 贪心策略：遇到可以偷的房屋就偷（金额<=cap），然后跳相邻
# - 为什么贪心最优：提前偷不会比延后偷更差（对于"至少k个"的要求）
