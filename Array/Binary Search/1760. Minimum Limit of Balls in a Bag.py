"""
LeetCode #1760 - Minimum Limit of Balls in a Bag
中文题名：袋子里最少数量的球
https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/

You are given an integer array `nums` where the `ith` bag contains `nums[i]` balls. You are also given an integer `maxOperations`.

You can perform the following operation at most `maxOperations` times:

Take any bag of balls and divide it into two new bags with a positive number of balls.

For example, a bag of `5` balls can become two new bags of `1` and `4` balls, or two new bags of `2` and `3` balls.

Your penalty is the maximum number of balls in a bag. You want to minimize your penalty after the operations.

Return the minimum possible penalty after performing the operations.

Example 1:

Input: nums = [9], maxOperations = 2
Output: 3
Explanation:
- Divide the bag with 9 balls into two bags of sizes 6 and 3. [9] -> [6,3].
- Divide the bag with 6 balls into two bags of sizes 3 and 3. [6,3] -> [3,3,3].
The bag with the most number of balls has 3 balls, so your penalty is 3 and you should return 3.

Example 2:

Input: nums = [2,4,8,2], maxOperations = 4
Output: 2
Explanation:
- Divide the bag with 8 balls into two bags of sizes 4 and 4. [2,4,8,2] -> [2,4,4,4,2].
- Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,4,4,4,2] -> [2,2,2,4,4,2].
- Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,2,2,4,4,2] -> [2,2,2,2,2,4,2].
- Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,2,2,2,2,4,2] -> [2,2,2,2,2,2,2,2].
The bag with the most number of balls has 2 balls, so your penalty is 2 an you should return 2.

Example 3:

Input: nums = [7,17], maxOperations = 2
Output: 7

Constraints:

`1 <= nums.length <= 105`

`1 <= maxOperations, nums[i] <= 109`

【中文翻译】
给定整数数组 nums 表示每个袋子中的球数，以及 maxOperations 表示最多可以执行的操作次数。
每次操作：选择一个袋子，将袋子中的球分成两个新的袋子（每个袋子至少有一个球）。
求经过最多 maxOperations 次操作后，单个袋子中球数的最大值的最小可能值。

示例 1：
输入: nums = [9], maxOperations = 2
输出: 3
解释: 9→[6,3]（第1次操作），6→[3,3]（第2次操作）。单个袋子最大球数=3。
"""

from typing import List, Optional
import math


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def can_achieve(max_balls: int) -> bool:
            operations = 0
            for balls in nums:
                # 将一个袋子分成大小不超过 max_balls 的袋子
                # 需要 ceil(balls / max_balls) - 1 次操作
                operations += (balls - 1) // max_balls
                if operations > maxOperations:
                    return False
            return True

        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if can_achieve(mid):
                right = mid
            else:
                left = mid + 1

        return left
# ═══════════════════════════════════════════════════════════════════════════════
# Solution & Explanation
# ═══════════════════════════════════════════════════════════════════════════════
#
# Difficulty: Medium
# Paid Only: No
#
# 解题思路:
# 二分搜索。对单个袋子的最大球数上限值进行二分。
# 对于给定的上限 max_balls，一个袋子有 balls 个球需要 ceil(balls/max_balls)-1 次操作来分割成都不超过 max_balls 的小袋子。
# 公式化简为 (balls - 1) // max_balls。
# 如果总操作次数 <= maxOperations，该上限可行，缩小右边界。
#
# 时间复杂度: O(N * log M) — N 为数组长度，M 为最大值
# 空间复杂度: O(1)
#
# 关键点:
# - 二分搜索的是最大值的最小可能值
# - 操作次数公式 (balls-1)//max_balls 等价于 ceil(balls/max_balls)-1
# - 可行性函数只需检查总操作数
