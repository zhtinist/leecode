"""
LeetCode #2834 - Find the Minimum Possible Sum of a Beautiful Array
找出美丽数组的最小和
https://leetcode.cn/problems/find-the-minimum-possible-sum-of-a-beautiful-array/

给你两个正整数：`n` 和 `target` 。
如果数组 `nums` 满足下述条件，则称其为 美丽数组 。
`nums.length == n`.
`nums` 由两两互不相同的正整数组成。
在范围 `[0, n-1]` 内，不存在 两个 不同 下标 `i` 和 `j` ，使得 `nums[i] + nums[j] == target` 。
返回符合条件的美丽数组所可能具备的 最小 和，并对结果进行取模 `10^9 + 7`。

示例 1：
输入：n = 2, target = 3 输出：4 解释：nums = [1,3] 是美丽数组。 - nums 的长度为 n = 2 。 - nums 由两两互不相同的正整数组成。 - 不存在两个不同下标 i 和 j ，使得 nums[i] + nums[j] == 3 。 可以证明 4 是符合条件的美丽数组所可能具备的最小和。
示例 2：
输入：n = 3, target = 3 输出：8 解释： nums = [1,3,4] 是美丽数组。  - nums 的长度为 n = 3 。  - nums 由两两互不相同的正整数组成。  - 不存在两个不同下标 i 和 j ，使得 nums[i] + nums[j] == 3 。 可以证明 8 是符合条件的美丽数组所可能具备的最小和。
示例 3：
输入：n = 1, target = 1 输出：1 解释：nums = [1] 是美丽数组。

提示：
`1 <= n <= 10^9`
`1 <= target <= 10^9`
"""

from typing import List, Optional


class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        half = target // 2
        if n <= half:
            # Use 1, 2, ..., n
            return n * (n + 1) // 2 % MOD
        # Use 1..half, then target, target+1, ...
        first_sum = half * (half + 1) // 2
        remaining = n - half
        last = target + remaining - 1
        second_sum = (target + last) * remaining // 2
        return (first_sum + second_sum) % MOD



# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Tags: Greedy, Math
#
# 解题思路:
# 要最小化和，应选尽可能小的正整数。对于 target，数对 (x, target-x) 不能同时出现。
# 贪心策略：选取 1, 2, ..., target//2 这些较小的数（它们与 target 的补数都 >= target//2 以上，互不冲突）。
# 如果还需要更多数（n > target//2），从 target 开始往后取（target, target+1, ...），因为这些数与已有数不会和为 target。
# 使用等差数列求和公式计算总和，注意取模。
#
# 时间复杂度: O(1)
# 空间复杂度: O(1)
#
# 关键点:
# - 前半部分取 [1, target//2]，这些数的补数都 >= ceil(target/2)，不会冲突
# - 后半部分从 target 开始取，因为 target 及更大的数与 [1, target//2] 的和都 > target
# - 等差数列求和公式: sum = (首项 + 末项) * 项数 // 2
